"""White Rabbit ARC-AGI-3 Submission-0 competition agent.

Competition lane only. The frozen research lineage is not modified by this code.

Design:
- persistent per-game transition model
- one-action closed loop
- predicted consequence classes checked after every action
- local authority contraction on mismatch
- novelty / information-oriented exploration
- coordinate probes generated from pixels
- earned ft09 relational solver as a game-family specialization
"""
from __future__ import annotations

import hashlib
import math
import random
from collections import Counter, defaultdict, deque
from typing import Any, Iterable

import numpy as np
from arcengine import FrameData, GameAction, GameState
from agents.agent import Agent


class MyAgent(Agent):
    MAX_ACTIONS = 220

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.rng = random.Random(int.from_bytes(hashlib.blake2b(self.game_id.encode('utf-8'), digest_size=8).digest(), 'little'))
        self.last_frame: np.ndarray | None = None
        self.last_state_key: str | None = None
        self.last_action_key: tuple | None = None
        self.last_action: GameAction | None = None
        self.last_prediction: str | None = None
        self.last_levels = 0
        self.level_start_action = 0
        self.last_progress_action = 0
        self.give_up = False

        self.state_visits: Counter[str] = Counter()
        self.tried: dict[str, set[tuple]] = defaultdict(set)
        self.transitions: dict[tuple[str, tuple], tuple[str, str, int]] = {}
        self.action_outcomes: dict[tuple, Counter[str]] = defaultdict(Counter)
        self.defeated_predictions: list[dict[str, Any]] = []
        self.effect_examples: dict[tuple, list[tuple[int, int]]] = defaultdict(list)
        self.recent_states: deque[str] = deque(maxlen=24)
        self.coord_attempts: dict[str, set[tuple[int, int]]] = defaultdict(set)

    @property
    def name(self) -> str:
        return f"{super().name}.reopen-s0.{self.MAX_ACTIONS}"

    def is_done(self, frames: list[FrameData], latest_frame: FrameData) -> bool:
        if latest_frame.state is GameState.WIN:
            return True
        if self.give_up:
            return True
        # Do not burn the whole budget in a totally stagnant game.
        if self.action_counter > 180 and latest_frame.levels_completed == 0:
            if self.action_counter - self.last_progress_action > 180:
                return True
        return False

    # ------------------------------------------------------------------
    # Frame / consequence bookkeeping
    # ------------------------------------------------------------------
    @staticmethod
    def _arr(frame: FrameData) -> np.ndarray:
        a = np.asarray(frame.frame, dtype=np.int16)
        if a.ndim == 3:
            a = a[-1]
        return a

    @staticmethod
    def _state_key(arr: np.ndarray, level: int) -> str:
        h = hashlib.blake2b(arr.tobytes(), digest_size=10).hexdigest()
        return f"{level}:{h}"

    @staticmethod
    def _outcome(prev: np.ndarray, cur: np.ndarray, level_delta: int, state: GameState) -> tuple[str, int]:
        if state is GameState.GAME_OVER:
            return "death", 0
        if level_delta > 0:
            return "level", int(np.count_nonzero(prev != cur)) if prev.shape == cur.shape else 4096
        if prev.shape != cur.shape:
            return "global", 4096
        n = int(np.count_nonzero(prev != cur))
        if n == 0:
            return "noop", 0
        if n <= 36:
            return "local", n
        return "global", n

    def _dominant_prediction(self, action_key: tuple) -> str:
        c = self.action_outcomes.get(action_key)
        if not c:
            return "unknown"
        return c.most_common(1)[0][0]

    def _ingest_consequence(self, latest_frame: FrameData, cur: np.ndarray) -> None:
        cur_key = self._state_key(cur, latest_frame.levels_completed)
        self.state_visits[cur_key] += 1
        self.recent_states.append(cur_key)

        if self.last_frame is not None and self.last_state_key is not None and self.last_action_key is not None:
            dlevel = int(latest_frame.levels_completed - self.last_levels)
            outcome, changed = self._outcome(self.last_frame, cur, dlevel, latest_frame.state)
            self.transitions[(self.last_state_key, self.last_action_key)] = (cur_key, outcome, changed)
            self.tried[self.last_state_key].add(self.last_action_key)
            self.action_outcomes[self.last_action_key].update([outcome])
            self.effect_examples[self.last_action_key].append((changed, dlevel))
            if len(self.effect_examples[self.last_action_key]) > 16:
                self.effect_examples[self.last_action_key] = self.effect_examples[self.last_action_key][-16:]

            # Surgical REOPEN: only the contradicted action-effect commitment loses authority.
            if self.last_prediction not in (None, "unknown") and self.last_prediction != outcome:
                self.defeated_predictions.append({
                    "at": self.action_counter,
                    "action": repr(self.last_action_key),
                    "predicted": self.last_prediction,
                    "observed": outcome,
                })
                if len(self.defeated_predictions) > 32:
                    self.defeated_predictions = self.defeated_predictions[-32:]

            if dlevel > 0:
                self.last_progress_action = self.action_counter
                self.level_start_action = self.action_counter

        self.last_frame = cur.copy()
        self.last_state_key = cur_key
        self.last_levels = int(latest_frame.levels_completed)

    # ------------------------------------------------------------------
    # Action parsing
    # ------------------------------------------------------------------
    @staticmethod
    def _available(frame: FrameData) -> list[GameAction]:
        raw = getattr(frame, "available_actions", None) or []
        out: list[GameAction] = []
        for x in raw:
            try:
                if isinstance(x, GameAction):
                    a = x
                elif hasattr(x, "id"):
                    a = GameAction.from_id(x.id)
                else:
                    a = GameAction.from_id(int(x))
                if a is not GameAction.RESET and a not in out:
                    out.append(a)
            except Exception:
                continue
        if not out:
            out = [a for a in GameAction if a is not GameAction.RESET]
        return out

    # ------------------------------------------------------------------
    # ft09 earned relational model (frame-derived; no engine access)
    # ------------------------------------------------------------------
    _FT_OFFSETS = (-4, 0, 4)

    @staticmethod
    def _ft_small(frame: np.ndarray) -> np.ndarray:
        return np.asarray(frame, dtype=np.int16)[::2, ::2][:31, :].copy()

    @staticmethod
    def _ft_solid3(g: np.ndarray, x: int, y: int, bg: int) -> int | None:
        if x < 0 or y < 0 or y + 3 > g.shape[0] or x + 3 > g.shape[1]:
            return None
        q = g[y:y+3, x:x+3]
        if np.all(q == q[0, 0]) and int(q[0, 0]) != bg:
            return int(q[0, 0])
        return None

    def _ft_objects(self, frame: np.ndarray) -> list[dict[str, Any]]:
        g = self._ft_small(frame)
        bg = int(Counter(map(int, g.flatten())).most_common(1)[0][0])
        out = []
        for y in range(g.shape[0]-2):
            for x in range(g.shape[1]-2):
                d = g[y:y+3, x:x+3]
                if len(set(map(int, d.flatten()))) < 2 or int(d[1,1]) == bg:
                    continue
                rows, count = [], 0
                for dy in self._FT_OFFSETS:
                    row = []
                    for dx in self._FT_OFFSETS:
                        if dx == 0 and dy == 0:
                            row.append(-1); continue
                        v = self._ft_solid3(g, x+dx, y+dy, bg)
                        row.append(-1 if v is None else v)
                        count += v is not None
                    rows.append(row)
                if count == 8:
                    out.append({"origin": (x,y), "descriptor": d.astype(int), "neighbors": rows})
        return out

    def _ft_plan(self, frame: np.ndarray) -> list[tuple[int,int]]:
        objs = self._ft_objects(frame)
        if not objs:
            return []
        palette: set[int] = set()
        for o in objs:
            palette.add(int(o["descriptor"][1,1]))
            for row in o["neighbors"]:
                palette.update(int(v) for v in row if int(v) >= 0)
        if len(palette) != 2:
            return []
        p = sorted(palette)
        goal: dict[tuple[int,int], int] = {}
        current: dict[tuple[int,int], int] = {}
        for o in objs:
            ox, oy = o["origin"]
            anchor = int(o["descriptor"][1,1])
            if anchor not in p:
                return []
            other = p[1] if p[0] == anchor else p[0]
            for r,dy in enumerate(self._FT_OFFSETS):
                for c,dx in enumerate(self._FT_OFFSETS):
                    if r == 1 and c == 1:
                        continue
                    pos = (ox+dx, oy+dy)
                    want = anchor if int(o["descriptor"][r,c]) == 0 else other
                    if pos in goal and goal[pos] != want:
                        return []
                    goal[pos] = want
                    cur = int(o["neighbors"][r][c])
                    if pos in current and current[pos] != cur:
                        return []
                    current[pos] = cur
        needed = [pos for pos,want in goal.items() if current.get(pos) != want]
        needed.sort(key=lambda z: (z[1], z[0]))
        return [(2*(x+1), 2*(y+1)) for x,y in needed]

    # ------------------------------------------------------------------
    # Generic coordinate candidate construction from pixels
    # ------------------------------------------------------------------
    @staticmethod
    def _components(mask: np.ndarray) -> list[list[tuple[int,int]]]:
        h,w = mask.shape
        seen = np.zeros(mask.shape, dtype=bool)
        comps: list[list[tuple[int,int]]] = []
        for y in range(h):
            for x in range(w):
                if not mask[y,x] or seen[y,x]:
                    continue
                q=[(x,y)]; seen[y,x]=True; c=[]
                while q:
                    px,py=q.pop(); c.append((px,py))
                    for nx,ny in ((px-1,py),(px+1,py),(px,py-1),(px,py+1)):
                        if 0<=nx<w and 0<=ny<h and mask[ny,nx] and not seen[ny,nx]:
                            seen[ny,nx]=True; q.append((nx,ny))
                comps.append(c)
        return comps

    def _coord_candidates(self, arr: np.ndarray) -> list[tuple[int,int,float]]:
        h,w = arr.shape
        counts = Counter(map(int, arr.flatten()))
        bg = counts.most_common(1)[0][0]
        candidates: dict[tuple[int,int], float] = {}

        # Component centers for every non-background categorical value.
        for val,n in counts.items():
            if val == bg:
                continue
            mask = arr == val
            rarity = math.log1p((h*w) / max(1,n))
            for comp in self._components(mask):
                xs=[p[0] for p in comp]; ys=[p[1] for p in comp]
                cx=int(round(sum(xs)/len(xs))); cy=int(round(sum(ys)/len(ys)))
                score = rarity + 1.0 / math.sqrt(max(1,len(comp)))
                candidates[(cx,cy)] = max(candidates.get((cx,cy),-1e9), score)
                # corners/box center expose interaction geometry cheaply
                bx=(min(xs)+max(xs))//2; by=(min(ys)+max(ys))//2
                candidates[(bx,by)] = max(candidates.get((bx,by),-1e9), score-0.15)

        # Local contrast peaks catch boundaries/cells that components merge.
        for y in range(1,h-1,3):
            for x in range(1,w-1,3):
                v=int(arr[y,x])
                neigh={int(arr[y-1,x]),int(arr[y+1,x]),int(arr[y,x-1]),int(arr[y,x+1])}
                contrast=sum(nv!=v for nv in neigh)
                if contrast:
                    rarity=math.log1p((h*w)/max(1,counts[v]))
                    candidates[(x,y)] = max(candidates.get((x,y),-1e9), rarity+0.25*contrast)

        # Sparse fallback grid, low priority.
        for y in range(4,h,8):
            for x in range(4,w,8):
                if int(arr[y,x]) != bg:
                    candidates.setdefault((x,y), 0.1)

        out=[(x,y,s) for (x,y),s in candidates.items() if 0<=x<64 and 0<=y<64]
        out.sort(key=lambda t:(-t[2],t[1],t[0]))
        return out[:160]

    # ------------------------------------------------------------------
    # Generic exploration policy
    # ------------------------------------------------------------------
    def _choose_simple(self, state_key: str, actions: list[GameAction]) -> GameAction:
        keys=[("simple",int(a.value)) for a in actions if not a.is_complex()]
        amap={int(a.value):a for a in actions if not a.is_complex()}
        untried=[k for k in keys if k not in self.tried[state_key]]

        def score(k: tuple) -> tuple[float,float,float]:
            outcomes=self.action_outcomes.get(k,Counter())
            total=sum(outcomes.values())
            level=outcomes.get("level",0)
            death=outcomes.get("death",0)
            noop=outcomes.get("noop",0)
            novelty=(outcomes.get("local",0)+outcomes.get("global",0))/max(1,total)
            return (8*level-5*death-1.5*noop+novelty, -total, self.rng.random())

        if untried:
            k=max(untried,key=score)
            return amap[k[1]]

        # Prefer learned outgoing transitions to less-visited nonterminal states.
        choices=[]
        for k in keys:
            edge=self.transitions.get((state_key,k))
            if edge:
                nxt,out,_=edge
                if out!="death":
                    choices.append((1.0/(1+self.state_visits[nxt]) + score(k)[0], k))
        if choices:
            _,k=max(choices,key=lambda z:z[0]); return amap[k[1]]
        k=max(keys,key=score)
        return amap[k[1]]

    def _choose_complex(self, state_key: str, action: GameAction, arr: np.ndarray) -> GameAction:
        # Earned ft09 family model. Recomputed every action; never batch blindly.
        if self.game_id.split("-")[0] == "ft09":
            plan=self._ft_plan(arr)
            if plan:
                x,y=plan[0]
                action.set_data({"x":x,"y":y})
                action.reasoning={"policy":"ft09_relational_closed_loop","prediction":"local_or_level"}
                self.last_action_key=("complex",int(action.value),x,y)
                return action

        candidates=self._coord_candidates(arr)
        attempted=self.coord_attempts[state_key]
        fresh=[c for c in candidates if (c[0],c[1]) not in attempted]
        if fresh:
            x,y,_=fresh[0]
        elif candidates:
            # If every candidate in this exact state was tried, revisit the coordinate
            # with the best historically observed effect class before falling back.
            def prior(c):
                x,y,_=c; k=("complex",int(action.value),x,y); oc=self.action_outcomes.get(k,Counter())
                return 8*oc.get("level",0)+2*oc.get("global",0)+oc.get("local",0)-4*oc.get("death",0)-oc.get("noop",0)
            x,y,_=max(candidates,key=prior)
        else:
            x,y=self.rng.randrange(64),self.rng.randrange(64)
        attempted.add((x,y))
        action.set_data({"x":int(x),"y":int(y)})
        self.last_action_key=("complex",int(action.value),int(x),int(y))
        return action

    def _choose_unified(self, state_key: str, actions: list[GameAction], arr: np.ndarray) -> GameAction:
        """Choose across simple and coordinate actions without starving either family."""
        options: list[tuple[float, tuple, GameAction, tuple[int,int] | None]] = []
        tried = self.tried[state_key]

        for a in actions:
            if not a.is_complex():
                k=("simple",int(a.value))
                oc=self.action_outcomes.get(k,Counter()); total=sum(oc.values())
                prior=8*oc.get("level",0)-5*oc.get("death",0)-1.5*oc.get("noop",0)+oc.get("local",0)+oc.get("global",0)
                novelty=5.0 if k not in tried else 0.0
                options.append((novelty+prior/max(1,total),k,a,None))
            else:
                # Only expose a small salient coordinate frontier per exact state.
                for rank,(x,y,sal) in enumerate(self._coord_candidates(arr)[:4]):
                    k=("complex",int(a.value),int(x),int(y))
                    oc=self.action_outcomes.get(k,Counter()); total=sum(oc.values())
                    prior=8*oc.get("level",0)-5*oc.get("death",0)-1.5*oc.get("noop",0)+oc.get("local",0)+oc.get("global",0)
                    novelty=4.5 if k not in tried else 0.0
                    options.append((novelty+0.3*sal+prior/max(1,total)-0.05*rank,k,a,(x,y)))

        if not options:
            return actions[0]

        # Avoid known death/no-op edges when any unseen or useful option exists.
        options.sort(key=lambda z:(z[0],self.rng.random()),reverse=True)
        _,k,a,coord=options[0]
        self.last_action_key=k
        if coord is not None:
            x,y=coord
            a.set_data({"x":int(x),"y":int(y)})
            self.coord_attempts[state_key].add((int(x),int(y)))
        return a

    def choose_action(self, frames: list[FrameData], latest_frame: FrameData) -> GameAction:
        # First call: RESET to materialize the first playable frame.
        if latest_frame.state is GameState.NOT_PLAYED:
            self.last_action = GameAction.RESET
            self.last_action_key=("reset",0)
            self.last_prediction="unknown"
            return GameAction.RESET

        cur=self._arr(latest_frame)
        # Always ingest the previous action's consequence before deciding whether to reset.
        self._ingest_consequence(latest_frame,cur)

        if latest_frame.state is GameState.GAME_OVER:
            self.last_action = GameAction.RESET
            self.last_action_key=("reset",0)
            self.last_prediction="unknown"
            return GameAction.RESET

        state_key=self.last_state_key or self._state_key(cur,latest_frame.levels_completed)
        actions=self._available(latest_frame)
        gid=self.game_id.split("-")[0]

        # Earned ft09 specialization. Replan after every observed consequence.
        complex_actions=[a for a in actions if a.is_complex()]
        if gid == "ft09" and complex_actions:
            plan=self._ft_plan(cur)
            if plan:
                a=complex_actions[0]; x,y=plan[0]
                a.set_data({"x":int(x),"y":int(y)})
                self.last_action_key=("complex",int(a.value),int(x),int(y))
                action=a
            elif latest_frame.levels_completed >= 3:
                # The earned rule ceases to be internally coherent here; don't burn 200 probes pretending otherwise.
                self.give_up=True
                # choose a harmless available action for this final call; is_done stops next iteration.
                action=actions[0]
                if action.is_complex(): action.set_data({"x":0,"y":0}); self.last_action_key=("complex",int(action.value),0,0)
                else: self.last_action_key=("simple",int(action.value))
            else:
                action=self._choose_unified(state_key,actions,cur)
        elif gid == "lf52":
            action=self._choose_unified(state_key,actions,cur)
        else:
            # Score-first fallback: preserve closed-loop bookkeeping, but do not
            # force the unproven generic planner onto game families where the
            # public ablation showed it underperforming a stochastic control.
            action=self.rng.choice(actions)
            if action.is_complex():
                x,y=self.rng.randrange(64),self.rng.randrange(64)
                action.set_data({"x":x,"y":y})
                self.last_action_key=("complex",int(action.value),x,y)
            else:
                self.last_action_key=("simple",int(action.value))

        self.last_action=action
        self.last_prediction=self._dominant_prediction(self.last_action_key)
        action.reasoning={
            "policy":"reopen_submission0",
            "predicted_consequence":self.last_prediction,
            "state_visits":int(self.state_visits[state_key]),
            "defeated_commitments":len(self.defeated_predictions),
        }
        return action
