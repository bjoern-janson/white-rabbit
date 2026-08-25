# Gate 7 Pre-Open Constitution Review

Status: `PREOPEN_REVIEW / REPAIR_REQUIRED / TOKEN_MATCH_BLOCKED / EXECUTION_NOT_AUTHORIZED`

Reviewed constitution:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
commit: 7696bf90452cb13f86fe8e22cc860ff6e9d09dee
parent: 43717f4d77b817442a2cd13a83df61461828e365
```

This review occurs before any Gate 7 tokenizer preflight, B/C execution, capability evaluation, or scientific comparison.

## Review result

The constitution passes the following pre-open checks:

```text
ontology / program separation: PASS
C_improve treated as one candidate intervention: PASS
White Rabbit != C_improve effect: PASS
matched-context construction: PASS
authority / claim ceiling: PASS
CONSTITUTED != EXECUTED firewall: PASS
```

Two constitutional gaps block the next transition:

```text
1. primary-work censoring under max_tokens = 64
2. capability non-regression without an adequacy gate
```

Therefore:

```text
PREOPEN_TOKEN_MATCH: BLOCKED
GATE7_EXECUTION: NOT_AUTHORIZED
```

No token/context matching process may be started until a repaired constitution is frozen and reviewed.

---

## Gap 1 — work censoring

The frozen primary work currency is:

```text
C_work := N_generated
```

while the frozen request envelope contains:

```text
max_tokens = 64
```

Therefore an observation may be right-censored by the generation budget:

```text
N_observed = min(N_required, 64)
```

A run ending because the output budget is exhausted cannot be interpreted as an uncensored measurement of the generation work the model would otherwise have performed.

### Required repair

Preserve the fixed `max_tokens = 64` budget unless the repair itself explicitly identifies a contradiction requiring a separately justified revision.

Add literal completion/censoring custody, at minimum:

```text
finish_reason
backend/server truncation indicator when explicitly exposed
max_tokens budget
```

Define a mechanical state equivalent to:

```text
WORK_CENSORED
```

A run is work-censored if the authoritative response/backend evidence establishes termination by the frozen generation-length budget, including `finish_reason = length` or an equivalent explicitly exposed length/truncation condition.

A work-censored run remains preserved and may still contribute to the frozen capability grader if a complete mechanically gradable answer is present. It may not be treated as an uncensored `N_generated` observation for the work-reduction decision rule.

The repaired constitution must specify what happens if any required B/C cell contains work-censored runs. Minimum acceptable rule:

```text
uncensored work-reduction label cannot be emitted while required work observations are censored
```

Do not infer uncensored work from the cap value.

Do not silently classify ordinary EOS/stop termination as censoring.

---

## Gap 2 — capability adequacy

The current non-regression rule permits:

```text
S_B,j = 0
S_C,j = 0
```

for every task while still satisfying relative treatment non-regression.

That does not establish the White Rabbit minimum premise of preserving a useful result.

### Required repair

Add a separately frozen control-adequacy gate before treatment non-regression and before any work-reduction interpretation:

```text
ADEQUACY
-> NONREGRESSION
-> WORK COMPARISON
```

The adequacy criterion must be fixed before any Gate 7 output is observed.

For this assay's three elementary mechanically graded tasks, the repaired constitution must state an explicit per-task control requirement. It may not use a pooled score that allows one task to compensate for control failure on another.

The repair must distinguish at least:

```text
CONTROL_ADEQUACY_FAIL
CONTROL_ADEQUACY_OBSERVED
CAPABILITY_NONREGRESSION_FAIL
CAPABILITY_NONREGRESSION_OBSERVED
```

If treatment succeeds where control does not, preserve that as a capability-effect observation under the assay but do not automatically promote it into an efficiency result.

A work-reduction label is eligible only after:

```text
CONTROL_ADEQUACY_OBSERVED
+
CAPABILITY_NONREGRESSION_OBSERVED
+
all required work observations uncensored
```

---

## Minimal-revision rule

Preserve all unaffected frozen structure from commit `7696bf90452cb13f86fe8e22cc860ff6e9d09dee`, including:

```text
3 frozen tasks and exact hashes
literal C_improve source text
frozen neutral prelude
source-level matching table
n = 5 per condition per task
independence criterion
primary currency N_generated
secondary measures
mechanical grader
result claim ceiling
PREOPEN_TOKEN_MATCH_REQUIRED
CONSTITUTED != EXECUTED
```

Do not redesign the assay merely because two gaps were found.

## Required transition

```text
7696bf9 constitution
-> minimal constitutional repair
-> run existing repository tests + validator
-> freeze repaired commit
-> review repaired constitution
-> only then reconsider pre-open token/context matching
```

The existing repository tests/validator establish repository/provenance integrity only; their success must not be described as scientific validation of the assay.

## Current ledger

```text
Gate 4: PASS (user-reported engineering acceptance)
Gate 5: PASS (user-reported instrumental calibration)
Gate 6: PASS (user-reported frozen five-replicate characterization)
Gate 7 ontology: PASS
Gate 7 matched-context construction: PASS
Gate 7 authority boundary: PASS
Gate 7 work-censoring rule: REPAIR_REQUIRED
Gate 7 capability adequacy: REPAIR_REQUIRED
Gate 7 pre-open token match: BLOCKED
Gate 7 execution: NOT_AUTHORIZED / NOT_OPENED
White Rabbit G1-G4: NOT_OPENED
```

> **Find the ambiguity before it gets to look like a result.**
