# Minimum Identity Independence Implementation v0.1.11 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.11`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing semantic `C_extract_ops` realization. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v021.py
blob: c957a06286d31efd8014c879437af5d035fa38d4

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v021.py
blob: 89e5d28b2732325daad6868f4b9961cb65cf97ef

frozen cost contract:
assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f

persistence successor:
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

The successor changes only parent-side semantic extraction instrumentation and removes the child extraction cost event from ordinary serialized-field reconstruction.

It does not alter the reviewed architecture capability boundary:

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
one-way child event channel
```

No new architecture-visible case-bearing channel is introduced.

## Gate 2 — exact V_i projection realization

State: `PASS`

The exact serialized `V_i` fields, schemas, field order, evidence sources, opaque-handle rule, custody override semantics, serialization, and shared dispatch attestation remain unchanged.

The successor makes the semantic role of the raw-custody read explicit but does not alter the raw bytes or serialized field value delivered to chi_2/chi_3.

Preparation still ends at T1 with `C_view_bytes` pending under the reviewed v0.1.10 dispatch accounting.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

Extraction cost state remains parent-side and is not supplied to the architecture child.

The child remains a fresh sandbox process per invocation. Removing the child `EXTRACT_OPERATION` event removes instrumentation feedback rather than adding any architecture-readable state.

## Gate 4 — T0..T4 realization

State: `PASS`

The successor inherits the reviewed v0.1.10 lifecycle unchanged:

```text
T1 preparation/custody path
-> sandbox readiness
-> exact V_i transfer
-> T2
-> terminal freeze
-> T3
-> referee/oracle join
-> T4
```

The authority-bearing chi_3 custody extraction occurs inside `[T1,T2]`. Child serialized-field reconstruction occurs inside `[T2,T3]` but is no longer assigned primary extraction authority.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — semantic `C_extract_ops` realization

The historical extraction defect is repaired mechanically without amending the frozen cost contract.

The successor explicitly separates two semantic roles over the same low-level custody read mechanism:

```text
read_diagnostic(name)
extract_authority_bytes(name)
```

For chi_3:

```text
executed.raw custody
-> extract_authority_bytes
-> completed bytes recovery
-> C_extract_ops += 1
-> bytes become substrate for independent H_e recomputation
```

For chi_2:

```text
executed.raw custody
-> read_diagnostic
-> C_extract_ops += 0
-> custody_reported_executed_sha256 remains H_e authority
```

Thus generic filesystem access no longer determines cost semantics.

The ambiguous inherited `Store.read()` path is disabled and raises.

The child UTF-8-string-to-bytes conversion is renamed/recast as serialized-field reconstruction and emits no primary extraction event. Any child `EXTRACT_OPERATION` event is rejected as an inconsistent second definition of the frozen primary extraction unit and fails total operation measurement closed.

Therefore the successor now realizes one deterministic primary extraction interpretation:

```text
chi_3 completed authority-bearing raw-custody recovery -> +1
chi_2 diagnostic custody read -> +0
child serialized-field reconstruction -> +0
```

The published 14-fixture file encodes those requirements. No fixture execution result is claimed by this review.

### Next blocking defect — `C_capture_bytes` is attached to helper return, not proven copy into the constituted evidence channel

The frozen cost contract defines `C_capture_bytes` as:

```text
exact number of identity-bearing bytes copied
from the already-fixed synthetic actual object
into an architecture-specific evidence channel
solely because chi_i requires that evidence
```

and states specifically that raw executed-object bytes copied into chi_2/chi_3 custody count.

The inherited capture implementation is:

```python
def _capture_identity_bytes(data: bytes) -> bytes:
    return bytes(data)


def capture(self, data: bytes) -> bytes:
    self.complete["C_capture_bytes"] = False
    captured = _capture_identity_bytes(data)
    self.C_capture_bytes += len(captured)
    if len(captured) != len(data):
        raise ConformanceError("required capture incomplete")
    self.complete["C_capture_bytes"] = True
    return captured
```

Production then performs separately:

```text
captured = cost.capture(case.executed_bytes)
store.write("executed.raw", captured)
```

The capture dimension is therefore marked complete before the subsequent architecture-specific custody write occurs.

Two semantic problems follow.

First, the implementation has not frozen or mechanically demonstrated that the return value of `_capture_identity_bytes` itself is the constituted architecture-specific evidence channel. The frozen contract speaks about bytes copied into an architecture-specific evidence channel/custody, while the current code grants cost authority at an intermediate helper return.

Second, the helper is `bytes(data)` where `data` is already typed as `bytes`. That expression does not mechanically guarantee creation of a distinct copied byte representation; an immutable bytes value may be reused. Therefore the implementation does not establish that `len(captured)` corresponds to bytes that were actually copied at that boundary.

A later custody-write failure can consequently leave:

```text
C_capture_bytes = len(executed_bytes)
measurement_complete = true
C_persist_bytes = incomplete
```

without proof that the constituted copy-into-custody/evidence-channel event ever completed.

This is not the historical v0.1.8 attempted-versus-completed counter-order defect. That defect was repaired. The new defect is semantic/physical realization:

```text
helper returned bytes
!= established bytes copied into constituted evidence channel
```

Thus `C_capture_bytes` is still not guaranteed to measure the event named by the frozen primary currency.

This is the first remaining Gate-5 blocker. Later instrumentation sub-burdens are not promoted by this review.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture authority semantics, sandbox, lifecycle, extraction semantics, view/persistence/SHA/compare accounting, scoring, missingness rules, or Pareto rules.

Before another code patch, freeze the implementation mapping of the already-frozen capture currency:

```text
what exact causal operation constitutes
"copied into an architecture-specific evidence channel"?
```

Then make the sole capture instrument coincide with that operation.

A conforming successor must prospectively prove at minimum:

```text
capture count is earned only when an actual copy into the constituted architecture-specific evidence channel occurs
successful capture -> count actual bytes copied at that boundary
failed/partial/unknown copy -> preserve known work where available and remain incomplete
custody/persistence failure cannot leave capture complete unless the frozen capture event has independently already completed
chi_0/chi_1 no-capture paths remain justified complete zero
chi_2/chi_3 use the same common capture primitive
no helper-name or object-alias shortcut can manufacture capture work
```

The repair must preserve the distinction between capture and persistence rather than silently redefining one as the other after implementation outcomes are known.

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

capture completed-work ordering:
REPAIRED HISTORICALLY

cumulative persistence partial-write accounting:
REPAIRED

exact-view dispatch-byte accounting:
REPAIRED

semantic extraction instrumentation:
REPAIRED

failure locus:
CAPTURE SEMANTIC / PHYSICAL COPY BOUNDARY

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
FREEZE EXACT IMPLEMENTATION MAPPING OF THE EXISTING C_CAPTURE_BYTES CURRENCY
THEN MINIMAL CAPTURE-BOUNDARY REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
