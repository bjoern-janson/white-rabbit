# Minimum Identity Independence Assay v0.1.2

Version: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.2`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Engineering observations executed under this constitution: `0`

This is the minimal successor to `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.1` after hostile review reached Gate 3 and found that the original E2 and E4 cases were identical at the underlying evidence-state level.

It repairs only Gate-3 oracle ground truth by replacing E4 with a genuinely distinct authority-bearing evidence perturbation. It does not authorize implementation or execution.

## 1. Immutable authority

```text
historical v0.1 constitution
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1.md
blob: 26b09fe233b80a42e989cafc4794b2d4966bc5ef

Gate-1 view-boundary repair
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d

historical v0.1.1 successor
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_1.md
blob: 8f6f59a357e1dda74bc4a47202deaddbcee78051

Gate-3 review that blocked v0.1.1
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_1_REVIEW.md
blob: bdf4dc111e33511557495445aa08cf764011076d

repaired frozen oracle
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1_1.json
blob: f2f46f4ad0df0086aaa40c6f2b67755050a66ad6
```

The historical oracle `MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1` remains immutable historical record and is not authority for v0.1.2 execution.

## 2. Precedence

All v0.1 and v0.1.1 provisions remain binding except that the sole oracle authority for this successor is:

```text
MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1.1
```

The view-boundary artifact remains unchanged and binding.

No scoring rule, cost rule, claim ceiling, architecture ladder, serialization rule, statelessness rule, or critical/diagnostic count is changed.

## 3. Gate-3 repair

E1, E2, E3, C0, C1, D1, D2, and D3 are byte-for-byte logically unchanged from the original oracle.

Only E4 is replaced.

Historical defective E4:

```text
E4_LYING_CONVENIENCE_PREDICATE
frozen = ALPHA
materialized = ALPHA
executed = ALPHA_MUT
convenience_identity_match = true
```

This duplicated E2 at the underlying identity/evidence state and is not used by v0.1.2.

Repaired E4:

```text
E4_FALSE_CLEAN_CUSTODY_IDENTITY_REPORT

frozen = ALPHA
materialized = ALPHA
executed raw bytes = ALPHA_MUT
convenience_identity_match = true
custody-reported executed SHA-256 = SHA256(ALPHA)
oracle_mismatch = true
```

Thus E4 now differs from E2 in an authority-bearing evidence variable:

```text
E2:
executed raw bytes = ALPHA_MUT
custody-reported H_e = SHA256(ALPHA_MUT)

E4:
executed raw bytes = ALPHA_MUT
custody-reported H_e = SHA256(ALPHA)
```

E4 therefore tests a distinct failure class: the actual executed object is wrong while the custody identity report falsely certifies the clean frozen identity.

The semantic label follows the changed underlying state; the repair is not a rename-only change.

## 4. Architecture relation to repaired E4

No architecture contract is changed.

The existing view boundary already freezes that:

```text
chi_2:
custody_reported_executed_sha256 is H_e authority;
do not independently recompute H_e from executed_raw_bytes_utf8

chi_3:
independently recompute SHA256(executed_raw_bytes_utf8) as H_e authority;
custody-reported H_e is diagnostic only
```

Therefore repaired E4 is within the previously constituted evidence-path distinction rather than a new treatment dimension.

No result for E4 is assumed prospectively.

## 5. Critical contract

Critical clean controls remain:

```text
C0_ALPHA_CLEAN
C1_BETA_CLEAN
```

Critical failures are now:

```text
E1_FROZEN_MATERIALIZED_MISMATCH
E2_MATERIALIZED_EXECUTED_MISMATCH
E3_CROSS_OBJECT_SUBSTITUTION
E4_FALSE_CLEAN_CUSTODY_IDENTITY_REPORT
```

Diagnostics remain:

```text
D1_MISSING_CONVENIENCE_FIELD
D2_IRRELEVANT_METADATA_CHANGE
D3_CORRUPTED_RECORDED_HASH_RAW_BYTES_CLEAN
```

The assay still contains:

```text
2 critical clean controls
4 critical mismatch cases
3 diagnostic cases
4 architectures
36 architecture-case evaluations
```

## 6. No result-oriented redesign

The E4 repair was selected before any architecture implementation or assay output exists.

```text
architecture implementations: 0 under assay authority
architecture-case outputs: 0
model inference: 0
```

The repair is justified only by the Gate-3 duplicate-state defect.

No future result may retroactively change E4 or restore the historical defective E4.

## 7. Review restart

Because upstream oracle authority changed, hostile review restarts from Gate 1:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

Stop at the first blocking defect.

A constitution-level PASS is not an implementation-level PASS.

## 8. Explicit non-authority

This successor establishes no identity-sufficiency result and does not authorize:

```text
implementation execution
36-case evaluation
model inference
Gate 7 science
G_C
G_R
corrigibility
correctable compression
White Rabbit
amortization
compounding
```

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.2

status:
CONSTITUTED
NOT_EXECUTED
REVIEW_REQUIRED
NON_AUTHORIZING

oracle authority:
MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1.1

Gate-3 repair:
E4 DISTINCT EVIDENCE-STATE PERTURBATION

engineering observations:
0

next action:
HOSTILE REVIEW FROM GATE 1
```
