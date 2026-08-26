# Minimum Identity Independence Implementation v0.1.2

Version: `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.2`

Status: `IMPLEMENTED / CONFORMANCE_FIXTURES_PUBLISHED / IMPLEMENTATION_REVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

This artifact records the one-way instrumentation successor after `MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0.1.1` failed hostile implementation review because mutable instrumentation state remained locally reachable inside the architecture evaluator.

It does not authorize the constituted 36 architecture-case evaluations.

## Authority

```text
constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4.md
blob: f6d7817153176383b24c283ccc1e421b298fff1a

constitution hostile review
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_4_REVIEW.md
blob: 08436c34754503313219b11fac7dcd5d199634b3

historical implementation review blocker
assays/MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_1_REVIEW.md
blob: 91b834f23e5167673c48ef1a407afcfc04d082cf

successor implementation
tools/minimum_identity_independence_v014_v012.py
commit introducing file: b65c7eaede5495668a568f9ef38c9b58e8a546d5
blob: d7da53b96b6eda28a5a8132a0c910ff548b2fcac

successor conformance fixtures
tests/test_minimum_identity_independence_v014_v012.py
commit introducing file: 9c8f07c487348c31bedb0f27129ed51b10f81c54
blob: fe7442b67c6cef21d3a0e14f9918e73e1fa77353
```

Both committed files were read back after publication.

## Sole intended repair

The architecture no longer owns or receives a mutable measurement object.

Each evaluation launches a fresh isolated Python child whose constituted case-bearing input is supplied only as the exact serialized `V_i` bytes on stdin.

The child emits operation events only outward:

```text
chi_i(V_i)
    -> stderr event stream
    -> parent-side decoder
    -> external cost ledger
```

The emitted vocabulary is frozen to:

```text
SHA256_OPERATION
EXTRACT_OPERATION
IDENTITY_COMPARE_OPERATION
```

The child-side event function returns only `None` and exposes no count, sequence number, timestamp, history, or mutable meter handle.

Architecture terminal bytes are copied/frozen before the parent decodes or merges instrumentation events.

## Process boundary

The child is launched using:

```text
python -I -c <frozen generated architecture source>
```

with:

```text
stdin  = exact V_i bytes
stdout = terminal output only
stderr = one-way operation events only
cwd    = fresh random temporary directory
env    = empty except optional SYSTEMROOT/WINDIR runtime roots
```

No semantic case ID, oracle verdict, case partition, global ordinal, pre-dispatch ledger, event history, or previous-case state is intentionally supplied in argv/env/stdin/cwd.

## Conformance fixtures

A 20-test synthetic conformance suite is published at the frozen path above.

It includes checks for:

```text
schema hashes
referee-side alias resolution
forbidden extra fields
fresh opaque handles
minimal child environment
absence of readable meter/oracle tokens from generated child source
emit(event) -> None
same V_i under different hidden parent environment
same V_i under different hidden pre-dispatch ledgers
fresh-process repeatability
chi_1 unresolved behavior
chi_2 / chi_3 authority split
literal operation-event counts
no informative event return channel
output freeze before event decode/merge
referee join blocked before T3
malformed event rejection
cumulative persistence accounting
literal view-byte / missingness semantics
aggregate + Pareto contract
```

These are engineering conformance fixtures only. They do not constitute assay observations.

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
