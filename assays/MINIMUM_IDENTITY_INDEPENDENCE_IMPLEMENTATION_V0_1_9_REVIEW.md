# Minimum Identity Independence Implementation v0.1.9 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.9`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing cumulative persistence partial-write accounting. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v019.py
blob: 8be4d8cf409079a243a6dfe6fabc60bfd2283c1d

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v019.py
blob: 596d9ebc87392bbb5c9f0fdae0bfe3d918653881

frozen cost contract:
assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1_1.md
blob: bd15bf90c8ccade881d5b8a2e7973f58eef28602
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

State: `PASS_ON_FROZEN_LINUX_X86_64_RUNTIME`

The successor changes only harness-side architecture-evidence persistence instrumentation and which `Store` subclass is instantiated during preparation.

It does not alter the reviewed architecture runtime boundary:

```text
user/network/PID namespaces
PR_SET_NO_NEW_PRIVS
seccomp capability denial
empty environment
closed inherited file descriptors
fresh temporary cwd
import denial
SANDBOX_READY barrier
exact V_i stdin channel
one-way event channel
```

No new architecture-visible case-bearing channel is introduced.

## Gate 2 — exact V_i projection realization

State: `PASS`

The successor re-expresses the reviewed preparation path only to instantiate the repaired cumulative-persistence `Store`.

The constituted view remains unchanged:

```text
same schemas
same field order
same opaque-handle rule
same frozen/materialized/executed sources
same serialization
same custody override semantics
same dispatched-view attestation
prepare still ends at T1
```

The only evidence-path semantic change is how architecture-attributable persistence bytes and their completeness are recorded.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

The repaired persistence state is parent-side only and is never supplied to the architecture child.

No persistent architecture state, readable instrumentation state, or cross-evaluation channel is introduced.

## Gate 4 — T0..T4 realization

State: `PASS`

The successor inherits the reviewed lifecycle implementation unchanged:

```text
prepare ends at T1
sandbox readiness precedes exact V_i transfer
successful full transfer precedes T2
terminal bytes freeze precedes T3
T3 precedes referee/oracle join at T4
```

Persistence work remains within `[T1,T2]` and does not move any lifecycle event.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — cumulative persistence partial-write accounting

The historical persistence defect is repaired mechanically.

The successor common persistence primitive now separates:

```text
known cumulative bytes actually written
measurement completeness
```

For a returned write count `written`, the implementation first performs:

```text
C_persist_bytes += written
```

and only then determines whether the intended write completed fully.

Therefore:

```text
full write -> exact known bytes accrued, complete
short write -> actual short count accrued, incomplete, failure propagated
zero-byte short write -> zero accrued, incomplete
unknown-transfer exception -> no invented delta, incomplete
```

Persistence incompleteness is sticky: later successful writes do not restore comparability after any partial or unknowable architecture-attributable persistence event.

The common instrumented path covers create/overwrite, append, and replacement/rewrite. Repeated writes count repeatedly. Later truncate/delete operations do not subtract previously accrued write bytes.

Thus the implementation now realizes:

```text
C_persist_bytes = cumulative known architecture-attributable bytes newly written
C_persist_bytes != terminal retained filesystem size
```

The published 12-fixture file encodes these requirements. No fixture execution result is claimed by this review.

### Next blocking defect — `C_view_bytes` is granted complete before actual dispatch

The frozen cost contract defines:

```text
C_view_bytes = len(exact UTF-8 serialized V_i bytes dispatched to chi_i)
```

and the reviewed lifecycle separately defines:

```text
T2 = EXACT_VIEW_DISPATCHED
```

The inherited cost primitive remains:

```python
def mark_view(self, data: bytes) -> None:
    self.C_view_bytes = len(data)
    self.complete["C_view_bytes"] = True
```

The v0.1.9 `prepare()` still invokes:

```text
cost.mark_view(data)
```

while lifecycle authority remains only through T1.

Actual dispatch happens later in the production sandbox path:

```text
wait for SANDBOX_READY
-> write exact V_i bytes to child stdin
-> flush/close successful full transfer
-> T2_EXACT_VIEW_DISPATCHED
```

Therefore the current implementation can represent:

```text
C_view_bytes = len(full intended V_i)
measurement_complete = true
T2 absent
```

if sandbox readiness fails or child-stdin transfer fails before the exact view is successfully dispatched.

For a partial stdin transfer, the implementation likewise retains the full intended view length as complete even though only a prefix may have actually crossed the dispatch channel.

Thus:

```text
complete C_view_bytes
!= proof that the counted exact-view bytes were actually dispatched
```

in the current realization.

This violates the same accounting principle established for persistence:

```text
known work that actually occurred
must be represented separately from
whether measurement/required completion succeeded
```

and violates the frozen meaning of `C_view_bytes` as bytes dispatched to `chi_i`, not merely bytes prepared for possible dispatch.

This is the first remaining Gate-5 blocker. Later instrumentation sub-burdens are not promoted by this review.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture logic, sandbox capability boundary, lifecycle meanings, SHA/extract/compare/capture/persistence semantics, cost dimensions, scoring, missingness rules, or Pareto rules.

Repair only exact-view byte accounting so that view measurement is pending after projection and becomes complete only when the actual dispatch path establishes the frozen quantity.

At minimum, a conforming successor must ensure:

```text
prepare/frozen V_i -> C_view_bytes not yet complete
full exact dispatch -> actual full byte count recorded, complete=true
readiness failure before transfer -> incomplete, no invented dispatched bytes
known partial transfer -> retain actual known transferred byte count, incomplete
unknown transfer amount -> incomplete, no invented full/zero count
T2 cannot exist unless the exact full view transfer completed
aggregate rejects incomplete view-byte measurement
```

The exact numeric treatment of a known partial transfer must remain subordinate to the frozen primary meaning and missingness rule; it cannot be silently promoted to a complete exact-view dispatch.

After repair, restart hostile implementation review from Gate 1.

## Terminal review state

```text
ORACLE_ISOLATION_REALIZATION:
PASS_ON_FROZEN_LINUX_X86_64_RUNTIME

EXACT_VIEW_PROJECTION_REALIZATION:
PASS

STATELESS_EVALUATION_REALIZATION:
PASS

T0_T4_REALIZATION:
PASS

COST_INSTRUMENTATION_REALIZATION:
FAIL

operation-event completion semantics:
REPAIRED

operation-measurement completeness/missingness:
REPAIRED

projection-side SHA completion accounting:
REPAIRED

capture-byte completion accounting:
REPAIRED

cumulative persistence partial-write accounting:
REPAIRED

failure locus:
EXACT-VIEW BYTE DISPATCH ACCOUNTING / COMPLETENESS

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
MINIMAL IMPLEMENTATION GATE-5 EXACT-VIEW DISPATCH-BYTE ACCOUNTING REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
