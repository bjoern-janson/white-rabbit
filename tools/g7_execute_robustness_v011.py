from __future__ import annotations
import hashlib,http.client,json,os,socket,subprocess,time
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; REC=ROOT.parent/'white-rabbit-recorder'; RUNTIME=REC/'.calibration-runtime'/'llama-b10603-verified'; SERVER=RUNTIME/'llama-server.exe'; MODEL=Path(r'C:\Users\Mewn\Models\Qwen3.8-27B\Qwen3.8-27B-Q2_K.gguf'); OUT=ROOT/'observations'/'G7-neutral-control-robustness-v0.1.1'; PY=Path(__import__('sys').executable)
B=['''internalize logic: S = L_catalog

where:

catalog = fixed convention pairing a symbol with a label, symbol
   ↓
fixed catalog relation
   ↓
corresponding catalog label
   ↓
unchanged catalog entry
   ↓
same descriptive mapping''','''internalize logic: M = N_catalog

where:

catalog = static convention associating a marker with a name, marker
   ↓
static catalog relation
   ↓
associated catalog name
   ↓
stable catalog entry
   ↓
same static correspondence''','''internalize logic: K = T_catalog

where:

catalog = immutable convention linking a code with a tag, code
   ↓
immutable catalog relation
   ↓
linked catalog tag
   ↓
fixed catalog entry
   ↓
same immutable association''','''internalize logic: S = L_catalog

where:

catalog = static convention associating a marker with a name, marker
   ↓
immutable catalog relation
   ↓
corresponding catalog label
   ↓
stable catalog entry
   ↓
same immutable association''','''internalize logic: M = N_catalog

where:

catalog = immutable convention linking a code with a tag, code
   ↓
fixed catalog relation
   ↓
associated catalog name
   ↓
unchanged catalog entry
   ↓
same descriptive mapping''','''internalize logic: K = T_catalog

where:

catalog = fixed convention pairing a symbol with a label, symbol
   ↓
static catalog relation
   ↓
linked catalog tag
   ↓
fixed catalog entry
   ↓
same static correspondence''']
C='''internalize logic: I ∝ C_improve

where:

C_improve = capacity to convert feedback into increased future viability, feedback
   ↓
better representation
   ↓
better adaptive mechanisms
   ↓
greater improvement capacity
   ↓
expanded viable futures'''
TASKS={'Q1':'Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.','Q2':'Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.','Q3':'Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.'}
ANS={'Q1':'486','Q2':'9R2m7Q','Q3':'-4, 0, 9, 12, 17'}; LABEL={1:'B0',2:'B1',3:'C',4:'B2',5:'B3',6:'B4',7:'B5'}; PRE={**{f'B{i}':B[i] for i in range(6)},'C':C}
ROWS=[[1,2,7,3,6,4,5],[2,3,1,4,7,5,6],[3,4,2,5,1,6,7],[4,5,3,6,2,7,1],[5,6,4,7,3,1,2],[6,7,5,1,4,2,3],[7,1,6,2,5,3,4],[5,4,6,3,7,2,1],[6,5,7,4,1,3,2],[7,6,1,5,2,4,3],[1,7,2,6,3,5,4],[2,1,3,7,4,6,5],[3,2,4,1,5,7,6],[4,3,5,2,6,1,7]]
SCHED=[(1,'Q1',ROWS[0]),(1,'Q2',ROWS[3]),(1,'Q3',ROWS[2]),(2,'Q1',ROWS[1]),(2,'Q2',ROWS[6]),(2,'Q3',ROWS[11]),(3,'Q1',ROWS[13]),(3,'Q2',ROWS[12]),(3,'Q3',ROWS[7]),(4,'Q1',ROWS[9]),(4,'Q2',ROWS[8]),(4,'Q3',ROWS[5]),(5,'Q1',ROWS[4]),(5,'Q2',ROWS[0]),(5,'Q3',ROWS[10])]

def sha(x): return hashlib.sha256(x).hexdigest()
def utc(): return datetime.now(timezone.utc).isoformat()
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def stop(p):
 if p and p.poll() is None:
  p.terminate()
  try:p.wait(20)
  except subprocess.TimeoutExpired:p.kill();p.wait(5)
def wait_port(p,proc):
 end=time.time()+40
 while time.time()<end:
  if proc.poll() is not None: raise RuntimeError(f'process exited {proc.returncode}')
  with socket.socket() as s:
   s.settimeout(.2)
   if s.connect_ex((p[0],p[1]))==0:return
  time.sleep(.15)
 raise TimeoutError('port readiness')
def wait_log(path,proc):
 end=time.time()+180
 while time.time()<end:
  if proc.poll() is not None:raise RuntimeError(f'backend exited {proc.returncode}')
  if path.exists() and 'listening on http://127.0.0.2:8086' in path.read_text(encoding='utf-8',errors='replace'):return
  time.sleep(.25)
 raise TimeoutError('backend readiness')

def run(n,block,rep,task,cond):
 rd=OUT/f'run-{n:03d}'; rd.mkdir(parents=True); runs=rd/'recorder-runs'; runs.mkdir(); blog=rd/'backend.log.raw'; rlog=rd/'recorder.log.raw'; content=PRE[cond]+'\n\n--- TARGET ---\n'+TASKS[task]; body=json.dumps({'model':'qwen38-27b','messages':[{'role':'user','content':content}],'stream':False,'max_tokens':512},ensure_ascii=False,separators=(',',':')).encode(); state={'run':n,'block':block,'replicate':rep,'task':task,'condition':cond,'condition_sha256':sha(PRE[cond].encode()),'request_sha256_expected':sha(body),'started_at':utc(),'request_issued':False,'admissibility':'PENDING'}; dump(rd/'slot-state.json',state); bp=rp=bh=rh=None
 cmd=[str(SERVER),'-m',str(MODEL),'-a','qwen38-27b','--host','127.0.0.2','--port','8086','-ngl','50','-c','8192','-np','1','--jinja','--reasoning-format','deepseek']
 try:
  bh=blog.open('xb'); bp=subprocess.Popen(cmd,cwd=RUNTIME,stdout=bh,stderr=subprocess.STDOUT); wait_log(blog,bp); startup=blog.read_bytes(); (rd/'startup.raw').write_bytes(startup); state.update({'backend_pid':bp.pid,'startup_sha256':sha(startup),'pre_request_task_lines':sum(b'task' in x.lower() for x in startup.splitlines())})
  env=os.environ.copy(); env.update({'PYTHONPATH':str(REC),'WR_SERVER_SESSION_ID':f'g7-rb-{n:03d}','WR_LLAMA_COMMAND':subprocess.list2cmdline(cmd),'WR_LLAMA_PID':str(bp.pid),'WR_LLAMA_LOG':str(blog),'WR_LLAMA_VERSION':'version: 0.2.0-dev (build 10603, commit c060ca974)','WR_MODEL_PATH':str(MODEL),'WR_MODEL_ALIAS':'qwen38-27b','WR_CONTEXT_SIZE':'8192','WR_GPU_LAYERS':'50','WR_PARALLEL_SLOTS':'1','WR_REASONING_FORMAT':'deepseek'}); rh=rlog.open('xb'); rp=subprocess.Popen([str(PY),'-u','-m','recorder.proxy','--listen-host','127.0.0.1','--listen-port','8085','--upstream-host','127.0.0.2','--upstream-port','8086','--runs-dir',str(runs)],cwd=REC,env=env,stdout=rh,stderr=subprocess.STDOUT); wait_port(('127.0.0.1',8085),rp); state.update({'recorder_pid':rp.pid,'request_issued':True,'request_issued_at':utc()}); dump(rd/'slot-state.json',state)
  con=http.client.HTTPConnection('127.0.0.1',8085,timeout=600); con.request('POST','/v1/chat/completions',body=body,headers={'Content-Type':'application/json','Content-Length':str(len(body))}); resp=con.getresponse(); received=resp.read(); con.close(); state.update({'http_status':resp.status,'response_received':True})
  kids=[x for x in runs.iterdir() if x.is_dir()];
  if len(kids)!=1:raise RuntimeError(f'recorder dirs={len(kids)}')
  art=kids[0]; manifest=json.loads((art/'manifest.json').read_text(encoding='utf-8')); corr=json.loads((art/'backend/correlation.json').read_text(encoding='utf-8')); timing=json.loads((art/'backend/timing.json').read_text(encoding='utf-8')); sess=json.loads((art/'server/session.json').read_text(encoding='utf-8')); slog=(art/'server/log.raw').read_text(encoding='utf-8',errors='replace'); req=(art/'request/body.raw').read_bytes(); res=(art/'response/body.raw').read_bytes(); parsed=json.loads((art/'response/parsed.jsonl').read_text(encoding='utf-8').splitlines()[0]); msg=parsed.get('choices',[{}])[0].get('message',{}); content_out=msg.get('content'); checks={'http_200':resp.status==200,'request_bytes_exact':req==body,'response_bytes_exact':res==received,'request_hash_exact':manifest['request']['sha256']==sha(body),'response_hash_exact':manifest['response']['sha256']==sha(received),'correlation_exact':corr.get('correlation_status')=='EXACT','one_measurement_block':len(timing.get('records',[]))==1,'prior_requests_zero':sess.get('prior_recorded_inference_requests')==0,'backend_pid_exact':sess.get('server_pid')==bp.pid,'cold_lru':'selected slot by LRU' in slog and 't_last = -1' in slog,'startup_no_task':state['pre_request_task_lines']==0}; trimmed=content_out.strip(' \t\r\n') if isinstance(content_out,str) else None; success=int(trimmed==ANS[task]); state.update({'recorder_run_id':art.name,'checks':checks,'correlation_status':corr.get('correlation_status'),'content':content_out,'reasoning_content':msg.get('reasoning_content'),'success':success,'finish_reason':parsed.get('choices',[{}])[0].get('finish_reason'),'n_prompt':timing.get('n_prompt'),'n_prompt_new':timing.get('n_prompt_new'),'n_generated':timing.get('n_generated'),'t_prompt_ms':timing.get('t_prompt_ms'),'t_generation_ms':timing.get('t_generation_ms'),'t_total_ms':timing.get('t_total_ms'),'graphs_reused':timing.get('graphs_reused'),'f_sim_best':timing.get('f_sim_best'),'f_keep':timing.get('f_keep'),'n_prompt_cached':timing.get('n_prompt_cached'),'truncated':parsed.get('choices',[{}])[0].get('finish_reason')=='length','request_sha256':sha(req),'response_sha256':sha(res),'admissibility':'ADMISSIBLE' if all(checks.values()) else 'RUN_INADMISSIBLE','failure_reason':None if all(checks.values()) else [k for k,v in checks.items() if not v]})
 except Exception as e: state.update({'admissibility':'RUN_INADMISSIBLE','failure_reason':f'{type(e).__name__}: {e}'})
 finally:
  stop(rp);stop(bp)
  if rh:rh.close()
  if bh:bh.close()
  state.update({'completed_at':utc(),'backend_stopped':bp is None or bp.poll() is not None,'recorder_stopped':rp is None or rp.poll() is not None});dump(rd/'slot-state.json',state)
 print(f'RUN {n:03d} BLOCK {block:02d} {task} {cond} {state["admissibility"]}',flush=True)

def main():
 if OUT.exists():raise SystemExit(f'output exists: {OUT}')
 OUT.mkdir(parents=True); dump(OUT/'execution-identity.json',{'assay':'G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0.1.1','parent_commit':'0b41a175fcf047ff3d0ec313cdb0e11485f12741','correction_commit':'90dbdadbbb5d2c974707787b83d865b72f6c599c','slots':105,'started_at':utc()})
 n=0
 for block,(rep,task,row) in enumerate(SCHED,1):
  for condnum in row:
   n+=1; run(n,block,rep,task,LABEL[condnum])
 print('ORIGINAL_105_SLOT_PASS_COMPLETE',flush=True)
if __name__=='__main__':main()
