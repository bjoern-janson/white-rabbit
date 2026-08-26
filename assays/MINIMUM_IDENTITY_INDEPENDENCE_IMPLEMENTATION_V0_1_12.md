# Minimum Identity Independence Implementation v0.1.12

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.12`

Status: `IMPLEMENTED / CONFORMANCE_FIXTURES_PUBLISHED / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the minimal Gate-5 successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.11` failed hostile implementation review because `C_capture_bytes` was attached to an intermediate helper return rather than the constituted transfer into the architecture-specific evidence channel.

It does not authorize the constituted 36 architecture-case evaluations.

## Authority

```text
constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4.md
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution hostile review
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4_REVIEW.md
blob: 08436c34754503313219b11fac7dcd5d199634b3

frozen cost contract v0.1
assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f

cost-contract persistence successor
assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1_1.md
blob: bd15bf90c8ccade881d5b8a2e7973f58eef28602

historical implementation blocker
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_11_REVIEW.md
blob: 4d7203f26891e3ca815d3b608b12c8d5cd0de589

successor implementation
tools/minimum_identity_independence_v014_v022.py
commit introducing file: 06f7007c346da67e0879ce6a333526cc9392d272
blob: e490035c0ce68e0d39066a07ba337c2a3671a36f

successor conformance fixtures
tests/test_minimum_identity_independence_v014_v022.py
commit introducing file: 105f239cdce18ba561749f141397e9de914efa72
blob: c68a4cda465d573d9d3cae538c674c69b9112b99
```

Both committed successor files were read back after publication.

## No cost-contract amendment

The frozen cost contract already defines `C_capture_bytes` as the exact number of identity-bearing bytes copied from the already-fixed synthetic actual object into an architecture-specific evidence channel solely because the selected architecture requires that evidence.

This successor freezes only the implementation mapping of that existing currency.

## Frozen capture boundary

For this assay implementation, the architecture-specific evidence channel is the `executed.raw` custody artifact required by chi_2 and chi_3.

The constituted CAPTURE event is exactly:

```text
fixed executed-object source bytes
-> authoritative architecture-specific executed.raw transfer
```

`C_capture_bytes` is the authoritative returned number of bytes transferred across that boundary.

A Python in-memory conversion such as `bytes(data)` is not capture authority.

The inherited `Cost.capture(data)` method is overridden and raises so the historical helper-return boundary cannot silently regain cost authority.

## Capture and persistence remain distinct

The initial `executed.raw` transfer has two prospectively frozen measurement roles:

```text
C_capture_bytes:
  source -> architecture-specific evidence-channel bytes

C_persist_bytes:
  cumulative architecture-attributable bytes newly written
```

The same physical initial write can therefore contribute the same returned byte count to both dimensions without scalar double-counting or semantic conflation.

Later overwrite/append/replacement writes contribute only to persistence. They never create new capture work.

## Completion / missingness

For chi_2/chi_3, capture begins pending at T1.

Full exact evidence-channel transfer:

```text
returned bytes = len(fixed executed source)
C_capture_bytes = returned bytes
capture measurement_complete = true
C_persist_bytes += returned bytes
persistence completeness follows its existing sticky rules
```

Known partial transfer:

```text
C_capture_bytes = known returned byte count
capture measurement_complete = false
C_persist_bytes += same known returned byte count
persistence measurement_complete = false
failure propagates
```

Unknown transfer amount:

```text
C_capture_bytes = null
capture measurement_complete = false
no invented capture count
persistence receives no invented delta and remains incomplete
failure propagates
```

For chi_0/chi_1:

```text
C_capture_bytes = 0
measurement_complete = true
```

because their constituted paths require no executed-object capture.

## Retained prior repairs

The successor inherits unchanged:

```text
hard architecture capability sandbox
exact V_i projection and isolation
stateless child invocation
actual T2 dispatch lifecycle
exact-view dispatch-byte accounting
cumulative persistence accounting
completed projection/child SHA accounting
semantic chi_3 authority extraction accounting
completed authority-bearing identity comparison events
fail-closed operation-stream completeness
componentwise aggregate/Pareto rules
```

## Published conformance fixtures

The successor fixture file prospectively checks:

```text
historical memory-helper capture authority is disabled
full evidence-channel transfer -> capture and persistence exact/complete
known partial transfer -> known capture/persist work retained, both incomplete
unknown transfer -> no invented capture count, both incomplete
bytes(data) alone -> no capture work
successful memory preparation + failed channel write -> capture incomplete
later rewrite -> persistence increases, capture unchanged
delete/replacement -> persistence cumulative, capture remains single event
chi_2 prepare -> exact custody capture, diagnostic extraction zero
chi_3 prepare -> exact custody capture plus distinct authority extraction
chi_0/chi_1 no-capture -> complete zero
incomplete capture -> aggregate rejection
semantic extraction rules retained
view dispatch authority remains pending after prepare
```

These are published engineering conformance tests only.

No execution result for these fixtures is claimed in this artifact.

## Execution firewall

```text
constituted assay architecture-case evaluations executed: 0
scientific/model observations: 0
Gate 7 observations created: 0
```

Next permitted action:

```text
HOSTILE IMPLEMENTATION-CONFORMANCE REVIEW FROM GATE 1
```

Execution remains unauthorized.
