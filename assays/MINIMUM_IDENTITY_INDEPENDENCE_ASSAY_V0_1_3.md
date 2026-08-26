# Minimum Identity Independence Assay v0.1.3

Version: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.3`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Engineering observations executed under this constitution: `0`

This is the minimal successor to `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.2` after hostile review reached Gate 5 and found that the primary cost vector was not prospectively frozen tightly enough to support Pareto or unique-minimum claims.

It repairs only Gate-5 cost separability by incorporating a frozen mandatory cost-measurement contract. It does not authorize implementation or execution.

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

historical v0.1.2 successor
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_2.md
blob: 4278156d454a7dd2d84b83875129c8ea8ac96bfa

Gate-5 review that blocked v0.1.2
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_2_REVIEW.md
blob: f87001961ac0dddfa0c3734bbfc8a486d8f0a96a

Gate-5 cost contract
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f
```

Historical constitutions and reviews remain immutable records.

## 2. Precedence

All v0.1/v0.1.1/v0.1.2 provisions remain binding except that cost measurement, cost attribution, completeness, dominance, Pareto membership, and unique-minimum conditions are governed exclusively by:

```text
MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1
```

The repaired oracle and view boundary remain unchanged and binding.

No oracle case, view schema, architecture evidence authority, scoring rule, critical/diagnostic partition, or claim ceiling is changed by this successor.

## 3. Frozen primary cost vector

The mandatory primary architecture vector is now exactly:

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

All six dimensions are mandatory non-negative integer measurements.

No other dimension may enter the v0.1.3 Pareto or unique-minimum decision.

Wall-clock and CPU time are diagnostic only.

## 4. Frozen comparison horizon

Primary cost comparison uses exactly the six critical cases:

```text
C0
C1
E1
E2
E3
E4
```

The three diagnostic cases remain outside the primary cost comparison and are reported separately.

Architecture primary vectors are componentwise sums over the six critical per-case vectors.

## 5. Frozen accounting classes

Every cost observation must be classified prospectively as:

```text
architecture-attributable
shared experiment scaffolding
one-time fixture/oracle construction
```

Only architecture-attributable cost enters `C_primary`.

Shared and one-time costs are separately reportable but cannot alter architecture dominance.

## 6. Missingness

A zero primary cost component is valid only when instrumentation explicitly records measurement completion and value zero.

Any incomplete mandatory component produces:

```text
COST_VECTOR_INCOMPLETE
```

If any critically sufficient architecture has an incomplete primary vector:

```text
COST_COMPARISON_INCOMPLETE
```

and no global Pareto or unique-minimum claim may be emitted.

Missing values are never converted to zero and never dropped from the frozen vector.

## 7. No scalarization

No weighting, unit conversion, normalization, ratio, lexicographic ranking, or aggregate scalar cost is constituted.

Componentwise dominance and Pareto membership follow the exact frozen rules in the cost contract.

A unique minimum requires one critically sufficient architecture to weakly dominate every other critically sufficient architecture across all six dimensions, with at least one strict improvement against each dominated architecture, and complete vectors for all critically sufficient architectures.

## 8. Implementation review burden

This successor still authorizes no implementation execution.

Before any execution authorization, implementation review must demonstrate realization of both:

```text
Gate-1 information boundary
Gate-5 cost instrumentation boundary
```

including:

- exact architecture-visible `V_i` schemas;
- stateless/no-oracle architecture execution;
- exact `T0..T4` event boundaries;
- common instrumented SHA-256 primitive;
- common instrumented authority-bearing extraction primitive;
- common instrumented identity-comparison primitive;
- cumulative architecture-evidence write accounting;
- exact dispatched-view byte counting;
- explicit measurement-complete markers;
- separation of architecture, shared, and one-time ledgers.

A constitution-level review PASS does not establish that implementation realization is correct.

## 9. Explicit non-repairs

This successor does not revise:

```text
ALPHA / ALPHA_MUT / BETA bytes
oracle hashes
C0/C1/E1/E2/E3/E4/D1/D2/D3 definitions
critical/diagnostic membership
chi_0..chi_3 architecture contracts
primary D(i,k) scoring
anti-triviality
claim ceiling
36-evaluation count
```

No architecture result exists and no result-oriented redesign is permitted.

## 10. Review restart

Because a new cost authority is introduced, hostile review restarts from Gate 1:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

Stop at the first blocking defect.

## 11. Stop rule

This successor authorizes no 36-case execution.

Next permitted action:

```text
RESTART HOSTILE CONSTITUTION REVIEW FROM GATE 1
```

If the constitution clears all six review gates, implementation may become eligible for a separate implementation review. Execution still requires separate explicit authorization.

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.3

status:
CONSTITUTED
NOT_EXECUTED
REVIEW_REQUIRED
NON_AUTHORIZING

Gate-5 repair:
FROZEN MANDATORY COST CONTRACT REFERENCED

engineering observations:
0

next action:
HOSTILE REVIEW FROM GATE 1
```
