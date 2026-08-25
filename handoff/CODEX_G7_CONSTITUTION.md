# Codex Handoff — Constitute Gate 7 Matched-Context Assay v0.1

Status: `CONSTITUTION_AUTHORING_AUTHORIZED / EXECUTION_NOT_AUTHORIZED / STOP_AFTER_SPEC`

## Mission

Create the first auditable Gate 7 assay constitution:

```text
G7_MATCHED_CONTEXT_ASSAY_V0.1
```

Target output path:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
```

This task is **specification authoring only**.

```text
Gate 6 PASS
-> Gate 7 constitution authoring
-> constitution artifact complete
-> STOP
```

Do not execute the assay.

## Read first

1. `program/GATE6_COLD_CHARACTERIZATION_MILESTONE.md`
2. `program/GATE5_REAL_SERVER_CALIBRATION_MILESTONE.md`
3. `program/STATE.md`
4. `program/ROADMAP.md`
5. `measurement/MEASUREMENT_MODEL.md`
6. `constitution/instrumentation_invariants.md`
7. `interfaces/WHITE_RABBIT_RECORDER_V0_1.md`
8. `observations/WR-OBS-002/raw_observation.md`
9. `program/WHITE_RABBIT.md`

The only admissible source for the literal `C_improve` intervention text is:

```text
observations/WR-OBS-002/raw_observation.md
```

Do not reconstruct, improve, paraphrase, or extend it from memory.

## Constitutional objective

Gate 7 asks only whether a matched-context treatment condition can preserve mechanically judged task capability while changing directly observed generation work relative to a neutral matched control under independently constituted cold runs.

It does **not** establish a White Rabbit.

The assay constitution must freeze exactly five components:

```text
1. capability criterion
2. work currency
3. independence criterion
4. matched-context control
5. replicate design
```

and must include an explicit stop/authority boundary.

---

## 1 — Capability criterion

Do not operationalize "intelligence" or use an LLM judge.

Create a small frozen set of held-out, self-contained tasks with mechanically checkable success criteria.

Requirements:

```text
- exact task payloads are frozen in the constitution;
- each task is independent of White Rabbit / C_improve content;
- no web, retrieval, external files, human adjudication, or LLM judge is required;
- correctness is determined mechanically from a frozen expected result / validator rule;
- output format is constrained enough for deterministic grading;
- target payload for a given task is byte-identical between B and C conditions;
- no task answer is present or derivable from either prelude by direct leakage.
```

Prefer a minimal set, not a benchmark suite. The constitution must state the exact task count and exact task contents.

Define realized capability for this assay only as:

```text
C_realized = mechanical task success under the frozen correctness rule
```

Minimum non-regression rule:

```text
C_treatment >= C_control
```

The constitution must make the aggregation rule explicit. It must not allow improved performance on one task to silently compensate for a material regression on another task without that fact being surfaced.

A work reduction may not rescue a capability-regression failure.

---

## 2 — Work currency

Primary directly observed work currency:

```text
C_work := N_generated
```

Secondary recorded quantities:

```text
T_generation
T_total
N_prompt,new
T_prompt
graphs_reused (literal only)
f_sim_best (only if exposed)
f_keep (only if exposed)
explicit cached-token field (only if exposed)
```

Do not invent or estimate:

```text
FLOPs
energy
reasoning effort
cached-token counts
model-visible post-template token sequence
```

`graphs_reused` must remain literal and must never be renamed cached tokens.

Gate 7 is not authorized to claim total White Rabbit compute economics. Primary comparison on `N_generated` is an assay-local work measure only.

Work results must be interpreted only after the capability criterion is evaluated. Shorter wrong answers are not computational wins.

---

## 3 — Independence criterion

Every measured observation must begin from a separately controlled cold backend.

Freeze at least the Gate 6 cold-state admissibility evidence:

```text
new backend PID
new recorder/session as required by the frozen protocol
zero pre-request task lines
prior_recorded_inference_requests = 0
first slot selection = LRU, t_last = -1
one unambiguous measurement block
exact request/task/slot correlation
no cross-run retained KV/cache state
```

A browser window, conversation reset, or request ID is not independence evidence.

If any cold-state/correlation condition fails:

```text
RUN_INADMISSIBLE
```

Do not repair or reinterpret the run into admissibility.

---

## 4 — Matched-context control

Freeze two conditions:

```text
B = neutral matched prelude + target
C = literal C_improve prelude + target
```

The target portion for each task must be byte-identical across B and C.

The `C_improve` prelude must be copied literally from the preserved WR-OBS-002 source.

The neutral prelude must be a separately frozen artifact in the constitution. It must contain no `C_improve` logic, no White Rabbit hypothesis, no metacognitive optimization instruction, and no direct task answer/help.

The constitution must include a side-by-side matching table covering at least:

```text
message count
message roles
conversational position
line/block structure
UTF-8 byte length
source-text length
prelude/target ordering
```

The neutral prelude's semantic neutrality is a **design assumption to be reviewed**, not an earned scientific fact.

### Pre-open token/context matching requirement

Because source-level similarity does not prove model-visible equality, the constitution must require a separate pre-open matching check before any Gate 7 execution is authorized.

At minimum, the future pre-open check must establish under the exact frozen model/template/runtime that B and C do not differ materially in prompt-token burden merely because of prelude length.

Prefer exact equality of total tokenized prompt length if the same tokenizer/template can establish it without generation. If exact equality is not achievable, the constitution must freeze the allowed mismatch and corresponding claim limitation **before** any assay execution.

Do not claim that HTTP-body matching establishes exact post-Jinja model token identity.

The constitution-authoring task itself must not start llama-server, recorder, tokenizer preflight, or any model process unless a separate authorization explicitly permits it. If token equality cannot be established during authoring, record:

```text
PREOPEN_TOKEN_MATCH_REQUIRED
```

rather than guessing.

---

## 5 — Replicate design

Use independent cold replicates. Do not use a single B/C realization.

Freeze:

```text
n = 5 independent runs per condition per task
```

for the first assay unless the constitution explicitly identifies a contradiction that makes this impossible. Do not silently change `n`.

For each frozen task `q_j`:

```text
B_j,1 ... B_j,5
C_j,1 ... C_j,5
```

Every replicate receives a new independently constituted cold backend under the independence criterion above.

Freeze the exact request/model/runtime/sampling configuration fields that must remain identical across conditions except for the prelude content itself.

Preserve full per-run observations. Do not replace the run distribution with only a mean.

The mechanical analysis plan must report at least:

```text
per-task success count by condition
aggregate success count by condition
N_generated per run
mean / median / min-max N_generated by condition
T_generation per run and summary
T_total per run and summary
N_prompt,new per run
all inadmissible runs and reasons
all raw artifact identifiers/hashes
```

Do not add inferential significance claims unless separately constituted. This first assay may remain descriptive/mechanical.

---

## Required assay result states

The constitution must define mechanical result labels without claiming White Rabbit success. At minimum include equivalents of:

```text
ASSAY_NOT_RUN
RUN_INADMISSIBLE
CAPABILITY_NONREGRESSION_FAIL
CAPABILITY_NONREGRESSION_OBSERVED
WORK_REDUCTION_NOT_OBSERVED
WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
ASSAY_COMPLETE_NO_WR_CLAIM
```

A work result may only be reported together with the capability result and the frozen assay-local currency.

No Gate 7 result may directly emit:

```text
WHITE_RABBIT_DEMONSTRATED
C_IMPROVE_CAUSAL
GENERAL_CAPABILITY_IMPROVED
COMPUTE_ELIMINATED
AMORTIZATION_DEMONSTRATED
CROSS_SUBSTRATE_TRANSFER
```

Those require later authority/gates.

---

## Provenance / freeze requirements

The constitution must preserve:

```text
exact literal C_improve source locator
exact neutral prelude text
exact task texts
exact expected answers / grading rules
exact replicate count
exact admissibility rules
exact work currency
exact summary calculations
exact result labels
exact forbidden claims
```

Use `SOURCE != DERIVED != INTERPRETATION` discipline.

Do not silently turn Gate 6 sample statistics into population parameters.

Explicitly preserve:

```text
Gate 6 five replicates characterize the frozen protocol
!=
underlying stochastic distribution fully known
```

---

## Hard stop / forbidden operations

The following are forbidden in this Codex task:

```text
execute C_improve
execute neutral prelude
start a treatment/control run
start llama-server for Gate 7
start the recorder for Gate 7
perform tokenizer/model preflight unless separately authorized
run any B condition
run any C condition
run capability evaluation on live model output
compare treatment/control results
open Gate 8
claim a White Rabbit effect
modify RD_HARNESS
modify white-rabbit-recorder runtime code unless a contradiction in the constitution absolutely requires a separately reported blocker
```

Constitution text may contain the literal treatment/control/task payloads. It may not send them to a model.

```text
CONSTITUTED != EXECUTED
```

After the assay constitution is written and internally audited for completeness:

```text
STOP
```

## Completion report

Return exactly enough information to audit the constitution:

```text
Gate 7 constitution version:
constitution path:
parent commit:
constitution commit:
files added:
files changed:

capability criterion frozen: YES/NO
task count:
mechanical grading frozen: YES/NO
LLM judge present: YES/NO
primary work currency:
secondary measures:
independence criterion frozen: YES/NO
neutral prelude frozen: YES/NO
literal C_improve source reused without paraphrase: YES/NO
matched-context dimensions frozen: YES/NO
pre-open token-match status: MATCHED / PREOPEN_TOKEN_MATCH_REQUIRED / BLOCKED
replicates per condition per task:
result labels frozen: YES/NO

C_improve executed: YES/NO
neutral prelude executed: YES/NO
B run executed: YES/NO
C run executed: YES/NO
llama-server started for Gate 7: YES/NO
recorder started for Gate 7: YES/NO
scientific comparison executed: YES/NO
White Rabbit claim emitted: YES/NO

ambiguities/blockers:
working tree clean: YES/NO
```

Then stop.

## Governing rule

> **Constitute the counterfactual before observing the treatment.**
