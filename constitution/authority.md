# White Rabbit Research-State Authority Boundary

Version: `0.1`

Status: `FROZEN_FOUNDING_CONSTITUTION`

## Authorized jurisdiction

This repository may mechanically record source custody, normalize bounded fields without changing their scientific meaning, record explicit derivations, preserve status provenance, represent revision history, and determine whether the resulting provenance graph is structurally complete.

The only successful validator outcome is:

```text
PROVENANCE_VALID
```

This means that required objects and fields exist, schemas hold, references resolve, typed provenance paths are complete, and mechanically checkable history constraints hold.

It does not mean that a source entails a proposition, a claim is scientifically warranted, an experiment is valid, an interpretation is correct, or any proposition is true.

```text
source exists != source entails proposition
```

## Founding invariants

1. `SOURCE`, `NORMALIZED`, and `DERIVED` are distinct epistemic roles.
2. Every normalized object has a mechanically resolvable, field-located path to source evidence.
3. Every derived object has a complete path through one or more normalized parents to source evidence.
4. Status records carry value, scope, effective commit, subject, and source provenance.
5. Stable IDs are unique. Historical change uses distinct objects plus explicit `REVISES`, `SUPERSEDES`, or `INVALIDATES` relations.
6. Missing provenance is reported; it is never inferred, repaired, substituted, or guessed.

## Unauthorized jurisdiction

This constitution does not authorize scientific warrant, source-entailment inference, corpus ingestion, task views, retrieval, ranking, prompting, model calls, embeddings, vector search, graph search, representation learning, adaptive controllers, White Rabbit treatment, compute optimization, or experiment adjudication.

Later layers must receive their own frozen constitutions before they can act. Provenance-valid research state is infrastructure, not the answer.
