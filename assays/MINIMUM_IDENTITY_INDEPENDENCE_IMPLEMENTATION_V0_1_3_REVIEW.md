# Minimum Identity Independence Implementation v0.1.3 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.3`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after adding a hard runtime capability boundary. It reviews gates in order and stops at the first blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v013.py
blob: 11957b8b90c68cd45c40a9a2e2161a40d06cb91f

capability-denial fixtures:
tests/test_minimum_identity_independence_v014_v013.py
blob: e8ea93a37b3443577dda11d754837ff9c31da042
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

The v0.1.3 child does not receive `V_i` until after a sandbox readiness barrier.

Before readiness, trusted bootstrap code installs:

```text
PR_SET_NO_NEW_PRIVS
seccomp BPF capability denial
import denial
module-discovery clearing
```

The child is launched in fresh user/network/PID namespaces with:

```text
env = {}
close_fds = true
fresh temporary cwd
```

Only after the child emits:

```text
SANDBOX_READY
```

does the parent write the exact `V_i` bytes to stdin.

The production architecture therefore receives case-bearing input only after the capability boundary is active.

The exact committed 11-fixture suite was executed locally against the committed implementation bytes and passed. It adversarially establishes on the tested Linux x86_64 runtime:

```text
forbidden file read -> denied
network socket creation -> denied
socketpair / peer IPC -> denied
fork -> denied
parent-process query -> denied
arbitrary import -> denied
parent environment -> absent
same V_i under different hidden parent state -> identical architecture result/event trace
changed forbidden sentinel contents -> unreadable
```

The implementation fails closed if the required Linux x86_64 namespace/seccomp runtime is unavailable.

This is stronger than the historical `python -I` implementation because the reviewed claim is now capability denial on the tested runtime, not source-level non-use.

Ceiling:

```text
PASS_ON_FROZEN_LINUX_X86_64_RUNTIME
!= universal sandbox theorem
```

## Gate 2 — exact V_i projection realization

State: `PASS`

The successor intentionally inherits the already-frozen projection and serialization implementation from v0.1.2/v0.1.1.

Before child launch, parent-side `parse(chi, view_bytes)` validates the exact serialized bytes against the frozen architecture view schema.

The child receives those same bytes on stdin without reserialization, wrapper metadata, case label, oracle field, cost ledger, or ordinal.

The child independently rejects unexpected key order or noncanonical compact JSON before executing architecture logic.

Thus the realized architecture case-bearing payload remains:

```text
exact serialized V_i bytes
```

with no extra case-bearing field introduced by the runtime-sandbox repair.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

Every architecture invocation creates a fresh process under fresh namespaces and a fresh temporary working directory.

The launcher supplies:

```text
env = {}
close_fds = true
no previous-run object
no persistent architecture process
no shared mutable meter
no inherited parent case state
```

The child PID namespace and denied process/filesystem/network capabilities prevent ordinary recovery of prior or peer evaluation state after readiness.

The identical-`V_i` hidden-parent-world regression produces an identical full `ArchitectureResult`, including terminal bytes and instrumentation event bytes.

Therefore no epistemically meaningful cross-evaluation architecture state is realized by v0.1.3 on the reviewed runtime.

## Gate 4 — T0..T4 realization

State: `FAIL`

The frozen cost/lifecycle contract defines:

```text
T2 = EXACT_VIEW_DISPATCHED
```

But v0.1.3 inherits `prepare()` from the previous implementation. That function marks:

```python
life.mark(Life.ORDER[2])
```

before returning the `Prepared` object.

At that moment no architecture child has necessarily been launched and no `V_i` bytes have been written to child stdin.

In v0.1.3, the actual dispatch occurs later inside `_spawn()`:

```text
launch sandbox child
wait for SANDBOX_READY
then proc.communicate(input=input_bytes)
```

Therefore the implemented event ordering is effectively:

```text
mark T2
-> later create/ready sandbox
-> later write exact V_i to architecture stdin
```

rather than the constituted meaning:

```text
exact V_i dispatched
-> mark T2
```

So the lifecycle label currently asserts an event before the event actually occurs.

This is an identity/provenance defect in the measurement timeline, not merely cosmetic naming. The cost contract uses `T1..T3` to determine which operations are architecture-attributable, and implementation review must prove the frozen boundaries are real events.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture logic, capability sandbox, scoring, or cost definitions.

Repair only lifecycle realization so that:

```text
T2_EXACT_VIEW_DISPATCHED
```

is marked at the actual successful dispatch boundary, after sandbox readiness and when the exact frozen `V_i` bytes are committed to the child input channel.

A successor should include adversarial lifecycle fixtures proving at minimum:

```text
T2 cannot exist before SANDBOX_READY
T2 cannot exist if dispatch fails before V_i transfer
T3 cannot exist before terminal output bytes are frozen
T4 cannot exist before T3
```

After repair, restart hostile implementation review from Gate 1.

## Gate 5 — six-dimensional cost instrumentation realization

State: `NOT_OPENED`

Gate 4 failed first. No Gate-5 implementation conclusion is authorized by this review.

## Terminal review state

```text
ORACLE_ISOLATION_REALIZATION:
PASS_ON_FROZEN_LINUX_X86_64_RUNTIME

EXACT_VIEW_PROJECTION_REALIZATION:
PASS

STATELESS_EVALUATION_REALIZATION:
PASS

T0_T4_REALIZATION:
FAIL

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
MINIMAL IMPLEMENTATION GATE-4 LIFECYCLE-REALIZATION REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
