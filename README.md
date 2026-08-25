# White Rabbit 🐇

**White Rabbit is the search for reusable computational structure that changes the economics of reasoning.**

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
    -> eliminate previously required future computation
```

The research state is evidence infrastructure, not the answer.

> **Spend computation changing the future computational policy, and recover more computation than was spent doing so.**

> **A White Rabbit exists only when previously required computation demonstrably disappears under a valid accounting boundary.**

## Current program decomposition

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

- `C_latent`: capability available in a fixed model/substrate; not directly observed here.
- `C_realized(R, q)`: capability actually elicited under representation/context `R` for task `q`.
- `C_work(R, q)`: computation expended to produce that behavior.

A future candidate `M` must eventually earn both:

```text
C_realized(M, q) >= C_realized(R0, q)
```

and, over a constituted reuse horizon:

```text
C_acquire(M) + sum_i C_work(M, q_i)
    <
sum_i C_work(R0, q_i)
```

These are program targets, **not established results and not currently authorized experiments**.

See [program/WHITE_RABBIT.md](program/WHITE_RABBIT.md).

---

## What this repository currently is

This repository is the White Rabbit **research/control plane**.

It currently contains:

```text
frozen research-state constitution
mechanical provenance validator
measurement/accounting invariants
preserved uncontrolled observations
program definitions and gated roadmap
non-runnable recorder interface contract
```

It does **not** currently contain:

```text
White Rabbit treatment
adaptive policy
representation learner
capability benchmark
Qwen treatment runner
retrieval/vector system
scientific claim adjudicator
```

The intended runnable recorder is a future isolated sibling component, not runtime code in this repository.

## Founding authority boundary

The currently constituted path is deliberately narrow:

```text
research evidence
    -> typed research state
    -> PROVENANCE_VALID
```

The founding invariants are:

```text
SOURCE != NORMALIZED != DERIVED
status is provenance-bearing
historical objects are never silently overwritten
missing provenance is never guessed
validator jurisdiction = provenance validity, not scientific warrant
```

> **No object enters normalized state without a mechanically inspectable provenance path to source evidence.**

> **The validator establishes provenance validity, not scientific warrant.**

The founding constitution explicitly does not authorize corpus ingestion, task-view compilation, retrieval, model calls, representation learning, adaptive control, scientific adjudication, or compute experiments.

See [constitution/authority.md](constitution/authority.md).

---

## Measurement model

Current-run work is separated from reusable state:

```text
C_run = C_prompt,new + C_generation + C_other
```

```text
K_reused = previously constituted state reused by this run
```

Across a reuse horizon:

```text
C_total = C_cache,acquire + sum_i C_run,i
```

The governing measurement rules are:

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

> **Fresh chat is not fresh compute.**

> **UI-visible token categories must not be assigned computational semantics without backend confirmation.**

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

See:

- [measurement/MEASUREMENT_MODEL.md](measurement/MEASUREMENT_MODEL.md)
- [constitution/instrumentation_invariants.md](constitution/instrumentation_invariants.md)

---

## Current observations

### WR-OBS-001 — UI anomaly corrected by backend evidence

The original UI observation is preserved, but the interpretation of `371 -> 11` as generated reasoning-token disappearance is superseded.

The backend trace establishes the narrower classification:

```text
371 and 11 = freshly processed prompt-evaluation token counts
full `hi` pre-generation/context length ~= 370 tokens in both runs
later request explicitly used LCP/prefix reuse
generated tokens = 44 -> 88
reasoning-work reduction = NOT_DEMONSTRATED
C_improve causality = UNESTABLISHED
White Rabbit effect = NOT_DEMONSTRATED
```

The historical v1 state remains intact; v2 records an explicit supersession rather than rewriting history.

- [Original UI custody](observations/WR-OBS-001/raw_observation.md)
- [Original research state v1](observations/WR-OBS-001/research_state.json)
- [Backend correction](observations/WR-OBS-001/backend_correction.md)
- [Superseding research state v2](observations/WR-OBS-001/research_state_v2.json)

### WR-OBS-002 — three fresh browser windows, persistent backend confound

Three separately reported fresh browser chat windows received the same `C_improve` prompt.

Backend/UI measurements preserve:

```text
fresh prompt-eval tokens: 65 / 65 / 65
generated tokens:         1246 / 995 / 1038
generation rate:          ~13.98 / 14.14 / 13.83 tokens/s
```

The stop-count arithmetic is consistent with the same approximate 424-token pre-generation/context length and approximately 359 tokens not requiring fresh prompt evaluation in each run.

That arithmetic is not promoted into a primary cached-token meter.

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

## Open capability question

The local Qwen setup has displayed substantially richer analytical behavior than the first trivial setup interactions revealed.

Why remains unresolved.

Current competing explanations include:

```text
H1: initial backend slowdown obscured capability
H2: later tasks simply elicited capabilities early prompts never tested
H3: C_improve provided a useful in-context computational scaffold
H4: some combination of H1-H3
```

The cache/prefill explanation for the speed anomaly does **not** by itself adjudicate the semantic capability question.

The sharper future hypothesis is:

> **Can a compact reusable meta-representation cause a fixed model to activate more of its existing reasoning capability while reducing wasted computation required to do so?**

This remains an open hypothesis.

---

## Next specified engineering target

The next build target is **White Rabbit Recorder v0.1**: a transparent, byte-faithful inference recorder that establishes raw HTTP custody plus backend execution custody.

Topology:

```text
browser
   -> recorder :8085
   -> llama-server :8086
```

The recorder contract requires:

```text
exact HTTP request-body custody
exact response-body custody
server invocation/build/PID/session custody
literal llama.cpp timing/token/LCP extraction
no guessed defaults
no guessed cached-token count
explicit ambiguous-correlation failure
```

Its first acceptance must use a deterministic fake upstream only.

Claim ceiling:

```text
IMPLEMENTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE PASS
```

Then:

```text
STOP
```

No real Qwen treatment is opened by the recorder specification.

See [interfaces/WHITE_RABBIT_RECORDER_V0_1.md](interfaces/WHITE_RABBIT_RECORDER_V0_1.md).

---

## Gated path

The intended dependency order is:

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

Current next transition:

```text
recorder implementation in isolated sibling
-> fake-upstream acceptance
-> STOP
```

See:

- [program/STATE.md](program/STATE.md)
- [program/ROADMAP.md](program/ROADMAP.md)

---

## Repository map

```text
constitution/   frozen authority boundary + measurement invariants
corpus/         container only; ingestion not authorized
schema/         typed research-state schemas
validator/      deterministic provenance validator
tests/          validator tests/fixtures
observations/   preserved empirical/uncontrolled observation lineage
program/        program definition, state ledger, gated roadmap
measurement/    compute/accounting vocabulary
interfaces/     non-runnable future-component contracts
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

> **Measure what ran before interpreting what it means.**

> **Qwen can generate candidate structure; generation does not grant the candidate research authority.**

> **Make research state mechanically trustworthy before making it computationally useful.**

> **Build the microscope before chasing the rabbit.**
