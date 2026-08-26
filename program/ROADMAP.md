# White Rabbit Gated Roadmap

Status: `ROADMAP / NON_AUTHORIZING`

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

Machine-readable current state: `program/CURRENT_AUTHORITY_STATE.json`

This roadmap describes dependency order. It does not grant permission to cross any scientific gate.

## 0. Governing rule

```text
historical artifact
!=
current authority
!=
execution authorization
```

Current repository integrity requirement:

```text
identity
-> authority acquisition
-> authority propagation
-> operative revision
```

A downstream surface whose assumed authority no longer matches its source may not silently remain
`CURRENT`.

## 1. Founding research-state substrate

State:

```text
FROZEN_FOUNDING_CONSTITUTION
validator implemented
success ceiling = PROVENANCE_VALID
```

Artifacts:

- `constitution/authority.md`
- `validator/validate.py`

This layer validates structural provenance only. It does not grant scientific warrant.

## 2. White Rabbit program burden

Canonical minimum:

```text
same relevant capability, less required computation
```

Economic gate family:

```text
G1 capability preserved
G2 independent reproduction
G3 work reduction
G4 amortization
```

Correctability burden family in the conceptual freeze:

```text
G_S semantic sufficiency
G_C challenge sufficiency
G_R operative revision
```

These burden families are not yet composed into one authoritative conjunctive decision rule.
See `program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1_ERRATA.md`.

White Rabbit remains unestablished.

## 3. Historical Gate 7 evidence

### v0.3

State:

```text
HISTORICAL_LOCAL_OBSERVATION
PROSPECTIVE_EXECUTION_PROVENANCE_LIMIT
```

Use:

```text
local observation / target-selection / context
```

Do not upgrade it to the authority of a prospectively reviewed and separately authorized replication.

### Robustness panel

State:

```text
PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN
```

The B4/B5 identity contradiction invalidates panel-level scientific authority. Historical raw data
remain preserved.

The old analyzer's raw-custody builder is deprecated for regeneration. A deterministic successor is:

`tools/g7_analyze_robustness_v012.py`

## 4. Q1 / Q3 replication lane

Q2 repository support:

```text
SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
```

Current effective Q1 constitution:

`assays/G7_Q1_REPLICATION_ASSAY_V0_1_1.md`

Current effective Q3 constitution:

`assays/G7_Q3_REPLICATION_ASSAY_V0_1_1.md`

Current state:

```text
Q1: REVIEW_REQUIRED / NOT_EXECUTED / authorized=false
Q3: REVIEW_REQUIRED / NOT_EXECUTED / authorized=false
```

Required transition:

```text
independent constitution review
-> freeze review result
-> create explicit execution authorization bound to exact reviewed target
-> authority validator PASS
-> scientific execution
```

Any earlier failure:

```text
STOP
later gates NOT_OPENED
```

No task-heterogeneity or interaction claim is opened before fresh Q1/Q3 outcomes exist.

## 5. Minimum Identity Independence lane

Current implementation state:

```text
IMPLEMENTATION_REVIEW_PASS
FULL_RUNTIME_CONFORMANCE_PASS
122/122 non-assay tests PASS
N_assay=0
```

Current scientific execution authority:

```text
authorized=false
```

Required transition:

```text
separate MII assay authorization
-> bind exact constitution/oracle/implementation/runtime target
-> authority validator PASS
-> 36-case assay execution
```

The implementation pass does not itself authorize the assay.

Claim ceiling remains:

```text
contract-relative evidence-authority sufficiency
!= globally minimal architecture
chi_3 independent recomputation from shared custody
!= independent world observation
```

## 6. Repository authority-propagation lane

Current bounded experiment:

`program/AUTHORITY_PROPAGATION_INVENTORY_V0_1.md`

The four live cases are:

```text
result authority    -> rendered result
state authority     -> orientation
evidence authority  -> dependent claim
execution authority -> operative transition
```

Current purpose:

```text
enumerate source authority
enumerate dependents
apply/observe known authority revisions
record actual downstream state
```

Explicitly forbidden at this stage:

```text
universal propagation engine
automatic mutation of all artifacts
assumption that all four failures share one cause
new scientific execution
```

Terminal question:

```text
common failure topology
OR
materially distinct propagation failures
```

Only the first can earn a shared architecture.

## 7. Machine authority checks

Current checkpoint:

`program/CURRENT_AUTHORITY_STATE.json`

Execution dispositions:

`authority/execution/*.json`

Validator:

`tools/validate_authority_propagation.py`

Tests:

```text
tests/test_authority_propagation.py
tests/test_g7_analyze_robustness_v012.py
```

CI:

`.github/workflows/authority-propagation.yml`

## 8. Platform enforcement residual

Current observed GitHub state:

```text
main protected = false
required checks = off
rulesets = none
```

Therefore:

```text
repository check exists
but
direct-push bypass remains possible
```

The final infrastructure transition required to make authorization operative is external GitHub
configuration:

```text
protect main
require pull request review
require authority-propagation status check
block direct bypass
```

Until that platform state exists, label the execution-governance layer:

```text
MACHINE_CHECKED / PLATFORM_BYPASSABLE
```

not `OPERATIVELY_ENFORCED`.

## 9. Current frontier

```text
White Rabbit theory: frozen; no new ontology required
Gate 7: Q1/Q3 review frontier
MII: implementation PASS; scientific authorization pending
Repository integrity: authority-propagation inventory
```

The next repository move is to verify the inventory and current authority checkpoint, not to invent
another conceptual layer.

> **Measure the topology before inventing the mechanism.**
