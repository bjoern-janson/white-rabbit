# White Rabbit

**White Rabbit is a search for reusable computational structure. The research state is evidence infrastructure, not the answer.**

This repository begins with a deliberately narrow substrate: typed research records, explicit provenance, immutable-history relations, and a deterministic mechanical validator.

> **No object enters normalized state without a mechanically inspectable provenance path to source evidence.**

> **The validator establishes provenance validity, not scientific warrant.**

> **No optimization, retrieval strategy, model behavior, or White Rabbit treatment is authorized by this repository constitution alone.**

## Current authorized path

```text
research evidence
    -> typed research state
    -> PROVENANCE_VALID
```

The wider program sequence is:

```text
research evidence
    -> S_research
    -> V(q)
    -> Qwen
    -> future compute experiment
```

Everything after validated research state is future scope. This constitution does not authorize task-view compilation, retrieval, prompting, model integration, scientific adjudication, representation learning, adaptive policy, or compute experiments.

## Research-state roles

Every research object declares one epistemic role:

- `SOURCE`: immutable or commit-bound source evidence.
- `NORMALIZED`: a bounded representation with explicit field-level source locators.
- `DERIVED`: a mechanically recorded derivative with complete normalized parents.

These roles are not interchangeable. Deterministic transformation does not promote a derived record into evidence.

## Instrumentation invariants

White Rabbit now carries explicit measurement constraints learned from the first backend correction. These constraints do not open an experiment.

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

> **Fresh chat is not fresh compute.**

> **UI-visible token categories must not be assigned computational semantics without backend confirmation.**

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

See [constitution/instrumentation_invariants.md](constitution/instrumentation_invariants.md).

## Open observations

### WR-OBS-001 — UI anomaly with backend measurement correction

`WR-OBS-001` remains `OPEN / UNCONTROLLED_OBSERVATION / WHITE_RABBIT_EFFECT=NOT_DEMONSTRATED`.

The original UI custody is preserved unchanged. A later llama.cpp server trace supersedes the earlier interpretation of `371 -> 11` as generated reasoning-token disappearance.

The backend correction establishes the narrower accounting:

```text
371 and 11 = freshly processed prompt-evaluation token counts
full `hi` prompt/context ~= 370 tokens in both runs
later request explicitly used LCP/prefix reuse
generated tokens = 44 -> 88
reasoning-work reduction = NOT_DEMONSTRATED
C_improve causality = UNESTABLISHED
White Rabbit effect = NOT_DEMONSTRATED
```

The v1 research-state object is preserved historically. The v2 state adds a provenance-bearing `SUPERSEDES` relation rather than silently rewriting the old interpretation.

- [Original raw UI custody](observations/WR-OBS-001/raw_observation.md)
- [Original normalized state v1](observations/WR-OBS-001/research_state.json)
- [Backend measurement correction](observations/WR-OBS-001/backend_correction.md)
- [Superseding provenance state v2](observations/WR-OBS-001/research_state_v2.json)

Methodological constraint:

> **Preserve anomaly != explain anomaly != optimize anomaly.**

> **Follow the footprint. Don't manufacture a trail.**

No controlled reproduction is opened by preserving or correcting this observation.

## Validation

The implementation uses the Python standard library only.

```powershell
python -m unittest discover -s tests -v
python -m validator.validate tests/fixtures/valid_state.json
```

Successful validation returns `PROVENANCE_VALID`. It does not return or imply `TRUE`, `SUPPORTED`, `PROVEN`, or any scientific-warrant judgment.

See [constitution/authority.md](constitution/authority.md) for the frozen jurisdiction boundary.
