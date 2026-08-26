# Minimum Identity Independence Implementation v0.1.4

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.4`

Status: `IMPLEMENTED / LIFECYCLE_FIXTURES_PUBLISHED / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the minimal Gate-4 lifecycle-realization successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.3` failed hostile implementation review because `T2_EXACT_VIEW_DISPATCHED` was marked before the exact `V_i` bytes were actually dispatched.

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
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_3_REVIEW.md
blob: 235ab19cd2ce6f73cb60c84c7984450f8be71601

successor implementation
tools/minimum_identity_independence_v014_v014.py
commit introducing file: 229acf6b6e44c0cb9ce83ecfe1b0ad41f179fef1
blob: 6da915ec0ee71e41e52e6383e296ac1afd921516

lifecycle conformance fixtures
tests/test_minimum_identity_independence_v014_v014.py
commit introducing file: b6245cef26376eb154d64242a5264b671f5e7012
blob: 0207c03cc787b910bac53f9a327d694a90ddf9c5
```

Both committed successor files were read back after publication.

## Sole intended repair

No constitution, oracle, frozen view schema, architecture identity logic, capability sandbox, scoring rule, or cost definition is changed.

The repair changes only lifecycle realization.

Historical v0.1.3 behavior:

```text
prepare()
  -> mark T2_EXACT_VIEW_DISPATCHED
  -> later launch sandbox
  -> later SANDBOX_READY
  -> later write V_i
```

Successor v0.1.4 behavior:

```text
prepare()
  -> T0
  -> T1
  -> construct/freeze exact V_i
  -> return with lifecycle authority stopped at T1

run()
  -> launch unchanged v0.1.3 sandbox
  -> wait for SANDBOX_READY
  -> write exact frozen V_i bytes to child stdin
  -> flush and close the child input stream
  -> verify full byte count was written
  -> mark T2_EXACT_VIEW_DISPATCHED
  -> receive/validate terminal output
  -> copy/freeze/hash terminal bytes
  -> mark T3_TERMINAL_ARCHITECTURE_VERDICT_FROZEN
  -> decode/merge one-way instrumentation

score()
  -> inherited T3 prerequisite
  -> T4_REFEREE_ORACLE_JOIN
```

Thus the authoritative invariant is now:

```text
T2 -> sandbox restrictions active
   AND exact V_i fixed
   AND full exact V_i byte write completed
```

An attempted or failed dispatch does not earn T2.

## Failure behavior

The successor fails without T2 when:

```text
sandbox readiness is absent/fails
child stdin is unavailable
child input write breaks
write returns zero/None before completion
flush/close fails
full byte count is not written
```

If dispatch succeeds but terminal execution subsequently fails, T2 may remain true while T3 remains absent. This reflects the actual event history rather than collapsing attempted execution into a false all-or-nothing state.

## Lifecycle conformance fixtures

The frozen successor fixture file contains 12 synthetic engineering tests, including:

```text
prepare stops at T1
forced delay inside exact-view write: T2 remains impossible while write is blocked
failed write -> no T2
sandbox readiness failure -> no T2
normal production path -> T2 then T3 then T4
terminal path failure after T2 -> no T3
T4 cannot occur before T3
successor spawn retains file denial
successor spawn retains network/socketpair denial
successor spawn retains parent-environment denial
identical V_i remains invariant to hidden parent environment
projection schema/field order remains frozen
```

These are implementation-conformance fixtures only. They are not assay observations.

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
