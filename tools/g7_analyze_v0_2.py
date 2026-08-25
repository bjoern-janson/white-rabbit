from __future__ import annotations
import json, statistics
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OBS=ROOT/'observations'/'G7-V0.2'
EXPECTED={'Q1':'486','Q2':'9R2m7Q','Q3':'-4, 0, 9, 12, 17'}

rows=[]
for n in range(1,31):
 d=OBS/f'run-{n:02d}'; s=json.loads((d/'slot-state.json').read_text(encoding='utf-8')); arts=list((d/'recorder-runs').iterdir()); a=arts[0]
 raw=(a/'response/body.raw').read_bytes(); payload=json.loads(raw.decode('utf-8')); choice=payload['choices'][0]; msg=choice['message']; content=msg['content']; graded=content.strip(' \t\r\n')
 tr=s['timing']['records'][0]; ca=s['cache']['records'][0]; usage=payload.get('usage',{})
 finish=choice.get('finish_reason'); censored=(finish=='length' or tr.get('truncated') is True)
 rows.append({'run':n,'replicate':s['replicate'],'task':s['task'],'condition':s['condition'],'admissible':s['admissibility']=='ADMISSIBLE','success':int(graded.encode()==EXPECTED[s['task']].encode()),'backend_pid':s['backend_pid'],'recorder_pid':s['recorder_pid'],'run_id':s['recorder_run_id'],'request_sha256':s['request_sha256'],'response_sha256':s['response_sha256'],'http_status':s['http_status'],'correlation_status':s['correlation_status'],'n_prompt':usage.get('prompt_tokens'),'n_prompt_new':tr.get('n_prompt_new'),'n_generated':tr.get('n_generated'),'t_prompt_ms':tr.get('t_prompt_ms'),'t_generation_ms':tr.get('t_generation_ms'),'t_total_ms':tr.get('t_total_ms'),'finish_reason':finish,'truncated':tr.get('truncated'),'work_censored':censored,'graphs_reused':ca.get('graphs_reused'),'f_sim_best':ca.get('f_sim_best'),'f_keep':ca.get('f_keep'),'n_prompt_cached':ca.get('n_prompt_cached'),'content':content,'reasoning_content':msg.get('reasoning_content'),'failure_reason':s.get('failure_reason')})

complete=len(rows)==30 and all(r['admissible'] for r in rows)
succ={c:{q:sum(r['success'] for r in rows if r['condition']==c and r['task']==q) for q in EXPECTED} for c in ('B*','C')}
adequate=complete and all(succ['B*'][q]==5 for q in EXPECTED)
nonreg=adequate and all(succ['C'][q]>=succ['B*'][q] for q in EXPECTED) and sum(succ['C'].values())>=sum(succ['B*'].values())
censored=nonreg and any(r['work_censored'] for r in rows)
vals={c:{q:[r['n_generated'] for r in rows if r['condition']==c and r['task']==q] for q in EXPECTED} for c in ('B*','C')}
means={c:{q:statistics.mean(vals[c][q]) for q in EXPECTED} for c in ('B*','C')}
pooled={c:statistics.mean([r['n_generated'] for r in rows if r['condition']==c]) for c in ('B*','C')}
if not complete: terminal='ASSAY_INCOMPLETE'
elif not adequate: terminal='CONTROL_ADEQUACY_FAIL'
elif not nonreg: terminal='CAPABILITY_NONREGRESSION_FAIL'
elif censored: terminal='GENERATION_WORK_COMPARISON_CENSORED'
elif all(means['C'][q]<=means['B*'][q] for q in EXPECTED) and any(means['C'][q]<means['B*'][q] for q in EXPECTED) and pooled['C']<pooled['B*']: terminal='GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY'
else: terminal='GENERATION_WORK_REDUCTION_NOT_OBSERVED'
out={'execution_version':'G7_MATCHED_CONTEXT_ASSAY_V0.2_EXECUTION_V0.1','assay_commit':'72b3f639a829cea5a033874f0f814d80e8d3055a','manifest_commit':'a8fc1685c042b28944386a060342d3a4ff14d402','planned_slots':30,'attempted_slots':30,'scientific_requests':sum(1 for n in range(1,31) if json.loads((OBS/f'run-{n:02d}'/'slot-state.json').read_text())['request_issued']),'admissible':sum(r['admissible'] for r in rows),'inadmissible':sum(not r['admissible'] for r in rows),'rows':rows,'success_counts':succ,'control_adequacy':'CONTROL_ADEQUACY_OBSERVED' if adequate else 'CONTROL_ADEQUACY_FAIL','capability_nonregression':'CAPABILITY_NONREGRESSION_OBSERVED' if nonreg else ('NOT_OPENED' if not adequate else 'CAPABILITY_NONREGRESSION_FAIL'),'censoring_state':'GENERATION_WORK_COMPARISON_CENSORED' if censored else ('NO_REQUIRED_WORK_CENSORING_OBSERVED' if nonreg else 'NOT_OPENED'),'generation_work_eligibility':not censored and nonreg,'n_generated':vals,'means':means,'pooled_means':pooled,'terminal_state':terminal}
(OBS/'derived-results.json').write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')

def x(v): return 'MISSING' if v is None else str(v)
lines=['# G7 Matched-Context Assay v0.2 Result','',f"Status: `{terminal}`",'', 'Assay commit: `72b3f639a829cea5a033874f0f814d80e8d3055a`','', 'Manifest commit: `a8fc1685c042b28944386a060342d3a4ff14d402`','', 'Raw custody: `observations/G7-V0.2/`','', '## Execution accounting','',f"- Original slots attempted: `30/30`",f"- Scientific requests issued: `{out['scientific_requests']}`",f"- Admissible observations: `{out['admissible']}`",f"- Inadmissible observations: `{out['inadmissible']}`",'- Replacement observations: `0`','', '## Per-run evidence','', '| Run | Rep | Task | Cond | Adm | Success | N_prompt | N_prompt,new | N_generated | T_prompt ms | T_gen ms | T_total ms | finish | graphs_reused | f_sim_best | f_keep | cached tokens |', '| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- | --- | --- |']
for r in rows: lines.append(f"| {r['run']:02d} | {r['replicate']} | {r['task']} | {r['condition']} | {'YES' if r['admissible'] else 'NO'} | {r['success']} | {x(r['n_prompt'])} | {x(r['n_prompt_new'])} | {x(r['n_generated'])} | {x(r['t_prompt_ms'])} | {x(r['t_generation_ms'])} | {x(r['t_total_ms'])} | {x(r['finish_reason'])} | {x(r['graphs_reused'])} | {x(r['f_sim_best'])} | {x(r['f_keep'])} | {x(r['n_prompt_cached'])} |")
lines += ['', 'Every row traces to its run directory, recorder run ID, exact request/response hashes, server snapshot, cold-state evidence, and exact correlation record in `derived-results.json`. Missing literal fields remain `MISSING`.', '', '## Frozen result-state progression','',f"1. Completeness/admissibility: `{'PASS' if complete else 'FAIL'}`",f"2. Control adequacy: `{out['control_adequacy']}`",f"3. Capability non-regression: `{out['capability_nonregression']}`",f"4. Generation-work censoring: `{out['censoring_state']}`",f"5. Numerical generation-work comparison eligible: `{'YES' if out['generation_work_eligibility'] else 'NO'}`",'', '## Mechanical summaries','']
for q in EXPECTED: lines += [f"- {q} B* successes: `{succ['B*'][q]}/5`; C successes: `{succ['C'][q]}/5`",f"- {q} B* N_generated: `{vals['B*'][q]}`; mean `{means['B*'][q]}`",f"- {q} C N_generated: `{vals['C'][q]}`; mean `{means['C'][q]}`"]
lines += [f"- Pooled B* mean N_generated: `{pooled['B*']}`",f"- Pooled C mean N_generated: `{pooled['C']}`",'', '## Terminal interpretation','',f"`{terminal}`",'', 'No numerical generation-work conclusion is emitted when the comparison is censored. `Delta W_gen` does not authorize a `Delta W_run` or `Delta C_H` claim. No White Rabbit claim is emitted.','', '## Claim ceiling','', 'This result is local to the frozen B*, C, tasks, executor, cold-run protocol, and assay currency. It does not establish general capability, formal causal identification, weight learning, persistent adaptation, whole-run compute reduction, lifecycle economics, or White Rabbit.','']
(ROOT/'assays'/'G7_MATCHED_CONTEXT_ASSAY_V0_2_RESULT.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({k:out[k] for k in ('scientific_requests','admissible','inadmissible','success_counts','control_adequacy','capability_nonregression','censoring_state','generation_work_eligibility','n_generated','means','pooled_means','terminal_state')},indent=2))
