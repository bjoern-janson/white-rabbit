# Codex Handoff — Repair Gate 7 Constitution Before Token Matching

Status: `CONSTITUTION_REPAIR_AUTHORIZED / TOKEN_MATCH_NOT_AUTHORIZED / EXECUTION_NOT_AUTHORIZED`

## Mission

Apply the minimum sufficient repair to:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
```

Current constitution commit:

```text
7696bf90452cb13f86fe8e22cc860ff6e9d09dee
```

Pre-open review:

```text
program/GATE7_PREOPEN_CONSTITUTION_REVIEW.md
```

This task repairs two constitutional gaps only:

```text
1. work censoring under max_tokens = 64
2. capability adequacy before non-regression/work comparison
```

Do not perform token/context matching. Do not execute Gate 7.

## Read first

1. `program/GATE7_PREOPEN_CONSTITUTION_REVIEW.md`
2. `assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md`
3. `handoff/CODEX_G7_CONSTITUTION.md`
4. `program/STATE.md`
5. `program/ROADMAP.md`
6. `measurement/MEASUREMENT_MODEL.md`
7. `constitution/instrumentation_invariants.md`

## Repair 1 — explicit work censoring

Keep the primary assay-local currency:

```text
C_work := N_generated
```

Do not silently reinterpret it as uncensored work when generation stops at the frozen length budget.

Preserve `max_tokens = 64` unless you find a direct contradiction that makes retaining it impossible. If such a contradiction exists, STOP and report it rather than redesigning the assay.

Add per-run literal custody for at least:

```text
finish_reason
max_tokens
backend/server truncation or length indicator only if explicitly exposed
```

Add a deterministic state:

```text
WORK_CENSORED
```

A run is work-censored only when authoritative response/backend evidence establishes termination by the frozen generation-length budget, e.g. `finish_reason = length` or an explicitly equivalent length/truncation indicator.

Rules:

```text
- preserve the run and raw evidence;
- do not infer uncensored N_generated beyond the cap;
- a complete mechanically gradable answer may still contribute to capability grading;
- censored work observations may not establish an uncensored work-reduction result;
- ordinary stop/EOS is not censoring unless the backend evidence says so.
```

The work-decision rule must require all work observations needed for the comparison to be uncensored before emitting:

```text
WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
```

If censoring prevents the work decision, add a distinct mechanical result state such as:

```text
WORK_COMPARISON_CENSORED
```

Do not collapse this into `WORK_REDUCTION_NOT_OBSERVED`.

## Repair 2 — capability adequacy

The current relative rule can accept `0/5` control and `0/5` treatment on a task. Add a separate control-adequacy gate before non-regression and work comparison:

```text
CONTROL ADEQUACY
-> CAPABILITY NONREGRESSION
-> WORK COMPARISON
```

Freeze an explicit per-task adequacy threshold before any Gate 7 output is observed.

For these three elementary, mechanically checked tasks, use the strongest simple criterion unless the constitution itself contains a contradiction:

```text
for every q_j: S_B,j = 5/5
```

This means the frozen control must demonstrate the required task capability on every independent replicate of every task before the assay can interpret treatment behavior as preservation of an adequate baseline capability.

If you find that `5/5` conflicts with another frozen constitutional requirement, STOP and report the contradiction; do not choose a weaker threshold ad hoc.

Add mechanical states:

```text
CONTROL_ADEQUACY_FAIL
CONTROL_ADEQUACY_OBSERVED
```

Then retain the existing non-regression rule only after adequacy passes:

```text
for every q_j: S_C,j >= S_B,j
and
sum_j S_C,j >= sum_j S_B,j
```

Since adequacy requires `S_B,j = 5/5`, treatment non-regression under the repaired v0.1 effectively requires `S_C,j = 5/5` on every task as well. State that consequence explicitly rather than hiding it.

If treatment succeeds where an inadequate control does not, preserve the observation but do not call it an efficiency result. The assay should remain blocked from the efficiency work comparison when control adequacy fails.

## Required eligibility chain

Freeze the work-result eligibility chain as:

```text
all required runs admissible
+
CONTROL_ADEQUACY_OBSERVED
+
CAPABILITY_NONREGRESSION_OBSERVED
+
all required work observations uncensored
-> work comparison eligible
```

Anything else must not emit `WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY`.

## Preserve unaffected constitution

Do not modify unless necessary to keep the repaired document internally consistent:

```text
exact 3 tasks, task text, expected results, hashes
mechanical grader
literal C_improve text and provenance
neutral prelude text and hashes
source-level matching dimensions
PREOPEN_TOKEN_MATCH_REQUIRED
n = 5 per condition per task
cold independence criterion
runtime/build/model envelope
primary work currency N_generated
secondary measurement list
no LLM judge
claim ceiling and forbidden scientific promotions
CONSTITUTED != EXECUTED
```

This is a minimal sufficient revision, not a redesign.

## Tests / validation

After editing, run:

```powershell
python -m unittest discover -s tests -v
python -m validator.validate tests/fixtures/valid_state.json
```

Report exact results.

These checks establish repository/test/provenance integrity only. Do not describe them as scientific validation of Gate 7.

Also mechanically inspect the repaired constitution and report whether all of the following literal concepts are present and coherent:

```text
WORK_CENSORED
WORK_COMPARISON_CENSORED
CONTROL_ADEQUACY_FAIL
CONTROL_ADEQUACY_OBSERVED
PREOPEN_TOKEN_MATCH_REQUIRED
CONSTITUTED != EXECUTED
```

## Forbidden operations

Do not:

```text
run tokenizer preflight
start llama-server for Gate 7
start recorder for Gate 7
execute neutral prelude
execute C_improve
run B or C
observe treatment/control outputs
grade live model output
perform token/context matching
modify task answers or treatment text
open Gate 8
emit a White Rabbit claim
modify RD_HARNESS
modify white-rabbit-recorder runtime
```

After the repaired constitution is committed and tests/validator are run:

```text
STOP
```

## Completion report

Return:

```text
Gate 7 repaired constitution version:
constitution path:
parent commit:
repair commit:
files added:
files changed:

max_tokens changed: YES/NO
finish_reason custody frozen: YES/NO
WORK_CENSORED frozen: YES/NO
WORK_COMPARISON_CENSORED frozen: YES/NO
control adequacy threshold:
CONTROL_ADEQUACY_FAIL frozen: YES/NO
CONTROL_ADEQUACY_OBSERVED frozen: YES/NO
non-regression retained after adequacy: YES/NO
work eligibility chain frozen: YES/NO
PREOPEN_TOKEN_MATCH_REQUIRED preserved: YES/NO

unit test command:
unit test result:
validator command:
validator result:

pre-open token match executed: YES/NO
C_improve executed: YES/NO
neutral prelude executed: YES/NO
B/C executed: YES/NO
llama-server started for Gate 7: YES/NO
recorder started for Gate 7: YES/NO
scientific comparison executed: YES/NO
White Rabbit claim emitted: YES/NO

ambiguities/blockers:
working tree clean: YES/NO
```

Then stop.

> **Repair the measurement contract before measuring the treatment.**
