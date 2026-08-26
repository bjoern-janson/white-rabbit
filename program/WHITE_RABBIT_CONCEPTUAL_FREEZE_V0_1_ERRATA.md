# White Rabbit Conceptual Freeze v0.1 — Errata / Type Clarification

Status: `ERRATA / SUCCESSOR_CLARIFICATION / NON_AUTHORIZING`

Parent frozen artifact:

`program/WHITE_RABBIT_CONCEPTUAL_FREEZE_V0_1.md`

Parent blob at remediation boundary:

`ee91f970cebf99b1de82e553d92b0fa9026321c6`

The parent remains a frozen historical artifact. This file corrects downstream use without silently
rewriting the original freeze.

## 1. `C_improve` type clarification

The parent uses `C_improve` first as:

```text
candidate capacity or mechanism for converting feedback
into improved future computational policy/economics
```

and later places the same symbol inside additive cost equations and an ROI denominator.

Those are incompatible mathematical roles.

Successor notation:

```text
kappa_improve = improvement capacity/mechanism
W_improve,t   = work/cost expended invoking improvement at t
```

Use:

```text
I proportional to kappa_improve
```

for the intelligence/capacity hypothesis.

Use:

```text
C_H =
    C_initial
    + sum_t [
        C_execute,t
        + C_observe,t
        + C_revise,t
        + W_improve,t
      ]
```

for lifecycle work accounting.

A type-correct future ROI form is:

```text
ROI_C(t) =
    (C_baseline,future - C_candidate,future)
    /
    W_improve,t
```

provided the denominator is a measured/constituted cost quantity.

No empirical claim changes.

## 2. Gate-family composition clarification

The canonical White Rabbit economic gates:

```text
G1 capability preservation
G2 independent reproduction
G3 work reduction
G4 amortization
```

and the conceptual-freeze correctability burdens:

```text
G_S semantic sufficiency
G_C challenge sufficiency
G_R operative revision
```

are distinct burden families.

This repository does **not** currently freeze a single authoritative rule such as:

```text
G_S AND G_C AND G_R AND G1 AND G2 AND G3 AND G4
```

as the sole White Rabbit decision criterion.

Current state:

```text
INTEGRATION_OPEN / NO_COMBINED_VERDICT_RULE_FROZEN
```

This is an integration ambiguity, not a contradiction.

## 3. Authority-propagation refinement

The parent already contains:

```text
F_propagation:
    authority changes but operative execution does not
```

Repository evidence now motivates a more granular diagnostic decomposition:

```text
Identity
-> Authority acquisition
-> Authority propagation
-> Operative revision
```

This is a repository diagnostic refinement only. It does not amend the frozen White Rabbit ontology
or establish a general corrigibility theorem.

Current repository inventory:

`program/AUTHORITY_PROPAGATION_INVENTORY_V0_1.md`

## Claim ceiling

This erratum corrects type/use and integration interpretation. It does not:

- establish `kappa_improve`;
- establish a causal effect on `Phi`;
- establish compounding;
- establish a White Rabbit;
- authorize any experiment;
- unfreeze the parent ontology.
