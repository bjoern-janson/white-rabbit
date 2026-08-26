from __future__ import annotations
import hashlib,json,statistics,tarfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; OBS=ROOT/'observations'/'G7-neutral-control-robustness-v0.1.1'; RESULT=ROOT/'assays'/'G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md'
TASKS=['Q1','Q2','Q3']; CONDITIONS=['B0','B1','B2','B3','B4','B5','C']; ANS={'Q1':'486','Q2':'9R2m7Q','Q3':'-4, 0, 9, 12, 17'}
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def getrow(n):
    s=read(OBS/f'run-{n:03d}'/'slot-state.json'); art=next((OBS/f'run-{n:03d}'/'recorder-runs').iterdir())
    parsed=read(art/'response/parsed.jsonl'); v=parsed.get('value',{}); ch=v.get('choices',[{}])[0]; msg=ch.get('message',{}); timing=read(art/'backend/timing.json'); rec=(timing.get('records') or [{}])[0]
    s.update({'content':msg.get('content'),'reasoning_content':msg.get('reasoning_content'),'finish_reason':ch.get('finish_reason'),'n_prompt':v.get('usage',{}).get('prompt_tokens'),'n_prompt_new':rec.get('n_prompt_new'),'n_prompt_cached':v.get('usage',{}).get('prompt_tokens_details',{}).get('cached_tokens'),'n_generated':rec.get('n_generated'),'t_prompt_ms':rec.get('t_prompt_ms'),'t_generation_ms':rec.get('t_generation_ms'),'t_total_ms':rec.get('t_total_ms'),'graphs_reused':None,'f_sim_best':None,'f_keep':None,'truncated':rec.get('truncated'),'recorder_run_id':art.name,'response_sha256':sha(art/'response/body.raw'),'request_sha256':sha(art/'request/body.raw'),'success':int(isinstance(msg.get('content'),str) and msg['content'].strip(' \\t\\r\\n')==ANS[s['task']]),'censored':ch.get('finish_reason')=='length' or rec.get('truncated') is True})
    return s
def main():
    rows=[getrow(n) for n in range(1,106)]
    complete=len(rows)==105 and all(r.get('admissibility')=='ADMISSIBLE' and all(r.get('checks',{}).values()) for r in rows)
    successes={c:{t:sum(r['success'] for r in rows if r['condition']==c and r['task']==t) for t in TASKS} for c in CONDITIONS}
    control=complete and all(successes[c][t]==5 for c in CONDITIONS[:-1] for t in TASKS)
    nonreg=control and all(successes['C'][t]>=5 for t in TASKS)
    censored=nonreg and any(r['censored'] for r in rows)
    vals={c:{t:[r['n_generated'] for r in rows if r['condition']==c and r['task']==t] for t in TASKS} for c in CONDITIONS}
    means={c:{t:statistics.mean(vals[c][t]) for t in TASKS} for c in CONDITIONS}; medians={c:{t:statistics.median(vals[c][t]) for t in TASKS} for c in CONDITIONS}; mins={c:{t:min(vals[c][t]) for t in TASKS} for c in CONDITIONS}; maxs={c:{t:max(vals[c][t]) for t in TASKS} for c in CONDITIONS}; pooled={c:statistics.mean([x for t in TASKS for x in vals[c][t]]) for c in CONDITIONS}
    pair={}
    for c in CONDITIONS[:-1]:
        pair[c]={'taskwise_pass':{t:means['C'][t]<=means[c][t] for t in TASKS},'pooled_pass':pooled['C']<pooled[c],'pass':all(means['C'][t]<=means[c][t] for t in TASKS) and pooled['C']<pooled[c],'task_differences':{t:means['C'][t]-means[c][t] for t in TASKS},'pooled_difference':pooled['C']-pooled[c]}
    k=sum(x['pass'] for x in pair.values())
    if not complete: terminal='ASSAY_INCOMPLETE'
    elif not control: terminal='PANEL_CONTROL_ADEQUACY_FAIL'
    elif not nonreg: terminal='CAPABILITY_NONREGRESSION_FAIL'
    elif censored: terminal='ROBUSTNESS_WORK_COMPARISON_CENSORED'
    elif k==6: terminal='ROBUST_CONTROL_REALIZATION_ADVANTAGE_OBSERVED'
    elif k>=1: terminal='CONTROL_REALIZATION_DEPENDENCE_OBSERVED'
    else: terminal='ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED'
    archive=OBS/'raw-custody.tar.gz'
    with tarfile.open(archive,'w:gz') as tar:
        tar.add(OBS,arcname=OBS.name,filter=lambda x:None if x.name.endswith(archive.name) else x)
    archive_sha=sha(archive); (OBS/'raw-custody.sha256').write_text(f'{archive_sha}  raw-custody.tar.gz\n',encoding='utf-8')
    derived={'assay':'G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0.1.1','parent_commit':'0b41a175fcf047ff3d0ec313cdb0e11485f12741','correction_commit':'90dbdadbbb5d2c974707787b83d865b72f6c599c','planned_observations':105,'original_attempted':105,'scientific_requests':105,'admissible':sum(r['admissibility']=='ADMISSIBLE' for r in rows),'inadmissible':sum(r['admissibility']!='ADMISSIBLE' for r in rows),'replacements':0,'rows':rows,'successes':successes,'panel_adequacy':'PANEL_CONTROL_ADEQUACY_OBSERVED' if control else 'PANEL_CONTROL_ADEQUACY_FAIL','c_capability':'CAPABILITY_NONREGRESSION_OBSERVED' if nonreg else 'CAPABILITY_NONREGRESSION_FAIL','censoring':'NO_REQUIRED_WORK_CENSORING_OBSERVED' if nonreg and not censored else 'ROBUSTNESS_WORK_COMPARISON_CENSORED','values':vals,'means':means,'medians':medians,'minimums':mins,'maximums':maxs,'pooled_means':pooled,'pairwise':pair,'K':k,'terminal_state':terminal,'archive_sha256':archive_sha}
    (OBS/'derived-results.json').write_text(json.dumps(derived,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    lines=['# Gate 7 Neutral-Control Robustness Assay v0.1.1 Result','',f'Status: {terminal}','',f'Parent constitution: 0b41a175fcf047ff3d0ec313cdb0e11485f12741',f'Verification correction: 90dbdadbbb5d2c974707787b83d865b72f6c599c','',f'Original observations attempted: 105/105',f'Admissible: {derived["admissible"]}; inadmissible: {derived["inadmissible"]}; replacements: 0','',f'Raw archive SHA-256: {archive_sha}','', '## Frozen precedence','',f'1. Completeness/admissibility: {"PASS" if complete else "FAIL"}',f'2. Panel control adequacy: {derived["panel_adequacy"]}',f'3. C capability: {derived["c_capability"]}',f'4. Censoring: {derived["censoring"]}',f'5. Pairwise comparisons opened: {"YES" if nonreg and not censored else "NO"}','', '## Per-condition/task summaries','', '| Condition | Task | Values | Mean | Median | Min | Max |','| --- | --- | --- | ---: | ---: | ---: | ---: |']
    for c in CONDITIONS:
        for t in TASKS: lines.append(f'| {c} | {t} | {vals[c][t]} | {means[c][t]} | {medians[c][t]} | {mins[c][t]} | {maxs[c][t]} |')
    lines += ['', '## Pairwise robustness', '', '| Control | Task differences C-Bi | Pooled difference | PASS |','| --- | --- | ---: | --- |']
    for c in CONDITIONS[:-1]: lines.append(f'| {c} | {pair[c]["task_differences"]} | {pair[c]["pooled_difference"]} | {"PASS" if pair[c]["pass"] else "FAIL"} |')
    lines += ['',f'K / 6: {k}/6','', '## FINAL TERMINAL STATE','',terminal,'', 'All 105 observations are fresh. No historical observation was reused. Delta W_gen does not authorize Delta W_run or Delta C_H. No White Rabbit claim is emitted.','', 'Literal secondary fields, run IDs, hashes, PIDs, and checks are in observations/G7-neutral-control-robustness-v0.1.1/derived-results.json. Missing fields remain missing.','', '## Claim ceiling','', 'Any positive result is conditional on the exact six-control structural panel, frozen tasks, executor, cold-run protocol, and N_generated currency. It does not establish robustness across all 729 controls, a family-average effect, other tasks/models, persistent learning, whole-run compute reduction, lifecycle economics, or White Rabbit.','']
    RESULT.write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({'admissible':derived['admissible'],'inadmissible':derived['inadmissible'],'successes':successes,'terminal':terminal,'K':k,'archive_sha256':archive_sha},indent=2))
if __name__=='__main__': main()
