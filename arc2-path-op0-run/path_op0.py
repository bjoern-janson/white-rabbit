from __future__ import annotations
from dataclasses import dataclass, asdict
from collections import deque, Counter
from itertools import combinations
from typing import Any, Iterable
import hashlib, json

import sys
sys.path.insert(0, '/mnt/data/arc2_r1_artifact')
from r1_solver import r1_solver as r1
from r1_solver import r0_b2_solver as r0

Grid = r0.Grid

MAX_TERMINALS = 128
MAX_OPERANDS = 4096
SELECTOR_FEATURES = (
    'kind','src_role','tgt_role','src_size_rank','tgt_size_rank',
    'src_border','tgt_border','bend_count','orientation','length'
)

@dataclass(frozen=True)
class Component:
    cid: int
    role: int
    cells: tuple[tuple[int,int], ...]
    size: int
    size_rank: int
    bbox: tuple[int,int,int,int]
    border: int
    thin: int

@dataclass(frozen=True)
class Terminal:
    y: int
    x: int
    role: int
    cid: int
    size_rank: int
    border: int
    singleton: int

@dataclass(frozen=True)
class PathOperand:
    kind: str
    cells: tuple[tuple[int,int], ...]
    src: tuple[int,int]
    tgt: tuple[int,int]
    src_role: int
    tgt_role: int
    src_size_rank: int
    tgt_size_rank: int
    src_border: int
    tgt_border: int
    bend_count: int
    orientation: str
    length: int

    def feature(self, name: str):
        return getattr(self, name)

    @property
    def sort_key(self):
        return (
            self.length, self.kind, self.src_role, self.tgt_role,
            self.src_size_rank, self.tgt_size_rank,
            self.src_border, self.tgt_border, self.bend_count,
            self.orientation, self.src, self.tgt, self.cells,
        )

@dataclass(frozen=True)
class OperationalPathRepresentation:
    background_role: int
    components: tuple[Component, ...]
    terminals: tuple[Terminal, ...]
    paths: tuple[PathOperand, ...]
    abstained: bool = False
    reason: str | None = None

@dataclass(frozen=True)
class PathProgram:
    selector: tuple[tuple[str, Any], ...]
    paint_role: int
    selected_count_train: int
    painted_length_train: int

    @property
    def key(self):
        return (len(self.selector), self.selected_count_train, self.painted_length_train, self.paint_role, self.selector)

    def descriptor(self):
        return {
            'kind': 'PATH_OP0_PAINT',
            'selector': [list(x) for x in self.selector],
            'paint_role': self.paint_role,
            'selected_count_train': self.selected_count_train,
            'painted_length_train': self.painted_length_train,
        }


def _shape(g: Grid):
    return len(g), len(g[0]) if g else 0


def _modal_role(g: Grid) -> int:
    c = Counter(v for row in g for v in row)
    m = max(c.values())
    return min(k for k,v in c.items() if v == m)


def _component_cells(g: Grid, bg: int):
    h,w = _shape(g)
    seen=set(); out=[]
    cid=0
    for y in range(h):
        for x in range(w):
            role=g[y][x]
            if role==bg or (y,x) in seen:
                continue
            q=deque([(y,x)]); seen.add((y,x)); cells=[]
            while q:
                cy,cx=q.popleft(); cells.append((cy,cx))
                for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny,nx=cy+dy,cx+dx
                    if 0<=ny<h and 0<=nx<w and (ny,nx) not in seen and g[ny][nx]==role:
                        seen.add((ny,nx)); q.append((ny,nx))
            out.append((cid,role,tuple(sorted(cells)))); cid+=1
    return out


def _size_ranks(raw):
    sizes={cid:len(cells) for cid,role,cells in raw}
    vals=sorted(set(sizes.values()), reverse=True)
    rank={v:i for i,v in enumerate(vals)}
    return {cid:rank[s] for cid,s in sizes.items()}


def _degree_map(cells: set[tuple[int,int]]) -> dict[tuple[int,int], int]:
    return {p:sum((p[0]+dy,p[1]+dx) in cells for dy,dx in ((1,0),(-1,0),(0,1),(0,-1))) for p in cells}


def _straight_cells(a: tuple[int,int], b: tuple[int,int]) -> tuple[tuple[int,int], ...] | None:
    ay,ax=a; by,bx=b
    if ay==by:
        lo,hi=sorted((ax,bx))
        return tuple((ay,x) for x in range(lo,hi+1))
    if ax==bx:
        lo,hi=sorted((ay,by))
        return tuple((y,ax) for y in range(lo,hi+1))
    return None


def _segment_oriented(a,b):
    ay,ax=a; by,bx=b
    if ay==by: return 'H'
    if ax==bx: return 'V'
    return None


def _join_paths(p1, p2):
    if not p1 or not p2: return None
    if p1[-1]==p2[0]: return p1 + p2[1:]
    if p2[-1]==p1[0]: return p2 + p1[1:]
    if p1[0]==p2[0]: return tuple(reversed(p1)) + p2[1:]
    if p1[-1]==p2[-1]: return p1 + tuple(reversed(p2))[1:]
    return None


def _interior_clear(g: Grid, cells: tuple[tuple[int,int],...], bg: int, endpoints: set[tuple[int,int]]) -> bool:
    return all((p in endpoints) or g[p[0]][p[1]]==bg for p in cells)


def operationalize_grid(g: Grid) -> OperationalPathRepresentation:
    h,w=_shape(g)
    if not g or not g[0]:
        return OperationalPathRepresentation(0,(),(),(),True,'empty')
    bg=_modal_role(g)
    raw=_component_cells(g,bg)
    ranks=_size_ranks(raw)
    comps=[]; terms=[]
    comp_by_id={}
    for cid,role,cells_t in raw:
        cells=set(cells_t); deg=_degree_map(cells)
        thin=int(all(d<=2 for d in deg.values()))
        ys=[p[0] for p in cells]; xs=[p[1] for p in cells]
        border=int(any(y in (0,h-1) or x in (0,w-1) for y,x in cells))
        c=Component(cid,role,cells_t,len(cells_t),ranks[cid],(min(ys),min(xs),max(ys),max(xs)),border,thin)
        comps.append(c); comp_by_id[cid]=c
        if len(cells)==1:
            y,x=next(iter(cells))
            terms.append(Terminal(y,x,role,cid,ranks[cid],int(y in (0,h-1) or x in (0,w-1)),1))
        elif thin:
            for y,x in sorted(p for p,d in deg.items() if d<=1):
                terms.append(Terminal(y,x,role,cid,ranks[cid],int(y in (0,h-1) or x in (0,w-1)),0))
    terms=sorted(set(terms), key=lambda t:(t.y,t.x,t.role,t.cid))
    if len(terms)>MAX_TERMINALS:
        return OperationalPathRepresentation(bg,tuple(comps),tuple(terms),(),True,'too_many_terminals')

    operands=[]; seen=set()
    def add(op: PathOperand):
        k=(op.kind,op.cells,op.src,op.tgt,op.src_role,op.tgt_role,op.orientation)
        if k not in seen:
            seen.add(k); operands.append(op)

    # terminal-terminal segments/elbows
    for ta,tb in combinations(terms,2):
        a=(ta.y,ta.x); b=(tb.y,tb.x)
        straight=_straight_cells(a,b)
        if straight is not None and len(straight)>=2 and _interior_clear(g,straight,bg,{a,b}):
            add(PathOperand('segment',straight,a,b,ta.role,tb.role,ta.size_rank,tb.size_rank,ta.border,tb.border,0,_segment_oriented(a,b),len(straight)))
            # ordered reverse version because src/tgt roles may be semantically directional
            add(PathOperand('segment',tuple(reversed(straight)),b,a,tb.role,ta.role,tb.size_rank,ta.size_rank,tb.border,ta.border,0,_segment_oriented(a,b),len(straight)))
        if a[0]!=b[0] and a[1]!=b[1]:
            for bend in ((a[0],b[1]),(b[0],a[1])):
                p1=_straight_cells(a,bend); p2=_straight_cells(bend,b)
                path=_join_paths(p1,p2) if p1 and p2 else None
                if path and _interior_clear(g,path,bg,{a,b}):
                    orient='HV' if bend[0]==a[0] else 'VH'
                    add(PathOperand('elbow',path,a,b,ta.role,tb.role,ta.size_rank,tb.size_rank,ta.border,tb.border,1,orient,len(path)))
                    ro='VH' if orient=='HV' else 'HV'
                    add(PathOperand('elbow',tuple(reversed(path)),b,a,tb.role,ta.role,tb.size_rank,ta.size_rank,tb.border,ta.border,1,ro,len(path)))

    # terminal -> boundary rays
    for t in terms:
        a=(t.y,t.x)
        for ori,(dy,dx) in [('N',(-1,0)),('E',(0,1)),('S',(1,0)),('W',(0,-1))]:
            cells=[a]; y,x=a
            while True:
                ny,nx=y+dy,x+dx
                if not (0<=ny<h and 0<=nx<w): break
                cells.append((ny,nx)); y,x=ny,nx
            if len(cells)<2: continue
            path=tuple(cells)
            if _interior_clear(g,path,bg,{a}):
                b=path[-1]
                add(PathOperand('ray',path,a,b,t.role,-1,t.size_rank,-1,t.border,1,0,ori,len(path)))

    operands.sort(key=lambda z:z.sort_key)
    operands=operands[:MAX_OPERANDS]
    return OperationalPathRepresentation(bg,tuple(comps),tuple(terms),tuple(operands),False,None)


def _matches(op: PathOperand, selector: tuple[tuple[str,Any],...]) -> bool:
    return all(op.feature(k)==v for k,v in selector)


def apply_program(g: Grid, oprep: OperationalPathRepresentation, prog: PathProgram) -> Grid | None:
    if oprep.abstained: return None
    selected=[op for op in oprep.paths if _matches(op,prog.selector)]
    if not selected: return None
    out=[list(row) for row in g]
    for op in selected:
        for y,x in op.cells:
            if g[y][x]==oprep.background_role:
                out[y][x]=prog.paint_role
    return tuple(tuple(row) for row in out)


def _selector_space(first_ops: tuple[PathOperand,...]):
    selectors={()}
    # Construct 1-predicate selectors from values observed in first demo.
    one=[]
    for feat in SELECTOR_FEATURES:
        vals=sorted({op.feature(feat) for op in first_ops}, key=lambda z:(str(type(z)),str(z)))
        for v in vals:
            one.append(((feat,v),))
    for s in one: selectors.add(s)
    # Two predicates on distinct features, using co-occurring values from an actual operand.
    for op in first_ops:
        feats=[(f,op.feature(f)) for f in SELECTOR_FEATURES]
        for a,b in combinations(feats,2):
            selectors.add(tuple(sorted((a,b))))
    return sorted(selectors, key=lambda s:(len(s),tuple((k,str(v)) for k,v in s)))


def synthesize_path_programs(normalized_task: dict[str,Any]) -> tuple[list[PathProgram], list[OperationalPathRepresentation]]:
    train=[(r0.to_grid(ex['input']),r0.to_grid(ex['output'])) for ex in normalized_task['train']]
    if not train or any(_shape(x)!=_shape(y) for x,y in train):
        return [], []
    opreps=[operationalize_grid(x) for x,y in train]
    if any(o.abstained for o in opreps) or not opreps[0].paths:
        return [], opreps
    selectors=_selector_space(opreps[0].paths)
    roles=sorted({v for x,y in train for row in x for v in row})
    programs=[]; seen=set()
    for selector in selectors:
        for paint_role in roles:
            selected_count=0; painted_len=0; ok=True
            for (x,y),orep in zip(train,opreps):
                selected=[op for op in orep.paths if _matches(op,selector)]
                if not selected:
                    ok=False; break
                selected_count += len(selected)
                painted_len += sum(len(op.cells) for op in selected)
                probe=PathProgram(selector,paint_role,0,0)
                pred=apply_program(x,orep,probe)
                if pred!=y:
                    ok=False; break
            if ok:
                p=PathProgram(selector,paint_role,selected_count,painted_len)
                k=(p.selector,p.paint_role)
                if k not in seen:
                    seen.add(k); programs.append(p)
    programs.sort(key=lambda p:p.key)
    return programs, opreps

@dataclass(frozen=True)
class PathCandidate:
    rep: r1.InducedRepresentation
    normalized_task: dict[str,Any]
    program: PathProgram
    @property
    def key(self):
        return (self.rep.assignment_cost,self.rep.complexity_proxy,self.program.key,self.rep.representation_hash)


def synthesize_path_candidates(task: dict[str,Any]) -> tuple[list[PathCandidate], dict[str,int]]:
    cands=[]
    reps=r1.induce_role_representations(task)
    operationalized_hashes=set()
    for rep in reps:
        nt=r1._normalized_task(task,rep)
        if nt is None: continue
        progs,oreps=synthesize_path_programs(nt)
        if oreps and all((not o.abstained and len(o.paths)>0) for o in oreps):
            operationalized_hashes.add(rep.representation_hash)
        for p in progs:
            cands.append(PathCandidate(rep,nt,p))
    cands.sort(key=lambda c:c.key)
    return cands, {'role_representations':len(reps),'operationalized_representations':len(operationalized_hashes)}


def predict_candidate(task: dict[str,Any], cand: PathCandidate, test_index: int) -> Grid | None:
    x_orig=r0.to_grid(task['test'][test_index]['input'])
    test_map=dict(cand.rep.test_color_to_role[test_index])
    role_to_color={role:color for color,role in test_map.items()}
    nx=r1._normalize_grid(x_orig,test_map)
    if nx is None: return None
    orep=operationalize_grid(nx)
    if orep.abstained: return None
    ny=apply_program(nx,orep,cand.program)
    if ny is None: return None
    return r1._decode_grid(ny,role_to_color)


def path_top2(task: dict[str,Any]):
    cands,diag=synthesize_path_candidates(task)
    preds=[]
    for ti,_ in enumerate(task['test']):
        arr=[]; seen=set()
        for c in cands:
            y=predict_candidate(task,c,ti)
            if y is None or y in seen: continue
            seen.add(y); arr.append((y,c))
            if len(arr)>=2: break
        preds.append(arr)
    return cands,preds,diag


def task_path_oracle_solved(task: dict[str,Any], truths: list[Grid]):
    cands,diag=synthesize_path_candidates(task)
    for c in cands:
        ok=True
        for ti,t in enumerate(truths):
            if predict_candidate(task,c,ti)!=t:
                ok=False; break
        if ok: return True,c,diag,len(cands)
    return False,None,diag,len(cands)


def task_path_top2_solved(task: dict[str,Any], truths: list[Grid]):
    cands,preds,diag=path_top2(task)
    ok=all(any(y==truths[ti] for y,c in preds[ti]) for ti in range(len(truths)))
    return ok,diag,len(cands),preds

if __name__=='__main__':
    print('PATH-OP0 module loaded')
