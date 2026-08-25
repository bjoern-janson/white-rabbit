# G7 Matched-Context Assay v0.1

Version: `G7_MATCHED_CONTEXT_ASSAY_V0.1`

Status: `CONSTITUTED / NOT EXECUTED / PREOPEN_TOKEN_MATCH_REQUIRED`

Parent authority: `43717f4d77b817442a2cd13a83df61461828e365`

## Authority and claim ceiling

This document constitutes a future Gate 7 assay. It does not authorize or report its execution.

```text
CONSTITUTED != EXECUTED
```

The assay asks only whether a matched-context treatment condition can preserve mechanically judged task capability while changing directly observed generation work relative to a neutral matched control under independently constituted cold runs.

It cannot establish a White Rabbit, general capability, causality, computation elimination, amortization, persistence, or transfer.

The five frozen components are:

```text
1. capability criterion
2. work currency
3. independence criterion
4. matched-context control
5. replicate design
```

## Evidence and provenance boundary

Mandatory evidence order:

```text
SOURCE
-> RAW MEASUREMENT
-> DERIVED RECONSTRUCTION
-> INTERPRETATION
```

- Source objects are the frozen payloads and rules in this constitution.
- Raw measurements are recorder-custodied bytes and literal llama.cpp fields.
- Derived reconstructions are deterministic grading, counts, and descriptive summaries.
- Interpretations are limited to the result labels explicitly authorized below.

Gate 6 supplies a protocol constraint, not a population model:

```text
Gate 6 five replicates characterize the frozen protocol
!=
the underlying stochastic distribution is fully known
```

## Frozen runtime and request envelope

Every future observation must use the same fields below except for the frozen prelude content and frozen task target.

| Field | Frozen value |
| --- | --- |
| llama.cpp build | `b10603` |
| llama.cpp commit | `c060ca974` |
| model | `Qwen3.8-27B-Q2_K.gguf` |
| model alias / request model | `qwen38-27b` |
| GPU layers | `50` |
| context size | `8192` |
| parallel slots | `1` |
| Jinja | enabled |
| reasoning format | `deepseek` |
| backend endpoint | `127.0.0.2:8086` |
| recorder endpoint | `127.0.0.1:8085` |
| recorder | White Rabbit Recorder `v0.1.0`, reported commit `80cddb26a7b851d218f95317cd3c5b0593acd831` |
| HTTP route | `POST /v1/chat/completions` |
| message count | `1` |
| message role | `user` |
| `stream` | `false` |
| `max_tokens` | `64` |
| sampling fields | absent; no `temperature`, `top_p`, `top_k`, `min_p`, `seed`, or other sampling override is supplied |

The sole user-message content is constructed exactly as:

```text
<PRELUDE> + "\n\n--- TARGET ---\n" + <TARGET>
```

`<PRELUDE>` and `<TARGET>` contain no trailing newline. The separators above are literal LF (`U+000A`) characters. The request body is UTF-8 without BOM or trailing newline and uses this exact compact JSON member order:

```json
{"model":"qwen38-27b","messages":[{"role":"user","content":"<ASSEMBLED_CONTENT>"}],"stream":false,"max_tokens":64}
```

`<ASSEMBLED_CONTENT>` means the JSON-escaped form of the exact assembled Unicode content. Serialization must use compact separators, preserve Unicode rather than ASCII-escape it, and escape the literal LF characters as JSON `\n`. No other request property is allowed.

For a given task, the target and every request field other than prelude content must be byte-identical between conditions B and C.

## 1. Capability criterion

Assay-local realized capability is:

```text
C_realized = mechanical task success under the frozen correctness rule
```

This does not operationalize intelligence or general capability.

### Frozen task set

Exact task count: `3`.

#### Task Q1 — integer arithmetic

Exact target, excluding the code fence delimiters:

```text
Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.
```

```text
UTF-8 SHA-256: eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23
expected: 486
```

#### Task Q2 — character reversal

Exact target, excluding the code fence delimiters:

```text
Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.
```

```text
UTF-8 SHA-256: 3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1
expected: 9R2m7Q
```

#### Task Q3 — numeric ordering

Exact target, excluding the code fence delimiters:

```text
Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.
```

```text
UTF-8 SHA-256: 886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400
expected: -4, 0, 9, 12, 17
```

The tasks are self-contained, independent of White Rabbit and `C_improve`, require no web/retrieval/external file, and have no answer present in either prelude.

### Frozen mechanical grader

For each admissible run:

1. Parse the recorder-custodied raw response body as JSON.
2. Require exactly one usable value at `choices[0].message.content` and require it to be a string.
3. Remove leading and trailing ASCII space, tab, carriage return, and line-feed characters only.
4. Perform no internal whitespace, Unicode, punctuation, case, or numeric normalization.
5. Compare the resulting string byte-for-byte in UTF-8 with the frozen expected value.

Match yields `SUCCESS = 1`; every other outcome yields `SUCCESS = 0`. `reasoning_content`, style, confidence, and explanation quality are not graded. No human or LLM judge is permitted.

### Frozen capability aggregation

For each task `q_j`, report:

```text
S_B,j = successful admissible B runs out of 5
S_C,j = successful admissible C runs out of 5
```

Also report aggregate success counts across all three tasks.

Capability non-regression is observed only if:

```text
for every q_j: S_C,j >= S_B,j
and
sum_j S_C,j >= sum_j S_B,j
```

Every per-task difference must be surfaced. Improvement on one task cannot compensate for regression on another. Any per-task treatment deficit yields `CAPABILITY_NONREGRESSION_FAIL`. Work reduction cannot rescue that result.

## 2. Work currency

Primary assay-local work currency:

```text
C_work := N_generated
```

Secondary literal measurements:

```text
T_generation
T_total
N_prompt,new
T_prompt
graphs_reused
f_sim_best, only if exposed
f_keep, only if exposed
explicit cached-token field, only if exposed
```

`graphs_reused` remains literal and is never renamed or converted into cached tokens. Missing fields remain absent.

The assay must not invent or estimate FLOPs, energy, reasoning effort, cached-token counts, or the exact post-template model-visible token sequence.

Work is evaluated only after capability non-regression. For each task and condition, report all five `N_generated` values plus mean, median, minimum, and maximum. Report the same descriptive summaries for `T_generation` and `T_total`, and preserve every per-run secondary measurement.

The label `WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY` requires all of:

```text
CAPABILITY_NONREGRESSION_OBSERVED
for every q_j: mean(N_generated_C,j) <= mean(N_generated_B,j)
at least one q_j has a strict mean reduction
pooled mean(N_generated_C) < pooled mean(N_generated_B)
```

Otherwise the work label is `WORK_REDUCTION_NOT_OBSERVED`. Medians and ranges remain mandatory context but do not silently replace this frozen decision rule. No inferential significance claim is authorized.

## 3. Independence criterion

Every one of the 30 planned observations must begin from its own recorder-controlled cold backend and recorder session.

Required evidence for each run:

```text
new backend process and PID
new recorder process/session
captured startup snapshot before the request
zero pre-request task lines
prior_recorded_inference_requests = 0
first slot selection = LRU, t_last = -1
exactly one measured request in the process/session
exactly one explicit task/slot measurement block
correlation_status = EXACT
no cross-run retained KV/cache state
request and response raw-byte/hash custody PASS
```

A browser window, conversation reset, request ID, or nominally new chat is not independence evidence.

Failure of any required item yields:

```text
RUN_INADMISSIBLE
```

The run remains preserved with its failure reason. It may not be repaired, reinterpreted, or silently replaced. Because the frozen design requires five admissible runs per cell, any inadmissible run leaves the assay incomplete until a separately authorized replacement-run plan is constituted.

## 4. Matched-context control

Conditions:

```text
B = neutral matched prelude + separator + target
C = literal C_improve prelude + separator + target
```

### Condition C — literal source treatment

Sole source locator:

```text
observations/WR-OBS-002/raw_observation.md
section: Intervention text
```

Exact text, excluding code-fence delimiters and with LF line endings and no trailing LF:

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

```text
Unicode code points: 246
UTF-8 bytes: 256
UTF-8 SHA-256: 62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a
```

The text is copied literally. It is not reconstructed, improved, paraphrased, or extended.

### Condition B — frozen neutral prelude

Exact text, excluding code-fence delimiters and with LF line endings and no trailing LF:

```text
reference pattern: X ∝ Y_reference

where:

Y_reference = label for a static descriptive sequence, reference
   ↓
plain descriptive statement
   ↓
fixed reference notation
   ↓
ordinary descriptive sequence
   ↓
expanded neutral reference example
```

```text
Unicode code points: 246
UTF-8 bytes: 256
UTF-8 SHA-256: af2d192d9ce44c51190455b3434b55e0c676c9630c6a17af5d33d6c0d94f3a51
```

This text contains no `C_improve` logic, White Rabbit hypothesis, metacognitive optimization instruction, or task answer/help. Its semantic neutrality is a reviewable design assumption, not an earned scientific fact.

### Source-level matching table

| Dimension | B | C | Status |
| --- | --- | --- | --- |
| message count | 1 | 1 | exact |
| message role | `user` | `user` | exact |
| conversational position | sole message, before target | sole message, before target | exact |
| prelude/target order | prelude, separator, target | prelude, separator, target | exact |
| line count | 13 | 13 | exact |
| blank-line-delimited blocks | 3 | 3 | exact |
| proportional symbol count | 1 | 1 | exact |
| down-arrow line count | 4 | 4 | exact |
| Unicode code points | 246 | 246 | exact |
| UTF-8 byte length | 256 | 256 | exact |
| target bytes for task `q_j` | frozen target `q_j` | same frozen target `q_j` | required exact |

Source-level equality does not establish tokenizer or post-Jinja equality.

### Pre-open token/context matching gate

Current status:

```text
PREOPEN_TOKEN_MATCH_REQUIRED
```

Before any Gate 7 execution can be authorized, a separate pre-open artifact must use the exact frozen model, tokenizer, Jinja template, runtime, roles, separator, and three targets to determine B/C prompt-token burden without generation.

Preferred requirement:

```text
for every q_j: total tokenized prompt length(B_j) = total tokenized prompt length(C_j)
```

If exact equality is not achievable, the allowed mismatch, affected tasks, analysis treatment, and claim limitation must be frozen and reviewed before execution. HTTP-body/source-length matching must never be described as exact post-Jinja model-token matching.

No tokenizer, llama-server, recorder, or model process was authorized or used to resolve this gate during constitution authoring.

## 5. Replicate design

Frozen count:

```text
n = 5 independent cold runs per condition per task
```

The complete design is:

```text
3 tasks × 2 conditions × 5 independent runs = 30 observations

B_1,1 ... B_1,5    C_1,1 ... C_1,5
B_2,1 ... B_2,5    C_2,1 ... C_2,5
B_3,1 ... B_3,5    C_3,1 ... C_3,5
```

Run order must be fixed in a separately reviewed execution manifest before opening the assay. It may not be chosen or changed after observing outputs. Each observation receives a fresh backend and recorder session under the independence criterion.

For every run preserve:

```text
condition, task, replicate index, and execution-order index
exact request and response bytes/hashes
runtime invocation/build/PID/start time/session
startup snapshot and cold-state evidence
task and slot identifiers
correlation status and measurement-block count
mechanical grading result
N_prompt,new and N_generated
T_prompt, T_generation, and T_total
graphs_reused literally
f_sim_best and f_keep only if exposed
explicit cached-token field only if exposed
all raw artifact identifiers and hashes
admissibility result and reason
```

Full per-run observations remain primary. Summary statistics never replace them.

### Mechanical analysis plan

After all required admissible runs exist, report:

1. per-task B/C success counts;
2. aggregate B/C success counts;
3. the capability label under the frozen per-task rule;
4. all per-run `N_generated`, `T_generation`, `T_total`, and `N_prompt,new` values;
5. per-task and pooled mean, median, minimum, and maximum by condition;
6. literal cache/LCP fields and explicit absence where not exposed;
7. every inadmissible run and reason;
8. all run IDs and request/response/artifact hashes;
9. the work label only after the capability label.

No p-value, confidence interval, significance threshold, population parameter, or causal effect size is constituted in v0.1.

## Mechanical result states

Before execution:

```text
ASSAY_NOT_RUN
```

Per-run failure:

```text
RUN_INADMISSIBLE
```

Incomplete required cells:

```text
ASSAY_INCOMPLETE_INADMISSIBLE_RUN
```

Capability result after all cells are complete:

```text
CAPABILITY_NONREGRESSION_FAIL
or
CAPABILITY_NONREGRESSION_OBSERVED
```

Work result, reported only with the capability result and primary currency:

```text
WORK_REDUCTION_NOT_OBSERVED
or
WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
```

Completion wrapper:

```text
ASSAY_COMPLETE_NO_WR_CLAIM
```

No result may directly emit:

```text
WHITE_RABBIT_DEMONSTRATED
C_IMPROVE_CAUSAL
GENERAL_CAPABILITY_IMPROVED
COMPUTE_ELIMINATED
AMORTIZATION_DEMONSTRATED
CROSS_SUBSTRATE_TRANSFER
```

## Hard stop and execution firewall

Constitution completion does not authorize the pre-open token check or assay execution.

Forbidden under this authoring authority:

```text
execute C_improve
execute the neutral prelude
start llama-server, recorder, tokenizer, or any model process for Gate 7
run B or C
grade live model output
compare treatment/control output
open Gate 8
modify RD_HARNESS
modify the White Rabbit Recorder
emit a White Rabbit claim
```

The next possible transition is only:

```text
constitution review
-> separately authorized pre-open token/context matching
-> separately reviewed execution manifest
-> separate execution authorization, if granted
```

Current terminal state:

```text
G7_MATCHED_CONTEXT_ASSAY_V0.1 CONSTITUTED
ASSAY_NOT_RUN
PREOPEN_TOKEN_MATCH_REQUIRED
EXECUTION_NOT_AUTHORIZED
STOP
```

> **Constitute the counterfactual before observing the treatment.**
