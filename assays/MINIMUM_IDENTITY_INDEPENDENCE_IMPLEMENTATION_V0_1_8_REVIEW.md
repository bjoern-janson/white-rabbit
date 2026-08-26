# Minimum Identity Independence Implementation v0.1.8 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.8`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing capture-byte completion accounting. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v018.py
blob: 030c2b35055755cb44cd8e56c2af99d7852b8eea

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v018.py
blob: 57eaf9d646250507d4c1247510d3b74e4b0f70ac

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

The successor changes only the harness-side capture cost wrapper and which `Cost` subclass is instantiated during preparation.

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

The successor re-expresses the reviewed preparation path only so it can instantiate the repaired capture-aware `Cost` subclass.

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

The only projection-side semantic change is when and how capture-byte cost authority is granted.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

The repaired capture ledger is parent-side only and is never supplied to the architecture child.

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

Capture remains wholly inside `[T1,T2]` and does not move any lifecycle event.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — capture-byte completion accounting

The historical capture defect is repaired mechanically.

For chi_2/chi_3, capture measurement is marked pending before the required capture can occur. The wrapper then performs:

```text
captured = capture_identity_bytes(data)
C_capture_bytes += len(captured)
```

only after the capture body returns.

Therefore:

```text
capture exception -> no false intended-length increment, complete=false
successful exact capture -> actual returned length credited, complete=true
partial returned capture -> only actual returned length credited, complete=false, failure propagated
```

chi_0/chi_1 retain a justified complete-zero capture measurement because those constituted architectures require no executed-byte capture.

The published 11-fixture file encodes these requirements. No fixture execution result is claimed by this review.

### Next blocking defect — partial persistence writes are omitted from the cumulative primary counter

The frozen persistence currency is:

```text
C_persist_bytes = cumulative architecture-attributable evidence bytes newly written
```

and explicitly requires repeated/replacement writes to count cumulatively rather than using terminal retained size.

The inherited common persistence primitive currently performs:

```python
with path.open("wb") as f:
    written = f.write(data)
if written != len(data):
    self.cost.complete["C_persist_bytes"] = False
    raise ConformanceError("partial write")
self.cost.C_persist_bytes += written
```

This correctly refuses to call a short write complete, but it raises before adding the bytes that the write operation reports as actually written.

Therefore, for a short write with:

```text
0 < written < len(data)
```

the ledger can contain:

```text
C_persist_bytes unchanged
measurement_complete = false
```

while real architecture-attributable persistence bytes were already written.

That violates the frozen cumulative-work semantics:

```text
actual bytes newly written
!= bytes recorded in C_persist_bytes
```

Even though the incomplete flag correctly blocks Pareto comparison, the retained measured value itself is not the constituted cumulative byte count.

This is the first remaining Gate-5 blocker. Later persistence and instrumentation sub-burdens are not promoted by this review.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture logic, sandbox, lifecycle, SHA/extract/compare/capture semantics, cost dimensions, scoring, missingness rules, or Pareto rules.

Repair only cumulative persistence accounting so that every positively known number of bytes actually written is accumulated before completeness is decided.

Semantically:

```text
written = write(data)
C_persist_bytes += written
if written != len(data):
    measurement_complete = false
    propagate failure
```

If write acquisition fails in a way that makes the number of bytes actually written unknowable, the persistence dimension must remain incomplete rather than inventing zero or a full count.

A successor should prospectively test at minimum:

```text
full write -> exact bytes counted, complete
short write -> actual short count retained, incomplete
zero-byte failed/short write -> zero retained, incomplete
write exception with unknown transferred amount -> incomplete, no invented count
repeated successful writes -> cumulative sum
truncate/delete after prior write -> prior written bytes remain counted
aggregate rejects incomplete persistence measurement
```

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

failure locus:
CUMULATIVE PERSISTENCE PARTIAL-WRITE ACCOUNTING

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
MINIMAL IMPLEMENTATION GATE-5 CUMULATIVE-PERSISTENCE PARTIAL-WRITE REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
