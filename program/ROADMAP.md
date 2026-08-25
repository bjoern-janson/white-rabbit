# White Rabbit Gated Roadmap

Status: `ROADMAP / NON_AUTHORIZING`

This file describes the intended dependency order. It does not grant permission to cross a gate.

## Governing dependency

```text
research evidence
    -> S_research
    -> provenance validation
    -> V(q)
    -> model-visible state
    -> Qwen reasoning
    -> measurement apparatus
    -> controlled compute comparison
    -> candidate White Rabbit claim
```

A later stage may not be treated as authorized merely because it appears in this roadmap.

## Gate 0 — Research-state constitution

State: `IMPLEMENTED`

Purpose:

```text
SOURCE != NORMALIZED != DERIVED
```

with provenance-bearing statuses and explicit historical revision relations.

Successful validator outcome:

```text
PROVENANCE_VALID
```

This is structural provenance validity only, not scientific warrant.

## Gate 1 — Evidence population

State: `NOT_AUTHORIZED BY FOUNDING CONSTITUTION`

The founding authority boundary explicitly does not authorize corpus ingestion.

Before corpus population, a separate ingestion constitution must freeze:

```text
source scope
custody rules
hash/locator requirements
normalization rules
ambiguity handling
failure behavior
```

No corpus-wide research state is opened by this roadmap.

## Gate 2 — Deterministic task-view compilation V(q)

State: `NOT_AUTHORIZED`

Future target:

```text
V(q) = smallest source-backed, evidence-complete state required for operation q
```

The compiler must be deterministic and mechanical. It may select source-backed facts; it may not invent scientific answers, repair ambiguous evidence, or silently adjudicate contradictions.

No retrieval/vector/embedding system is authorized here.

## Gate 3 — Qwen integration

State: `NOT_AUTHORIZED`

Future role:

```text
V(q) -> Qwen -> candidate claims
```

Qwen may synthesize and generate candidate structure. Model output does not acquire scientific authority by generation alone.

The required authority firewall is:

```text
Qwen-generated candidate
    !=
research truth
```

## Gate 4 — Recorder implementation

State: `SPECIFIED / NOT_IMPLEMENTED`

Contract:

```text
interfaces/WHITE_RABBIT_RECORDER_V0_1.md
```

The recorder must be implemented as an isolated sibling component and calibrated against a deterministic fake upstream before any real Qwen measurement.

Acceptance ceiling:

```text
IMPLEMENTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE PASS
```

After that acceptance: `STOP`.

## Gate 5 — Real-server recorder calibration

State: `NOT_AUTHORIZED`

Purpose only:

```text
prove the microscope does not bend the light
```

A single ordinary real-server run would verify that the recorder survives contact with llama.cpp while preserving HTTP/backend evidence.

It is not a capability comparison and not a White Rabbit treatment.

## Gate 6 — Cold baseline characterization

State: `NOT_AUTHORIZED`

Before a treatment comparison, a future protocol must constitute backend freshness and measure ordinary run-to-run variability.

A new browser tab is insufficient:

```text
fresh chat != fresh compute
```

No `Cold A`, `Cold B`, or `Cold C` run is authorized by this roadmap.

## Gate 7 — Matched-context capability assay

State: `NOT_AUTHORIZED`

The naive comparison:

```text
A = target alone
C = C_improve + target
```

is not sufficient because `C` contains additional context.

A future meaningful content comparison would require a matched control such as:

```text
B = neutral prelude + target
C = C_improve + target
```

with frozen payload, runtime, backend freshness, compute budget, evaluation, and provenance.

The neutral prelude itself is not designed or authorized here.

## Gate 8 — White Rabbit compute economics

State: `NOT_AUTHORIZED`

Only after a candidate representation `M` has a constituted capability assay can the program test both:

```text
C_realized(M, q) >= C_realized(R0, q)
```

and:

```text
C_acquire(M) + sum_i C_work(M, q_i)
    <
sum_i C_work(R0, q_i)
```

Reusable state acquisition must be charged. Cache reuse and computation elimination must remain distinct.

## Gate 9 — Persistence / transfer / revocability

State: `NOT_AUTHORIZED`

A positive one-task result would not establish a White Rabbit family.

Later gates would separately ask whether the candidate:

```text
persists
reuses
amortizes
transfers
retains an invalidation/revocation path
```

Each transition requires its own claim ceiling.

## Current next engineering target

The next specified build is only:

```text
White Rabbit Recorder v0.1
```

implemented outside this repository, fake-upstream calibrated, then stopped.

Nothing in this roadmap authorizes treatment execution.
