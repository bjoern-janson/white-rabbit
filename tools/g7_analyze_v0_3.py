from __future__ import annotations

import hashlib
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OBS = ROOT / "observations" / "G7-V0.3"
RESULT = ROOT / "assays" / "G7_MATCHED_CONTEXT_ASSAY_V0_3_RESULT.md"
EXPECTED = {"Q1": "486", "Q2": "9R2m7Q", "Q3": "-4, 0, 9, 12, 17"}
ASSAY_COMMIT = "00874aa34d2d0a2d4644765bd4e89a293d12d01a"
B_HASH = "37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663"
C_HASH = "62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def show(value):
    return "MISSING" if value is None else str(value)


rows = []
for number in range(1, 31):
    run_dir = OBS / f"run-{number:02d}"
    state = load(run_dir / "slot-state.json")
    artifacts = [p for p in (run_dir / "recorder-runs").iterdir() if p.is_dir()]
    if len(artifacts) != 1:
        raise RuntimeError(f"run {number:02d}: recorder artifact count={len(artifacts)}")
    artifact = artifacts[0]
    payload = json.loads((artifact / "response" / "body.raw").read_text(encoding="utf-8"))
    choice = payload["choices"][0]
    message = choice["message"]
    content = message["content"]
    if not isinstance(content, str):
        raise TypeError(f"run {number:02d}: response content is not string")
    graded = content.strip(" \t\r\n")
    timing = state["timing"]["records"]
    cache = state["cache"]["records"]
    if len(timing) != 1 or len(cache) != 1:
        raise RuntimeError(f"run {number:02d}: measurement block count is not one")
    timing = timing[0]
    cache = cache[0]
    usage = payload.get("usage", {})
    finish = choice.get("finish_reason")
    rows.append({
        "run": number,
        "replicate": state["replicate"],
        "task": state["task"],
        "condition": state["condition"],
        "admissible": state["admissibility"] == "ADMISSIBLE",
        "success": int(graded.encode("utf-8") == EXPECTED[state["task"]].encode("utf-8")),
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
        "t_prompt_ms": timing.get("t_prompt_ms"),
        "t_generation_ms": timing.get("t_generation_ms"),
        "t_total_ms": timing.get("t_total_ms"),
        "finish_reason": finish,
        "truncated": timing.get("truncated"),
        "graphs_reused": cache.get("graphs_reused"),
        "f_sim_best": cache.get("f_sim_best"),
        "f_keep": cache.get("f_keep"),
        "n_prompt_cached": cache.get("n_prompt_cached"),
        "content": content,
        "reasoning_content": message.get("reasoning_content"),
        "failure_reason": state.get("failure_reason"),
        "checks": state.get("checks"),
    })

attempted = len(rows)
issued = sum(bool(load(OBS / f"run-{n:02d}" / "slot-state.json")["request_issued"]) for n in range(1, 31))
admissible = sum(int(r["admissible"]) for r in rows)
complete = attempted == 30 and admissible == 30
success = {
    condition: {task: sum(r["success"] for r in rows if r["condition"] == condition and r["task"] == task) for task in EXPECTED}
    for condition in ("B*", "C")
}
control = complete and all(success["B*"][task] == 5 for task in EXPECTED)
nonreg = control and all(success["C"][task] >= success["B*"][task] for task in EXPECTED) and sum(success["C"].values()) >= sum(success["B*"].values())
censored = nonreg and any(r["finish_reason"] == "length" or r["truncated"] is True for r in rows)
values = {condition: {task: [r["n_generated"] for r in rows if r["condition"] == condition and r["task"] == task] for task in EXPECTED} for condition in ("B*", "C")}
means = {condition: {task: statistics.mean(values[condition][task]) for task in EXPECTED} for condition in values}
medians = {condition: {task: statistics.median(values[condition][task]) for task in EXPECTED} for condition in values}
mins = {condition: {task: min(values[condition][task]) for task in EXPECTED} for condition in values}
maxs = {condition: {task: max(values[condition][task]) for task in EXPECTED} for condition in values}
pooled = {condition: statistics.mean([r["n_generated"] for r in rows if r["condition"] == condition]) for condition in ("B*", "C")}

if not complete:
    terminal = "ASSAY_INCOMPLETE"
elif not control:
    terminal = "CONTROL_ADEQUACY_FAIL"
elif not nonreg:
    terminal = "CAPABILITY_NONREGRESSION_FAIL"
elif censored:
    terminal = "GENERATION_WORK_COMPARISON_CENSORED"
elif all(means["C"][task] <= means["B*"][task] for task in EXPECTED) and any(means["C"][task] < means["B*"][task] for task in EXPECTED) and pooled["C"] < pooled["B*"]:
    terminal = "GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY"
else:
    terminal = "GENERATION_WORK_REDUCTION_NOT_OBSERVED"

control_state = "CONTROL_ADEQUACY_OBSERVED" if control else "CONTROL_ADEQUACY_FAIL"
nonreg_state = "CAPABILITY_NONREGRESSION_OBSERVED" if nonreg else ("NOT_OPENED" if not control else "CAPABILITY_NONREGRESSION_FAIL")
censor_state = "GENERATION_WORK_COMPARISON_CENSORED" if censored else ("NO_REQUIRED_WORK_CENSORING_OBSERVED" if nonreg else "NOT_OPENED")
eligible = bool(nonreg and not censored)
archive_sha = file_sha(OBS / "raw-custody.tar.gz")
(OBS / "raw-custody.sha256").write_text(f"{archive_sha}  raw-custody.tar.gz\n", encoding="utf-8")

derived = {
    "assay_commit": ASSAY_COMMIT,
    "manifest_commit": None,
    "b_star_sha256": B_HASH,
    "c_sha256": C_HASH,
    "max_tokens": 512,
    "planned_slots": 30,
    "attempted_slots": attempted,
    "scientific_requests": issued,
    "admissible": admissible,
    "inadmissible": attempted - admissible,
    "replacement_observations": 0,
    "rows": rows,
    "success_counts": success,
    "control_adequacy": control_state,
    "capability_nonregression": nonreg_state,
    "censoring_state": censor_state,
    "generation_work_eligibility": eligible,
    "n_generated": values,
    "means": means,
    "medians": medians,
    "minimums": mins,
    "maximums": maxs,
    "pooled_means": pooled,
    "terminal_state": terminal,
    "raw_custody_archive_sha256": archive_sha,
}
(OBS / "derived-results.json").write_text(json.dumps(derived, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

lines = [
    "# G7 Matched-Context Assay v0.3 Result", "", f"Status: `{terminal}`", "",
    f"Assay commit: `{ASSAY_COMMIT}`", "", "Operational manifest: `NONE`", "",
    f"B* SHA-256: `{B_HASH}`", "", f"C SHA-256: `{C_HASH}`", "",
    f"Raw custody: `observations/G7-V0.3/`", "", f"Raw-custody archive SHA-256: `{archive_sha}`", "",
    "## Executor identity", "",
    "- llama.cpp: build `b10603`, commit `c060ca974`", "- model: `Qwen3.8-27B-Q2_K.gguf`; alias `qwen38-27b`",
    "- GPU layers: `50`; context: `8192`; parallel slots: `1`; Jinja: enabled; reasoning format: `deepseek`",
    "- backend: `127.0.0.2:8086`; recorder: `127.0.0.1:8085`; recorder v0.1.0 commit `80cddb26a7b851d218f95317cd3c5b0593acd831`",
    "- stream: `false`; sampling overrides: absent; max_tokens: `512`", "",
    "## Execution accounting", "", f"- Original slots attempted: `{attempted}/30`", f"- Scientific requests issued: `{issued}`", f"- Admissible observations: `{admissible}`", f"- Inadmissible observations: `{attempted - admissible}`", "- Replacements: `0`", "",
    "## Per-run evidence", "",
    "| Run | Rep | Task | Cond | Adm | Success | N_prompt | N_prompt,new | N_generated | Finish | T_prompt ms | T_gen ms | T_total ms | Graphs | f_sim_best | f_keep | Cached tokens | Failure |",
    "| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |",
]
for r in rows:
    lines.append(f"| {r['run']:02d} | {r['replicate']} | {r['task']} | {r['condition']} | {'YES' if r['admissible'] else 'NO'} | {r['success']} | {show(r['n_prompt'])} | {show(r['n_prompt_new'])} | {show(r['n_generated'])} | {show(r['finish_reason'])} | {show(r['t_prompt_ms'])} | {show(r['t_generation_ms'])} | {show(r['t_total_ms'])} | {show(r['graphs_reused'])} | {show(r['f_sim_best'])} | {show(r['f_keep'])} | {show(r['n_prompt_cached'])} | {show(r['failure_reason'])} |")
lines += ["", "Every row traces to its recorder run ID, exact request/response hashes, backend/recorder PIDs, startup snapshot, cold-state evidence, and exact correlation record in `derived-results.json`. Missing literal fields remain `MISSING`.", "", "## Mechanical summaries", ""]
for task in EXPECTED:
    lines += [f"- {task} B* successes: `{success['B*'][task]}/5`; C successes: `{success['C'][task]}/5`", f"- {task} B* N_generated: `{values['B*'][task]}`; mean `{means['B*'][task]}`; median `{medians['B*'][task]}`; min `{mins['B*'][task]}`; max `{maxs['B*'][task]}`", f"- {task} C N_generated: `{values['C'][task]}`; mean `{means['C'][task]}`; median `{medians['C'][task]}`; min `{mins['C'][task]}`; max `{maxs['C'][task]}`"]
lines += [f"- Pooled B* mean N_generated: `{pooled['B*']}`", f"- Pooled C mean N_generated: `{pooled['C']}`", "", "## Frozen precedence", "", f"1. Completeness/admissibility: `{'PASS' if complete else 'FAIL'}`", f"2. Control adequacy: `{control_state}`", f"3. Capability non-regression: `{nonreg_state}`", f"4. Censoring: `{censor_state}`", f"5. Generation-work eligibility: `{'YES' if eligible else 'NO'}`", "", "## Terminal interpretation", "", f"`{terminal}`", "", "No result from a later gate is emitted when an earlier gate blocks. `Delta W_gen` does not authorize `Delta W_run` or `Delta C_H`. No White Rabbit claim is emitted.", "", "## Historical firewall", "", "No G7 v0.2 or budget-calibration observation was reused or pooled. All v0.3 values are fresh.", "", "## Claim ceiling", "", "This result is local to canonical B*, the literal C treatment, the frozen tasks, executor, cold-run protocol, and N_generated assay currency. It does not establish universal neutral-control robustness, persistent adaptation, weight learning, C_improve -> Phi, whole-run compute reduction, lifecycle economics, reuse, compilation, amortization, transfer, or White Rabbit.", ""]
RESULT.write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({k: derived[k] for k in ("planned_slots", "attempted_slots", "scientific_requests", "admissible", "inadmissible", "success_counts", "control_adequacy", "capability_nonregression", "censoring_state", "generation_work_eligibility", "n_generated", "means", "medians", "minimums", "maximums", "pooled_means", "terminal_state")}, indent=2))
