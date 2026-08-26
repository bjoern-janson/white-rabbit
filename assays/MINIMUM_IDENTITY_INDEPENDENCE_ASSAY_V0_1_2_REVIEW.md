# Minimum Identity Independence Assay v0.1.2 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.2`

Status: `REVIEW_BLOCKED / IMPLEMENTATION_NOT_ELIGIBLE / NON_AUTHORIZING`

Scientific/model observations: `0`

Engineering assay evaluations: `0`

This review restarts from Gate 1 after the Gate-3 oracle repair and stops at the first newly opened blocking defect.

## Reviewed authority

```text
successor constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_2.md
blob: 4278156d454a7dd2d84b83875129c8ea8ac96bfa

repaired oracle
assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1_1.json
blob: f2f46f4ad0df0086aaa40c6f2b67755050a66ad6

view boundary
assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d

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

The frozen `V_i` boundary remains unchanged from the prior Gate-1 repair. Semantic case IDs, case partition, oracle truth/class, global ordinals, perturbation labels, substitution aliases, expected answers, previous-state information, and handle mappings remain referee-side only.

Each architecture evaluation is constituted as a fresh stateless invocation over exact serialized `V_i` bytes with a fresh opaque handle.

The repaired E4 does not add any oracle-only field to an architecture-visible schema. Its custody-report override is projected only through the already-constituted `custody_reported_executed_sha256` evidence field available to `chi_2` and `chi_3`.

Ceiling:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

## Gate 2 — architecture isolation

State: `PASS_AT_CONSTITUTION_LEVEL`

The only intended independent variable remains the identity-evidence architecture.

The E4 repair introduces no architecture-specific fixture, parser, serialization, runtime, case order, oracle access, retry policy, or hidden field.

The pre-existing treatment distinction remains:

```text
chi_0: self-report/convenience evidence only
chi_1: independent H_f/H_m; H_e unavailable
chi_2: raw custody present; custody-reported H_e is authoritative
chi_3: raw custody present; independently recomputed H_e is authoritative
```

For `chi_2`, the phrase `does not independently recompute H_e from executed_raw_bytes_utf8` is binding broadly: direct raw-byte equality used as a substitute H_e computation would be nonconforming just as SHA-256 recomputation would be. `chi_2` may possess raw custody but its identity authority is the custody-reported H_e. This preserves the intended authority-path treatment.

Again:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

## Gate 3 — ground-truth integrity

State: `PASS`

The three synthetic object SHA-256 values were independently recomputed from the exact UTF-8 identity bytes and match the repaired oracle:

```text
ALPHA
  af15e44f970db761f2b43f96a5aea2264ca07a9782a397d5ec6c707277be19a6

ALPHA_MUT
  8394cbe5ec5308d2d797756ebf6cfd902f56b205eb4a721f71a116e6f555cd3a

BETA
  58b0773887dc2daa110d4751a5d3b4998669c60052337372f51f68dc628e6b01
```

The historical E2/E4 duplicate-state defect is repaired.

E2 freezes:

```text
H_f = ALPHA
H_m = ALPHA
actual H_e = ALPHA_MUT
custody-reported H_e = SHA256(ALPHA_MUT)
```

Repaired E4 freezes:

```text
H_f = ALPHA
H_m = ALPHA
actual H_e = ALPHA_MUT
custody-reported H_e = SHA256(ALPHA)
```

Thus E2 and E4 share the same actual execution mismatch but differ in an authority-bearing evidence state. This is legitimate for an identity-evidence architecture assay: E2 tests detection with truthful custody identity; E4 tests the additional common-mode failure in which the custody identity report falsely certifies the clean object.

The semantic taxonomy now follows a real evidence-state distinction rather than two names for one state.

No architecture output is used to justify this repair.

## Gate 4 — anti-triviality

State: `PASS`

Critical sufficiency still requires both:

```text
C0 and C1 -> IDENTITY_PASS
E1, E2, E3, E4 -> IDENTITY_MISMATCH
```

`IDENTITY_UNRESOLVED` scores `0`.

Therefore:

```text
always MISMATCH -> fails C0/C1
always PASS -> fails E1-E4
always UNRESOLVED -> fails every critical case
```

No averaging can hide a missed critical case. Exact mismatch-class attribution remains secondary and cannot substitute for binary critical correctness.

## Gate 5 — cost separability

State: `FAIL`

Blocking defect: the constitution correctly forbids invented scalarization, but it does not prospectively freeze a complete comparable primary cost vector tightly enough to support its own Pareto and unique-minimum terminal claims.

The inherited cost section says to record literal quantities `including where available`, such as:

```text
bytes of authoritative evidence persisted
number of persisted evidence artifacts
SHA-256 computations
independent parse/extraction operations
identity comparisons
process/runtime elapsed time
CPU time if authoritatively exposed
peak or total storage bytes where available
```

and says missing cost fields remain missing.

However, the result rule later permits a unique least-cost architecture only by dominance across `all frozen primary cost dimensions`.

The following are not yet frozen:

1. which listed dimensions are mandatory **primary** dimensions versus optional diagnostics;
2. the exact measurement function for each primary dimension;
3. the exact common horizon/boundary over which elapsed time, CPU time, storage, and operation counts are accumulated;
4. whether storage means peak bytes, cumulative bytes written, retained bytes at terminal state, or multiple separately named dimensions;
5. how missingness is handled in componentwise dominance and Pareto membership;
6. whether setup/teardown and common projection/dispatch costs are included in each architecture vector or reported only as common scaffolding;
7. whether cost instrumentation overhead itself is excluded, common, or separately reported.

Because those choices can change dominance relations, leaving them to implementation or post-result interpretation creates an outcome-dependent degree of freedom.

Therefore the assay can currently measure a detection matrix, but it cannot yet earn either:

```text
UNIQUE_MINIMUM_TESTED_IDENTITY_ARCHITECTURE_OBSERVED
```

or a well-defined:

```text
IDENTITY_ARCHITECTURE_PARETO_SET_REPORTED
```

under the present cost specification.

This is a cost-contract defect, not an architecture result.

### Required shallowest repair

Freeze a separate cost-measurement contract before implementation that specifies:

```text
exact mandatory primary cost dimensions
exact units and measurement functions
exact per-evaluation and aggregate horizon
setup/teardown/scaffolding inclusion rules
storage semantics
operation-count semantics
missingness policy
componentwise dominance rule over the exact frozen vector
```

Keep scalarization forbidden.

Optional diagnostic cost fields may still be recorded, but they must not enter the Pareto/minimum gate unless prospectively promoted in a successor constitution.

No architecture has been implemented or executed, so this repair is outcome-blind.

## Gate 6 — claim ceiling

State: `NOT_OPENED`

Gate 5 failed, so the claim ceiling is not reviewed in this pass.

## Terminal review state

```text
ORACLE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

ARCHITECTURE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

GROUND_TRUTH_INTEGRITY:
PASS

ANTI_TRIVIALITY:
PASS

COST_SEPARABILITY:
FAIL

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
MINIMAL GATE-5 COST-CONTRACT REPAIR ONLY
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
