# Minimum Identity Independence Implementation v0.1.10

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.10`

Status: `IMPLEMENTED / CONFORMANCE_FIXTURES_PUBLISHED / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the minimal Gate-5 successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.9` failed hostile implementation review because `C_view_bytes` was granted complete during preparation rather than at the actual exact-view dispatch boundary.

It does not authorize the constituted 36 architecture-case evaluations.

## Authority

```text
constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4.md
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution hostile review
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4_REVIEW.md
blob: 08436c34754503313219b11fac7dcd5d199634b3

historical implementation blocker
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_9_REVIEW.md
blob: 7cc8beb7e1ee8a7c81972f77923a068fd6c8a148

successor implementation
tools/minimum_identity_independence_v014_v020.py
final repair commit: 60e5628c05676d4f9bbd7f350e28a91ab0bec361
blob: c9e01cc0abb592bf5417784c6881787590e6f5a3

successor conformance fixtures
tests/test_minimum_identity_independence_v014_v020.py
commit introducing file: 762b5d5dd761039995720967fe57aa45a1a4f5c5
blob: 659408eef189089823ed97df9ae54b151ba9ae90
```

Both committed successor files were read back after publication.

## Sole intended repair

No constitution, oracle, view schema, architecture authority logic, runtime capability boundary, lifecycle meaning, SHA/extract/compare/capture/persistence semantics, scoring rule, cost dimension, missingness rule, or Pareto rule changes.

The sole repaired primary dimension is:

```text
C_view_bytes
```

Preparation now leaves that dimension pending:

```text
C_view_bytes = null
measurement_complete = false
lifecycle = through T1 only
```

The historical `Cost.mark_view(data)` completion path is overridden and forbidden in the successor.

## Authoritative dispatch accounting

The production child stdin channel is opened unbuffered (`bufsize=0`).

The actual transfer loop is the sole production authority path for `C_view_bytes`.

For every positively known returned transfer count:

```text
known transferred prefix -> C_view_bytes = known prefix length
measurement_complete = false
```

A known partial transfer therefore retains its observed prefix count but cannot earn exact-view completion.

If a transfer attempt fails without an authoritative returned byte count:

```text
C_view_bytes = null
measurement_complete = false
T2 absent
```

No full or zero count is invented.

Only after the full exact serialized `V_i` has been transferred and the stream flush/close path succeeds does the lifecycle earn:

```text
T2_EXACT_VIEW_DISPATCHED
```

The `Cost` completion method itself requires lifecycle state through T2 before it may set:

```text
C_view_bytes = len(V_i)
measurement_complete = true
```

Thus the production invariant is mechanically:

```text
C_view_bytes measurement_complete = true
=> T2 exists
=> full exact V_i transfer completed
```

Sandbox readiness failure leaves the dimension pending and T2 absent.

## Single authority path

The successor contains one production assignment of:

```text
complete["C_view_bytes"] = true
```

and that assignment is guarded by:

```text
life.through(T2_EXACT_VIEW_DISPATCHED)
```

The inherited prepare-time convenience method is disabled by override rather than merely left unused.

Engineering-only `evaluate()` and capability probes do not create primary `C_view_bytes` authority.

## Published conformance fixtures

The successor fixture file prospectively checks:

```text
prepare leaves view measurement pending
historical prepare-time mark_view authority is disabled
full exact transfer -> exact bytes, T2, complete=true
known partial transfer -> actual prefix, incomplete, no T2
unknown transfer exception -> null/incomplete, no T2
flush failure -> fail closed, no T2
readiness failure -> pending/incomplete, no T2
view completion cannot be granted before T2
only one successor production complete=true assignment exists
production spawn uses unbuffered stdin transfer
aggregate rejects incomplete view measurement
capture/persistence repairs remain intact
projection/child completed-operation semantics remain intact
```

These are published engineering conformance tests only.

No fixture execution result is claimed in this artifact.

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
