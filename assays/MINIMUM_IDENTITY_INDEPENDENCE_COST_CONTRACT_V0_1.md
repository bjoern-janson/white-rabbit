# Minimum Identity Independence Cost Contract v0.1

Version: `MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1`

Status: `FROZEN_COST_CONTRACT / NON_EXECUTED / NON_AUTHORIZING`

This artifact is the minimal Gate-5 repair for `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.2` after hostile review found that the cost dimensions were not prospectively frozen tightly enough to support Pareto or unique-minimum claims.

It changes only the cost-comparability contract. It does not modify the oracle, identity-evidence architectures, view boundary, scoring, critical/diagnostic partition, claim ceiling, or execution authorization state.

## 1. Purpose

The cost question is contract-relative:

```text
among architectures that satisfy the frozen critical identity contract,
what literal architecture-attributable resource vector was required?
```

This contract freezes a mandatory primary cost vector and forbids post-result choice of dimensions, measurement boundaries, or missingness rules.

No scalar cost is defined.

## 2. Primary comparison horizon

The primary cost horizon is exactly the same six critical cases used by the sufficiency gate:

```text
C0_ALPHA_CLEAN
C1_BETA_CLEAN
E1_FROZEN_MATERIALIZED_MISMATCH
E2_MATERIALIZED_EXECUTED_MISMATCH
E3_CROSS_OBJECT_SUBSTITUTION
E4_FALSE_CLEAN_CUSTODY_IDENTITY_REPORT
```

Diagnostic cases `D1`, `D2`, and `D3` are measured separately and never enter primary Pareto or unique-minimum claims in v0.1.

For each architecture, the primary aggregate vector is the componentwise sum over its six critical evaluations.

The referee may use its sealed opaque-handle mapping to aggregate critical cases after architecture outputs and cost ledgers are frozen. Semantic case identity remains unavailable to the architecture under test.

## 3. Cost attribution classes

Every measured operation or byte belongs prospectively to exactly one of three accounting classes:

```text
A. architecture-attributable
B. shared experiment scaffolding
C. one-time fixture/oracle construction
```

Only class A enters the primary architecture cost vector.

Class B and C must be reported separately and cannot affect Pareto membership or minimum claims.

### A. Architecture-attributable

An operation or byte is architecture-attributable iff it exists because the selected `chi_i` evidence path requires it and it occurs after the common synthetic actual object has been fixed and before that architecture's terminal verdict is frozen.

Examples include:

- architecture-specific evidence capture;
- architecture-specific evidence persistence;
- fields added to the dispatched `V_i` because that architecture requires them;
- SHA-256 operations required to construct or consume architecture-specific identity evidence;
- raw executed-byte extraction/reconstruction required by the architecture contract;
- identity comparisons required to produce the terminal verdict.

### B. Shared experiment scaffolding

Shared scaffolding includes:

- synthetic case construction common to all architectures;
- oracle lookup and sealed handle mapping;
- opaque-handle generation;
- common schema validation framework;
- common `dispatched_view_sha256` attestation required equally for all architectures;
- referee scoring;
- architecture-output hashing used only for referee custody;
- common test runner setup/teardown;
- cost-ledger instrumentation overhead itself.

These costs are recorded separately where measured but are excluded from `C_primary(chi_i)`.

### C. One-time fixture/oracle construction

One-time costs include:

- construction of ALPHA / ALPHA_MUT / BETA fixtures;
- construction and freezing of the oracle manifest;
- constitution/review artifact generation.

These are reported as lineage/scaffolding and never attributed to an individual architecture.

## 4. Mandatory primary vector

For every architecture `chi_i`, the mandatory primary vector is exactly:

```text
C_primary(chi_i) = (
  C_view_bytes,
  C_capture_bytes,
  C_persist_bytes,
  C_sha256_ops,
  C_extract_ops,
  C_identity_compare_ops
)
```

All six dimensions are mandatory.

No other dimension may enter v0.1 Pareto or unique-minimum decisions.

All dimensions are non-negative integers.

## 5. Dimension definitions

### 5.1 `C_view_bytes`

Unit: bytes.

Per evaluation:

```text
C_view_bytes = len(exact UTF-8 serialized V_i bytes dispatched to chi_i)
```

Use the exact view serialization frozen by `MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0.1`:

```text
UTF-8
no BOM
compact JSON
frozen field order
ensure_ascii = false
no terminal newline
no extra fields
```

The value is measured after sealed projection and immediately before architecture dispatch.

The 64-character opaque handle is included because it is physically present in every dispatched view. Its fixed-length common contribution is therefore counted equally rather than subtracted.

No process arguments, environment variables, filenames, or referee metadata are included because they are forbidden architecture-visible case inputs.

### 5.2 `C_capture_bytes`

Unit: bytes.

Per evaluation, count the exact number of identity-bearing bytes copied from the already-fixed synthetic actual object into an architecture-specific evidence channel solely because `chi_i` requires that evidence.

For this assay:

```text
raw executed-object bytes copied into chi_2/chi_3 custody count;
bytes already present as immutable/shared synthetic fixtures do not count;
referee/oracle copies do not count;
metadata generated from bytes does not count here.
```

A valid zero is permitted only when the cost ledger explicitly records measurement completion and zero architecture-attributable capture bytes.

### 5.3 `C_persist_bytes`

Unit: bytes.

Each architecture evaluation must have a dedicated architecture-evidence custody root that is empty at the architecture-attributable cost start event.

Per evaluation:

```text
C_persist_bytes =
sum(final file sizes in that root at terminal-verdict freeze)
```

included:

- only evidence artifacts whose creation is required by the selected architecture evidence path;
- raw custody bytes;
- architecture-specific evidence metadata or architecture-specific stored hashes, if persisted.

excluded:

- cost-ledger files;
- common runner logs;
- oracle/referee artifacts;
- architecture output custody used equally by the referee;
- immutable pre-existing fixtures;
- shared schema/constitution files.

Files deleted before terminal freeze still count as bytes written and therefore must not be used to evade this metric. The instrumentation must maintain a cumulative `architecture_evidence_bytes_written` counter. The primary value is:

```text
C_persist_bytes = cumulative architecture-evidence bytes newly written
```

not terminal retained size.

The dedicated root is a custody boundary, not the measurement source by itself; the cumulative write counter is authoritative.

### 5.4 `C_sha256_ops`

Unit: completed SHA-256 digest operations.

Count every completed SHA-256 digest whose input or output is required solely by the selected architecture evidence path during the architecture-attributable interval.

Included examples:

- architecture-specific computation of visible frozen/materialized identity hashes when not already a shared pre-existing authority;
- custody-reported executed hash computation required for `chi_2` / `chi_3`;
- independent executed-byte SHA-256 recomputation required by `chi_3`.

Excluded:

- shared schema hash verification;
- common `dispatched_view_sha256`;
- oracle/referee hashes;
- architecture-output custody hashes;
- one-time fixture/oracle hashes.

A digest over any number of bytes counts as one operation.

Repeated/redundant digest calls count separately.

The implementation must route architecture-attributable SHA-256 calls through a common instrumented primitive. Bypassing the primitive makes the cost ledger incomplete and the implementation nonconforming.

### 5.5 `C_extract_ops`

Unit: completed authority-bearing raw-evidence extraction operations.

An extraction operation is one complete parse/decoding/read that transforms authoritative raw executed-object custody into a byte sequence used as identity authority by the architecture.

Count one operation each time such extraction completes.

Do not count:

- merely receiving an already serialized `V_i` field;
- ordinary JSON field lookup;
- referee parsing;
- operations on semantic case IDs, which are forbidden;
- extraction that is performed only for diagnostics and cannot affect identity authority.

For `chi_3`, the constituted independent `H_e` recomputation requires an authority-bearing extraction of executed raw bytes and therefore must generate at least one such operation when the evaluation reaches that path.

For `chi_2`, treating raw bytes as an alternate identity authority or directly comparing them to bypass the custody-reported `H_e` would violate the architecture contract rather than create an allowed extraction cost.

The implementation must use a common instrumented extraction primitive for any authority-bearing raw extraction.

### 5.6 `C_identity_compare_ops`

Unit: completed authority-bearing equality/inequality comparisons.

Count a comparison when two identity-bearing values are compared and the result is permitted to influence the architecture terminal state.

Examples:

```text
H_f == H_m
H_m == H_e
H_f == H_e
```

Each executed pairwise equality/inequality test counts once.

Do not count:

- schema validation comparisons;
- case-handle comparisons;
- convenience-field parsing without equality testing;
- referee/oracle scoring comparisons;
- string comparisons used only for control flow unrelated to identity authority.

Short-circuiting is allowed if it follows the frozen implementation; only comparisons actually executed count. Redundant comparisons count separately.

The implementation must route authority-bearing identity comparisons through a common instrumented comparison primitive.

## 6. Per-evaluation measurement interval

For attribution purposes, each architecture-case evaluation has these exact events:

```text
T0 = COMMON_ACTUAL_OBJECT_FIXED
T1 = ARCHITECTURE_SPECIFIC_EVIDENCE_PATH_OPEN
T2 = EXACT_VIEW_DISPATCHED
T3 = TERMINAL_ARCHITECTURE_VERDICT_FROZEN
T4 = REFEREE_ORACLE_JOIN
```

Primary architecture-attributable operations may occur only in `[T1, T3]`.

`T0 -> T1` common case construction is scaffolding.

`T3 -> T4` scoring/referee work is scaffolding.

Architecture-specific evidence capture/persistence that must happen before dispatch occurs in `[T1,T2]` and is included.

Architecture computation over `V_i` occurs in `[T2,T3]` and is included where it matches a mandatory dimension.

## 7. Aggregate rule

For architecture `chi_i`, first freeze a complete six-dimensional vector for every critical evaluation.

Then compute:

```text
C_primary(chi_i)
  = componentwise sum over C0, C1, E1, E2, E3, E4
```

Do not average, normalize by case, or weight dimensions for the primary comparison.

Per-case vectors must also be preserved in the result artifact.

Diagnostic-case vectors are reported in a separate table and do not enter `C_primary`.

## 8. Missingness and completeness

Zero is a valid measurement only when the corresponding instrument explicitly records:

```text
measurement_complete = true
value = 0
```

Absence of an event, unavailable instrumentation, process failure, or an unclosed ledger is not zero.

For each evaluation and each mandatory dimension, record:

```text
value: non-negative integer | null
measurement_complete: true | false
```

An architecture primary vector is `COST_VECTOR_COMPLETE` iff all six mandatory dimensions are complete for all six critical evaluations.

Otherwise it is:

```text
COST_VECTOR_INCOMPLETE
```

If any critically sufficient architecture has `COST_VECTOR_INCOMPLETE`, the assay may not emit a global Pareto set or unique-minimum claim across the tested critically sufficient architectures.

It must instead emit:

```text
COST_COMPARISON_INCOMPLETE
```

and report all measured values without filling missing dimensions.

This prevents an unmeasured dimension from being treated as zero or ignored post hoc.

## 9. Timing and CPU diagnostics

Wall-clock duration and CPU time may be recorded only as diagnostics in v0.1.

If recorded:

```text
wall_time_ns = monotonic time from T2 to T3
cpu_time_ns = process CPU time from T2 to T3
```

They must use the same timing primitives and runtime environment for every architecture.

They do not enter:

```text
critical sufficiency
Pareto membership
componentwise dominance
unique-minimum claims
```

A future successor may promote timing to a primary dimension only prospectively before execution.

## 10. Dominance rule

Let `a` and `b` be critically sufficient architectures with complete primary vectors.

`a` weakly dominates `b` iff:

```text
for every one of the six frozen primary dimensions:
C_a[d] <= C_b[d]

AND
for at least one frozen primary dimension:
C_a[d] < C_b[d]
```

No weights, ratios, unit conversions, normalization, or lexicographic ordering are permitted.

## 11. Pareto rule

The Pareto set is computed only over critically sufficient architectures with complete primary vectors, and only if every critically sufficient architecture has a complete primary vector.

An architecture belongs to the Pareto set iff no other critically sufficient architecture weakly dominates it under Section 10.

Critically insufficient architectures are never members of the primary Pareto set, regardless of cost.

Their cost vectors remain reportable diagnostics.

## 12. Unique minimum rule

The assay may emit:

```text
UNIQUE_MINIMUM_TESTED_IDENTITY_ARCHITECTURE_OBSERVED
```

only if all of the following hold:

1. at least one architecture is critically sufficient;
2. every critically sufficient architecture has a complete primary vector;
3. exactly one critically sufficient architecture weakly dominates every other critically sufficient architecture;
4. the result is stated only relative to the tested architectures, frozen critical case contract, and this frozen six-dimensional cost vector.

Otherwise, if cost comparison is complete, emit the Pareto set without forcing a single winner.

## 13. Shared-cost reporting

Shared scaffolding and one-time construction costs may be reported in separate ledgers.

They must never be added to or subtracted from individual architecture vectors to manufacture dominance.

If an implementation discovers that an operation thought to be shared is actually architecture-specific, implementation review must stop before execution and amend the cost contract prospectively rather than reclassifying it after outcomes.

Likewise, if an operation thought to be architecture-specific is mechanically forced and identical across all architectures, it remains counted if this contract classifies it as architecture-attributable; v0.1 accounting follows the frozen contract, not retrospective convenience.

## 14. Instrumentation conformance

Before execution authorization, implementation review must demonstrate:

- exact event boundaries `T0..T4`;
- common instrumented SHA-256 primitive;
- common instrumented authority-bearing extraction primitive;
- common instrumented identity-comparison primitive;
- cumulative architecture-evidence write accounting;
- exact dispatched-view byte counting;
- explicit measurement-complete markers;
- separation of architecture, scaffolding, and one-time ledgers;
- no architecture-dependent instrumentation behavior outside the constituted evidence-path treatment.

Instrumentation failure blocks cost comparison. It does not become an architecture cost of zero.

## 15. Scope of repair

This artifact repairs only Gate 5 cost separability.

It does not revise:

```text
oracle cases or hashes
view schemas
chi_0..chi_3 evidence authority
critical/diagnostic partition
D(i,k) scoring
anti-triviality rules
claim ceiling
implementation authorization
execution authorization
```

No architecture has been implemented or executed under assay authority.

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1

status:
FROZEN_COST_CONTRACT
NON_EXECUTED
NON_AUTHORIZING

mandatory primary dimensions:
6

primary comparison horizon:
6 critical cases

diagnostic cases in primary Pareto:
0

scalarization:
FORBIDDEN

next action:
CONSTITUTE SUCCESSOR REFERENCE
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
