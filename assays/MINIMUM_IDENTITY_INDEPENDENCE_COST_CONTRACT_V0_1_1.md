# Minimum Identity Independence Cost Contract v0.1.1

Version: `MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1.1`

Status: `FROZEN_COST_CONTRACT / NON_EXECUTED / NON_AUTHORIZING`

This is the minimal successor to `MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1` after hostile review found one internal ambiguity in the mandatory primary persistence dimension.

It changes only the authoritative definition of `C_persist_bytes`. Every other cost dimension, horizon, attribution class, missingness rule, dominance rule, Pareto rule, instrumentation requirement, and non-authority statement from v0.1 remains binding.

## 1. Immutable upstream authority

```text
historical cost contract
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f

blocking hostile review
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_3_REVIEW.md
blob: 89ff00000d8426d3bd0f544f59bb062ab8f04a83
```

The historical v0.1 cost contract remains immutable record.

## 2. Sole repair

For every architecture-case evaluation, the authoritative primary persistence metric is exactly:

```text
C_persist_bytes = cumulative architecture-attributable evidence bytes newly written
```

Unit: bytes.

The value is the monotonically accumulated sum of bytes written during the architecture-attributable interval `[T1,T3]` to architecture-specific evidence persistence because the selected `chi_i` evidence path requires that persistence.

A write of `n` bytes increments the counter by exactly `n`, regardless of whether those bytes are later:

```text
overwritten
deleted
truncated
replaced
compacted
```

Repeated writes count repeatedly.

No terminal retained-size measurement may substitute for this cumulative counter.

## 3. Included writes

Included in `C_persist_bytes`:

- raw custody bytes persisted because the selected architecture evidence path requires them;
- architecture-specific evidence metadata persisted because the selected architecture evidence path requires it;
- architecture-specific stored identity hashes persisted because the selected architecture evidence path requires them;
- any replacement/rewrite of those architecture-attributable evidence artifacts during `[T1,T3]`.

## 4. Excluded writes

Excluded from `C_persist_bytes`:

- cost-ledger files and instrumentation state;
- common runner logs;
- oracle/referee artifacts;
- architecture-output custody used only by the common referee;
- immutable fixtures and frozen constitution/schema files;
- shared projection/dispatch attestations classified as common scaffolding;
- one-time oracle/fixture construction.

The attribution classes frozen in v0.1 remain controlling.

## 5. Measurement source

The sole primary measurement source is a common instrumented cumulative-write primitive used by all architecture-specific evidence persistence.

For each evaluation, the ledger must record:

```text
architecture_evidence_bytes_written: non-negative integer | null
measurement_complete: true | false
```

A value of zero is valid only when:

```text
measurement_complete = true
architecture_evidence_bytes_written = 0
```

Any architecture-attributable evidence write that bypasses the common instrumented persistence primitive makes that evaluation's `C_persist_bytes` incomplete and therefore triggers the inherited `COST_VECTOR_INCOMPLETE` rule.

## 6. Terminal retained footprint is diagnostic only

If desired, the implementation may additionally record:

```text
persist_retained_bytes_terminal
```

Definition:

```text
sum of final file sizes of architecture-attributable evidence artifacts retained at T3
```

This is a diagnostic field only.

It must not enter:

```text
C_primary(chi_i)
componentwise dominance
Pareto membership
unique-minimum selection
```

Missing diagnostic retained-size data does not make the primary vector incomplete.

## 7. Primary vector identity

The mandatory primary vector remains exactly:

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

where `C_persist_bytes` has only the cumulative-write definition in this successor.

Thus, for every valid execution history `e`, the persistence component has one deterministic interpretation.

## 8. Explicit non-repairs

This successor does not modify:

```text
C_view_bytes
C_capture_bytes
C_sha256_ops
C_extract_ops
C_identity_compare_ops
primary six-case horizon
architecture/shared/one-time attribution classes
T0..T4 boundaries
missingness/completeness rules
timing/CPU diagnostic status
dominance/Pareto/unique-minimum rules
scalarization prohibition
oracle
view boundary
architecture ladder
scoring
claim ceiling
implementation authorization
execution authorization
```

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0.1.1

status:
FROZEN_COST_CONTRACT
NON_EXECUTED
NON_AUTHORIZING

repair scope:
C_PERSIST_BYTES DEFINITION ONLY

authoritative persistence metric:
CUMULATIVE ARCHITECTURE-ATTRIBUTABLE BYTES NEWLY WRITTEN

terminal retained bytes:
DIAGNOSTIC ONLY

next action:
CONSTITUTE SUCCESSOR REFERENCE
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
