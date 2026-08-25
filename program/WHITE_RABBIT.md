# White Rabbit Program Definition

Status: `FROZEN_CURRENT_PROGRAM_DEFINITION / NON_AUTHORIZING`

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
    -> preserve the relevant result with less required future computation
```

The program does not assume that `M` is a prompt, formula, representation, decomposition, compiler, lookup structure, canonicalization rule, or learned object. Those are candidate forms, not definitions.

## Canonical definition

> **White Rabbit is structure that makes adequate intelligence cheaper.**

The minimum success signature is:

> **same relevant capability, less required computation**

A White Rabbit exists only when reusable structure makes previously necessary computation unnecessary without sacrificing the capability or distinctions that mattered, and the saved work repays the structure's acquisition cost.

The defining prize is computation eliminated under a valid accounting boundary. Capability increase is optional upside, not a prerequisite.

## North star

> **Spend computation changing the future computational policy, and recover more computation than was spent doing so.**

A complementary formulation is:

> **A better rule for what intelligence bothers computing at all.**

Prettier reasoning, more tokens, hidden preprocessing, uncharged caches, answer leakage, or a one-instance trick do not satisfy the White Rabbit criterion.

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

## General White Rabbit gates

For a candidate reusable structure `M`, the general burden is sequential:

```text
G1 -> G2 -> G3 -> G4
```

with:

```text
G1: C_realized(M, q) >= C_realized(R0, q)
G2: the effect reproduces under independent constituted runs
G3: C_work(M, q) < C_work(R0, q)
G4: acquisition cost is repaid over the constituted reuse horizon
```

The horizon-level economics are:

```text
C_acquire(M) + sum_i C_work(M, q_i)
    <
sum_i C_work(R0, q_i)
```

A stronger optional result is:

```text
G1+: C_realized(M, q) > C_realized(R0, q)
```

This is a **Capability Rabbit**: the structure unlocks more realized capability rather than merely preserving adequate capability at lower cost.

The minimum White Rabbit definition does not require `G1+`.

## Rejection filter

The following are insufficient by themselves:

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

## Measurement doctrine

All White Rabbit evidence must respect:

```text
RAW MEASUREMENT
    -> DERIVED RECONSTRUCTION
    -> INTERPRETATION
```

No layer may silently inherit the authority of the layer before it.

Literal backend measurements remain literal measurements. Arithmetic reconstruction is labeled derived. Causal/scientific meaning is a later interpretation requiring its own evidence.

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

White Rabbit is currently a research program with evidence infrastructure, a reported local recorder implementation, and frozen measurement requirements.

No White Rabbit treatment is open in this repository.

No representation-learning policy, adaptive controller, capability benchmark, or compute-saving result is established here.
