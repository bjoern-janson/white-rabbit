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
    -> discover useful computational coordinates
    -> compile reusable structure M
    -> preserve the relevant result with less required computation
```

The research state is evidence infrastructure, not the answer.

> **Spend computation changing the future computational policy, and recover more computation than was spent doing so.**

> **A White Rabbit exists only when reusable structure makes previously necessary computation unnecessary without sacrificing the capability or distinctions that mattered, and the saved work repays the structure's acquisition cost.**

---

## Canonical White Rabbit definition

Minimum success signature:

```text
same relevant capability, less required computation
```

Current decomposition:

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

General gates:

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

`G1+` is a **Capability Rabbit**. It is upside, not part of the minimum White Rabbit definition.

Rejection filter:

```text
cache hit                         != White Rabbit
one-off trick                     != White Rabbit
answer leakage                    != White Rabbit
better answer only                != White Rabbit
cheaper but epistemically poorer  != White Rabbit
reusable but uneconomic structure != White Rabbit
```

The archetypal transformation is:

```text
change representation
    -> preserve required result
    -> eliminate computation
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

Current-run work is separated from reusable state:

```text
C_run = C_prompt,new + C_generation + C_other
K_reused = previously constituted state reused by this run
C_total = C_cache,acquire + sum_i C_run,i
```

Core instrumentation rules:

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

> **Fresh chat is not fresh compute.**

> **UI-visible token categories must not be assigned computational semantics without backend confirmation.**

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

> **Never interpret LCP similarity without retained-prefix size and its reference population.**

Literal backend fields remain distinct:

```text
f_sim_best != f_keep
```

Arithmetic reconstruction from slot/prompt/output counters is `DERIVED`; it is not promoted into a backend-reported cached-token meter.

See:

- [measurement/MEASUREMENT_MODEL.md](measurement/MEASUREMENT_MODEL.md)
- [constitution/instrumentation_invariants.md](constitution/instrumentation_invariants.md)

---

## What this repository is

This repository is the White Rabbit **research/control plane**.

It contains:

```text
frozen research-state constitution
mechanical provenance validator
measurement/accounting invariants
preserved uncontrolled observations
program definition + state ledger + gated roadmap
recorder interface contract
closed Codex implementation handoff
reported recorder engineering milestone
```

It does **not** contain:

```text
White Rabbit treatment
adaptive policy
representation learner
capability benchmark
Qwen treatment runner
retrieval/vector system
scientific claim adjudicator
```

The runnable recorder is a separate local sibling component, not runtime code in this repository.

## Founding authority boundary

The constituted research-state path remains deliberately narrow:

```text
research evidence
    -> typed research state
    -> PROVENANCE_VALID
```

Founding invariants:

```text
SOURCE != NORMALIZED != DERIVED
status is provenance-bearing
historical objects are never silently overwritten
missing provenance is never guessed
validator jurisdiction = provenance validity, not scientific warrant
```

> **No object enters normalized state without a mechanically inspectable provenance path to source evidence.**

> **The validator establishes provenance validity, not scientific warrant.**

The founding constitution does not authorize corpus ingestion, task-view compilation, retrieval, model calls, representation learning, adaptive control, scientific adjudication, or compute experiments.

See [constitution/authority.md](constitution/authority.md).

---

## Current observations

### WR-OBS-001 — UI anomaly corrected by backend evidence

The original UI observation is preserved, but the interpretation of `371 -> 11` as generated reasoning-token disappearance is superseded.

Current boundary:

```text
371 and 11 = freshly processed prompt-evaluation counts
prefix/LCP reuse = OBSERVED
generated tokens = 44 -> 88
reasoning-work reduction = NOT_DEMONSTRATED
C_improve causality = UNESTABLISHED
White Rabbit effect = NOT_DEMONSTRATED
```

- [Original UI custody](observations/WR-OBS-001/raw_observation.md)
- [Original research state v1](observations/WR-OBS-001/research_state.json)
- [Backend correction](observations/WR-OBS-001/backend_correction.md)
- [Superseding research state v2](observations/WR-OBS-001/research_state_v2.json)

### WR-OBS-002 — fresh browser windows, persistent backend confound

Three reported fresh browser windows received the same `C_improve` prompt.

```text
fresh prompt-eval tokens: 65 / 65 / 65
generated tokens:         1246 / 995 / 1038
generation rate:          ~13.98 / 14.14 / 13.83 tokens/s
```

Current boundary:

```text
fresh browser windows: OBSERVED
backend-state independence: NOT_ESTABLISHED
C_improve causality: UNESTABLISHED
persistent policy change: UNESTABLISHED
capability improvement: NOT_DEMONSTRATED
White Rabbit effect: NOT_DEMONSTRATED
```

- [Raw observation custody](observations/WR-OBS-002/raw_observation.md)
- [Normalized provenance state](observations/WR-OBS-002/research_state.json)

Methodological constraint:

> **Preserve anomaly != explain anomaly != optimize anomaly.**

> **Follow the footprint. Don't manufacture a trail.**

---

## Task-specific Qwen analytical behavior

The local Qwen setup has demonstrated substantive analysis over the White Rabbit representation.

Current narrow evidence ledger:

```text
White Rabbit representation ingested: OBSERVED
task-specific structured analysis: OBSERVED
authority distinctions preserved in observed task: OBSERVED
deep continuation under inherited state: OBSERVED
general research competence: NOT_ESTABLISHED
C_improve causal role: UNESTABLISHED
independent replication: UNESTABLISHED
compute advantage: UNESTABLISHED
```

This is capability evidence at a task-specific level, not independence or White Rabbit evidence.

The sharper future question remains:

> **Can reusable structure change the computational representation of a task so that the same useful result requires less work?**

---

## White Rabbit Recorder v0.1.0

The recorder specification was implemented by Codex in an isolated local repository according to a user-supplied completion report.

Reported identity:

```text
version: 0.1.0
local implementation commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
files added: 27
dependencies: none / Python standard library only
working tree: clean
remote: none
```

Reported acceptance:

```text
python -m unittest discover -s tests -v
PASS — 30/30
deterministic fake upstream only
```

Reported properties include:

```text
all-route transparent proxying
byte-faithful request custody
raw response-body custody
streaming preservation
server invocation/build/PID/session custody
literal prompt/generated/timing extraction
literal f_sim_best / f_keep / graphs_reused preservation
no guessed cached-token count
explicit ambiguous-correlation failure
concurrent measured requests rejected with HTTP 409
```

Reported forbidden-scope state:

```text
C_improve treatment: NOT ADDED / NOT RUN
neutral prelude: NOT ADDED
capability evaluator: NOT ADDED
White Rabbit policy: NOT ADDED
real Qwen request through recorder: NOT RUN
scientific comparison: NOT RUN
```

Important limitation:

```text
exact HTTP body custody != exact post-Jinja model-visible token sequence
```

The recorder implementation is local-only, so this GitHub repository cannot independently inspect commit `80cddb26...` or rerun its reported tests. The current claim ceiling is therefore:

```text
LOCAL IMPLEMENTATION REPORTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE REPORTED PASS
+
SCIENTIFIC RESULT: NONE
```

See:

- [Recorder interface](interfaces/WHITE_RABBIT_RECORDER_V0_1.md)
- [Recorder engineering milestone](program/RECORDER_V0_1_MILESTONE.md)
- [Closed Codex handoff](handoff/CODEX_RECORDER_BUILD.md)

---

## Current gate position

The gated sequence remains:

```text
research evidence
-> S_research
-> provenance validation
-> V(q)
-> model-visible state
-> Qwen candidate synthesis
-> recorder / execution custody
-> controlled capability comparison
-> compute economics
-> persistence / transfer / revocability
```

A stage appearing in the roadmap does not authorize it.

Current position:

```text
Gate 4 — recorder implementation / fake-upstream acceptance:
    USER-REPORTED COMPLETE

Gate 5 — real-server recorder calibration:
    NOT_AUTHORIZED
```

The recorder's mandated stop boundary has been reached according to the supplied completion report.

There is currently **no authorized real-Qwen or treatment transition**.

See:

- [program/STATE.md](program/STATE.md)
- [program/ROADMAP.md](program/ROADMAP.md)

---

## Repository map

```text
constitution/   frozen authority boundary + active instrumentation invariants
corpus/         container only; ingestion not authorized
schema/         typed research-state schemas
validator/      deterministic provenance validator
tests/          validator tests/fixtures
observations/   preserved empirical/uncontrolled observation lineage
program/        definition, state ledger, roadmap, engineering milestones
measurement/    raw/derived/interpretation + compute/accounting vocabulary
interfaces/     component contracts
handoff/        closed/active implementation handoffs
```

## Validation

The research-state validator uses the Python standard library only.

```powershell
python -m unittest discover -s tests -v
python -m validator.validate tests/fixtures/valid_state.json
```

Successful validation returns:

```text
PROVENANCE_VALID
```

It does not return or imply:

```text
TRUE
SUPPORTED
PROVEN
SCIENTIFICALLY_VALID
WARRANT_SUFFICIENT
```

---

## Governing rules

> **Raw measurement first, derived reconstruction second, interpretation last.**

> **Qwen can generate candidate structure; generation does not grant the candidate research authority.**

> **Make research state mechanically trustworthy before making it computationally useful.**

> **Capability preserved. Independence demonstrated. Work actually removed. Acquisition repaid.**

> **Build the microscope before chasing the rabbit.**
