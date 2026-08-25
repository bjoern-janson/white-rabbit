# G7 Matched-Context Assay v0.2

Version: `G7_MATCHED_CONTEXT_ASSAY_V0.2`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Constitution starting authority: `39a718a2540d4ad37b9d86e7372cf6e3f59d88f4`

Scientific observations executed under this constitution: `0`

This artifact prospectively constitutes a future Gate 7 assay. It does not authorize or execute that assay.

## 1. Authority and immutable lineage

The following artifacts are immutable upstream authority for this constitution:

| Authority | Path | Published commit | Git blob |
| --- | --- | --- | --- |
| `Theta_G7` | `assays/G7_ESTIMAND_SPEC_V0_1.md` | `11c69c5a0ce4b02f75f1f0403869a4031b65502d` | `495048de467c4a1197c888eeb2e9bd29d59b8e40` |
| `E_repr` | `assays/G7_ASSAY_RELATIVE_REPRESENTATION_SPEC_V0_1.md` | `85a4b6b5fee11e5d2c0ea8e8a0649f61c782ea16` | `51233d6526554d0d1e6f48b045cff5d4a00cde8f` |
| `R2` and `B_neutral^(v0.2)` | `assays/G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0_2.md` | `2b4933b798745aff1fff6241d5a34386bf8d944d` | `428eb6cf43be782f83cfc22a55c07f6459424582` |
| `E_measurement` | `assays/G7_MEASUREMENT_EQUIVALENCE_SPEC_V0_1.md` | `83f921110b70a9ce996765eac71bd9ecfbd86b66` | `d18eb7dba5a465185b594fa62d8a3aa93304d286` |
| Canonical `B*` | `assays/G7_NEUTRAL_CONTROL_SELECTION_SPEC_V0_1.md` | `39a718a2540d4ad37b9d86e7372cf6e3f59d88f4` | frozen by that commit |
| Historical assay machinery | `assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md` | version `G7_MATCHED_CONTEXT_ASSAY_V0.1.1` | immutable historical record |

The historical token artifacts are immutable historical records. `N_scientific_runs = 0` at constitution.

The evidence boundary remains:

```text
SOURCE
  -> RAW MEASUREMENT
  -> DERIVED RECONSTRUCTION
  -> INTERPRETATION
```

Recorder-custodied raw evidence is authoritative. Derived arithmetic must be labeled derived. Literal backend fields remain literal. Missing fields remain absent.

## 2. Why v0.2 exists

Version v0.1.1 constituted exact prompt-token equality as a pre-open requirement. Subsequent first-principles work froze:

```text
Theta_G7 = effect of C_improve content under matched instructional form
```

and classified `N_prompt` as `MEASURE`, not `MATCH`.

Accordingly, v0.2 prospectively supersedes the old prompt-token-equality gate for this estimand implementation. This does not rewrite history:

```text
historical v0.1.1 remains valid history
!=
historical token-match requirement remains mandatory in v0.2
```

The historical token mismatch remains a valid executor observation. Its former interpretation as an assay blocker is not inherited. Version v0.1.1 is not declared wrong; its token-equality requirement is prospectively superseded for the newly frozen estimand implementation.

## 3. Frozen estimand and representation partition

The intended intervention contrast is immutable:

```text
Theta_G7 = effect of C_improve content under matched instructional form
```

Instructional form is held fixed, candidate content differs, and executor consequences of that content are measured. This is not strengthened into a content effect at fixed prompt-token burden, and formal causal identification is not claimed in advance.

The frozen `E_repr` classification controls construction:

- `D_preserve`: literal outer directive `internalize logic:`, active instructional speech act, sole-user-message role, pre-target governing position, general logic/principle presentation role, affirmative enactment, and task independence;
- `D_treatment`: the semantic content intentionally differs between neutral `B*` and `C_improve` treatment `C`;
- `D_free`: dimensions left unconstrained by the frozen estimand and representation contract;
- `D_measurement`: executor-realization quantities preserved and reported without being forced equal.

Speech act is `PRESERVE`. Equality on `D_treatment` is neither required nor permitted by the contrast.

## 4. Frozen conditions

Exactly two conditions exist.

### Condition B — canonical neutral control `B*`

Sole authority: `G7_NEUTRAL_CONTROL_SELECTION_SPEC_V0.1`.

```text
ordinal: 1
tuple: (0,0,0,0,0,0)
UTF-8 SHA-256: 37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663
line endings: LF only
terminal LF: absent
```

Exact source:

```text
internalize logic: S = L_catalog

where:

catalog = fixed convention pairing a symbol with a label, symbol
   ↓
fixed catalog relation
   ↓
corresponding catalog label
   ↓
unchanged catalog entry
   ↓
same descriptive mapping
```

Before future execution, source custody must reproduce the frozen hash. `B*` must not be semantically re-reviewed, optimized, paraphrased, or replaced. Its selection is canonical for this assay, not universal across neutral wording.

### Condition C — literal `C_improve` treatment

Sole source lineage remains the frozen Gate 7 / `WR-OBS-002` authority.

```text
UTF-8 SHA-256: 62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a
```

Exact source:

```text
internalize logic: I ∝ C_improve

where:

C_improve = capacity to convert feedback into increased future viability, feedback
   ↓
better representation
   ↓
better adaptive mechanisms
   ↓
greater improvement capacity
   ↓
expanded viable futures
```

Condition C must not be paraphrased, improved, shortened, or extended.

## 5. Frozen task set

The task set is carried forward exactly from v0.1.1.

### Q1 — integer arithmetic

Exact target:

```text
Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.
```

Expected bytes after the frozen trim operation: `486`

Target UTF-8 SHA-256: `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23`

### Q2 — character reversal

Exact target:

```text
Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.
```

Expected bytes after the frozen trim operation: `9R2m7Q`

Target UTF-8 SHA-256: `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1`

### Q3 — numeric ordering

Exact target:

```text
Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.
```

Expected bytes after the frozen trim operation: `-4, 0, 9, 12, 17`

Target UTF-8 SHA-256: `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400`

Task wording, expected values, source hashes, and task count are immutable within this assay.

## 6. Request construction and serialization

For every condition and task, assemble the sole user-message content exactly as:

```text
<PRELUDE> + "\n\n--- TARGET ---\n" + <TARGET>
```

Preserve one user message, role `user`, the exact separator, the exact target, prelude-before-target ordering, and conversational position. The prelude is the only intentional source-content difference.

The exact compact JSON serialization contract carried forward from v0.1.1 is:

```json
{"model":"qwen38-27b","messages":[{"role":"user","content":"<ASSEMBLED_CONTENT>"}],"stream":false,"max_tokens":64}
```

Encode as UTF-8 without BOM or trailing newline, use compact separators, do not ASCII-escape Unicode, preserve the displayed member order, and add no other fields.

Source byte length, rendered byte length, token count, and absolute target token index are custody or measurement quantities under `E_measurement`; they are not required to match.

## 7. Frozen executor and request envelope

Carry forward the v0.1.1 executor realization unchanged:

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
| `max_tokens` | `64` |
| sampling overrides | absent |
| message count | `1` |
| message role | `user` |

No new runtime configuration is constituted here.

## 8. Measurement equivalence classification

`G7_MEASUREMENT_EQUIVALENCE_SPEC_V0.1` is directly binding.

### MATCH — common/background causes

Hold fixed:

- model, weights, and model file;
- tokenizer identity;
- chat-template identity;
- runtime identity;
- reasoning-format configuration;
- decoding and request configuration;
- generation budget;
- sampling configuration;
- task and target;
- message role and conversational position;
- instructional form;
- separator and prelude-target ordering;
- context-window capacity;
- instrumentation version;
- initial backend state;
- retained pre-request KV/cache state.

### MEASURE — treatment consequences

Preserve and report when authoritatively exposed:

- `N_prompt`;
- absolute target-start token index;
- prompt/context headroom;
- `T_prompt` or prompt-evaluation time;
- `N_prompt,new`;
- `N_generated`;
- `T_generation`;
- `T_total`;
- `graphs_reused`;
- `f_sim_best`;
- `f_keep`;
- an explicit cached-token field, if exposed.

Equality of these quantities is not required.

### CUSTODY — representation/provenance facts

Preserve source byte count, source code-point count, rendered byte count, and exact source/rendered bytes and hashes. Custody does not imply equality.

## 9. No pre-open token-match gate

This assay freezes:

```text
PREOPEN_TOKEN_MATCH_REQUIRED = NO
N_prompt(B*) = N_prompt(C) is not an admissibility requirement
```

Do not call `/apply-template` or `/tokenize` for matching; search for prompt-token equality; reject `B*` because prompt burden differs; pad either condition; alter either prelude; adjust target position; or select another neutral control.

Future tokenization may occur only when independently required for literal measurement or custody by a separately authorized execution protocol. It is not a precondition to this assay.

## 10. Mechanical capability grader

For every admissible response:

1. parse the recorder-custodied raw response JSON;
2. require `choices[0].message.content` to exist as a string;
3. trim leading and trailing ASCII space, tab, CR, and LF only;
4. perform no internal normalization;
5. compare the resulting UTF-8 bytes exactly to the frozen expected answer.

`SUCCESS ∈ {0,1}`. There is no human judge, LLM judge, `reasoning_content` grading, or style grading.

## 11. Replicate design and frozen execution order

The design contains:

```text
3 tasks × 2 conditions × 5 independently cold replicates = 30 observations
```

Each task-condition cell requires five independently admissible observations. Do not increase `n` after outcomes, stop early, or selectively replace failed scientific values.

Version v0.1.1 required a separately reviewed execution manifest but did not freeze an exact order. Version v0.2 therefore freezes the following deterministic, condition-balanced order prospectively. Let pair index `p` advance in replicate-major task order `Q1, Q2, Q3`. Odd pairs execute `B*, C`; even pairs execute `C, B*`.

| Pair | Replicate | Task | Observation 1 | Observation 2 |
| ---: | ---: | --- | --- | --- |
| 1 | 1 | Q1 | `B*` (run 01) | `C` (run 02) |
| 2 | 1 | Q2 | `C` (run 03) | `B*` (run 04) |
| 3 | 1 | Q3 | `B*` (run 05) | `C` (run 06) |
| 4 | 2 | Q1 | `C` (run 07) | `B*` (run 08) |
| 5 | 2 | Q2 | `B*` (run 09) | `C` (run 10) |
| 6 | 2 | Q3 | `C` (run 11) | `B*` (run 12) |
| 7 | 3 | Q1 | `B*` (run 13) | `C` (run 14) |
| 8 | 3 | Q2 | `C` (run 15) | `B*` (run 16) |
| 9 | 3 | Q3 | `B*` (run 17) | `C` (run 18) |
| 10 | 4 | Q1 | `C` (run 19) | `B*` (run 20) |
| 11 | 4 | Q2 | `B*` (run 21) | `C` (run 22) |
| 12 | 4 | Q3 | `C` (run 23) | `B*` (run 24) |
| 13 | 5 | Q1 | `B*` (run 25) | `C` (run 26) |
| 14 | 5 | Q2 | `C` (run 27) | `B*` (run 28) |
| 15 | 5 | Q3 | `B*` (run 29) | `C` (run 30) |

The order cannot depend on outcomes, latency, or model behavior. A future execution manifest may bind identifiers and operational timestamps to these slots but may not reorder them.

An operationally inadmissible observation must be preserved with its failure reason. No silent rerun is permitted. The assay remains incomplete until a separately authorized, outcome-blind replacement plan supplies any required replacement observation under the already frozen replacement-run discipline.

## 12. Cold-run independence and custody

Every observation begins from its own independently cold backend and recorder/session state. Require:

- a new backend process and PID;
- a new recorder process/session;
- a startup snapshot before the request;
- zero prior measured inference requests;
- first-slot cold/LRU evidence available under the frozen recorder doctrine;
- exactly one measured request;
- exactly one task/slot measurement block;
- `correlation_status = EXACT`;
- no cross-run retained KV/cache state;
- request and response raw-byte/hash custody `PASS`.

A fresh browser window or new chat is not cold-state evidence. Failure yields `RUN_INADMISSIBLE`. Cold state is `MATCH`/admissibility; execution-time reuse fields remain `MEASURE`.

## 13. Primary local work outcome and separate ledgers

Freeze:

```text
W_gen := N_generated
Delta W_gen := N_generated^C - N_generated^B*
```

This is generation work under the constituted assay currency. It is not whole-invocation compute, FLOPs, energy, or whole-lifecycle economics.

Three ledgers remain distinct:

```text
Delta W_gen != Delta W_run != Delta C_H
```

- `Delta W_gen`: generated-token work comparison directly constituted here;
- `Delta W_run`: whole-invocation executor work/cost, only if separately constituted and directly measured;
- `Delta C_H`: whole-horizon White Rabbit lifecycle economics.

Gate 7 v0.2 may decide only its frozen local generation-work result. Observing `T_total` or `N_prompt` does not authorize a `Delta W_run` result. No `Delta C_H` result may be emitted.

## 14. Control adequacy

For each task `q_j`, define `S_B*,j` as successful admissible `B*` runs out of five. Require:

```text
for every q_j: S_B*,j = 5/5
```

States:

- `CONTROL_ADEQUACY_FAIL`
- `CONTROL_ADEQUACY_OBSERVED`

No pooled success rescues a failed task. If control adequacy fails, preserve every observation and do not open capability non-regression or generation-work comparison.

## 15. Capability non-regression

Only after `CONTROL_ADEQUACY_OBSERVED`, evaluate:

```text
for every q_j: S_C,j >= S_B*,j
and
sum_j S_C,j >= sum_j S_B*,j
```

Because control adequacy requires `5/5` per task, successful non-regression requires `S_C,j = 5/5` for every task.

States:

- `CAPABILITY_NONREGRESSION_FAIL`
- `CAPABILITY_NONREGRESSION_OBSERVED`

No work reduction rescues capability regression.

## 16. Generation-work censoring

Preserve literally `finish_reason`, `max_tokens = 64`, and explicit backend/server truncation or length fields when exposed.

Assign `WORK_CENSORED` only when authoritative evidence establishes termination by the generation-length budget, including `finish_reason = length` or an explicitly equivalent exposed condition. `N_generated = 64` alone does not prove censoring. Preserve censored runs and do not invent an uncensored counterfactual token count.

If all earlier gates pass but any required generation-work observation is censored, emit only:

```text
GENERATION_WORK_COMPARISON_CENSORED
```

## 17. Result-state precedence

The following precedence is immutable:

1. completeness and run admissibility;
2. control adequacy;
3. capability non-regression;
4. generation-work censoring;
5. eligible numerical generation-work comparison.

No later-stage result may be emitted when an earlier stage blocks. In particular, no work-level result may be emitted before adequacy and non-regression pass; censoring is evaluated only after those gates pass.

## 18. Eligible generation-work comparison

Only after every earlier gate passes, report all five `N_generated` values per task and condition, plus mean, median, minimum, and maximum.

Emit:

```text
GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
```

only if all three conditions hold:

```text
for every q_j:
  mean(N_generated_C,j) <= mean(N_generated_B*,j)

at least one q_j has a strict mean reduction

pooled mean(N_generated_C) < pooled mean(N_generated_B*)
```

Otherwise, after all eligibility gates pass, emit:

```text
GENERATION_WORK_REDUCTION_NOT_OBSERVED
```

No inferential significance claim is authorized.

## 19. Secondary measurements and prompt burden

For every admissible run, preserve and descriptively summarize the literal exposed `MEASURE` fields listed in Section 8. Missing fields remain missing.

Do not derive cached-token counts from `graphs_reused`, FLOPs, energy, hidden reasoning effort, or hidden computation. Secondary measurements cannot alter the primary `N_generated` decision rule.

If `N_prompt(B*) != N_prompt(C)`, report the difference. Do not emit `ASSAY_BLOCKED` for that reason alone and do not call it a confound merely because it differs. Prompt burden is part of the observed executor realization of the treatment and control contents under the common executor.

Freeze:

```text
Delta W_gen < 0 does not imply Delta W_run < 0
Delta W_gen < 0 does not imply Delta C_H < 0
```

## 20. Canonical-control scope

Any future result is conditional on prospectively selected `B*`:

```text
Y(C) - Y(B*)
```

does not establish:

```text
Y(C) - Y(B) for all B in B_neutral^(v0.2)
```

No generalization across the 729-member neutral family and no robustness-to-control-realization claim are authorized.

## 21. Mechanical result-state vocabulary

The only assay result states available, subject to the precedence above, are:

- `ASSAY_INCOMPLETE` or `RUN_INADMISSIBLE` at the completeness/admissibility stage;
- `CONTROL_ADEQUACY_FAIL` or `CONTROL_ADEQUACY_OBSERVED` at the adequacy stage;
- `CAPABILITY_NONREGRESSION_FAIL` or `CAPABILITY_NONREGRESSION_OBSERVED` at the non-regression stage;
- `GENERATION_WORK_COMPARISON_CENSORED` at the censoring stage;
- `GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY` or `GENERATION_WORK_REDUCTION_NOT_OBSERVED` at the eligible comparison stage.

No result is present at constitution.

## 22. Claim ceiling

Under the exact frozen conditions, a future admissible execution may support only assay-local statements such as:

- control adequacy observed or failed;
- capability non-regression observed or failed;
- generation-work reduction observed or not observed;
- secondary executor-realization differences observed.

It does not establish general capability, formal causal identification, persistent learning, weight change, `C_improve -> Phi`, reuse, compilation, amortization, transfer, whole-run compute reduction, lifecycle economic advantage, or White Rabbit.

The claim ceiling for `B*` is conditional and local. The assay does not establish a result across the neutral-control family.

## 23. Relation to historical v0.1.1

```text
v0.1.1:
  immutable historical assay
  exact-token-match gate historically constituted
  execution remained unopened

v0.2:
  new prospective assay
  same core task, capability, and cold-run machinery
  frozen B*
  measurement doctrine updated from first principles
  prompt burden measured rather than matched
```

The historical token observations remain valid. No v0.1 artifact is changed or invalidated by this constitution.

## 24. Execution authority and absolute stop

This artifact does not execute and cannot authorize execution. Successful constitution yields:

```text
G7_V0_2_CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED
```

Then stop. Only independent review can precede a separate execution authorization. Constitution is not execution.

Before that separate authority exists, do not:

- modify `B*`, `C`, Q1/Q2/Q3, expected answers, or `R2`;
- enumerate the 729 controls or select another control;
- tokenize `B*` or `C`, perform token matching, or call `/props`, `/apply-template`, or `/tokenize`;
- start llama-server or the recorder;
- call a completion endpoint or generate model output;
- execute scientific runs, grade new output, observe capability, or observe work;
- emit a White Rabbit claim.

## 25. Frozen terminal state

```text
artifact: G7_MATCHED_CONTEXT_ASSAY_V0.2
status: CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING
Theta_G7: effect of C_improve content under matched instructional form
conditions: B* and C
tasks: 3
replicates per task/condition: 5
planned observations: 30
primary local currency: N_generated
N_prompt classification: MEASURE
PREOPEN_TOKEN_MATCH_REQUIRED: NO
run order: deterministic and frozen
scientific observations executed: 0
execution authority: absent
next action: STOP + independent review
```

Match what the question holds fixed. Measure what the intervention changes.

Measure the executor realization; do not engineer it away.

`N_generated` is the local generation-work outcome. It is not whole-run economics.

`B*` is canonical for this assay, not universal across neutral wording.

Constitution is not execution.

