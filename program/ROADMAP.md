# White Rabbit Gated Roadmap

Status: `ROADMAP / NON_AUTHORIZING`

This file describes the intended dependency order. It does not grant permission to cross a gate unless an explicit transition below says so.

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

Before corpus population, a separate ingestion constitution must freeze source scope, custody rules, hash/locator requirements, normalization rules, ambiguity handling, and failure behavior.

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

```text
Qwen-generated candidate != research truth
```

## Gate 4 — Recorder implementation

State: `USER_REPORTED COMPLETE / FAKE-UPSTREAM ACCEPTANCE REPORTED PASS`

Contract:

```text
interfaces/WHITE_RABBIT_RECORDER_V0_1.md
```

Milestone:

```text
program/RECORDER_V0_1_MILESTONE.md
```

Reported identity:

```text
version: 0.1.0
local commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
tests: 30/30 PASS
upstream: deterministic fake only
```

The recorder repository is local-only and is not independently inspectable by this GitHub repository. No scientific result follows from Gate 4.

## Gate 5 — Real-server recorder calibration

State: `USER_REPORTED PASS / INSTRUMENTAL ONLY`

Milestone:

```text
program/GATE5_REAL_SERVER_CALIBRATION_MILESTONE.md
```

Reported purpose achieved narrowly:

```text
prove the microscope survives contact with the real llama.cpp/Qwen stack
while preserving the constituted evidence boundary
```

The reported cold run had fresh-process evidence, one unambiguous task/slot measurement block, exact request/response custody, and no treatment/comparison.

This does not establish capability, compute saving, C_improve causality, or White Rabbit effect.

## Gate 6 — Cold baseline characterization

State: `USER_REPORTED PASS / FROZEN FIVE-REPLICATE PROTOCOL`

Milestone:

```text
program/GATE6_COLD_CHARACTERIZATION_MILESTONE.md
```

Earned statement recorded from the supplied report:

> **Cold baseline operationally characterized under the frozen five-replicate protocol.**

Explicit ceiling:

```text
5 replicates characterize the frozen protocol
!=
the underlying stochastic distribution is fully known
```

Reported Gate 6 facts include stable `N_prompt,new = 53` across all five cold replicates and material variation in generated-token count, generation time, total time, and response content.

Methodological consequence:

```text
a future treatment effect must be evaluated against independently constituted baseline variability,
not against one privileged baseline realization
```

No treatment, neutral prelude, benchmark, or capability evaluation was run under Gate 6.

## Gate 7 — Matched-context capability/work assay

State: `CONSTITUTION REPAIRED / AWAITS REVIEW / TOKEN MATCH BLOCKED / EXECUTION NOT AUTHORIZED`

Original constitution and repair authority:

```text
original constitution commit: 7696bf90452cb13f86fe8e22cc860ff6e9d09dee
original constitution version: G7_MATCHED_CONTEXT_ASSAY_V0.1
repair handoff: handoff/CODEX_G7_CONSTITUTION_REPAIR.md
repaired constitution version: G7_MATCHED_CONTEXT_ASSAY_V0.1.1
```

Constitution artifact:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
```

The Gate 7 constitution freezes five components before any execution can even be considered:

```text
1. capability criterion
2. primary work currency
3. independence criterion
4. matched-context control
5. replicate design
```

Frozen assay form, still subject to repaired-constitution review:

```text
B = neutral matched prelude + target
C = literal C_improve prelude + target
```

The literal `C_improve` source must come from:

```text
observations/WR-OBS-002/raw_observation.md
```

The neutral prelude must be frozen separately and reviewed. Source-level similarity does not establish model-visible token equality; the constitution must preserve a pre-open token/context-matching requirement if equality cannot be mechanically established during authoring.

The repaired v0.1.1 contract adds only explicit work-censoring custody and a per-task `S_B,j = 5/5` control-adequacy gate. It preserves mechanically checkable held-out tasks, no LLM judge, primary work currency `N_generated`, independently cold runs, and repeated observations rather than one B/C pair.

Critical boundary:

```text
CONSTITUTED != EXECUTED
```

Creating the Gate 7 constitution does not authorize:

```text
C_improve execution
neutral-prelude execution
B or C runs
llama-server / recorder startup for Gate 7
capability comparison
White Rabbit claim
```

The next possible transition is:

```text
review repaired constitution
-> only then consider separately authorizing pre-open token/context matching
-> STOP
```

Repair completion does not itself authorize token/context matching or execution.

## Gate 8 — White Rabbit compute economics

State: `NOT_AUTHORIZED / NOT OPENED`

The general White Rabbit burden remains:

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

Gate 7 cannot directly emit a Gate 8 / White Rabbit result.

## Gate 9 — Persistence / transfer / revocability

State: `NOT_AUTHORIZED / NOT OPENED`

A positive one-task result would not establish a White Rabbit family.

Later gates would separately ask whether a candidate persists, reuses, amortizes, transfers, and retains an invalidation/revocation path.

Each transition requires its own claim ceiling.

## Current gate position

```text
Gate 4: USER_REPORTED PASS
Gate 5: USER_REPORTED PASS
Gate 6: USER_REPORTED PASS
Gate 7 repaired constitution v0.1.1: FROZEN / AWAITS REVIEW
Gate 7 pre-open token/context matching: BLOCKED
Gate 7 execution: NOT AUTHORIZED / NOT OPENED
White Rabbit G1-G4: NOT OPENED
```

Current authorized transition only:

```text
review repaired Gate 7 constitution
-> only then consider separately authorizing pre-open token/context matching
-> STOP
```

Nothing in this roadmap authorizes treatment execution.
