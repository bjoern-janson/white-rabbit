# White Rabbit Program Definition

Status: `PROGRAM_DEFINITION / NON_AUTHORIZING`

White Rabbit is the search for small, reusable computational structure that changes the economics of reasoning.

The archetype is Fast Inverse Square Root:

```text
expensive general operation
    -> discover representation-dependent structure
    -> compile reusable rule
    -> cheap repeated execution
```

The White Rabbit analogue is:

```text
expensive reasoning/search
    -> discover useful computational coordinates or invariant
    -> compile reusable structure M
    -> reduce future required computation
```

The program does not assume that `M` is a prompt, formula, representation, decomposition, compiler, lookup structure, canonicalization rule, or learned object. Those are candidate forms, not definitions.

## North star

> **Spend computation changing the future computational policy, and recover more computation than was spent doing so.**

A complementary formulation is:

> **A better rule for what intelligence bothers computing at all.**

A White Rabbit exists only when previously required computation demonstrably disappears under a valid accounting boundary.

Prettier reasoning, more tokens, hidden preprocessing, uncharged caches, answer leakage, or a one-instance trick do not satisfy that criterion.

## Capability/work decomposition

The current conceptual decomposition is:

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

where:

- `C_latent` denotes capability available in the fixed model/substrate. It is not directly observed by the current repository.
- `C_realized(R, q)` denotes capability actually elicited for question/task `q` under representation or computational context `R`.
- `C_work(R, q)` denotes computation expended to produce the realized behavior.

This decomposition prevents three different phenomena from being collapsed into one claim:

```text
model has capability
model deploys capability
model spends less computation
```

## Candidate White Rabbit condition

For a reusable candidate structure `M`, a future scientific treatment would need to earn both sides:

```text
C_realized(M, q) >= C_realized(R0, q)
```

and, over a constituted reuse horizon:

```text
C_acquire(M) + sum_i C_work(M, q_i)
    <
sum_i C_work(R0, q_i)
```

These inequalities are program targets, not established results and not presently authorized experiments.

## Corrigibility requirement

Cheap execution is insufficient if the compiled structure cannot be invalidated when evidence changes.

The lifecycle target is:

```text
discover
-> validate
-> compile
-> reuse
-> monitor validity
-> reopen / revoke / replace
```

The program therefore seeks both computational leverage and reachable correction.

## Authority boundary

Qwen or any other model may generate candidate structure.

```text
candidate structure generated
    !=
candidate structure warranted
```

Likewise:

```text
provenance valid
    !=
scientifically warranted
```

The research-state constitution controls provenance only. Any future scientific adjudication layer requires its own frozen authority boundary.

## Present status

White Rabbit is currently a research program with evidence infrastructure and measurement requirements.

No White Rabbit treatment is open in this repository.

No representation-learning policy, adaptive controller, capability benchmark, or compute-saving result is established here.
