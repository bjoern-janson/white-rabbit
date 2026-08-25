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

## Open observations

### WR-OBS-001 — post-`C_improve` reasoning-work anomaly

`WR-OBS-001` is preserved as `OPEN / UNCONTROLLED_OBSERVATION / MECHANISM=UNKNOWN`.

The raw custody record preserves the reported before/after Qwen UI measurements and the exact `C_improve` intervention text. The normalized research state earns only the mechanical observation that the reported `hi` reasoning-token count differed from `371` to `11` while the reported final-generation throughput was approximately unchanged at the displayed precision.

The repository does **not** attribute that change to `C_improve`, session state, runtime state, KV/cache behavior, or any other mechanism. Persistence, transfer, amortization, and a White Rabbit effect remain unestablished.

- [Raw observation custody](observations/WR-OBS-001/raw_observation.md)
- [Normalized provenance state](observations/WR-OBS-001/research_state.json)

Methodological constraint:

> **Preserve anomaly != explain anomaly != optimize anomaly.**

> **Follow the footprint. Don't manufacture a trail.**

No controlled reproduction is opened by preserving this observation.

## Validation

The implementation uses the Python standard library only.

```powershell
python -m unittest discover -s tests -v
python -m validator.validate tests/fixtures/valid_state.json
```

Successful validation returns `PROVENANCE_VALID`. It does not return or imply `TRUE`, `SUPPORTED`, `PROVEN`, or any scientific-warrant judgment.

See [constitution/authority.md](constitution/authority.md) for the frozen jurisdiction boundary.
