from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSERVATIONS = ROOT / "observations" / "G7-generation-budget-calibration-v0.1"
RESULT = ROOT / "assays" / "G7_GENERATION_BUDGET_CALIBRATION_V0_1_RESULT.md"

VERSION = "G7_GENERATION_BUDGET_CALIBRATION_V0.1"
CONSTITUTION_COMMIT = "23cd33dad0fad7e91d1a9ebe06e7cf0f28c33c99"
B_STAR_SHA256 = "37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663"
MAX_TOKENS = 512
EXPECTED = {
    "Q1": "486",
    "Q2": "9R2m7Q",
    "Q3": "-4, 0, 9, 12, 17",
}


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def display(value: object) -> str:
    return "MISSING" if value is None else str(value)


rows: list[dict[str, object]] = []
for run in range(1, 16):
    run_dir = OBSERVATIONS / f"run-{run:02d}"
    state = load_json(run_dir / "slot-state.json")
    assert isinstance(state, dict)
    artifacts = [path for path in (run_dir / "recorder-runs").iterdir() if path.is_dir()]
    if len(artifacts) != 1:
        raise RuntimeError(f"run {run:02d}: recorder artifact count {len(artifacts)}")
    artifact = artifacts[0]
    response_raw = (artifact / "response" / "body.raw").read_bytes()
    response = json.loads(response_raw.decode("utf-8"))
    choice = response["choices"][0]
    message = choice["message"]
    content = message["content"]
    if not isinstance(content, str):
        raise TypeError(f"run {run:02d}: choices[0].message.content is not a string")
    graded = content.strip(" \t\r\n")
    timing_records = state["timing"]["records"]
    cache_records = state["cache"]["records"]
    if len(timing_records) != 1 or len(cache_records) != 1:
        raise RuntimeError(f"run {run:02d}: non-unique measurement record")
    timing = timing_records[0]
    cache = cache_records[0]
    usage = response.get("usage", {})
    finish_reason = choice.get("finish_reason")
    natural = finish_reason == "stop"
    rows.append({
        "run": run,
        "replicate": state["replicate"],
        "task": state["task"],
        "condition": state["condition"],
        "admissible": state["admissibility"] == "ADMISSIBLE",
        "success": int(graded.encode("utf-8") == EXPECTED[state["task"]].encode("utf-8")),
        "natural_termination": natural,
        "backend_pid": state["backend_pid"],
        "recorder_pid": state["recorder_pid"],
        "run_id": state["recorder_run_id"],
        "request_sha256": state["request_sha256"],
        "response_sha256": state["response_sha256"],
        "http_status": state["http_status"],
        "correlation_status": state["correlation_status"],
        "n_prompt": usage.get("prompt_tokens"),
        "n_prompt_new": timing.get("n_prompt_new"),
        "n_generated": timing.get("n_generated"),
        "finish_reason": finish_reason,
        "truncated": timing.get("truncated"),
        "t_prompt_ms": timing.get("t_prompt_ms"),
        "t_generation_ms": timing.get("t_generation_ms"),
        "t_total_ms": timing.get("t_total_ms"),
        "graphs_reused": cache.get("graphs_reused"),
        "f_sim_best": cache.get("f_sim_best"),
        "f_keep": cache.get("f_keep"),
        "n_prompt_cached": cache.get("n_prompt_cached"),
        "content": content,
        "reasoning_content": message.get("reasoning_content"),
        "failure_reason": state.get("failure_reason"),
        "checks": state.get("checks"),
    })

planned = 15
attempted = len(rows)
requests = sum(
    int(load_json(OBSERVATIONS / f"run-{run:02d}" / "slot-state.json")["request_issued"])
    for run in range(1, 16)
)
admissible = sum(int(row["admissible"]) for row in rows)
inadmissible = attempted - admissible
complete = attempted == planned and admissible == planned
all_natural = complete and all(row["natural_termination"] for row in rows)
success_counts = {
    task: sum(int(row["success"]) for row in rows if row["task"] == task)
    for task in EXPECTED
}
baseline_complete = all_natural and all(success_counts[task] == 5 for task in EXPECTED)

if not complete:
    terminal = "CALIBRATION_INCOMPLETE"
elif not all_natural:
    terminal = "GENERATION_BUDGET_STILL_BINDING"
elif not baseline_complete:
    terminal = "GENERATION_BUDGET_NONBINDING_BUT_BASELINE_INADEQUATE"
else:
    terminal = "GENERATION_BUDGET_CALIBRATION_PASS"

if not complete:
    generation_budget_state = "NOT_OPENED"
    baseline_completion_state = "NOT_OPENED"
elif not all_natural:
    generation_budget_state = "GENERATION_BUDGET_STILL_BINDING"
    baseline_completion_state = "NOT_OPENED"
else:
    generation_budget_state = "GENERATION_BUDGET_NONBINDING"
    baseline_completion_state = (
        "BASELINE_COMPLETION_OBSERVED"
        if baseline_complete
        else "BASELINE_COMPLETION_FAIL"
    )

archive = OBSERVATIONS / "raw-custody.tar.gz"
archive_sha256 = sha256_file(archive)
(OBSERVATIONS / "raw-custody.sha256").write_text(
    f"{archive_sha256}  raw-custody.tar.gz\n",
    encoding="utf-8",
)

derived = {
    "calibration_version": VERSION,
    "constitution_commit": CONSTITUTION_COMMIT,
    "b_star_sha256": B_STAR_SHA256,
    "executor": {
        "llama_cpp_build": "b10603",
        "llama_cpp_commit": "c060ca974",
        "model": "Qwen3.8-27B-Q2_K.gguf",
        "model_alias": "qwen38-27b",
        "gpu_layers": 50,
        "context_size": 8192,
        "parallel_slots": 1,
        "jinja": True,
        "reasoning_format": "deepseek",
        "backend": "127.0.0.2:8086",
        "recorder": "127.0.0.1:8085",
        "recorder_version": "0.1.0",
        "recorder_commit": "80cddb26a7b851d218f95317cd3c5b0593acd831",
        "stream": False,
        "sampling_overrides": None,
        "max_tokens": MAX_TOKENS,
    },
    "planned_observations": planned,
    "original_observations_attempted": attempted,
    "calibration_requests_issued": requests,
    "admissible": admissible,
    "inadmissible": inadmissible,
    "replacement_observations": 0,
    "rows": rows,
    "success_counts": success_counts,
    "length_terminated_observations": sum(row["finish_reason"] == "length" for row in rows),
    "natural_stop_observations": sum(row["finish_reason"] == "stop" for row in rows),
    "completeness_state": "CALIBRATION_COMPLETE" if complete else "CALIBRATION_INCOMPLETE",
    "generation_budget_state": generation_budget_state,
    "baseline_completion_state": baseline_completion_state,
    "terminal_state": terminal,
    "successor_max_tokens_earned": MAX_TOKENS if terminal == "GENERATION_BUDGET_CALIBRATION_PASS" else None,
    "g7_v0_3_created": False,
    "condition_c_executed": False,
    "raw_custody_archive_sha256": archive_sha256,
}
(OBSERVATIONS / "derived-results.json").write_text(
    json.dumps(derived, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

lines = [
    "# G7 Generation-Budget Calibration v0.1 Result",
    "",
    f"Status: `{terminal}`",
    "",
    f"Calibration constitution commit: `{CONSTITUTION_COMMIT}`",
    "",
    f"Canonical B* SHA-256: `{B_STAR_SHA256}`",
    "",
    f"Raw custody: `observations/G7-generation-budget-calibration-v0.1/`",
    "",
    f"Raw-custody archive SHA-256: `{archive_sha256}`",
    "",
    "## Frozen executor identity",
    "",
    "- llama.cpp: build `b10603`, commit `c060ca974`",
    "- model: `Qwen3.8-27B-Q2_K.gguf`; alias `qwen38-27b`",
    "- GPU layers: `50`; context size: `8192`; parallel slots: `1`",
    "- Jinja: enabled; reasoning format: `deepseek`",
    "- backend: `127.0.0.2:8086`; recorder: `127.0.0.1:8085`",
    "- recorder: `v0.1.0`, commit `80cddb26a7b851d218f95317cd3c5b0593acd831`",
    "- stream: `false`; sampling overrides: absent",
    f"- `max_tokens`: `{MAX_TOKENS}`",
    "",
    "## Execution accounting",
    "",
    f"- Planned observations: `{planned}`",
    f"- Original observations attempted: `{attempted}`",
    f"- Calibration requests issued: `{requests}`",
    f"- Admissible observations: `{admissible}`",
    f"- Inadmissible observations: `{inadmissible}`",
    "- Replacement observations: `0`",
    "- Condition C executed: `NO`",
    "",
    "## Per-run evidence",
    "",
    "| Run | Rep | Task | Adm | Success | N_prompt | N_prompt,new | N_generated | finish | T_prompt ms | T_gen ms | T_total ms | graphs_reused | f_sim_best | f_keep | cached tokens | failure reason |",
    "| ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
]
for row in rows:
    lines.append(
        f"| {row['run']:02d} | {row['replicate']} | {row['task']} | "
        f"{'YES' if row['admissible'] else 'NO'} | {row['success']} | "
        f"{display(row['n_prompt'])} | {display(row['n_prompt_new'])} | "
        f"{display(row['n_generated'])} | {display(row['finish_reason'])} | "
        f"{display(row['t_prompt_ms'])} | {display(row['t_generation_ms'])} | "
        f"{display(row['t_total_ms'])} | {display(row['graphs_reused'])} | "
        f"{display(row['f_sim_best'])} | {display(row['f_keep'])} | "
        f"{display(row['n_prompt_cached'])} | {display(row['failure_reason'])} |"
    )

lines.extend([
    "",
    "Each row traces to its recorder run ID, exact request/response hashes, backend PID, recorder PID, startup snapshot, cold-state checks, and exact correlation record in `derived-results.json`. Missing literal fields remain `MISSING`.",
    "",
    "## Mechanical task results",
    "",
    f"- Q1 B* successes: `{success_counts['Q1']}/5`",
    f"- Q2 B* successes: `{success_counts['Q2']}/5`",
    f"- Q3 B* successes: `{success_counts['Q3']}/5`",
    f"- Length-terminated observations: `{derived['length_terminated_observations']}`",
    f"- Natural-stop observations: `{derived['natural_stop_observations']}`",
    "",
    "## Frozen state progression",
    "",
    f"1. Completeness/admissibility: `{derived['completeness_state']}`",
    f"2. Generation-budget non-binding: `{generation_budget_state}`",
    f"3. Baseline completion: `{baseline_completion_state}`",
    "",
    "## Terminal interpretation",
    "",
    f"`{terminal}`",
    "",
    f"Successor `max_tokens = {MAX_TOKENS}` earned: `{'YES' if derived['successor_max_tokens_earned'] else 'NO'}`",
    "",
    "G7 v0.3 created: `NO`",
    "",
    "Condition C executed: `NO`",
    "",
    "## Historical firewall",
    "",
    "No G7 v0.2 observation was reused or counted. The historical terminal state remains `CONTROL_ADEQUACY_FAIL`; historical capability non-regression, censoring, and work comparison remain unopened.",
    "",
    "## Claim ceiling",
    "",
    "A calibration pass establishes only that, under the frozen executor and canonical B*, `max_tokens = 512` was non-binding across these 15 calibration observations and permitted mechanically correct natural completion of the three frozen tasks.",
    "",
    "It does not establish a C_improve effect, generation-work reduction, whole-run work reduction, lifecycle economics, compilation, amortization, reuse, or White Rabbit. Calibration observations are not successor-assay observations.",
    "",
])
RESULT.write_text("\n".join(lines), encoding="utf-8")

print(json.dumps({
    key: derived[key]
    for key in (
        "planned_observations",
        "original_observations_attempted",
        "calibration_requests_issued",
        "admissible",
        "inadmissible",
        "replacement_observations",
        "success_counts",
        "length_terminated_observations",
        "natural_stop_observations",
        "completeness_state",
        "generation_budget_state",
        "baseline_completion_state",
        "terminal_state",
        "successor_max_tokens_earned",
    )
}, indent=2))
