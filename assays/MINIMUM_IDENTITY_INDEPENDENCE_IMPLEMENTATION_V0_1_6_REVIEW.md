# Minimum Identity Independence Implementation v0.1.6 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.6`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing operation-measurement completeness/missingness. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v016.py
blob: 685d01034a4fa8bb40471e9656caebf1a818f5cf

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v016.py
blob: 47b88d2ab7df629b11813fd890cd60ab923a1cc9

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

The successor changes only harness-side completeness state and post-T3 event-stream merge semantics.

It does not alter the previously reviewed hard runtime boundary:

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

The successor calls the reviewed v0.1.5/v0.1.4 `prepare()` and changes only the harness-side completeness flags after the exact serialized `V_i` has been constructed.

No schema field, field order, serialized byte, custody source, opaque handle, or dispatch attestation is modified.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

The new completeness state remains in the parent-side `Cost` ledger and is never passed into the architecture child.

No meter, history, prior result, or cross-evaluation object is introduced into `chi_i`.

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

Operation-stream completeness is resolved only after T3 and does not move or redefine any lifecycle event.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — operation-measurement completeness / missingness

The historical defect is repaired mechanically.

After `prepare()`, the total per-evaluation operation dimensions are pending:

```text
C_sha256_ops complete = false
C_extract_ops complete = false
C_identity_compare_ops complete = false
```

They become complete only after the one-way architecture operation stream is successfully decoded and merged.

Malformed, truncated, unknown, non-ASCII, or otherwise undecodable event data propagates failure while the dimensions remain incomplete.

A valid empty event stream is distinguishable from missing measurement:

```text
valid empty stream -> complete=true, count=0
invalid/unavailable stream -> complete=false
```

The inherited aggregate rule therefore rejects any six-case architecture vector containing such an incomplete mandatory dimension.

The published 11-fixture file encodes these requirements. No execution result for those fixtures is claimed by this review.

### Next blocking defect — projection-side SHA count is incremented before digest completion

The frozen cost contract defines:

```text
C_sha256_ops = completed SHA-256 digest operations
```

and includes architecture-attributable SHA work performed during the pre-dispatch evidence path in `[T1,T2]`.

The inherited projection-side SHA primitive is still:

```python
def projection_sha(self, data: bytes) -> str:
    self.C_sha256_ops += 1
    return hashlib.sha256(data).hexdigest()
```

Thus the primary counter is incremented before the SHA-256 operation has successfully completed.

If `hashlib.sha256(data).hexdigest()` fails after the increment, the cost ledger records a completed SHA operation that did not complete.

This is the same attempted-versus-completed semantic defect previously repaired on the child `T2->T3` event path, now exposed on the parent `T1->T2` projection path.

Therefore:

```text
C_sha256_ops
!= guaranteed count of completed SHA-256 operations
```

in the current realization.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture logic, sandbox, lifecycle, event vocabulary, missingness rules, cost dimensions, scoring, or Pareto rules.

Repair only the projection-side SHA primitive so that the counter increments after successful digest completion:

```text
result = SHA256(data)
C_sha256_ops += 1
return result
```

A conforming successor should include forced projection-SHA failure fixtures proving:

```text
failed projection SHA -> no increment
successful projection SHA -> exactly one increment
failed projection SHA during prepare -> no false completed-op count
operation-measurement completeness remains fail-closed
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

failure locus:
PROJECTION-SIDE SHA COMPLETION ACCOUNTING

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
MINIMAL IMPLEMENTATION GATE-5 PROJECTION-SHA COMPLETION REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
