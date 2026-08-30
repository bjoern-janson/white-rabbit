from __future__ import annotations
import json, sys
from pathlib import Path

ROOT=Path('/tmp/r1')
sys.path.insert(0,str(ROOT))
from r1_solver import r0_b2_solver as r0
from r1_solver import r1_solver as r1


def visible_and_truth(task):
    visible={"train":task["train"],"test":[{"input":ex["input"]} for ex in task["test"]]}
    truths=[r0.to_grid(ex["output"]) for ex in task["test"]]
    return visible, truths


def r1_all_outputs(visible, ti):
    x_orig=r0.to_grid(visible['test'][ti]['input'])
    out=[]; seen=set()
    for rank,cand in enumerate(r1.synthesize_r1(visible)):
        rep=cand.representation
        test_map=dict(rep.test_color_to_role[ti])
        role_to_color={role:color for color,role in test_map.items()}
        nx=r1._normalize_grid(x_orig,test_map)
        if nx is None: continue
        try: ny=cand.program.apply(nx)
        except Exception: continue
        if ny is None: continue
        y=r1._decode_grid(ny,role_to_color)
        if y is None or not y or not y[0] or len(y)>30 or len(y[0])>30: continue
        if y in seen: continue
        seen.add(y)
        out.append({'unique_rank':len(out),'candidate_rank':rank,'grid':y,'hash':r0.grid_hash(y),'rep':rep.descriptor(),'program':cand.program.descriptor()})
    return out


def distinct_r0_attempts(res, ti, admitted):
    if not admitted: return []
    out=[]; seen=set()
    for a in res['predictions'][ti]['attempts']:
        g=r0.to_grid(a['output'])
        if g not in seen:
            seen.add(g); out.append(('R0',g,a))
    return out


def current_r1_attempts(res, ti):
    out=[]; seen=set()
    for a in res['predictions'][ti]['attempts']:
        g=r0.to_grid(a['output'])
        if g not in seen:
            seen.add(g); out.append(('R1',g,a))
    return out


def conservative_union(r0res,r1res,ti):
    chosen=[]; seen=set()
    if r0res['candidate_count']>0:
        for src,g,a in distinct_r0_attempts(r0res,ti,True):
            if g not in seen:
                seen.add(g); chosen.append((src,g))
                if len(chosen)==2: return chosen
    for src,g,a in current_r1_attempts(r1res,ti):
        if g not in seen:
            seen.add(g); chosen.append((src,g))
            if len(chosen)==2: return chosen
    if not chosen:
        for a in r0res['predictions'][ti]['attempts']:
            g=r0.to_grid(a['output'])
            if g not in seen:
                seen.add(g); chosen.append(('R0_FALLBACK',g))
                if len(chosen)==2: break
    if len(chosen)==1: chosen.append(chosen[0])
    return chosen[:2]


def main(corpus,out):
    corpus=Path(corpus); rows=[]; union_task=union_out=r0_task=r0_out=r1_task=r1_out=0
    regression_details=[]; r0_solved_audit=[]; all_output_diffs=0; union_regressions=[]; union_new=[]
    for p in sorted(corpus.rglob('*.json')):
        task=json.loads(p.read_text())
        if not isinstance(task,dict) or 'train' not in task or 'test' not in task: continue
        visible,truths=visible_and_truth(task)
        r0res=r0.solve_task(visible); r1res=r1.solve_task_r1(visible,truths)
        r0oks=[]; r1oks=[]; uoks=[]; tests=[]
        for ti,truth in enumerate(truths):
            r0attempt=[r0.to_grid(a['output']) for a in r0res['predictions'][ti]['attempts']]
            r1attempt=[r0.to_grid(a['output']) for a in r1res['predictions'][ti]['attempts']]
            ro=any(g==truth for g in r0attempt); r1o=any(g==truth for g in r1attempt)
            union=conservative_union(r0res,r1res,ti); uo=any(g==truth for _,g in union)
            r0oks.append(ro); r1oks.append(r1o); uoks.append(uo)
            if {r0.grid_hash(g) for g in r0attempt}!={r0.grid_hash(g) for g in r1attempt}: all_output_diffs+=1
            allr1=r1_all_outputs(visible,ti) if ro else []
            correct_entries=[x for x in allr1 if x['grid']==truth]
            tests.append({'test_index':ti,'r0_correct':ro,'r1_correct':r1o,'union_correct':uo,'r0_attempt_hashes':[r0.grid_hash(g) for g in r0attempt],'r1_attempt_hashes':[r0.grid_hash(g) for g in r1attempt],'union_sources':[s for s,_ in union],'union_hashes':[r0.grid_hash(g) for _,g in union],'correct_exists_anywhere_in_r1_candidates':bool(correct_entries),'best_correct_r1_unique_rank':(correct_entries[0]['unique_rank'] if correct_entries else None),'best_correct_r1_candidate_rank':(correct_entries[0]['candidate_rank'] if correct_entries else None)})
        a=all(r0oks); b=all(r1oks); u=all(uoks)
        r0_task+=a; r1_task+=b; union_task+=u; r0_out+=sum(r0oks);r1_out+=sum(r1oks);union_out+=sum(uoks)
        row={'task':str(p.relative_to(corpus)),'r0_candidates':r0res['candidate_count'],'r1_representations':r1res['r1_representation_count'],'r1_candidates':r1res['r1_candidate_count'],'r0_outputs':sum(r0oks),'r1_outputs':sum(r1oks),'union_outputs':sum(uoks),'r0_task':a,'r1_task':b,'union_task':u,'tests':tests}
        rows.append(row)
        if a:
            r0_solved_audit.append(row)
            if not b: regression_details.append(row)
            if not u: union_regressions.append(str(p.relative_to(corpus)))
        if u and not a: union_new.append(str(p.relative_to(corpus)))
    for row in regression_details:
        lost=[t for t in row['tests'] if t['r0_correct'] and not t['r1_correct']]
        if all(t['correct_exists_anywhere_in_r1_candidates'] for t in lost): row['regression_class']='R1_RANKING_DISPLACED_CORRECT_R0'
        elif any(t['correct_exists_anywhere_in_r1_candidates'] for t in lost): row['regression_class']='MIXED_R1_RANKING_AND_REPRESENTATION'
        else: row['regression_class']='R1_REPRESENTATION_EXCLUDES_CORRECT_ROUTE_AND_DISPLACES_R0'
    summary={'protocol':'Post-hoc regression audit; frozen R0/R1, no solver changes','task_count':len(rows),'output_count':sum(len(r['tests']) for r in rows),'r0_tasks':r0_task,'r1_tasks':r1_task,'conservative_union_tasks':union_task,'r0_outputs':r0_out,'r1_outputs':r1_out,'conservative_union_outputs':union_out,'r0_full_task_regressions_under_r1':len(regression_details),'r0_full_task_regressions_under_union':len(union_regressions),'union_new_full_tasks_vs_r0':len(union_new),'union_new_task_names':union_new,'r0_solved_task_audit':r0_solved_audit,'regression_details':regression_details,'all_output_attempt_set_differences':all_output_diffs,'claim_ceiling':['This audit reuses ConceptARC-160 after observing R1.0 results and is post-hoc development analysis.','The conservative union is a truth-free counterfactual routing policy, not fresh validation evidence.','No representation-construction or transformation mechanism was changed.']}
    Path(out).write_text(json.dumps(summary,indent=2))
    print(json.dumps({k:v for k,v in summary.items() if k not in ('r0_solved_task_audit','regression_details')},indent=2))
    print('REGRESSIONS')
    for x in regression_details: print(json.dumps(x,indent=2))

if __name__=='__main__': main(sys.argv[1],sys.argv[2])
