from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any
import json

from arc2_competition_router_candidate.r1_solver import r0_b2_solver as r0
from arc2_competition_router_candidate.r1_solver import r1_solver as r1

Grid = r0.Grid


def _rep_overhead(rep: str) -> float:
    s = rep.lower()
    if 'memorized_output' in s:
        return 8.0
    cost = 0.0
    if 'raw' in s:
        cost += 0.0
    if 'non_bg_bbox' in s:
        cost += 0.8
    if 'component' in s:
        cost += 1.5
    if 'relational_cell_features' in s:
        cost += 2.0
    if 'separator_aligned_panels' in s:
        cost += 2.0
    if 'color_specific' in s:
        cost += 1.2
    if '+color_relation' in s:
        cost += 0.4
    return cost


@dataclass(frozen=True)
class JointCandidate:
    source: str  # R0_FIXED or R1_TASK_ROLE
    program: r0.Program
    r1_candidate: r1.R1Candidate | None
    F_exact_demo_fit: int
    P_successes: int
    P_trials: int
    I_recurrences: int
    I_trials: int
    C_joint: float
    schema: tuple[Any, ...]

    @property
    def P_rate(self) -> float | None:
        return self.P_successes / self.P_trials if self.P_trials else None

    @property
    def I_rate(self) -> float | None:
        return self.I_recurrences / self.I_trials if self.I_trials else None

    @property
    def rank(self) -> tuple[Any, ...]:
        # No scalar weights. Exact fit is mandatory before construction of this object.
        # Prospective failures dominate recurrence failures. Among equally un-falsified
        # hypotheses, prefer more opportunities to falsify, then shorter joint code.
        p_fail = self.P_trials - self.P_successes
        i_fail = self.I_trials - self.I_recurrences
        return (
            p_fail,
            -self.P_trials,
            i_fail,
            -self.I_trials,
            round(self.C_joint, 6),
            self.source,
            self.program.key,
        )

    def descriptor(self) -> dict[str, Any]:
        d = asdict(self)
        d['program'] = self.program.descriptor()
        d['r1_candidate'] = None if self.r1_candidate is None else {
            'representation': self.r1_candidate.representation.descriptor(),
            'program': self.r1_candidate.program.descriptor(),
        }
        d['P_rate'] = self.P_rate
        d['I_rate'] = self.I_rate
        d['rank'] = list(self.rank)
        return d


def _schema_r0(p: r0.Program) -> tuple[Any, ...]:
    # Joint schema = representation family + transformation family.
    return ('R0_FIXED', p.representation, p.kind)


def _schema_r1(c: r1.R1Candidate) -> tuple[Any, ...]:
    rep = c.representation
    return ('R1_TASK_ROLE', rep.role_count, c.program.representation, c.program.kind)


def _cost_r0(p: r0.Program) -> float:
    return float(p.complexity) + _rep_overhead(p.representation)


def _cost_r1(c: r1.R1Candidate) -> float:
    rep = c.representation
    # This is one joint code-length proxy, not independent optimization of X and T.
    # The role constructor pays for manufactured slots, ambiguity/alignment, and the
    # downstream program; role IDs themselves are anonymous and not charged as literals.
    return (
        float(c.program.complexity)
        + float(rep.complexity_proxy)
        + 0.10 * float(rep.assignment_cost)
        + _rep_overhead(c.program.representation)
    )


def _pseudo_task_holdout(task: dict[str, Any], k: int) -> dict[str, Any]:
    train = [ex for i, ex in enumerate(task['train']) if i != k]
    held = task['train'][k]
    return {'train': train, 'test': [{'input': held['input']}]}


def _predict_r1_candidate(c: r1.R1Candidate, test_input: list[list[int]], test_index: int = 0) -> Grid | None:
    rep = c.representation
    test_map = dict(rep.test_color_to_role[test_index])
    role_to_color = {role: color for color, role in test_map.items()}
    nx = r1._normalize_grid(r0.to_grid(test_input), test_map)  # frozen R1 semantics
    if nx is None:
        return None
    try:
        ny = c.program.apply(nx)
    except Exception:
        return None
    if ny is None:
        return None
    return r1._decode_grid(ny, role_to_color)


def _loo_stats_r0(task: dict[str, Any], schema: tuple[Any, ...]) -> tuple[int,int,int,int]:
    p_ok = p_trials = i_ok = i_trials = 0
    n = len(task['train'])
    for k in range(n):
        pt = _pseudo_task_holdout(task, k)
        # R0 can synthesize from one demonstration.
        if not pt['train']:
            continue
        i_trials += 1; p_trials += 1
        cs = r0.synthesize(pt)
        matched = [p for p in cs if _schema_r0(p) == schema]
        if matched:
            i_ok += 1
        truth = r0.to_grid(task['train'][k]['output'])
        x = r0.to_grid(task['train'][k]['input'])
        if any(p.apply(x) == truth for p in matched):
            p_ok += 1
    return p_ok,p_trials,i_ok,i_trials


def _loo_stats_r1(task: dict[str, Any], schema: tuple[Any, ...]) -> tuple[int,int,int,int]:
    p_ok = p_trials = i_ok = i_trials = 0
    n = len(task['train'])
    for k in range(n):
        pt = _pseudo_task_holdout(task, k)
        # Frozen R1 requires >=2 demonstrations; folds below that are untested, not failures.
        if len(pt['train']) < 2:
            continue
        i_trials += 1; p_trials += 1
        cs = r1.synthesize_r1(pt)
        matched = [c for c in cs if _schema_r1(c) == schema]
        if matched:
            i_ok += 1
        truth = r0.to_grid(task['train'][k]['output'])
        if any(_predict_r1_candidate(c, task['train'][k]['input']) == truth for c in matched):
            p_ok += 1
    return p_ok,p_trials,i_ok,i_trials


def enumerate_joint_candidates(task: dict[str, Any]) -> list[JointCandidate]:
    out: list[JointCandidate] = []
    loo_cache: dict[tuple[Any, ...], tuple[int,int,int,int]] = {}

    for p in r0.synthesize(task):
        schema = _schema_r0(p)
        st = loo_cache.get(schema)
        if st is None:
            st = _loo_stats_r0(task, schema); loo_cache[schema] = st
        po,pt,io,it = st
        out.append(JointCandidate('R0_FIXED', p, None, 1, po,pt,io,it,_cost_r0(p),schema))

    for c in r1.synthesize_r1(task):
        schema = _schema_r1(c)
        st = loo_cache.get(schema)
        if st is None:
            st = _loo_stats_r1(task, schema); loo_cache[schema] = st
        po,pt,io,it = st
        out.append(JointCandidate('R1_TASK_ROLE', c.program, c, 1, po,pt,io,it,_cost_r1(c),schema))

    out.sort(key=lambda c: c.rank)
    return out


def predict_candidate(c: JointCandidate, task: dict[str, Any], test_index: int) -> Grid | None:
    x = task['test'][test_index]['input']
    if c.source == 'R0_FIXED':
        try:
            return c.program.apply(r0.to_grid(x))
        except Exception:
            return None
    assert c.r1_candidate is not None
    return _predict_r1_candidate(c.r1_candidate, x, test_index)


def solve_joint(task: dict[str, Any], max_attempts: int = 2) -> dict[str, Any]:
    candidates = enumerate_joint_candidates(task)
    preds = []
    for ti, _ in enumerate(task['test']):
        attempts = []
        seen: set[Grid] = set()
        for c in candidates:
            y = predict_candidate(c, task, ti)
            if y is None or not y or not y[0] or len(y) > 30 or len(y[0]) > 30 or y in seen:
                continue
            seen.add(y)
            attempts.append({
                'output': r0.to_list(y),
                'source': c.source,
                'schema': list(c.schema),
                'joint_metrics': {
                    'F': c.F_exact_demo_fit,
                    'P_successes': c.P_successes,
                    'P_trials': c.P_trials,
                    'P_rate': c.P_rate,
                    'I_recurrences': c.I_recurrences,
                    'I_trials': c.I_trials,
                    'I_rate': c.I_rate,
                    'C_joint': c.C_joint,
                },
                'program': c.program.descriptor(),
                'representation': None if c.r1_candidate is None else c.r1_candidate.representation.descriptor(),
            })
            if len(attempts) >= max_attempts:
                break
        preds.append({'test_index':ti,'attempts':attempts})
    return {
        'candidate_count':len(candidates),
        'joint_candidates':[c.descriptor() for c in candidates],
        'predictions':preds,
    }
