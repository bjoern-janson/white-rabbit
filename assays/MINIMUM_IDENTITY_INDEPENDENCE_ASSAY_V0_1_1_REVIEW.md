# Minimum Identity Independence Assay v0.1.1 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.1`

Status: `REVIEW_BLOCKED / IMPLEMENTATION_NOT_ELIGIBLE / NON_AUTHORIZING`

Scientific/model observations: `0`

Engineering assay evaluations: `0`

This review restarts from Gate 1 after the oracle/view-boundary repair and stops at the first newly opened blocking defect.

## Reviewed authority

```text
successor constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_1.md
blob: 8f6f59a357e1dda74bc4a47202deaddbcee78051

view boundary
assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d

frozen oracle
assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1.json
blob: 90e1bca7f590b41f9688fcfef4f56cddfe893db6

historical v0.1 constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1.md
blob: 26b09fe233b80a42e989cafc4794b2d4966bc5ef
```

Review order:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

## Gate 1 — oracle isolation

State: `PASS_AT_CONSTITUTION_LEVEL`

The repaired specification now freezes a complete architecture-visible view `V_i` and makes the oracle/referee join external to `chi_i`:

```text
O --sealed P_i--> V_i --> chi_i --> frozen output

O + sealed handle mapping --> external referee
```

The architecture-visible schemas exclude semantic case ID, case partition, oracle truth/class, global ordinal, perturbation label, substitution aliases, expected answer, previous-case state, and handle-to-case mapping.

Each evaluation receives a fresh unrelated 256-bit opaque handle. The same oracle case receives a different handle for each architecture evaluation.

The specification requires stateless evaluation with no oracle/repository/harness filesystem, no network, no semantic case information in argv/env/cwd, no previous-run state, and no recoverable global case ordinal.

The exact schemas are SHA-256 frozen. Independent recomputation of the four canonical schema-contract hashes matched the published values:

```text
chi_0 54214df3b4b02e8304d96a36629ac8ce6c851d61c4e5e58fcade382f28b739d3
chi_1 b873fad1d01af7c3c57d27d68cbab0df008248780fd397c5c548e2a9477c7056
chi_2 61e1de0a04040172faa914813b86f8b31f7396f11db176e82e67e145f253c7a8
chi_3 bf17650e576cbd28f7c2cbb12b039b60a2885794ae812031a929fe77a52c43b1
```

Important ceiling on this PASS:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

A future implementation must still be reviewed to show that the pure/stateless boundary is actually realized before execution authorization.

## Gate 2 — architecture isolation

State: `PASS_AT_CONSTITUTION_LEVEL`

The intended independent variable is now sufficiently specified as the identity-evidence architecture.

Common across architectures:

```text
oracle cases
actual synthetic objects
common sealed projection mechanism
serialization rules
opaque-handle policy
terminal vocabulary
referee
cost instrumentation contract
scoring
runtime/sandbox contract
```

Constituted treatment differences are limited to evidence availability / evidence authority:

```text
chi_0: self-report/convenience evidence only
chi_1: independent H_f/H_m evidence; H_e unavailable
chi_2: raw custody present; custody-reported H_e is authoritative
chi_3: same raw-custody evidence level; independently recomputed H_e is authoritative
```

`chi_2` and `chi_3` intentionally receive equivalent raw-custody fields; their treatment difference is the authority/recomputation path, not an extra hidden oracle field.

The historical v0.1 implementation-firewall rule against parser/runtime/serialization differences remains binding.

Again:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

No implementation exists under review here.

## Gate 3 — ground-truth integrity

State: `FAIL`

Blocking defect:

```text
E2_MATERIALIZED_EXECUTED_MISMATCH
and
E4_LYING_CONVENIENCE_PREDICATE
```

freeze the same underlying case state for every field that defines the synthetic identity relation and primary architecture evidence:

```text
frozen = ALPHA
materialized = ALPHA
executed = ALPHA_MUT
declared_condition = ALPHA
convenience_identity_match = true
oracle_mismatch = true
```

They differ only in semantic case ID and `oracle_class`:

```text
E2 oracle_class = MATERIALIZED_EXECUTED_MISMATCH
E4 oracle_class = EXECUTED_OBJECT_IDENTITY_MISMATCH
```

Therefore the frozen oracle currently assigns two different semantic perturbation identities/classes to an otherwise identical synthetic case state.

The duplication is not harmless bookkeeping for this constitution because:

1. `E4_LYING_CONVENIENCE_PREDICATE` does not isolate a perturbation distinct from E2;
2. `convenience_identity_match = true` is already present in E1, E2, and E3, so E4 does not uniquely instantiate the claimed convenience-predicate failure;
3. exact failure-class truth is not a function of the underlying frozen case state for E2 versus E4;
4. the stated four-critical-failure family contains only three distinct underlying critical mismatch states;
5. retaining both as separate critical cases would redundantly count/cost the same state while describing it as a separate perturbation.

This is a ground-truth / perturbation-definition defect, not an architecture result.

No architecture has been implemented or executed.

### Required shallowest repair

Do not reinterpret results because there are none.

A successor oracle must prospectively make E4 a genuinely distinct case if `LYING_CONVENIENCE_PREDICATE` is to remain a separate critical perturbation, or remove/merge the duplicate under a new oracle version.

The repair must not be chosen based on architecture outputs; no architecture outputs exist.

After that repair, restart hostile review from Gate 1 because changing the oracle changes upstream authority.

## Later gates

Because Gate 3 failed:

```text
Gate 4 anti-triviality: NOT_OPENED
Gate 5 cost separability: NOT_OPENED
Gate 6 claim ceiling: NOT_OPENED
```

Previously written provisions at those layers remain unreviewed by this pass; they are neither accepted nor rejected here.

## Terminal review state

```text
ORACLE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

ARCHITECTURE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

GROUND_TRUTH_INTEGRITY:
FAIL

ANTI_TRIVIALITY:
NOT_OPENED

COST_SEPARABILITY:
NOT_OPENED

CLAIM_CEILING:
NOT_OPENED

IMPLEMENTATION:
NOT_ELIGIBLE

EXECUTION:
NOT_AUTHORIZED

ASSAY OBSERVATIONS:
0
```

Next admissible action:

```text
MINIMAL GATE-3 ORACLE REPAIR ONLY
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
