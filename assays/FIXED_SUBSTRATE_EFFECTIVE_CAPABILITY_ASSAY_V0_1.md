# Fixed-Substrate Effective Capability Assay v0.1

Version: `FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1`

Status: `CONSTITUTED / SUBSTRATE_MANIFEST_REQUIRED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Scientific observations under this constitution: `0`

## 1. Phenomenon-selection anchor

This assay exists because White Rabbit began from a practical anomaly: a local Qwen deployment on a fixed physical machine appeared to cross into a dramatically more useful operating regime.

The historical custody record is preserved in:

- `observations/WR-OBS-001/raw_observation.md`
- `observations/WR-OBS-001/backend_correction.md`
- `observations/WR-OBS-002/raw_observation.md`

Those records select the phenomenon. They do not supply causal authority.

The backend correction established that a major part of the visible `371 -> 11` prompt-work change was consistent with longest-common-prefix / KV reuse, while a separate low-throughput runtime regime remained unexplained. Therefore this assay prospectively separates a reproducible runtime-reuse path from the candidate structured path instead of treating the original anecdote as a causal result.

The scientific question is deliberately operational:

> **Does the candidate move the useful-capability frontier of the fixed machine beyond what is explained by prospectively created reusable runtime state alone?**

## 2. Frozen upstream objects

### Task set

Path:

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_TASKSET_V0_1.json`

Freeze commit:

`fd865a75fbb7a6394326bbfd2e31a5e9ec9102e2`

Git blob:

`88c1d7ad0de9051414608a52d5534e4eaeec70ee`

The task set was frozen before any v0.1 assay execution.

`Q01-Q03` are historically exposed Gate-7 tasks and serve only as floor/calibration controls. They are excluded from the primary frontier claim.

The primary outcome-naive frontier set is exactly:

```text
Q04,Q05,Q06,Q07,Q08,Q09,Q10,Q11,Q12
```

### Condition contract

Path:

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_CONDITIONS_V0_1.json`

Freeze commit:

`f63cf1d873c4fe73fcdec14ffc29bc4481caa8d3`

Git blob:

`af8afbf2d14353ac88bd3830abd8007cc71b2949`

This file is the sole machine-readable authority for B/R/C construction.

## 3. Frozen conditions

Exactly three conditions exist.

### B — cold neutral baseline

```text
B = COLD_NEUTRAL_BASELINE
```

- canonical neutral `B*` prelude;
- fresh backend process;
- fresh recorder session;
- zero prior inference requests;
- no retained pre-request prefix/KV state;
- measured request is the first inference request.

### R — warm neutral runtime-reuse control

```text
R = WARM_NEUTRAL_RUNTIME_REUSE_CONTROL
```

- same canonical neutral `B*` prelude as B;
- same measured task request bytes as B for the same task;
- fresh backend and recorder;
- exactly one prospectively frozen acquisition request before the measured request;
- no backend restart between acquisition and measurement.

Thus the intended contrast:

```text
R - B
```

changes reusable runtime state while holding measured neutral content fixed.

It is the direct control for the known prefix/KV-reuse confound exposed by the historical observation.

### C — warm candidate structured path

```text
C = WARM_CANDIDATE_STRUCTURED_PATH
```

- literal frozen `C_improve` candidate prelude;
- same fresh-backend protocol as R;
- same one-acquisition / one-measurement state protocol as R;
- same frozen task in the measured request.

The intended contrast:

```text
C - R
```

asks whether the candidate path changes practical capability beyond the neutral path under the same runtime-reuse protocol.

This is not strengthened into a pure semantic-content effect at fixed token burden. Realized prompt length, prompt work, and reuse fields are measured consequences.

## 4. Fixed substrate

The physical target is the user's local:

```text
NVIDIA GeForce RTX 3080 Ti
```

The reference executor lineage is the existing Gate-7 Qwen stack:

```text
llama.cpp build: b10603
llama.cpp commit: c060ca974
model: Qwen3.8-27B-Q2_K.gguf
model alias: qwen38-27b
n_gpu_layers: 50
context: 8192
parallel slots: 1
jinja: enabled
reasoning format: deepseek
```

However, historical names are not sufficient identity for this assay.

Before implementation is opened, a separate non-scientific substrate manifest must freeze at minimum:

```text
exact physical GPU/device identity
GPU driver identity
backend identity and configuration
runtime binary hash / build / commit
model-file SHA-256
tokenizer identity
chat-template identity
reasoning-format configuration
context size
GPU-layer count
parallel slots
decoding/sampling configuration
generation budget
recorder/instrumentation identity
power/performance mode when externally controllable
```

The same frozen substrate manifest binds B, R, and C.

```text
NO SUBSTRATE MANIFEST => IMPLEMENTATION NOT OPENED
```

## 5. Request construction

Measured request construction is frozen by the condition contract:

```text
<PRELUDE> + "\n\n--- TARGET ---\n" + <FROZEN TASK>
```

Acquisition request construction for R/C is:

```text
<PRELUDE> + "\n\n--- TARGET ---\n" + "Return exactly READY and nothing else."
```

For any fixed task `q`:

```text
MEASURED_BYTES_B(q) = MEASURED_BYTES_R(q)
```

The C measured request differs only through the constituted candidate prelude.

Acquisition responses are custody/runtime observations only. They are not graded as scientific task outcomes and are never inserted into the measured request.

## 6. Runtime-state realization gate

The assay is specifically intended to distinguish cold from prospectively reusable runtime state.

Therefore B is admissible only if the measured request is the first inference request on a fresh backend/session.

R and C are admissible only if:

```text
one acquisition request occurred
AND
no other inference request occurred
AND
no backend restart occurred before the measured request
```

The implementation must preserve literal runtime evidence sufficient to establish the intended state distinction.

Record when authoritatively exposed:

```text
N_prompt
N_prompt,new
prompt-evaluation time
f_sim_best
f_keep
graphs_reused
explicit cached-token field
```

Do not infer cached-token counts from proxy fields.

If the intended cold/warm state distinction cannot be established from authoritative custody, the affected observation is:

```text
RUN_INADMISSIBLE_RUNTIME_STATE
```

and no capability-frontier conclusion may use it.

## 7. Primary measurement axes

The conceptual target is effective capability on a fixed substrate:

```text
Phi_eff ~ verified useful work available within a fixed wall-clock/resource envelope
```

v0.1 does **not** collapse this into one opaque scalar score.

For every measured observation preserve the raw axes:

### Q — verified task capability

```text
SUCCESS in {0,1}
```

using only the mechanical exact-byte grader frozen in the task set.

No human or model judge is used.

### L — latency

Preserve separately when exposed:

```text
TTFT
L_prefill
L_generation
L_total
```

For R/C also preserve acquisition latency separately:

```text
L_acquire
```

Acquisition latency is never silently folded away.

### W — realized executor work indicators

Preserve literally:

```text
N_prompt
N_prompt,new when exposed
N_generated
finish_reason
context/headroom fields when exposed
```

These are measurement instruments, not synonyms for cognition.

### T — execution rates

Preserve literally:

```text
prefill tokens/s
decode tokens/s
```

plus any directly exposed backend throughput fields.

### M — memory/resource pressure

Preserve authoritative peak GPU-memory / allocation / OOM evidence if the frozen instrumentation exposes it.

Missing authoritative memory instrumentation remains missing and does not get reconstructed from unrelated fields.

### F — failure state

Preserve at minimum:

```text
timeout
OOM
backend failure
request failure
length censoring
grader failure
runtime-state inadmissibility
identity/custody failure
```

Failure is not silently replaced by a rerun.

## 8. Replicates and execution order

The constituted design contains:

```text
12 tasks x 3 conditions x 3 replicates = 108 measured observations
```

and:

```text
R/C: one acquisition request per measured observation = 72 acquisition requests
```

Every measured observation receives its own fresh backend and recorder process.

For every task the condition order is prospectively balanced:

```text
replicate 1: B,R,C
replicate 2: R,C,B
replicate 3: C,B,R
```

No order may be changed because of observed latency, success, thermal behavior, or model output.

## 9. Practical feasibility sets

Freeze the practical time budgets:

```text
tau in {30 s, 60 s, 120 s}
```

For condition `X`, task `q` is feasible at budget `tau` iff:

```text
all 3 measured replicates are admissible
AND
all 3 exact-grade SUCCESS = 1
AND
median(L_total) <= tau
```

Define:

```text
F_X(tau) = set of primary novel tasks feasible under condition X at tau
```

where only `Q04-Q12` enter the primary frontier sets.

`Q01-Q03` are reported separately as historical floor controls.

The frozen time budgets are operational thresholds, not claims that human usefulness has one universal scalar cutoff.

## 10. Runtime-control result

For every frozen `tau`, report:

```text
F_B(tau)
F_R(tau)
F_R(tau) - F_B(tau)
F_B(tau) - F_R(tau)
```

A runtime-reuse frontier shift is observed at `tau` only if:

```text
F_B(tau) is a proper subset of F_R(tau)
```

That is:

```text
no B-feasible novel task becomes infeasible under R
AND
at least one novel task becomes feasible under R that was not feasible under B
```

Possible descriptive terminal:

```text
RUNTIME_REUSE_FRONTIER_SHIFT_OBSERVED_AT_FROZEN_BUDGET
```

or:

```text
RUNTIME_REUSE_FRONTIER_SHIFT_NOT_OBSERVED
```

This result concerns the prospectively constituted reusable runtime state only. It does not explain the historical unknown low-throughput regime.

## 11. Candidate effective-capability result

The primary White Rabbit v0.1 question compares C to R.

For every frozen `tau`, report:

```text
F_R(tau)
F_C(tau)
F_C(tau) - F_R(tau)
F_R(tau) - F_C(tau)
```

A candidate frontier shift is observed at `tau` only if:

```text
F_R(tau) is a proper subset of F_C(tau)
```

That is:

```text
no R-feasible novel task becomes infeasible under C
AND
at least one novel task becomes feasible under C that was not feasible under R
```

The strongest primary positive terminal is:

```text
FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_FRONTIER_SHIFT_OBSERVED
```

and requires a proper-superset C frontier at at least one of the three prospectively frozen time budgets.

If no such budget exists, emit:

```text
FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_FRONTIER_SHIFT_NOT_OBSERVED
```

This terminal does not erase mixed raw outcomes. All task-level Q/L/W/T/M/F measurements remain primary evidence.

## 12. Regime-crossing localization

For every novel task and budget preserve the exact crossing state:

```text
R infeasible, C feasible     -> candidate positive crossing
R feasible, C infeasible     -> candidate negative crossing
R feasible, C feasible       -> no feasibility crossing; compare raw axes descriptively
R infeasible, C infeasible   -> no feasibility crossing
```

The scientifically interesting unit is therefore not merely a pooled token mean.

It is possible to observe:

```text
Q_C > Q_R and L_C < L_R
Q_C = Q_R and L_C < L_R
Q_C < Q_R and L_C < L_R
```

These states must remain distinct.

## 13. Acquisition-cost firewall

R and C intentionally create reusable runtime state before the measured request.

Preserve acquisition cost separately:

```text
C_acquire,R
C_acquire,C
```

using only directly measured available fields.

v0.1 may report steady-state measured-request capability/latency after acquisition, but it may **not** claim that the acquisition paid for itself.

Freeze:

```text
steady-state effective-capability gain != amortization
```

and:

```text
L_measured improvement != lifecycle cost reduction
```

Amortization requires a later separately constituted reuse-horizon assay.

## 14. Historical observation firewall

The original WR-OBS-001/002 experience is target-selection evidence only.

No historical before/after number enters:

```text
task selection for Q04-Q12
feasibility adjudication
condition outcome
latency threshold selection after execution
terminal selection
```

The known Q01-Q03 G7 history is explicitly exposed and excluded from the primary frontier set rather than treated as outcome-naive evidence.

## 15. Claim ceiling

A positive result may establish only:

> Under the exact frozen Qwen/3080-Ti substrate, B/R/C condition contract, novel task set, runtime-state protocol, and frozen wall-clock budgets, the candidate structured path expanded the set of mechanically verified tasks that were practically feasible relative to the warm neutral runtime-reuse control.

It does **not** establish:

```text
C_improve caused the original WR-OBS-001 event
a general White Rabbit mechanism
model weights became smarter
persistent learning
held-out reuse
transfer beyond the frozen task set
amortization
lifecycle cost reduction
compounding improvement
general intelligence improvement
generalization to other models/hardware/runtimes
```

The local fixed-substrate result is the scientific object.

## 16. Pre-execution review gates

Before implementation is opened, hostile review must attack at minimum:

```text
task-oracle correctness and uniqueness
historical-exposure firewall
B/R byte identity for measured requests
R/C warm-state protocol equivalence
runtime-state observability/admissibility
substrate identity sufficiency
mechanical grader correctness
feasibility-set logic
frontier-shift terminal logic
acquisition-cost firewall
claim ceiling
```

The separate substrate manifest must also be frozen and reviewed.

Any constitution defect returns to repair.

## 17. Execution authority

This constitution authorizes none of:

```text
building a scientific runner
starting the 3080 Ti assay backend
issuing acquisition requests
issuing any of the 108 measured requests
producing B/R/C outcomes
opening result interpretation
claiming a frontier shift
```

Current state:

```text
artifact: FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1
task set: FROZEN
condition contract: FROZEN
substrate manifest: REQUIRED / NOT YET FROZEN
constitution: CONSTITUTED
hostile review: REQUIRED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
```

Next actions:

```text
1. freeze exact local substrate manifest
2. hostile-review constitution + task oracle + condition contract + substrate manifest
3. STOP
```

No runner and no scientific execution are opened by this artifact.

**The experiment is about the frontier, not the token counter.**
