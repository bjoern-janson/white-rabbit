from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORDER_ROOT = ROOT.parent / "white-rabbit-recorder"
RUNTIME = RECORDER_ROOT / ".calibration-runtime" / "llama-b10603-verified"
SERVER = RUNTIME / "llama-server.exe"
MODEL = Path(r"C:\Users\Mewn\Models\Qwen3.8-27B\Qwen3.8-27B-Q2_K.gguf")
OUTPUT = ROOT / "observations" / "G7-generation-budget-calibration-v0.1"
PYTHON = Path(sys.executable)

VERSION = "G7_GENERATION_BUDGET_CALIBRATION_V0.1"
CONSTITUTION_COMMIT = "23cd33dad0fad7e91d1a9ebe06e7cf0f28c33c99"
B_STAR_SHA256 = "37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663"
MAX_TOKENS = 512

B_STAR = """internalize logic: S = L_catalog

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

TASKS = {
    "Q1": "Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.",
    "Q2": "Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.",
    "Q3": "Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.",
}

TASK_SHA256 = {
    "Q1": "eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23",
    "Q2": "3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1",
    "Q3": "886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400",
}

ORDER = [
    (1, 1, "Q1"), (2, 1, "Q2"), (3, 1, "Q3"),
    (4, 2, "Q1"), (5, 2, "Q2"), (6, 2, "Q3"),
    (7, 3, "Q1"), (8, 3, "Q2"), (9, 3, "Q3"),
    (10, 4, "Q1"), (11, 4, "Q2"), (12, 4, "Q3"),
    (13, 5, "Q1"), (14, 5, "Q2"), (15, 5, "Q3"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def endpoint_is_open(host: str, port: int) -> bool:
    with socket.socket() as probe:
        probe.settimeout(0.25)
        return probe.connect_ex((host, port)) == 0


def wait_for_log(path: Path, needle: str, process: subprocess.Popen[bytes], timeout: int = 300) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"backend exited before readiness: {process.returncode}")
        if path.exists() and needle in path.read_text(encoding="utf-8", errors="replace"):
            return
        time.sleep(0.25)
    raise TimeoutError("backend readiness timeout")


def wait_for_port(host: str, port: int, process: subprocess.Popen[bytes], timeout: int = 30) -> None:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"recorder exited before readiness: {process.returncode}")
        if endpoint_is_open(host, port):
            return
        time.sleep(0.1)
    raise TimeoutError("recorder readiness timeout")


def stop_controlled(process: subprocess.Popen[bytes] | None) -> None:
    if process is None or process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(15)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(5)


def request_body(task: str) -> bytes:
    content = B_STAR + "\n\n--- TARGET ---\n" + TASKS[task]
    payload = {
        "model": "qwen38-27b",
        "messages": [{"role": "user", "content": content}],
        "stream": False,
        "max_tokens": MAX_TOKENS,
    }
    return json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def verify_frozen_inputs() -> dict[str, object]:
    actual_b = sha256_bytes(B_STAR.encode("utf-8"))
    if actual_b != B_STAR_SHA256:
        raise RuntimeError(f"B* hash mismatch: {actual_b}")
    actual_tasks = {task: sha256_bytes(text.encode("utf-8")) for task, text in TASKS.items()}
    if actual_tasks != TASK_SHA256:
        raise RuntimeError(f"task hash mismatch: {actual_tasks}")
    if not SERVER.is_file():
        raise FileNotFoundError(SERVER)
    if not MODEL.is_file():
        raise FileNotFoundError(MODEL)
    if not RECORDER_ROOT.is_dir():
        raise FileNotFoundError(RECORDER_ROOT)
    if OUTPUT.exists():
        raise RuntimeError(f"refusing existing output path: {OUTPUT}")
    occupied = [
        f"{host}:{port}"
        for host, port in (("127.0.0.2", 8086), ("127.0.0.1", 8085))
        if endpoint_is_open(host, port)
    ]
    if occupied:
        raise RuntimeError(f"required endpoint already occupied: {occupied}")
    bodies = {task: sha256_bytes(request_body(task)) for task in TASKS}
    return {
        "version": VERSION,
        "constitution_commit": CONSTITUTION_COMMIT,
        "b_star_sha256": actual_b,
        "task_sha256": actual_tasks,
        "request_sha256": bodies,
        "max_tokens": MAX_TOKENS,
        "planned_observations": len(ORDER),
        "condition": "B*",
        "server": str(SERVER),
        "model": str(MODEL),
    }


def execute_one(run: int, replicate: int, task: str) -> None:
    if endpoint_is_open("127.0.0.2", 8086) or endpoint_is_open("127.0.0.1", 8085):
        raise RuntimeError("controlled endpoint occupied before run")

    run_dir = OUTPUT / f"run-{run:02d}"
    run_dir.mkdir(parents=True, exist_ok=False)
    backend_log = run_dir / "backend.log.raw"
    recorder_log = run_dir / "recorder.log.raw"
    recorder_runs = run_dir / "recorder-runs"
    recorder_runs.mkdir()
    body = request_body(task)

    state: dict[str, object] = {
        "calibration_version": VERSION,
        "constitution_commit": CONSTITUTION_COMMIT,
        "run": run,
        "replicate": replicate,
        "task": task,
        "condition": "B*",
        "max_tokens": MAX_TOKENS,
        "started_at": utc_now(),
        "request_issued": False,
        "request_sha256_expected": sha256_bytes(body),
        "admissibility": "PENDING",
    }
    write_json(run_dir / "slot-state.json", state)

    server_command = [
        str(SERVER),
        "-m", str(MODEL),
        "-a", "qwen38-27b",
        "--host", "127.0.0.2",
        "--port", "8086",
        "-ngl", "50",
        "-c", "8192",
        "-np", "1",
        "--jinja",
        "--reasoning-format", "deepseek",
    ]

    backend: subprocess.Popen[bytes] | None = None
    recorder: subprocess.Popen[bytes] | None = None
    backend_handle = None
    recorder_handle = None
    try:
        backend_handle = backend_log.open("xb")
        backend = subprocess.Popen(
            server_command,
            cwd=RUNTIME,
            stdout=backend_handle,
            stderr=subprocess.STDOUT,
        )
        wait_for_log(backend_log, "listening on http://127.0.0.2:8086", backend)
        startup = backend_log.read_bytes()
        (run_dir / "startup.raw").write_bytes(startup)
        state.update({
            "backend_pid": backend.pid,
            "startup_sha256": sha256_bytes(startup),
            "startup_bytes": len(startup),
            "pre_request_task_lines": sum(b"task" in line.lower() for line in startup.splitlines()),
        })

        environment = os.environ.copy()
        environment.update({
            "PYTHONPATH": str(RECORDER_ROOT),
            "WR_SERVER_SESSION_ID": f"g7-budget-cal-v01-run-{run:02d}",
            "WR_LLAMA_COMMAND": subprocess.list2cmdline(server_command),
            "WR_LLAMA_VERSION": "version: 0.2.0-dev (build 10603, commit c060ca974)\nbuilt with Clang 20.1.8 for Windows x86_64",
            "WR_LLAMA_PID": str(backend.pid),
            "WR_LLAMA_LOG": str(backend_log),
            "WR_MODEL_PATH": str(MODEL),
            "WR_MODEL_ALIAS": "qwen38-27b",
            "WR_CONTEXT_SIZE": "8192",
            "WR_GPU_LAYERS": "50",
            "WR_PARALLEL_SLOTS": "1",
            "WR_REASONING_FORMAT": "deepseek",
        })
        recorder_handle = recorder_log.open("xb")
        recorder = subprocess.Popen(
            [
                str(PYTHON), "-u", "-m", "recorder.proxy",
                "--listen-host", "127.0.0.1",
                "--listen-port", "8085",
                "--upstream-host", "127.0.0.2",
                "--upstream-port", "8086",
                "--runs-dir", str(recorder_runs),
            ],
            cwd=RECORDER_ROOT,
            env=environment,
            stdout=recorder_handle,
            stderr=subprocess.STDOUT,
        )
        wait_for_port("127.0.0.1", 8085, recorder)
        state["recorder_pid"] = recorder.pid
        write_json(run_dir / "slot-state.json", state)

        connection = http.client.HTTPConnection("127.0.0.1", 8085, timeout=1800)
        state["request_issued"] = True
        state["request_issued_at"] = utc_now()
        write_json(run_dir / "slot-state.json", state)
        connection.request(
            "POST",
            "/v1/chat/completions",
            body=body,
            headers={"Content-Type": "application/json", "Content-Length": str(len(body))},
        )
        response = connection.getresponse()
        received = response.read()
        connection.close()
        state.update({
            "http_status": response.status,
            "response_received": True,
            "client_response_sha256": sha256_bytes(received),
        })

        artifacts = [path for path in recorder_runs.iterdir() if path.is_dir()]
        if len(artifacts) != 1:
            raise RuntimeError(f"recorder run directory count: {len(artifacts)}")
        artifact = artifacts[0]
        state["recorder_run_id"] = artifact.name
        request_raw = (artifact / "request" / "body.raw").read_bytes()
        response_raw = (artifact / "response" / "body.raw").read_bytes()
        manifest = json.loads((artifact / "manifest.json").read_text(encoding="utf-8"))
        correlation = json.loads((artifact / "backend" / "correlation.json").read_text(encoding="utf-8"))
        timing = json.loads((artifact / "backend" / "timing.json").read_text(encoding="utf-8"))
        cache = json.loads((artifact / "backend" / "cache.json").read_text(encoding="utf-8"))
        session = json.loads((artifact / "server" / "session.json").read_text(encoding="utf-8"))
        server_log = (artifact / "server" / "log.raw").read_text(encoding="utf-8", errors="replace")

        checks = {
            "http_200": response.status == 200,
            "request_bytes_exact": request_raw == body,
            "response_bytes_exact": response_raw == received,
            "request_hash_exact": manifest["request"]["sha256"] == sha256_bytes(body),
            "response_hash_exact": manifest["response"]["sha256"] == sha256_bytes(received),
            "correlation_exact": correlation.get("correlation_status") == "EXACT",
            "one_measurement_block": len(timing.get("records", [])) == 1,
            "prior_requests_zero": session.get("prior_recorded_inference_requests") == 0,
            "backend_pid_exact": session.get("server_pid") == backend.pid,
            "cold_lru": "selected slot by LRU" in server_log and "t_last = -1" in server_log,
            "startup_no_task": state["pre_request_task_lines"] == 0,
        }
        state.update({
            "checks": checks,
            "request_sha256": sha256_bytes(request_raw),
            "response_sha256": sha256_bytes(response_raw),
            "correlation_status": correlation.get("correlation_status"),
            "timing": timing,
            "cache": cache,
            "server_session": session,
            "admissibility": "ADMISSIBLE" if all(checks.values()) else "RUN_INADMISSIBLE",
            "failure_reason": None if all(checks.values()) else [key for key, value in checks.items() if not value],
        })
    except Exception as error:
        state.update({
            "admissibility": "RUN_INADMISSIBLE",
            "failure_reason": f"{type(error).__name__}: {error}",
            "response_received": state.get("response_received", False),
        })
    finally:
        stop_controlled(recorder)
        stop_controlled(backend)
        if recorder_handle is not None:
            recorder_handle.close()
        if backend_handle is not None:
            backend_handle.close()
        state["completed_at"] = utc_now()
        state["backend_stopped"] = backend is None or backend.poll() is not None
        state["recorder_stopped"] = recorder is None or recorder.poll() is not None
        write_json(run_dir / "slot-state.json", state)

    print(
        f"RUN {run:02d} rep={replicate} task={task} B* "
        f"{state['admissibility']} issued={state['request_issued']}",
        flush=True,
    )


def execute() -> None:
    identity = verify_frozen_inputs()
    OUTPUT.mkdir(parents=True)
    write_json(
        OUTPUT / "execution-identity.json",
        {**identity, "started_at": utc_now(), "scientific_condition_executed": False},
    )
    for slot in ORDER:
        execute_one(*slot)
    print("ORIGINAL_15_SLOT_CALIBRATION_COMPLETE", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    arguments = parser.parse_args()
    if arguments.preflight:
        print(json.dumps(verify_frozen_inputs(), indent=2, sort_keys=True))
        return
    execute()


if __name__ == "__main__":
    main()
