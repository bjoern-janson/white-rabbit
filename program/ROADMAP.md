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

State: `USER_REPORTED COMPLETE / FAKE-UPSTREAM ACCEPTANCE REPORTED PASS / STOP REACHED`

Contract:

```text
interfaces/WHITE_RABBIT_RECORDER_V0_1.md
```

Milestone record:

```text
program/RECORDER_V0_1_MILESTONE.md
```

The supplied Codex completion report records:

```text
version: 0.1.0
local commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
tests: 30/30 PASS
upstream: deterministic fake only
real Qwen request: NO
scientific comparison: NO
```

The implementation is local-only and cannot be independently inspected or rerun by this GitHub repository. Therefore the current claim ceiling is:

```text
LOCAL IMPLEMENTATION REPORTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE REPORTED PASS
```

No scientific result follows.

Original gate stop condition:

```text
fake-upstream acceptance
-> STOP
```

is active and has been reached according to the supplied report.

## Gate 5 — Real-server recorder calibration

State: `NOT_AUTHORIZED`

Purpose only:

```text
prove the microscope does not bend the light
```

A single ordinary real-server run would verify that the recorder survives contact with llama.cpp while preserving HTTP/backend evidence.

It is not a capability comparison and not a White Rabbit treatment.

No such run is authorized or recorded here.

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

The general White Rabbit burden is:

```text
G1: C_realized(M, q) >= C_realized(R0, q)
G2: independent reproduction
G3: C_work(M, q) < C_work(R0, q)
G4: acquisition cost repaid over reuse
```

with optional stronger result:

```text
G1+: C_realized(M, q) > C_realized(R0, q)
```

The horizon accounting is:

```text
C_acquire(M) + sum_i C_work(M, q_i)
    <
sum_i C_work(R0, q_i)
```

Reusable-state acquisition must be charged. Cache reuse and computation elimination must remain distinct.

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

## Current gate position

```text
Gate 4: REPORTED COMPLETE
Gate 5: NOT_AUTHORIZED
```

There is no currently authorized real-server or treatment transition.

The next unopened gate is only:

```text
Gate 5 — real-server recorder calibration
```

Nothing in this roadmap authorizes that gate merely by naming it.
