# Minimum Identity Independence Assay v0.1.1

Version: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.1`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Engineering observations executed under this constitution: `0`

This is the minimal successor to `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1` after hostile review blocked at oracle isolation.

It repairs only the architecture-visible information boundary. No oracle case, scoring rule, cost rule, case partition, or claim ceiling is changed.

## 1. Immutable authority

This successor inherits the following exact upstream artifacts:

```text
v0.1 constitution
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1.md
blob: 26b09fe233b80a42e989cafc4794b2d4966bc5ef

frozen oracle
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1.json
blob: 90e1bca7f590b41f9688fcfef4f56cddfe893db6

view-boundary repair
path: assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d
```

The original v0.1 constitution remains historical and unmodified.

## 2. Precedence

All v0.1 provisions remain binding except where the view-boundary artifact is more specific about:

```text
oracle isolation
architecture-visible inputs
opaque handles
statelessness
case-order blindness
schema identity
dispatch attestation
projection rules
```

For those topics:

```text
MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0.1
    overrides less-specific v0.1 wording.
```

No other v0.1 section is reopened by this successor.

## 3. Repaired information graph

The only permissible architecture information path is:

```text
frozen oracle/case authority
        |
        v
sealed common projection P_i
        |
        v
exact serialized V_i bytes
        |
        v
chi_i
        |
        v
frozen architecture output

separately:

frozen oracle + sealed handle mapping
        |
        v
external referee
```

The referee joins architecture output to oracle truth only after architecture output is frozen.

No architecture may read the oracle or infer its semantic case from identifiers, ordering, persistent state, path names, environment, or previous evaluations.

## 4. Complete architecture-visible input

For each `chi_i`:

```text
V_i = complete and only architecture-visible case input.
```

The exact schemas, canonical schema contracts, SHA-256 schema identities, field ordering, serialization, and forbidden information are frozen exclusively by:

```text
assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
```

An implementation that supplies any extra case field is nonconforming.

An implementation that omits a required field is nonconforming.

## 5. Opaque handles and order blindness

Semantic IDs such as:

```text
C0_ALPHA_CLEAN
E2_MATERIALIZED_EXECUTED_MISMATCH
E4_LYING_CONVENIENCE_PREDICATE
```

remain referee-side only.

They must never be sent to an architecture.

The deterministic global assay schedule remains a harness/referee fact only. Each architecture evaluation receives a fresh unrelated 256-bit opaque handle, and no architecture has persistent state or a recoverable global ordinal.

Thus:

```text
known assay schedule
    !=
architecture-visible case position
```

## 6. Statelessness is mandatory

Every architecture evaluation must be realizable as:

```text
result = chi_i(V_i)
```

with no epistemically meaningful memory or input outside `V_i`.

Before execution authorization, implementation review must establish the stateless boundary required by the frozen view-boundary artifact.

If an implementation exposes oracle/repository/harness files, global ordinals, semantic paths, previous outputs, or any equivalent side channel:

```text
ORACLE_ISOLATION_FAIL
IMPLEMENTATION_NOT_ELIGIBLE
```

## 7. Dispatch identity

Before every future architecture invocation, the sealed projection layer must:

```text
validate exact V_i schema
compute dispatched_view_sha256 over exact serialized bytes
record schema_id
record frozen schema_sha256
record opaque handle referee-side
```

Architecture self-report cannot substitute for projection-layer dispatch evidence.

## 8. Explicit non-repairs

This successor deliberately does NOT inspect, reinterpret, or repair later review gates.

In particular it does not change:

```text
ALPHA / ALPHA_MUT / BETA bytes
oracle hashes
C0/C1/E1/E2/E3/E4/D1/D2/D3 case definitions
critical vs diagnostic membership
oracle mismatch truth
oracle class labels
primary scoring
anti-triviality rules
cost ledger
Pareto rule
claim ceiling
36-evaluation count
```

Any defect in those objects must be found by restarting review from Gate 1 and reaching the relevant later gate in order.

## 9. Review precedence

The hostile review restarts from the beginning:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

Stop at the first blocking defect.

Earlier PASS does not imply later PASS.

Earlier FAIL means all later gates are `NOT_OPENED`.

## 10. Claim ceiling

Unchanged from v0.1.

This successor does not establish identity sufficiency, challenge sufficiency, operative revision, corrigibility, correctable compression, White Rabbit, amortization, compounding, or any scientific result.

## 11. Stop rule

This artifact authorizes no implementation execution and no 36-case evaluation.

Next permitted action:

```text
RESTART HOSTILE CONSTITUTION + ORACLE REVIEW FROM GATE 1
```

If review reaches a new blocking defect, stop there and repair only that layer.

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.1

status:
CONSTITUTED
NOT_EXECUTED
REVIEW_REQUIRED
NON_AUTHORIZING

Gate-1 repair:
FROZEN VIEW BOUNDARY REFERENCED

engineering observations:
0

next action:
HOSTILE REVIEW FROM GATE 1
```
