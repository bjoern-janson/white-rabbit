from __future__ import annotations
import argparse,json,time,hashlib
from collections import Counter,defaultdict
from pathlib import Path
from arc2_competition_router_candidate.r1_solver import r0_b2_solver as r0
from arc2_competition_router_candidate.r1_solver import r1_solver as r1
import joint_xt_scorer as joint

def g(a): return r0.to_grid(a['output'])
def ok(attempts,truth): return any(g(a)==truth for a in attempts)
def distinct(attempts):
    out=[]; seen=set()
    for a in attempts:
        x=g(a)
        if x not in seen: seen.add(x); out.append(a)
    return out

def router(r0res,r1res):
    a0=distinct(r0res['predictions'][0]['attempts']); a1=distinct(r1res['predictions'][0]['attempts'])
    seq=([('R0',a) for a in a0]+[('R1',a) for a in a1]) if r0res['candidate_count'] else [('R1',a) for a in a1]
    out=[]; seen=set()
    for src,a in seq:
        x=g(a)
        if x in seen: continue
        seen.add(x); out.append((src,a))
        if len(out)==2: break
    if not out:
        out=[('R0_FALLBACK',a) for a in r0res['predictions'][0]['attempts'][:2]]
    if len(out)==1: out.append((out[0][0],dict(out[0][1])))
    return out[:2]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root',type=Path); ap.add_argument('--out',type=Path,required=True); a=ap.parse_args()
    exp={'r0':'92db3a4ec0f0484773b6b19f1e65e87b84fabf5a38ba1e6698888f332e678c66','r1':'7d61faa79c8989738f72df38dd6d74800c9b8ca25435f06f0d6fb473e493b42a','joint':'524ef54095f94fc0132de8d320ab0280d7a05761adc1b9dfddf937c73aae86bb'}
    paths={'r0':Path('arc2_competition_router_candidate/r1_solver/r0_b2_solver.py'),'r1':Path('arc2_competition_router_candidate/r1_solver/r1_solver.py'),'joint':Path('joint_xt_scorer.py')}
    got={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()}
    if got!=exp: raise SystemExit(f'hash mismatch {got}')
    tot=Counter(); cats=defaultdict(Counter); rows=[]; t0=time.time()
    ps=sorted(a.root.rglob('*.json'))
    for i,p in enumerate(ps,1):
        task=json.loads(p.read_text())
        if not task.get('train') or len(task.get('test',[]))!=1 or 'output' not in task['test'][0]: continue
        truth=r0.to_grid(task['test'][0]['output']); vis={'train':task['train'],'test':[{'input':task['test'][0]['input']}]}
        z0=r0.solve_task(vis); z1=r1.solve_task_r1(vis); zj=joint.solve_joint(vis,2); zr=router(z0,z1)
        a0=z0['predictions'][0]['attempts']; a1=z1['predictions'][0]['attempts']; ar=[x[1] for x in zr]; aj=zj['predictions'][0]['attempts']
        s0=ok(a0,truth); s1=ok(a1,truth); sr=ok(ar,truth); sj=ok(aj,truth)
        union=s1 or sr; jo=sj and not s1 and not sr
        perfect_wrong=0
        if aj:
            m=aj[0]['joint_metrics']; perfect_wrong=int(m['P_trials']>0 and m['P_successes']==m['P_trials'] and g(aj[0])!=truth)
        vals=Counter(tasks=1,r0=int(s0),r1=int(s1),router=int(sr),joint=int(sj),joint_only=int(jo),reg_r1=int(s1 and not sj),reg_router=int(sr and not sj),pres_r1=int(s1 and sj),pres_router=int(sr and sj),union=int(union),pres_union=int(union and sj),joint_cov=int(zj['candidate_count']>0),r1_cov=int(z1['r1_candidate_count']>0),diff_r1=int({g(x) for x in a1}!={g(x) for x in aj}),diff_router=int({g(x) for x in ar}!={g(x) for x in aj}),perfectP_wrong=perfect_wrong)
        tot.update(vals); cats[p.parent.name].update(vals)
        rows.append({'task':str(p.relative_to(a.root)),'category':p.parent.name,'r0':s0,'r1':s1,'router':sr,'joint':sj,'joint_only':jo,'regression_vs_r1':s1 and not sj,'regression_vs_router':sr and not sj,'r0_candidates':z0['candidate_count'],'r1_representations':z1['r1_representation_count'],'r1_candidates':z1['r1_candidate_count'],'joint_candidates':zj['candidate_count'],'router_sources':[x[0] for x in zr],'joint_sources':[x['source'] for x in aj],'joint_top_metrics':None if not aj else aj[0]['joint_metrics'],'joint_top_schema':None if not aj else aj[0]['schema']})
        if i%50==0: print(f'{i}/{len(ps)} {time.time()-t0:.1f}s',flush=True)
    n=tot['tasks']
    catout={k:{'tasks':v['tasks'],'r1':v['r1'],'router':v['router'],'joint':v['joint'],'joint_only':v['joint_only'],'reg_vs_r1':v['reg_r1'],'reg_vs_router':v['reg_router']} for k,v in sorted(cats.items())}
    out={'protocol':'JOINT-XT-0 frozen prospective external test','corpus':'khalil-research/1D-ARC','corpus_commit':'1e74dc4cb4c58d8160e1fbd0ba638eb745f37147','task_count':n,'frozen_hashes':got,'r0_tasks':tot['r0'],'r1_tasks':tot['r1'],'router_tasks':tot['router'],'joint_tasks':tot['joint'],'r0_rate':tot['r0']/n,'r1_rate':tot['r1']/n,'router_rate':tot['router']/n,'joint_rate':tot['joint']/n,'N_joint_only':tot['joint_only'],'N_route_preserved_from_r1':tot['pres_r1'],'N_route_preserved_from_router':tot['pres_router'],'N_control_union_routes':tot['union'],'N_control_union_routes_preserved':tot['pres_union'],'N_regressions_vs_r1':tot['reg_r1'],'N_regressions_vs_router':tot['reg_router'],'joint_candidate_covered_tasks':tot['joint_cov'],'r1_candidate_covered_tasks':tot['r1_cov'],'attempt_sets_changed_vs_r1':tot['diff_r1'],'attempt_sets_changed_vs_router':tot['diff_router'],'top1_perfect_LOO_P_but_wrong_fresh_test':tot['perfectP_wrong'],'elapsed_seconds':time.time()-t0,'by_category':catout,'claim_ceiling':['1D-ARC was unused in prior program development before this run.','JOINT-XT-0 and controls share the same R0/R1 candidate generators; gains are selection/ranking only.','N_joint_only means top-two success absent from both control top-two sets, not new expressivity.','1D-ARC is development evidence after this run.'],'rows':rows}
    a.out.write_text(json.dumps(out,indent=2)); print(json.dumps({k:v for k,v in out.items() if k not in {'rows','by_category'}},indent=2)); print(json.dumps({'by_category':catout},indent=2))
if __name__=='__main__': main()
