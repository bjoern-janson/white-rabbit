# Minimum Identity Independence Implementation v0.1.7 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.7`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing projection-side SHA completion accounting. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v017.py
blob: 0640b93e82277315b3016329a62fd94a4854df88

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v017.py
blob: 5ad94541e07148fa62d94a7998c1dc3dae533c33

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

The successor changes only the parent-side projection cost wrapper and preparation cost-object implementation.

It does not alter the reviewed hard architecture runtime boundary:

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

The successor re-expresses the reviewed preparation path so that it can instantiate the repaired `Cost` subclass.

The exact frozen projection semantics remain unchanged:

```text
same schemas
same field order
same opaque-handle generation rule
same frozen/materialized/executed evidence sources
same serialization
same custody override semantics
same dispatched-view attestation
prepare still ends at T1
```

The only semantic change inside projection is when the primary SHA counter increments relative to digest completion.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

The repaired `Cost` object remains harness-side and is never passed into the architecture child.

No persistent architecture state, readable instrumentation state, or new cross-evaluation channel is introduced.

## Gate 4 — T0..T4 realization

State: `PASS`

The successor inherits the reviewed v0.1.6/v0.1.4 production `run()` path and actual-dispatch lifecycle unchanged:

```text
prepare ends at T1
sandbox readiness precedes exact V_i transfer
successful full transfer precedes T2
terminal bytes freeze precedes T3
T3 precedes referee/oracle join at T4
```

The projection-SHA repair occurs entirely inside `[T1,T2]` and does not move any lifecycle boundary.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — projection-side SHA completion accounting

The historical defect is repaired mechanically.

The successor projection SHA wrapper now performs:

```python
self.complete["C_sha256_ops"] = False
result = _projection_sha256_digest(data)
self.C_sha256_ops += 1
return result
```

Therefore:

```text
failed projection SHA -> no increment, total SHA dimension remains incomplete
successful projection SHA -> exactly one increment
```

The already-reviewed child SHA path remains:

```text
successful digest
-> SHA256_OPERATION event
-> return digest
```

so both production primary-SHA accounting paths now share the same completed-work semantics.

Common schema/dispatch/referee/output hashes remain excluded scaffolding under the frozen cost contract and are not primary-vector SHA paths.

The published 10-fixture file encodes these requirements. Fixture execution in the current tool runtime is not established because a fresh GitHub clone could not be obtained; no fixture PASS is claimed.

### Next blocking defect — capture-byte counter increments before capture completion

The frozen cost contract defines:

```text
C_capture_bytes = exact number of identity-bearing bytes copied
from the already-fixed synthetic actual object
into an architecture-specific evidence channel
solely because chi_i requires that evidence
```

The inherited common capture primitive is still:

```python
def capture(self, data: bytes) -> bytes:
    self.C_capture_bytes += len(data)
    return bytes(data)
```

Thus the primary capture counter is incremented before the capture conversion has returned successfully.

If the capture operation raises after the increment, the ledger can record bytes as captured even though the instrumented capture operation did not complete.

This violates the same completed-work invariant now enforced for primary SHA operations:

```text
attempted capture
!= completed capture
```

and means:

```text
C_capture_bytes
!= guaranteed count of successfully completed captured bytes
```

in the current realization.

This is the first remaining Gate-5 blocker; later instrumentation sub-burdens are not promoted by this review.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture logic, sandbox, lifecycle, event vocabulary, SHA semantics, missingness rules, cost dimensions, scoring, or Pareto rules.

Repair only the common capture primitive so that capture-byte accounting is granted after successful capture completion, for example semantically:

```text
captured = capture_bytes(data)
C_capture_bytes += len(captured)
return captured
```

A failed required capture must not produce a false positive byte count and must not be silently interpreted as complete zero measurement.

A successor should prospectively test:

```text
successful capture -> exact captured byte count
failed capture -> no increment
failed required capture -> capture measurement not promoted as complete zero
successful chi_2/chi_3 prepare -> literal executed-byte capture count
chi_0/chi_1 valid no-capture path -> complete zero only when measurement path is known complete
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

failure locus:
CAPTURE-BYTE COMPLETION ACCOUNTING

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
MINIMAL IMPLEMENTATION GATE-5 CAPTURE-BYTE COMPLETION REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
