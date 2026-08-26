# Minimum Identity Independence Implementation v0.1.8

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.8`

Status: `IMPLEMENTED / CONFORMANCE_FIXTURES_PUBLISHED / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the minimal Gate-5 successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.7` failed hostile implementation review because `C_capture_bytes` was incremented before the capture operation completed.

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
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_7_REVIEW.md
blob: c80e6e6c60bfdb79f4c5936ebdf7b9dd2599fcc9

successor implementation
tools/minimum_identity_independence_v014_v018.py
commit introducing file: a09662f62bfb5ad87ee256fac48ced59f0d47da2
blob: 030c2b35055755cb44cd8e56c2af99d7852b8eea

successor conformance fixtures
tests/test_minimum_identity_independence_v014_v018.py
commit introducing file: 770aa7a90a883005acc3d7b7439b37a7accd89f0
blob: 57eaf9d646250507d4c1247510d3b74e4b0f70ac
```

Both committed successor files were read back after publication.

## Sole intended repair

No constitution, oracle, view schema, architecture authority logic, runtime sandbox, lifecycle meaning, SHA/extract/compare completed-operation semantics, scoring rule, cost dimension, missingness rule, or Pareto rule changes.

The capture path now has the authoritative ordering:

```text
captured = capture_identity_bytes(data)
-> C_capture_bytes += len(captured)
-> return captured
```

The intended input length is never credited before capture returns.

For a required chi_2/chi_3 capture:

```text
capture measurement starts incomplete at T1
successful exact capture -> count actual returned bytes, complete=true
capture exception -> no false input-length increment, complete=false
partial returned capture -> count only actual returned bytes, complete=false, propagate failure
```

For chi_0/chi_1:

```text
no executed-byte capture is required
C_capture_bytes = 0
measurement_complete = true
```

so complete-zero is granted only for the constituted no-capture architectures.

## Completed-work consistency

The production primary completed-work paths now mechanically realize:

```text
C_sha256_ops:
  parent projection digest succeeds before +1
  child digest succeeds before completed-operation event

C_extract_ops:
  child extraction succeeds before completed-operation event

C_identity_compare_ops:
  child comparison succeeds before completed-operation event

C_capture_bytes:
  actual captured bytes return before byte credit
```

The total SHA/extract/compare dimensions remain fail-closed until the one-way T2->T3 event stream is acquired and decoded successfully.

## Published conformance fixtures

The successor fixture file prospectively checks:

```text
successful capture -> count actual returned bytes
failed capture -> no increment and incomplete
partial returned capture -> count only actual returned bytes and remain incomplete
failed required capture during prepare -> not complete-zero
chi_2 exact executed-byte capture
chi_3 exact executed-byte capture
chi_0 valid no-capture complete-zero
chi_1 valid no-capture complete-zero
projection-SHA completion semantics retained
operation-stream dimensions remain pending after prepare
aggregate rejects incomplete required capture
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
