# Minimum Identity Independence Assay v0.1.4

Version: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Engineering observations executed under this constitution: `0`

This is the minimal successor to `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.3` after hostile review found one internal ambiguity in the mandatory primary persistence-cost definition.

It repairs only that Gate-5 ambiguity by incorporating `MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1.1`. It does not authorize implementation or execution.

## 1. Immutable authority

```text
historical v0.1 constitution
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1.md
blob: 26b09fe233b80a42e989cafc4794b2d4966bc5ef

Gate-1 view-boundary repair
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d

repaired oracle
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1_1.json
blob: f2f46f4ad0df0086aaa40c6f2b67755050a66ad6

historical v0.1.3 successor
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_3.md
blob: 2116f6a50d12a0c92469af1a2cee2a80d43309ff

blocking v0.1.3 hostile review
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_3_REVIEW.md
blob: 89ff00000d8426d3bd0f544f59bb062ab8f04a83

historical Gate-5 cost contract
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f

Gate-5 persistence-definition repair
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1_1.md
blob: bd15bf90c8ccade881d5b8a2e7973f58eef28602
```

Historical artifacts remain immutable records.

## 2. Precedence

All prior provisions remain binding except that the authoritative definition of `C_persist_bytes` is governed exclusively by:

```text
MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1.1
```

For every other Gate-5 cost provision, `MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1` remains binding.

No oracle case, view schema, architecture evidence authority, scoring rule, case partition, primary horizon, other cost dimension, Pareto rule, or claim ceiling is changed.

## 3. Repaired primary vector

The mandatory primary vector remains:

```text
C_primary(chi_i) = (
  C_view_bytes,
  C_capture_bytes,
  C_persist_bytes,
  C_sha256_ops,
  C_extract_ops,
  C_identity_compare_ops
)
```

with the sole authoritative persistence definition:

```text
C_persist_bytes = cumulative architecture-attributable evidence bytes newly written during [T1,T3]
```

Terminal retained evidence footprint, if measured, is diagnostic only and cannot enter dominance, Pareto membership, or unique-minimum selection.

## 4. No result-oriented redesign

The persistence repair was made before any architecture implementation or assay output exists.

```text
architecture implementations under assay authority: 0
architecture-case outputs: 0
model inference: 0
```

The repair is justified only by the single-valued-cost defect identified in the v0.1.3 hostile review.

## 5. Explicit non-repairs

This successor does not revise:

```text
oracle bytes/hashes
critical or diagnostic cases
chi_0..chi_3 evidence contracts
view schemas or schema hashes
statelessness/oracle isolation
D(i,k) scoring
anti-triviality
C_view_bytes
C_capture_bytes
C_sha256_ops
C_extract_ops
C_identity_compare_ops
primary six-critical-case horizon
missingness/completeness rules
attribution classes
no-scalarization rule
dominance/Pareto/unique-minimum rules
claim ceiling
36-evaluation count
```

## 6. Review restart

Hostile review restarts from Gate 1:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

Stop at the first blocking defect.

A constitution-level PASS does not establish implementation realization.

## 7. Stop rule

This artifact authorizes no implementation execution and no 36-case evaluation.

Next permitted action:

```text
RESTART HOSTILE CONSTITUTION REVIEW FROM GATE 1
```

If all six constitution gates pass, implementation becomes eligible only for a separate implementation review. Execution still requires separate explicit authorization.

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4

status:
CONSTITUTED
NOT_EXECUTED
REVIEW_REQUIRED
NON_AUTHORIZING

Gate-5 persistence repair:
CUMULATIVE-WRITE DEFINITION FROZEN

engineering observations:
0

next action:
HOSTILE REVIEW FROM GATE 1
```
