# Minimum Identity Independence Implementation v0.1.10 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.10`

Status: `IMPLEMENTATION_REVIEW_BLOCKED / EXECUTION_NOT_ELIGIBLE / NON_AUTHORIZING`

Constituted assay evaluations: `0`

Scientific/model observations: `0`

This review restarts from implementation Gate 1 after repairing exact-view dispatch-byte accounting. It reviews gates in order and stops at the first remaining blocking defect.

## Reviewed authority

```text
constitution:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution review:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.4_REVIEW
blob: 08436c34754503313219b11fac7dcd5d199634b3

successor implementation:
tools/minimum_identity_independence_v014_v020.py
blob: c9e01cc0abb592bf5417784c6881787590e6f5a3

successor conformance fixtures:
tests/test_minimum_identity_independence_v014_v020.py
blob: 659408eef189089823ed97df9ae54b151ba9ae90

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

The successor changes only the harness-side exact-view transfer accounting path and uses unbuffered stdin so returned production write counts are the dispatch measurement primitive.

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
one-way event channel
```

No new architecture-visible case-bearing channel is introduced.

## Gate 2 — exact V_i projection realization

State: `PASS`

The exact serialized view is constructed with the same frozen schemas, field order, evidence sources, opaque-handle rule, custody override semantics, serialization, and shared dispatch attestation.

The historical `mark_view(data)` cost-authority call is removed from preparation, but this does not change the bytes of `V_i`; it changes only when primary view-byte cost authority is granted.

Preparation still ends at T1 with the exact view fixed.

## Gate 3 — stateless architecture evaluation realization

State: `PASS`

The new view-byte ledger state remains parent-side and is not serialized into `V_i`, argv, environment, filesystem, or any architecture-readable channel.

The child remains a fresh sandbox process per invocation with no readable prior cost or lifecycle state.

## Gate 4 — T0..T4 realization

State: `PASS`

The successor preserves the reviewed lifecycle meaning and strengthens the coupling between dispatch evidence and T2:

```text
prepare ends at T1
sandbox restrictions become active
SANDBOX_READY observed
exact V_i transfer attempted through unbuffered stdin
full exact transfer + flush/close succeeds
-> T2_EXACT_VIEW_DISPATCHED
terminal bytes freeze
-> T3
referee/oracle join
-> T4
```

A readiness failure, known partial transfer, unknown transfer failure, or flush/close failure cannot emit T2.

The view-cost completion method itself requires lifecycle state through T2.

## Gate 5 — six-dimensional cost instrumentation realization

State: `FAIL`

### Repaired sub-burden — exact-view dispatch-byte accounting

The historical defect is repaired mechanically.

After preparation:

```text
C_view_bytes = null
measurement_complete = false
T2 absent
```

The old prepare-time completion method is overridden and raises if called.

During actual production transfer:

```text
known transferred prefix -> C_view_bytes = prefix length, complete=false
known zero/short termination -> retain known prefix, complete=false, T2 absent
unknown transfer failure -> C_view_bytes = null, complete=false, T2 absent
full exact transfer -> T2 -> C_view_bytes = len(V_i), complete=true
```

The successor has one production assignment of:

```text
complete["C_view_bytes"] = true
```

and that assignment first requires lifecycle state through T2.

Thus:

```text
C_view_bytes complete=true
=> T2 exists
=> full exact V_i transfer completed
```

The published 13-fixture file encodes these requirements. No fixture execution result is claimed by this review.

### Next blocking defect — authority-bearing raw-custody read bypasses `C_extract_ops` instrumentation

The frozen cost contract defines `C_extract_ops` as completed authority-bearing raw-evidence extraction operations and states that an extraction includes a complete parse/decoding/read that transforms authoritative raw executed-object custody into a byte sequence used as identity authority by the architecture.

It further requires any authority-bearing raw extraction to use the common instrumented extraction primitive.

The current preparation path for chi_2/chi_3 performs:

```python
store.write("executed.raw", captured)
raw = store.read("executed.raw")
view["executed_raw_bytes_utf8"] = raw.decode()
```

The inherited `Store.read()` is a plain filesystem read:

```python
def read(self, name: str) -> bytes:
    return self.p(name).read_bytes()
```

and does not increment or otherwise instrument `C_extract_ops`.

For chi_3, `executed.raw` is not diagnostic-only evidence. The constituted chi_3 authority path independently recomputes executed-object identity from `executed_raw_bytes_utf8`:

```text
executed raw custody
-> raw bytes read from custody
-> V_i executed_raw_bytes_utf8
-> child byte reconstruction
-> independent SHA256
-> H_e authority
```

Therefore the pre-dispatch custody read is an authority-bearing raw-custody extraction on the chi_3 identity path.

Yet the only currently counted extraction event occurs later inside the child:

```python
executed_hash = digest(extract(view["executed_raw_bytes_utf8"]))
```

That event measures a transformation of an already-serialized architecture-visible string back into bytes. It does not instrument the earlier authoritative read from the architecture-specific raw custody artifact.

Thus the current implementation does not guarantee:

```text
every authority-bearing raw-custody extraction
-> common instrumented extraction primitive
```

and can underrepresent or semantically mislocate `C_extract_ops`.

The distinction between chi_2 and chi_3 matters:

```text
chi_2 raw bytes are diagnostic and may not become alternate H_e authority
chi_3 raw bytes are the substrate for independent H_e recomputation
```

So a repair must not blindly count every `Store.read()` for both architectures. It must instrument the extraction according to the frozen authority role.

This is the first remaining Gate-5 blocker. Later cost-instrumentation sub-burdens are not promoted by this review.

### Required shallowest repair

Do not change the constitution, oracle, schemas, architecture authority semantics, sandbox, lifecycle, view/capture/persistence/SHA accounting, scoring, cost dimensions, missingness rules, or Pareto rules.

Repair only `C_extract_ops` realization so that every completed authority-bearing extraction from executed raw custody is routed through one common instrumented extraction primitive, while diagnostic-only reads remain excluded as constituted.

A conforming successor must prospectively settle and test at minimum:

```text
chi_3 completed authority-bearing custody extraction -> counted exactly as constituted
chi_3 failed custody extraction -> no completed-op count; extraction measurement incomplete
chi_2 diagnostic raw-custody read -> cannot become identity authority and is excluded from primary extraction count
no authority-bearing custody extraction may bypass the common primitive
child-side serialized-field reconstruction must not create a second inconsistent definition of the same primary extraction unit
aggregate rejects incomplete extraction measurement
```

The repair must preserve one deterministic semantic interpretation of `C_extract_ops`; it may not count one notion of extraction in the parent and a different notion in the child without prospective justification under the frozen contract.

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

exact-view dispatch-byte accounting:
REPAIRED

failure locus:
AUTHORITY-BEARING RAW-CUSTODY EXTRACTION INSTRUMENTATION

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
MINIMAL IMPLEMENTATION GATE-5 AUTHORITY-BEARING EXTRACTION-INSTRUMENTATION REPAIR ONLY
THEN RESTART HOSTILE IMPLEMENTATION REVIEW FROM GATE 1
```
