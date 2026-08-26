# White Rabbit 🐇

**White Rabbit is the search for reusable computational structure that makes adequate intelligence cheaper without compressing away correctability.**

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

> This README is an orientation surface. Current authority is defined by
> [`program/CURRENT_AUTHORITY_STATE.json`](program/CURRENT_AUTHORITY_STATE.json)
> and checked by [`tools/validate_authority_propagation.py`](tools/validate_authority_propagation.py).

## Canonical target

Minimum White Rabbit signature:

```text
same relevant capability, less required computation
```

Canonical economic gates remain:

```text
G1: capability preserved
G2: independently reproduced
G3: less required work
G4: acquisition cost repaid over the constituted reuse horizon
```

The derived conceptual freeze remains frozen and non-authorizing:

- [`program/WHITE_RABBIT.md`](program/WHITE_RABBIT.md)
- [`program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1.md`](program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1.md)
- [`program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1_ERRATA.md`](program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1_ERRATA.md)

No current result establishes a White Rabbit.

## Current scientific / engineering state

### Gate 7 v0.3

Historical local observation:

```text
B* pooled mean N_generated = 117.5333...
C  pooled mean N_generated = 98.7333...
historical terminal = GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
```

Current authority is narrower than the original rendered result:

```text
HISTORICAL_LOCAL_OBSERVATION
PROSPECTIVE_EXECUTION_PROVENANCE_LIMIT
```

The numerical observation is preserved, but v0.3 lacked an intervening independently frozen
review/execution-authorization artifact, did not establish the later
`H_frozen = H_materialized = H_executed` identity gate, and under-custodied concrete executor/model identity.

See [`assays/G7_MATCHED_CONTEXT_ASSAY_V0_3_RESULT.md`](assays/G7_MATCHED_CONTEXT_ASSAY_V0_3_RESULT.md).

### Neutral-control robustness panel

Current panel-level scientific authority:

```text
WITHDRAWN
```

The historical 105-observation panel remains preserved, but B4/B5 violated exact constituted
condition identity. The old terminal `ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED` is historical
analyzer output only and is not a current panel conclusion.

See [`assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md`](assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md).

### Q2 provenance

Repository state:

```text
Q2_SOURCE_STATUS = SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
```

Q1/Q3 historically referenced a fresh Q2 replication, but the current repository contains no
resolvable Q2 constitution/result/custody object. That premise has therefore been downgraded to
unresolved motivation and supplies no authority or observations to Q1/Q3.

Current successors:

- [`assays/G7_Q1_REPLICATION_ASSAY_V0_1_1.md`](assays/G7_Q1_REPLICATION_ASSAY_V0_1_1.md)
- [`assays/G7_Q3_REPLICATION_ASSAY_V0_1_1.md`](assays/G7_Q3_REPLICATION_ASSAY_V0_1_1.md)

Both remain:

```text
CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING
```

### Minimum Identity Independence (MII)

Implementation status:

```text
CONSTITUTION_REVIEW: PASS
MECHANICAL_IMPLEMENTATION_REVIEW: PASS
FULL_RUNTIME_CONFORMANCE: PASS
IMPLEMENTATION_REVIEW: PASS
```

Exact non-assay runtime lineage:

```text
v013 ... v022
122 / 122 tests PASS
10 / 10 fixture files exit 0
N_assay = 0
```

Scientific assay execution remains separately unauthorized.

See [`assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_12_RUNTIME_REVIEW.md`](assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_12_RUNTIME_REVIEW.md).

## Current repository-integrity frontier

The live repository finding is:

```text
Delta evidence -> Delta authority
does not automatically imply
Delta downstream system
```

The current bounded object is an **authority-propagation inventory**, not a propagation engine:

- [`program/AUTHORITY_PROPAGATION_INVENTORY_V0_1.md`](program/AUTHORITY_PROPAGATION_INVENTORY_V0_1.md)
- [`constitution/authority_propagation.md`](constitution/authority_propagation.md)

The four inventory cases are:

```text
result authority    -> rendered scientific claim
state authority     -> README / STATE / ROADMAP
evidence authority  -> dependent claim
execution authority -> operative transition
```

No universal propagation primitive is claimed.

## Execution authority

Current machine-readable execution dispositions live under:

```text
authority/execution/
```

Current open scientific lanes are explicitly `authorized: false`.

Repository checks:

```text
python tools/validate_authority_propagation.py
python -m unittest tests.test_authority_propagation tests.test_g7_analyze_robustness_v012
```

A GitHub Actions workflow is provided at `.github/workflows/authority-propagation.yml`.

### Platform-enforcement residual

GitHub `main` is currently unprotected and the repository currently has no rulesets. Therefore the
repository can detect an authority violation, but GitHub itself still permits a direct push that
bypasses the check.

```text
DECLARED/MACHINE-CHECKED AUTHORITY != PLATFORM-ENFORCED AUTHORITY
```

To close that final infrastructure gap, GitHub branch protection/rulesets must require the
`authority-propagation` check and review before merge/direct update. This repository records that
residual explicitly rather than pretending it is already enforced.

## Measurement doctrine

Evidence order remains:

```text
RAW MEASUREMENT
    -> DERIVED RECONSTRUCTION
    -> INTERPRETATION
```

Core constraints:

> **Fresh chat is not fresh compute.**

> **A computation-saving claim must account for the cost of creating reusable state.**

> **Capability preservation does not compensate for identity failure.**

> **Prove identity at the layer that carries authority before promoting the record downstream.**

> **A primary cost unit becomes authoritative only at the causal/semantic boundary where that unit actually occurs.**

## Repository map

```text
constitution/   founding authority + later bounded authority constitutions
authority/      machine-readable execution dispositions
program/        current state, roadmap, conceptual program, propagation inventory
measurement/    raw/derived/interpretation accounting doctrine
interfaces/     recorder/component contracts
assays/         constitutions, results, reviews, current authority index
observations/   preserved raw/derived execution lineage
tools/          analyzers, execution helpers, authority validators
tests/          deterministic engineering/conformance tests
schema/         typed research-state + authorization schemas
validator/      founding provenance validator
```

Start with:

1. [`program/STATE.md`](program/STATE.md)
2. [`assays/README.md`](assays/README.md)
3. [`program/CURRENT_AUTHORITY_STATE.json`](program/CURRENT_AUTHORITY_STATE.json)
4. [`program/ROADMAP.md`](program/ROADMAP.md)

## Governing rules

> **Raw measurement first, derived reconstruction second, interpretation last.**

> **Constitute the counterfactual before observing the treatment.**

> **Historical result does not imply current authority.**

> **A corrected authority state must not leave a dependent surface silently CURRENT.**

> **Measure the topology before inventing the mechanism.**
