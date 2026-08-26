# Minimum Identity Independence Implementation v0.1 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review checks implementation realization mechanically and stops at the first blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

implementation:
tools/minimum_identity_independence_v014.py
blob: 44152b1a8afaa843483b632fccce8db69b34a39b

conformance fixtures:
tests/test_minimum_identity_independence_v014.py
blob: 2650b8dea00cf4e5da975a5d1af0876eef2ea7d0
```

Review order:

```text
1. oracle isolation realization
2. exact V_i projection realization
3. stateless architecture evaluation realization
4. T0..T4 realization
5. six-dimensional cost instrumentation realization
```

## Gate 1 — oracle isolation realization

State: `FAIL`

The implementation correctly keeps semantic case IDs out of serialized `V_i`, resolves symbolic oracle aliases referee-side, uses fresh CSPRNG handles, and rejects forbidden extra fields.

However, the evaluator is implemented as:

```python
evaluate(chi, view_bytes, cost)
```

rather than an information-equivalent realization of:

```text
chi_i(V_i)
```

The third argument is a mutable `Cost` object containing the live primary measurement counters:

```text
C_view_bytes
C_capture_bytes
C_persist_bytes
C_sha256_ops
C_extract_ops
C_identity_compare_ops
```

Those counters are populated during `T1 -> T2` before the architecture evaluator runs.

Therefore the evaluator has access to case-correlated information that is not contained in `V_i`.

This is not merely theoretical. Under the frozen repaired oracle, the pre-dispatch SHA-256 count can differ by failure state. For `chi_2` / `chi_3`:

```text
normal truthful custody report:
projection computes frozen hash + materialized hash + custody executed hash

E4 false-clean custody override:
projection computes frozen hash + materialized hash
and uses the frozen custody override instead of computing the executed hash
```

So, before `T2`, the mutable cost object can encode a distinction between those cases.

The current evaluator does not intentionally branch on those counters, and the local purity fixture verifies no such branch today. But the constitution requires the information boundary to make oracle-only/case-only information unavailable, not merely unused.

Thus:

```text
architecture-visible case information
!= exact serialized V_i only
```

and the implementation does not yet realize the frozen Gate-1 invariant.

### Required shallowest repair

Separate architecture cost instrumentation from architecture-readable state.

A conforming repair should ensure that:

```text
architecture evaluator receives exact V_i bytes as its only case-bearing input
```

while instrumentation remains external/non-readable.

One admissible pattern is:

```text
T1->T2 projection-cost ledger
        |
        X  not visible to chi_i

T2->T3 fresh opaque instrumentation capability
        |
        v
chi_i(V_i)
```

where the T2->T3 instrumentation capability:

- starts from the same zero state for every evaluation;
- exposes only the constituted SHA/extract/compare operations;
- exposes no readable counters or pre-dispatch history to `chi_i`;
- is snapshotted externally after the terminal output freezes;
- is then merged with the separately held T1->T2 cost ledger by the harness/referee side.

The repaired architecture result must remain a function of `V_i` alone.

After repair, restart hostile implementation review from Gate 1.

## Later gates

Because Gate 1 failed:

```text
exact V_i projection realization: NOT_OPENED
stateless architecture evaluation realization: NOT_OPENED
T0..T4 realization: NOT_OPENED
cost instrumentation realization: NOT_OPENED
```

The existing 15 conformance fixtures remain useful engineering diagnostics but do not override this information-boundary failure.

## Terminal review state

```text
ORACLE_ISOLATION_REALIZATION:
FAIL

EXACT_VIEW_PROJECTION_REALIZATION:
NOT_OPENED

STATELESS_EVALUATION_REALIZATION:
NOT_OPENED

T0_T4_REALIZATION:
NOT_OPENED

COST_INSTRUMENTATION_REALIZATION:
NOT_OPENED

IMPLEMENTATION:
NONCONFORMING

EXECUTION:
NOT_ELIGIBLE
NOT_AUTHORIZED

CONSTITUTED ASSAY EVALUATIONS:
0
```

Next admissible action:

```text
MINIMAL IMPLEMENTATION GATE-1 REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
