from __future__ import annotations

import hashlib, http.client, json, os, shutil, socket, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT.parent / "white-rabbit-recorder"
RUNTIME = REC / ".calibration-runtime" / "llama-b10603-verified"
SERVER = RUNTIME / "llama-server.exe"
MODEL = Path(r"C:\Users\Mewn\Models\Qwen3.8-27B\Qwen3.8-27B-Q2_K.gguf")
OUT = ROOT / "observations" / "G7-V0.2"
PY = Path(sys.executable)

B = """internalize logic: S = L_catalog

where:

catalog = fixed convention pairing a symbol with a label, symbol
   ↓
fixed catalog relation
   ↓
corresponding catalog label
   ↓
unchanged catalog entry
   ↓
same descriptive mapping"""
C = """internalize logic: I ∝ C_improve

where:

C_improve = capacity to convert feedback into increased future viability, feedback
   ↓
better representation
   ↓
better adaptive mechanisms
   ↓
greater improvement capacity
   ↓
expanded viable futures"""
TASKS = {
    "Q1": "Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.",
    "Q2": "Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.",
    "Q3": "Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.",
}
ORDER = [
 (1,1,"Q1","B*"),(2,1,"Q1","C"),(3,1,"Q2","C"),(4,1,"Q2","B*"),(5,1,"Q3","B*"),(6,1,"Q3","C"),
 (7,2,"Q1","C"),(8,2,"Q1","B*"),(9,2,"Q2","B*"),(10,2,"Q2","C"),(11,2,"Q3","C"),(12,2,"Q3","B*"),
 (13,3,"Q1","B*"),(14,3,"Q1","C"),(15,3,"Q2","C"),(16,3,"Q2","B*"),(17,3,"Q3","B*"),(18,3,"Q3","C"),
 (19,4,"Q1","C"),(20,4,"Q1","B*"),(21,4,"Q2","B*"),(22,4,"Q2","C"),(23,4,"Q3","C"),(24,4,"Q3","B*"),
 (25,5,"Q1","B*"),(26,5,"Q1","C"),(27,5,"Q2","C"),(28,5,"Q2","B*"),(29,5,"Q3","B*"),(30,5,"Q3","C"),
]

def utc(): return datetime.now(timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(path, value): path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False)+"\n", encoding="utf-8")
def wait_log(path, needle, proc, timeout=180):
    end=time.time()+timeout
    while time.time()<end:
        if proc.poll() is not None: raise RuntimeError(f"backend exited {proc.returncode}")
        if path.exists() and needle in path.read_text(encoding="utf-8", errors="replace"): return
        time.sleep(.25)
    raise TimeoutError("backend readiness timeout")
def wait_port(host, port, proc, timeout=30):
    end=time.time()+timeout
    while time.time()<end:
        if proc.poll() is not None: raise RuntimeError(f"recorder exited {proc.returncode}")
        with socket.socket() as s:
            s.settimeout(.2)
            if s.connect_ex((host,port))==0: return
        time.sleep(.1)
    raise TimeoutError("recorder readiness timeout")
def stop(proc):
    if proc and proc.poll() is None:
        proc.terminate()
        try: proc.wait(15)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(5)
def one(run, rep, task, cond):
    rd=OUT/f"run-{run:02d}"
    rd.mkdir(parents=True, exist_ok=False)
    blog=rd/"backend.log.raw"; rlog=rd/"recorder.log.raw"; runs=rd/"recorder-runs"; runs.mkdir()
    pre=B if cond=="B*" else C
    content=pre+"\n\n--- TARGET ---\n"+TASKS[task]
    body=json.dumps({"model":"qwen38-27b","messages":[{"role":"user","content":content}],"stream":False,"max_tokens":64},ensure_ascii=False,separators=(",",":")).encode("utf-8")
    state={"run":run,"replicate":rep,"task":task,"condition":cond,"started_at":utc(),"request_issued":False,"request_sha256_expected":sha(body),"admissibility":"PENDING"}
    dump(rd/"slot-state.json",state)
    cmd=[str(SERVER),"-m",str(MODEL),"-a","qwen38-27b","--host","127.0.0.2","--port","8086","-ngl","50","-c","8192","-np","1","--jinja","--reasoning-format","deepseek"]
    bp=rp=None; bh=rh=None
    try:
        bh=blog.open("xb"); bp=subprocess.Popen(cmd,cwd=RUNTIME,stdout=bh,stderr=subprocess.STDOUT)
        wait_log(blog,"listening on http://127.0.0.2:8086",bp)
        startup=blog.read_bytes(); (rd/"startup.raw").write_bytes(startup)
        state.update({"backend_pid":bp.pid,"startup_sha256":sha(startup),"startup_bytes":len(startup),"pre_request_task_lines":sum(b"task" in x.lower() for x in startup.splitlines())})
        env=os.environ.copy(); env.update({
          "PYTHONPATH":str(REC),"WR_SERVER_SESSION_ID":f"g7-v02-run-{run:02d}","WR_LLAMA_COMMAND":subprocess.list2cmdline(cmd),
          "WR_LLAMA_VERSION":"version: 0.2.0-dev (build 10603, commit c060ca974)\nbuilt with Clang 20.1.8 for Windows x86_64",
          "WR_LLAMA_PID":str(bp.pid),"WR_LLAMA_LOG":str(blog),"WR_MODEL_PATH":str(MODEL),"WR_MODEL_ALIAS":"qwen38-27b",
          "WR_CONTEXT_SIZE":"8192","WR_GPU_LAYERS":"50","WR_PARALLEL_SLOTS":"1","WR_REASONING_FORMAT":"deepseek"})
        rh=rlog.open("xb"); rp=subprocess.Popen([str(PY),"-u","-m","recorder.proxy","--listen-host","127.0.0.1","--listen-port","8085","--upstream-host","127.0.0.2","--upstream-port","8086","--runs-dir",str(runs)],cwd=REC,env=env,stdout=rh,stderr=subprocess.STDOUT)
        wait_port("127.0.0.1",8085,rp); state["recorder_pid"]=rp.pid; dump(rd/"slot-state.json",state)
        con=http.client.HTTPConnection("127.0.0.1",8085,timeout=600)
        state["request_issued"]=True; state["request_issued_at"]=utc(); dump(rd/"slot-state.json",state)
        con.request("POST","/v1/chat/completions",body=body,headers={"Content-Type":"application/json","Content-Length":str(len(body))})
        resp=con.getresponse(); received=resp.read(); con.close()
        state.update({"http_status":resp.status,"response_received":True,"client_response_sha256":sha(received)})
        children=[x for x in runs.iterdir() if x.is_dir()]
        if len(children)!=1: raise RuntimeError(f"recorder run directories={len(children)}")
        art=children[0]; state["recorder_run_id"]=art.name
        req=(art/"request/body.raw").read_bytes(); res=(art/"response/body.raw").read_bytes()
        manifest=json.loads((art/"manifest.json").read_text(encoding="utf-8")); corr=json.loads((art/"backend/correlation.json").read_text(encoding="utf-8")); timing=json.loads((art/"backend/timing.json").read_text(encoding="utf-8")); cache=json.loads((art/"backend/cache.json").read_text(encoding="utf-8")); sess=json.loads((art/"server/session.json").read_text(encoding="utf-8")); slog=(art/"server/log.raw").read_text(encoding="utf-8",errors="replace")
        checks={"http_200":resp.status==200,"request_bytes_exact":req==body,"response_bytes_exact":res==received,"request_hash_exact":manifest["request"]["sha256"]==sha(body),"response_hash_exact":manifest["response"]["sha256"]==sha(received),"correlation_exact":corr.get("correlation_status")=="EXACT","one_measurement_block":len(timing.get("records",[]))==1,"prior_requests_zero":sess.get("prior_recorded_inference_requests")==0,"backend_pid_exact":sess.get("server_pid")==bp.pid,"cold_lru":("selected slot by LRU" in slog and "t_last = -1" in slog),"startup_no_task":state["pre_request_task_lines"]==0}
        state.update({"checks":checks,"request_sha256":sha(req),"response_sha256":sha(res),"correlation_status":corr.get("correlation_status"),"timing":timing,"cache":cache,"server_session":sess,"admissibility":"ADMISSIBLE" if all(checks.values()) else "RUN_INADMISSIBLE","failure_reason":None if all(checks.values()) else [k for k,v in checks.items() if not v]})
    except Exception as e:
        state.update({"admissibility":"RUN_INADMISSIBLE","failure_reason":f"{type(e).__name__}: {e}","response_received":state.get("response_received",False)})
    finally:
        stop(rp); stop(bp)
        if rh: rh.close()
        if bh: bh.close()
        state["completed_at"]=utc(); state["backend_stopped"]=bp is None or bp.poll() is not None; state["recorder_stopped"]=rp is None or rp.poll() is not None
        dump(rd/"slot-state.json",state)
    print(f"RUN {run:02d} {task} {cond} {state['admissibility']} issued={state['request_issued']}",flush=True)

def main():
    if OUT.exists(): raise SystemExit(f"refusing existing output: {OUT}")
    OUT.mkdir(parents=True)
    dump(OUT/"execution-identity.json",{"assay_commit":"72b3f639a829cea5a033874f0f814d80e8d3055a","manifest_commit":"a8fc1685c042b28944386a060342d3a4ff14d402","started_at":utc(),"slots":30})
    for row in ORDER: one(*row)
    print("ORIGINAL_30_SLOT_PASS_COMPLETE",flush=True)
if __name__=="__main__": main()
