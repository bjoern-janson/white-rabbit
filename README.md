# White Rabbit 🐇

**White Rabbit is the search for reusable computational structure that makes adequate intelligence cheaper.**

The archetype is Fast Inverse Square Root:

```text
expensive general operation
    -> discover representation-dependent structure
    -> compile reusable rule
    -> cheap repeated execution
```

White Rabbit asks whether an analogous move exists for reasoning:

```text
expensive reasoning/search
    -> discover useful computational structure M
    -> preserve the relevant result
    -> require less future computation
```

> **A White Rabbit exists only when reusable structure makes previously necessary computation unnecessary without sacrificing the capability or distinctions that mattered, and the saved work repays the structure's acquisition cost.**

---

## Canonical definition

Minimum success signature:

```text
same relevant capability, less required computation
```

Current decomposition:

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

General White Rabbit gates:

```text
G1: C_realized(M, q) >= C_realized(R0, q)
G2: independent reproduction
G3: C_work(M, q) < C_work(R0, q)
G4: acquisition cost is repaid over the constituted reuse horizon
```

Optional stronger result:

```text
G1+: C_realized(M, q) > C_realized(R0, q)
```

`G1+` is capability-unlocking upside, not part of the minimum definition.

Rejection filter:

```text
cache hit                         != White Rabbit
one-off trick                     != White Rabbit
answer leakage                    != White Rabbit
better answer only                != White Rabbit
cheaper but epistemically poorer  != White Rabbit
reusable but uneconomic structure != White Rabbit
```

See [program/WHITE_RABBIT.md](program/WHITE_RABBIT.md).

---

## Measurement doctrine

The evidence order is frozen as:

```text
RAW MEASUREMENT
    -> DERIVED RECONSTRUCTION
    -> INTERPRETATION
```

No silent promotion is allowed between layers.

Core constraints:

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

> **Fresh chat is not fresh compute.**

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

> **Never interpret LCP similarity without retained-prefix size and its reference population.**

Literal backend fields remain distinct:

```text
f_sim_best != f_keep
```

Arithmetic reconstruction is `DERIVED`; it is not promoted into a backend-reported cached-token meter.

Gate 6 adds another active constraint:

> **Treatment effects must be evaluated against independently constituted baseline variability, not against one privileged baseline run.**

See:

- [measurement/MEASUREMENT_MODEL.md](measurement/MEASUREMENT_MODEL.md)
- [constitution/instrumentation_invariants.md](constitution/instrumentation_invariants.md)

---

## Research/control-plane boundary

This repository is the White Rabbit **research/control plane**.

It contains:

```text
frozen research-state constitution
mechanical provenance validator
measurement/accounting invariants
preserved uncontrolled observations
program definition + state ledger + gated roadmap
recorder interface contract + reported engineering milestones
Gate 7 constitution-authoring handoff
```

It does **not** contain or authorize by default:

```text
White Rabbit treatment
adaptive policy
representation learner
open-ended capability judge
Qwen treatment runner
retrieval/vector system
scientific claim adjudicator
```

The founding research-state path remains:

```text
research evidence
    -> typed research state
    -> PROVENANCE_VALID
```

with:

```text
SOURCE != NORMALIZED != DERIVED
provenance validity != scientific warrant
```

See [constitution/authority.md](constitution/authority.md).

---

## Observation boundary

### WR-OBS-001

```text
371 -> 11 reasoning interpretation: SUPERSEDED
371 / 11: prompt-evaluation counts
prefix/LCP reuse: OBSERVED
reasoning-work reduction: NOT_DEMONSTRATED
C_improve causality: UNESTABLISHED
White Rabbit effect: NOT_DEMONSTRATED
```

### WR-OBS-002

```text
three fresh browser windows: OBSERVED
backend-state independence: NOT_ESTABLISHED
C_improve causality: UNESTABLISHED
persistent policy change: UNESTABLISHED
capability improvement: NOT_DEMONSTRATED
White Rabbit effect: NOT_DEMONSTRATED
```

The literal `C_improve` intervention text is preserved in:

- [observations/WR-OBS-002/raw_observation.md](observations/WR-OBS-002/raw_observation.md)

### Task-specific Qwen analytical behavior

Current narrow evidence:

```text
White Rabbit representation ingested: OBSERVED
task-specific structured analysis: OBSERVED
authority distinctions preserved: OBSERVED
deep continuation under inherited state: OBSERVED
general research competence: NOT_ESTABLISHED
C_improve causal role: UNESTABLISHED
independent replication: UNESTABLISHED
compute advantage: UNESTABLISHED
```

---

## Recorder and calibration ladder

### Gate 4 — recorder implementation / fake-upstream acceptance

State:

```text
USER_REPORTED PASS
```

Reported recorder identity:

```text
White Rabbit Recorder v0.1.0
local implementation commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
fake-upstream tests: 30/30 PASS
real Qwen during implementation acceptance: NO
scientific comparison: NO
```

The recorder repository is local-only; this GitHub repository does not independently verify that implementation commit or test run.

See [program/RECORDER_V0_1_MILESTONE.md](program/RECORDER_V0_1_MILESTONE.md).

### Gate 5 — real-server recorder calibration

State:

```text
USER_REPORTED PASS / INSTRUMENTAL ONLY
```

The supplied report records a strongly evidenced cold real-server run with exact request/response custody and unambiguous task/slot correlation.

No treatment or capability comparison followed.

See [program/GATE5_REAL_SERVER_CALIBRATION_MILESTONE.md](program/GATE5_REAL_SERVER_CALIBRATION_MILESTONE.md).

### Gate 6 — five-replicate cold characterization

State:

```text
USER_REPORTED PASS / FROZEN FIVE-REPLICATE PROTOCOL
```

Earned statement recorded from the supplied report:

> **Cold baseline operationally characterized under the frozen five-replicate protocol.**

Ceiling:

```text
5 replicates characterize the frozen protocol
!=
the underlying stochastic distribution is fully known
```

Reported mechanical envelope:

```text
N_prompt,new: 53 in all 5 runs
N_generated: 3-43
T_generation: 1281.79-13686.74 ms
T_total: 15345.59-27483.44 ms
responses: 5 distinct raw hashes / 4 distinct visible contents
```

No `f_sim_best`, `f_keep`, or explicit cached-token field was exposed. `graphs_reused` remains literal only.

See [program/GATE6_COLD_CHARACTERIZATION_MILESTONE.md](program/GATE6_COLD_CHARACTERIZATION_MILESTONE.md).

---

## Gate 7 — matched-context assay constitution

Current state:

```text
constitution authoring: AUTHORIZED
constitution artifact: NOT YET CONSTITUTED / NOT YET REVIEWED
assay execution: NOT AUTHORIZED / NOT OPENED
White Rabbit G1-G4: NOT OPENED
```

The authorized Codex task is specification authoring only:

- [handoff/CODEX_G7_CONSTITUTION.md](handoff/CODEX_G7_CONSTITUTION.md)

Target artifact:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
```

The constitution must freeze:

```text
1. capability criterion
2. work currency
3. independence criterion
4. matched-context control
5. replicate design
```

Intended assay form, subject to constitution review:

```text
B = neutral matched prelude + target
C = literal C_improve prelude + target
```

First-assay design constraints include:

```text
mechanically checkable held-out tasks
no LLM judge
primary assay-local work currency = N_generated
new cold backend for every observation
n = 5 per condition per task
full per-run preservation
capability non-regression before work-reduction interpretation
```

The neutral prelude's neutrality is a design assumption requiring review. Source-level matching does not establish post-template token equality; if equality is not established during constitution authoring, the spec must preserve:

```text
PREOPEN_TOKEN_MATCH_REQUIRED
```

Critical boundary:

```text
CONSTITUTED != EXECUTED
```

Creating the assay constitution does **not** authorize `C_improve`, the neutral prelude, B/C runs, recorder/server startup for Gate 7, capability comparison, Gate 8, or a White Rabbit claim.

After Codex authors the constitution:

```text
STOP
```

The constitution must survive review before any separate execution authorization is considered.

---

## Current gate ledger

```text
Gate 4 — fake-upstream recorder acceptance: USER_REPORTED PASS
Gate 5 — real-server recorder calibration: USER_REPORTED PASS
Gate 6 — five-replicate cold characterization: USER_REPORTED PASS
Gate 7 — constitution authoring: AUTHORIZED
Gate 7 — constitution: NOT YET REVIEWED / NOT YET FROZEN
Gate 7 — execution: NOT AUTHORIZED / NOT OPENED
White Rabbit G1-G4: NOT OPENED
```

Current authorized transition only:

```text
G6 PASS
-> author G7_MATCHED_CONTEXT_ASSAY_V0.1
-> review constitution
-> STOP
```

See:

- [program/STATE.md](program/STATE.md)
- [program/ROADMAP.md](program/ROADMAP.md)

---

## Repository map

```text
constitution/   authority boundary + active instrumentation invariants
corpus/         container only; ingestion not authorized
schema/         typed research-state schemas
validator/      deterministic provenance validator
tests/          validator tests/fixtures
observations/   preserved uncontrolled observation lineage
program/        definition, state, roadmap, engineering/calibration milestones
measurement/    raw/derived/interpretation + compute/accounting vocabulary
interfaces/     component contracts
handoff/        active bounded Codex handoffs
assays/         future frozen assay constitutions; not created until authorized authoring completes
```

## Governing rules

> **Raw measurement first, derived reconstruction second, interpretation last.**

> **Constitute the counterfactual before observing the treatment.**

> **Capability preserved. Independence demonstrated. Work actually removed. Acquisition repaid.**

> **Build the microscope before chasing the rabbit.**
