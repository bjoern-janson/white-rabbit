# G7 Generation-Budget Calibration v0.1

Version: `G7_GENERATION_BUDGET_CALIBRATION_V0.1`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / B_STAR_ONLY / NON_COMPARATIVE`

Constitution starting authority: `78ed5693dff06aadbadf07a19e9f64cc7916e4ec`

Calibration observations executed under this constitution: `0`

This artifact prospectively constitutes an instrument calibration. It does not execute the calibration, constitute G7 v0.3, authorize treatment execution, or amend the frozen scientific estimand.

## 1. Authority and immutable lineage

The following are immutable upstream authority:

| Object | Path or identity | Authority |
| --- | --- | --- |
| Executed assay | `assays/G7_MATCHED_CONTEXT_ASSAY_V0_2.md` | commit `72b3f639a829cea5a033874f0f814d80e8d3055a` |
| Historical result | `assays/G7_MATCHED_CONTEXT_ASSAY_V0_2_RESULT.md` | commit `78ed5693dff06aadbadf07a19e9f64cc7916e4ec`, subject only to its separately authorized reporting-sentence correction |
| Canonical neutral control | `B*` | SHA-256 `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` |
| Frozen tasks and grader | Q1, Q2, Q3 and exact mechanical grader | `G7_MATCHED_CONTEXT_ASSAY_V0.2` |

The historical terminal state remains `CONTROL_ADEQUACY_FAIL`. Its censoring state remains `NOT_OPENED`, and its numerical generation-work comparison remains `NOT_OPENED`. Historical raw evidence and `derived-results.json` remain unchanged.

## 2. Calibration diagnosis

The exact observed G7 v0.2 diagnostic is:

```text
completeness/admissibility = PASS
control adequacy = FAIL
```

For canonical `B*`, all 15 admissible historical observations recorded:

```text
N_generated = 64
finish_reason = length
success = 0
```

The preserved reasoning traces include task-solving trajectories before the generation ceiling fires. The calibrated hypothesis is therefore:

```text
measurement ceiling < baseline completion requirement
```

This diagnosis does not establish that `B*` is capable under an adequate ceiling. That remains to be tested by fresh calibration observations.

## 3. Shallowest revision and sole variable

The revision locus is the execution envelope's generation budget. The sole manipulated calibration variable is:

```text
max_tokens: 64 -> 512
```

Do not reopen or modify:

- `Theta_G7`;
- `E_repr`;
- `R2`;
- `E_measurement`;
- canonical `B*`;
- treatment `C`;
- Q1, Q2, or Q3;
- target answers or the mechanical grader;
- model, tokenizer, template, or request structure;
- runtime, cold-state doctrine, or recorder doctrine.

No control redesign is authorized.

## 4. Prospectively frozen candidate budget

Freeze exactly:

```text
max_tokens = 512
```

Rationale:

- the failed ceiling was `64`;
- `512` provides an eightfold generation envelope;
- it is deliberately generous rather than minimum-seeking;
- it remains comfortably within the frozen context-size budget;
- no historical trajectory is used to estimate a minimum completion length.

This is not an optimized budget, estimated minimum, token-efficiency claim, or White Rabbit result. No budget ladder is constituted. The calibration must not search `65`, `96`, `128`, `192`, `256`, or any other alternative. If `512` fails, the calibration fails and stops; it does not automatically escalate.

## 5. Frozen condition

Exactly one condition exists:

```text
B*
```

Use the already frozen canonical control exactly, with UTF-8 SHA-256:

```text
37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663
```

Condition `C` must not be executed or inspected. This calibration contains no treatment/control comparison.

## 6. Frozen tasks and grader

Use exactly the existing frozen Q1, Q2, and Q3 task wording, request structure, target separator, target hashes, expected answers, and exact mechanical grader from `G7_MATCHED_CONTEXT_ASSAY_V0.2`.

### Q1 — integer arithmetic

```text
Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.
```

### Q2 — character reversal

```text
Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.
```

### Q3 — numeric ordering

```text
Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.
```

| Task | Expected bytes after frozen trim | Target SHA-256 |
| --- | --- | --- |
| Q1 | `486` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` |
| Q2 | `9R2m7Q` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` |
| Q3 | `-4, 0, 9, 12, 17` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` |

The calibration asks only whether the existing baseline can finish naturally when the generation ceiling is moved out of the way.

For every task, assemble the sole user-message content using the frozen request construction:

```text
<B*> + "\n\n--- TARGET ---\n" + <TARGET>
```

Carry forward the frozen compact JSON serialization, changing only the authorized budget field:

```json
{"model":"qwen38-27b","messages":[{"role":"user","content":"<ASSEMBLED_CONTENT>"}],"stream":false,"max_tokens":512}
```

Encode as UTF-8 without BOM or trailing newline, preserve compact separators and displayed member order, do not ASCII-escape Unicode, and add no fields.

## 7. Replicates and frozen order

Prospectively freeze:

```text
3 tasks x 5 independently cold B* replicates = 15 calibration observations
```

Use the `B*` projection of the existing Gate 7 replicate-major structure:

| Calibration run | Replicate | Task | Condition | Prospective status |
| ---: | ---: | --- | --- | --- |
| 01 | 1 | Q1 | `B*` | `NOT_STARTED` |
| 02 | 1 | Q2 | `B*` | `NOT_STARTED` |
| 03 | 1 | Q3 | `B*` | `NOT_STARTED` |
| 04 | 2 | Q1 | `B*` | `NOT_STARTED` |
| 05 | 2 | Q2 | `B*` | `NOT_STARTED` |
| 06 | 2 | Q3 | `B*` | `NOT_STARTED` |
| 07 | 3 | Q1 | `B*` | `NOT_STARTED` |
| 08 | 3 | Q2 | `B*` | `NOT_STARTED` |
| 09 | 3 | Q3 | `B*` | `NOT_STARTED` |
| 10 | 4 | Q1 | `B*` | `NOT_STARTED` |
| 11 | 4 | Q2 | `B*` | `NOT_STARTED` |
| 12 | 4 | Q3 | `B*` | `NOT_STARTED` |
| 13 | 5 | Q1 | `B*` | `NOT_STARTED` |
| 14 | 5 | Q2 | `B*` | `NOT_STARTED` |
| 15 | 5 | Q3 | `B*` | `NOT_STARTED` |

Ordering cannot depend on outcomes. These are calibration observations, not G7 v0.3 scientific observations, and they may never be recycled into a successor treatment comparison.

## 8. Frozen executor and cold-run doctrine

Carry forward the G7 v0.2 executor unchanged except for `max_tokens`:

| Field | Frozen value |
| --- | --- |
| llama.cpp build | `b10603` |
| llama.cpp commit | `c060ca974` |
| model | `Qwen3.8-27B-Q2_K.gguf` |
| model alias | `qwen38-27b` |
| GPU layers | `50` |
| context size | `8192` |
| parallel slots | `1` |
| Jinja | enabled |
| reasoning format | `deepseek` |
| backend | `127.0.0.2:8086` |
| recorder | `127.0.0.1:8085` |
| recorder identity | White Rabbit Recorder `v0.1.0`, reported commit `80cddb26a7b851d218f95317cd3c5b0593acd831` |
| endpoint | `POST /v1/chat/completions` |
| stream | `false` |
| `max_tokens` | `512` |
| sampling overrides | absent |
| message count | `1` |
| message role | `user` |

Every calibration observation independently requires:

- a new backend process and PID;
- a new recorder process/session;
- a startup snapshot before the request;
- zero prior measured inference requests;
- cold/LRU evidence;
- exactly one measured request;
- exactly one correlated task/slot measurement block;
- `correlation_status = EXACT`;
- raw request/response byte and hash custody;
- teardown before the next observation.

No cross-run retained KV/cache state is admissible.

## 9. Required observation custody

For every calibration observation preserve at minimum:

- task and replicate;
- admissibility and mechanical success;
- `N_generated` and `finish_reason`;
- response `content` and `reasoning_content` when exposed;
- `N_prompt` and `N_prompt,new`;
- `T_prompt`, `T_generation`, and `T_total`;
- literal reuse/cache fields when exposed;
- raw request/response hashes;
- cold-state evidence.

Missing fields remain missing. No hidden-compute inference is authorized.

## 10. Primary calibration question

The primary question is:

> Is `max_tokens = 512` non-binding for competent `B*` execution on the three frozen tasks under the frozen executor?

Two properties remain distinct.

### A. Natural termination

Every admissible calibration observation must have:

```text
finish_reason = stop
```

or an explicitly equivalent authoritative natural-completion state. Any `finish_reason = length` means the proposed generation ceiling was binding in that observation.

### B. Baseline completion

Apply the existing exact mechanical grader. For every task require:

```text
5/5 successful B* calibration observations
```

## 11. Result-state precedence

Apply exactly:

```text
1. completeness/admissibility
2. generation-budget non-binding
3. baseline completion
```

No later state may be opened when an earlier state blocks.

The only terminal states are:

- `CALIBRATION_INCOMPLETE`: one or more required observations is operationally missing or inadmissible;
- `GENERATION_BUDGET_STILL_BINDING`: any required admissible observation terminates because of the 512-token generation ceiling;
- `GENERATION_BUDGET_NONBINDING_BUT_BASELINE_INADEQUATE`: all required observations terminate naturally, but `B*` does not achieve 5/5 success on every frozen task;
- `GENERATION_BUDGET_CALIBRATION_PASS`: all 15 observations are admissible, all 15 terminate naturally, and `B*` achieves 5/5 on Q1, Q2, and Q3.

These states must not be collapsed.

## 12. Successful freeze and failure behavior

Only `GENERATION_BUDGET_CALIBRATION_PASS` earns:

```text
successor generation budget: max_tokens = 512
```

for possible future constitution of `G7_MATCHED_CONTEXT_ASSAY_V0.3`.

```text
calibration pass
!= G7 v0.3 constituted
!= G7 v0.3 executed
```

If `512` remains binding, preserve the result and stop. Do not test `768`, `1024`, or another budget automatically. If `B*` terminates naturally but fails mechanically, preserve the result and stop. Do not redesign `B*`; require a new causal or diagnostic review before another revision.

## 13. Historical-run firewall

G7 v0.2 observations remain historical evidence only. Do not:

- reuse them as calibration observations;
- mix them into calibration success counts;
- recycle them into v0.3;
- reinterpret their terminal state;
- compare historical `C` measurements numerically;
- open the historical work comparison.

Calibration begins with fresh observations after separate execution authorization.

## 14. Claim ceiling

A successful calibration establishes only:

> Under the frozen executor and canonical `B*`, `max_tokens = 512` was non-binding across the calibration observations and permitted mechanically correct natural completion of the three frozen tasks.

It does not establish a `C_improve` effect, capability non-regression versus `C`, generation-work reduction, whole-run savings, reuse, compilation, amortization, or White Rabbit.

## 15. Execution authority and absolute stop

This constitution does not authorize execution. In this authoring task:

```text
C executed: NO
B* executed: NO
calibration requests issued: 0
G7 v0.3 created: NO
```

Before separately reviewed execution authority exists, do not start llama-server or the recorder; send calibration requests; generate model output; tokenize for matching; execute `C` or `B*`; reuse historical runs; or create G7 v0.3.

## 16. Frozen terminal state

```text
artifact: G7_GENERATION_BUDGET_CALIBRATION_V0.1
status: CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / B_STAR_ONLY / NON_COMPARATIVE
failure locus: execution envelope / generation budget
sole calibration variable: max_tokens
candidate generation budget: 512
budget ladder: NOT_CONSTITUTED
condition: B*
tasks: Q1, Q2, Q3
replicates per task: 5
planned calibration observations: 15
execution order: deterministic replicate-major Q1, Q2, Q3
calibration observations executed: 0
execution authority: absent
next action: STOP + independent review
```

Move the measurement boundary out of the phenomenon.

Do not optimize the ceiling.

Calibrate the baseline without touching the treatment.

Historical failure remains evidence.

Calibration observations are not successor-assay observations.

Change one thing.
