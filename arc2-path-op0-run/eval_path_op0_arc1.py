from __future__ import annotations
import argparse, json, sys, hashlib, time
from pathlib import Path
from typing import Any

# Workflow sets PYTHONPATH so these resolve to frozen files.
import path_op0 as path0
from r1_solver import r1_solver as r1
from r1_solver import r0_b2_solver as r0

Grid=r0.Grid

def truths(task):
    return [r0.to_grid(ex['output']) for ex in task['test']]

def r0_route_outputs(task, ti):
    x=r0.to_grid(task['test'][ti]['input'])
    out=[]; seen=set()
    for p in r0.synthesize(task):
        try: y=p.apply(x)
        except Exception: continue
        if y is None or y in seen: continue
        seen.add(y); out.append((y, {'source':'R0','program':p.descriptor()}))
    return out

def r1_route_outputs(task, ti):
    xorig=r0.to_grid(task['test'][ti]['input'])
    out=[]; seen=set()
    for c in r1.synthesize_r1(task):
        tm=dict(c.representation.test_color_to_role[ti])
        rtoc={role:color for color,role in tm.items()}
        nx=r1._normalize_grid(xorig,tm)
        if nx is None: continue
        try: ny=c.program.apply(nx)
        except Exception: continue
        if ny is None: continue
        y=r1._decode_grid(ny,rtoc)
        if y is None or y in seen: continue
        seen.add(y); out.append((y, {'source':'R1','representation_hash':c.representation.representation_hash,'program':c.program.descriptor()}))
    return out

def path_route_outputs(task, ti, cands=None):
    if cands is None:
        cands,_=path0.synthesize_path_candidates(task)
    out=[]; seen=set()
    for c in cands:
        y=path0.predict_candidate(task,c,ti)
        if y is None or y in seen: continue
        seen.add(y); out.append((y, {'source':'PATH_OP0','representation_hash':c.rep.representation_hash,'program':c.program.descriptor()}))
    return out

def all_output_solved(attempts_by_test, ts):
    return all(any(y==ts[ti] for y,_meta in attempts_by_test[ti]) for ti in range(len(ts)))

def any_single_route_r0(task, ts):
    tests=[r0.to_grid(ex['input']) for ex in task['test']]
    for p in r0.synthesize(task):
        ok=True
        for x,t in zip(tests,ts):
            try: y=p.apply(x)
            except Exception: ok=False; break
            if y!=t: ok=False; break
        if ok: return True
    return False

def any_single_route_r1(task, ts):
    tests=[r0.to_grid(ex['input']) for ex in task['test']]
    for c in r1.synthesize_r1(task):
        ok=True
        for ti,(xorig,t) in enumerate(zip(tests,ts)):
            tm=dict(c.representation.test_color_to_role[ti]); rtoc={role:color for color,role in tm.items()}
            nx=r1._normalize_grid(xorig,tm)
            if nx is None: ok=False; break
            try: ny=c.program.apply(nx)
            except Exception: ok=False; break
            y=r1._decode_grid(ny,rtoc) if ny is not None else None
            if y!=t: ok=False; break
        if ok: return True
    return False

def build_conservative(task, path_cands=None, include_path=False):
    # R0 route authority first, then R1, then PATH-OP0. Only distinct outputs fill the 2-slot budget.
    result=[]
    fallback=r0.solve_task(task)
    for ti,_ in enumerate(task['test']):
        arr=[]; seen=set()
        sources=[]
        streams=[r0_route_outputs(task,ti), r1_route_outputs(task,ti)]
        if include_path:
            streams.append(path_route_outputs(task,ti,path_cands))
        for stream in streams:
            for y,meta in stream:
                if y in seen: continue
                seen.add(y); arr.append((y,meta)); sources.append(meta['source'])
                if len(arr)>=2: break
            if len(arr)>=2: break
        # schema-safe fallback only after admitted route sources are exhausted
        if len(arr)<2:
            for a in fallback['predictions'][ti]['attempts']:
                y=r0.to_grid(a['output'])
                if y in seen: continue
                seen.add(y); arr.append((y,{'source':'FALLBACK'})); sources.append('FALLBACK')
                if len(arr)>=2: break
        if len(arr)==1: arr.append(arr[0])
        result.append(arr[:2])
    return result

def load_tasks(root: Path):
    files=sorted(root.glob('*.json'))
    for p in files:
        yield p.stem,json.loads(p.read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('eval_dir')
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    root=Path(args.eval_dir)
    rows=[]
    t0=time.time()
    for idx,(tid,task) in enumerate(load_tasks(root),1):
        ts=truths(task)
        reps=r1.induce_role_representations(task)
        path_cands,pdiag=path0.synthesize_path_candidates(task)
        operationalized=pdiag['operationalized_representations']>0
        executable=len(path_cands)>0

        # Pure PATH top2 and oracle-within-family.
        path_attempts=[]
        for ti in range(len(ts)):
            path_attempts.append(path_route_outputs(task,ti,path_cands)[:2])
        path_top2=all_output_solved(path_attempts,ts) if path_attempts else False
        path_oracle=False
        oracle_key=None
        for c in path_cands:
            if all(path0.predict_candidate(task,c,ti)==ts[ti] for ti in range(len(ts))):
                path_oracle=True; oracle_key=c.program.descriptor(); break

        r0_any=any_single_route_r0(task,ts)
        r1_any=any_single_route_r1(task,ts)
        new_route=bool(path_top2 and not r0_any and not r1_any)

        base_attempts=build_conservative(task,path_cands,False)
        plus_attempts=build_conservative(task,path_cands,True)
        base_solved=all_output_solved(base_attempts,ts)
        plus_solved=all_output_solved(plus_attempts,ts)

        rows.append({
            'task_id':tid,
            'train_pairs':len(task['train']),
            'test_outputs':len(task['test']),
            'role_active':bool(reps),
            'role_representation_count':len(reps),
            'operationalized':operationalized,
            'operationalized_representation_count':pdiag['operationalized_representations'],
            'path_candidate_count':len(path_cands),
            'executable':executable,
            'path_top2_solved':path_top2,
            'path_oracle_single_program_solved':path_oracle,
            'path_oracle_program':oracle_key,
            'r0_any_correct_route':r0_any,
            'r1_any_correct_route':r1_any,
            'strict_new_route':new_route,
            'baseline_conservative_solved':base_solved,
            'path_portfolio_solved':plus_solved,
            'portfolio_gain':bool(plus_solved and not base_solved),
            'portfolio_regression':bool(base_solved and not plus_solved),
            'path_attempt_sources':[ [meta['source'] for _y,meta in arr] for arr in path_attempts],
            'portfolio_attempt_sources':[ [meta['source'] for _y,meta in arr] for arr in plus_attempts],
        })
        if idx%25==0:
            print(f'processed {idx} tasks in {time.time()-t0:.1f}s', flush=True)

    n=len(rows)
    cnt=lambda key:sum(bool(r[key]) for r in rows)
    executable=cnt('executable'); exact=cnt('path_top2_solved')
    summary={
        'protocol':'PATH-OP0 fresh external evaluation; frozen before reading ARC-AGI-1 evaluation task contents',
        'corpus':'fchollet/ARC-AGI data/evaluation',
        'task_count':n,
        'N_role_active':cnt('role_active'),
        'N_operationalized':cnt('operationalized'),
        'N_executable':executable,
        'N_exact_top2':exact,
        'N_exact_oracle_single_program':cnt('path_oracle_single_program_solved'),
        'N_new_routes':cnt('strict_new_route'),
        'rho_path': (exact/executable if executable else None),
        'candidate_inflation_tasks':executable-exact,
        'baseline_conservative_solved':cnt('baseline_conservative_solved'),
        'path_portfolio_solved':cnt('path_portfolio_solved'),
        'portfolio_gains':cnt('portfolio_gain'),
        'portfolio_regressions':cnt('portfolio_regression'),
        'elapsed_seconds':time.time()-t0,
        'frozen_hashes':{
            'path_op0_py':'40d3fea73b7c2c27cc5b5188e4c0fda0079ba40bbc9ee3a9b32e56501e7b29c0',
            'preregistration':'023f9a0d8eac6a5d67b988cf7a494d1637fa3fd199e9d5b965450bc49eaa25ce',
            'r0_b2':'92db3a4ec0f0484773b6b19f1e65e87b84fabf5a38ba1e6698888f332e678c66',
            'r1_0':'7d61faa79c8989738f72df38dd6d74800c9b8ca25435f06f0d6fb473e493b42a',
        },
        'claim_ceiling':[
            'ARC-AGI-1 evaluation becomes development evidence for PATH-OP0 after this run.',
            'A positive result supports bounded path operand construction only; it does not establish general graph/path reasoning.',
            'A primitive whose arguments require new unit construction is not counted as pure executor power.'
        ]
    }
    out={'summary':summary,'rows':rows}
    Path(args.out).write_text(json.dumps(out,indent=2))
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
