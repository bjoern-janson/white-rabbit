# Minimum Identity Independence Assay v0.1.3 — Hostile Review

Review target: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1.3`

Status: `REVIEW_BLOCKED / IMPLEMENTATION_NOT_ELIGIBLE / NON_AUTHORIZING`

Scientific/model observations: `0`

Engineering assay evaluations: `0`

This review restarts from Gate 1 after the Gate-5 cost-contract repair and stops at the first blocking defect.

## Reviewed authority

```text
successor constitution
assays/MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0_1_3.md
blob: 2116f6a50d12a0c92469af1a2cee2a80d43309ff

cost contract
assays/MINIMUM_IDENTITY_INDEPENDENCE_COST_CONTRACT_V0_1.md
blob: efb3fb1fd2f3e77e9b2ca655aa877e54e1229c7f

repaired oracle
assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1_1.json
blob: f2f46f4ad0df0086aaa40c6f2b67755050a66ad6

view boundary
assays/MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0_1.md
blob: 565611214b61f82e2b817c669bc5e4522ed9a09d
```

Review order:

```text
1. oracle isolation
2. architecture isolation
3. ground-truth integrity
4. anti-triviality
5. cost separability
6. claim ceiling
```

## Gate 1 — oracle isolation

State: `PASS_AT_CONSTITUTION_LEVEL`

The Gate-5 repair changes no architecture-visible information. The frozen `V_i` schemas, opaque handles, stateless evaluation boundary, referee-only semantic mapping, forbidden oracle fields, and no-order/no-state requirements remain unchanged.

The cost contract explicitly keeps semantic critical-case aggregation referee-side after architecture outputs and cost ledgers are frozen.

No new oracle-only information is introduced into `V_i`.

Ceiling:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

## Gate 2 — architecture isolation

State: `PASS_AT_CONSTITUTION_LEVEL`

The identity-evidence architecture remains the only intended treatment variable.

The cost contract freezes common instrumentation semantics and does not alter case bytes, parser semantics, evidence authority, scoring, runtime contract, or oracle access.

The architecture-attributable/shared/one-time accounting classes apply symmetrically to all four architectures.

Ceiling:

```text
constitution-level isolation design PASS
!= implementation realization PASS
```

## Gate 3 — ground-truth integrity

State: `PASS`

The Gate-5 repair does not modify the repaired v0.1.1 oracle.

The previously repaired E4 remains distinct from E2 in the authority-bearing custody-report state:

```text
E2 actual H_e = ALPHA_MUT
E2 custody-reported H_e = SHA256(ALPHA_MUT)

E4 actual H_e = ALPHA_MUT
E4 custody-reported H_e = SHA256(ALPHA)
```

No new ground-truth field is introduced by the cost contract.

## Gate 4 — anti-triviality

State: `PASS`

The sufficiency rule remains unchanged:

```text
C0,C1 -> IDENTITY_PASS
E1,E2,E3,E4 -> IDENTITY_MISMATCH
IDENTITY_UNRESOLVED -> 0
```

Always-pass, always-mismatch, and always-unresolved strategies still fail the critical contract.

Cost cannot compensate for a missed critical case because only critically sufficient architectures enter the primary Pareto set.

## Gate 5 — cost separability

State: `FAIL`

The new cost contract successfully freezes:

- six mandatory primary dimensions;
- the six-critical-case primary horizon;
- architecture/shared/one-time accounting classes;
- explicit missingness semantics;
- diagnostic-only timing/CPU;
- componentwise dominance;
- Pareto and unique-minimum prerequisites;
- no scalarization.

However, one mandatory primary dimension remains internally contradictory.

### Blocking defect — `C_persist_bytes` has two incompatible measurement functions

Section 5.3 first defines:

```text
C_persist_bytes =
sum(final file sizes in that root at terminal-verdict freeze)
```

but later in the same section states:

```text
Files deleted before terminal freeze still count as bytes written
...
C_persist_bytes = cumulative architecture-evidence bytes newly written
not terminal retained size.
```

These are not equivalent.

For example, an implementation may write 100 bytes and later delete or overwrite them before terminal freeze:

```text
terminal retained bytes = 0 or less than 100
cumulative bytes written = 100 or more
```

The two definitions therefore assign different primary cost values to the same execution history.

Because Pareto and dominance can change depending on which definition is used, the cost vector is still not prospectively single-valued.

This is a Gate-5 contract defect, not an implementation result.

### Required shallowest repair

Freeze exactly one authoritative persistence metric.

The intended stronger rule is already apparent from the anti-evasion language:

```text
C_persist_bytes = cumulative architecture-evidence bytes newly written
```

If retained-size diagnostics are desired, give them a separate diagnostic name such as:

```text
persist_retained_bytes_terminal
```

and exclude that diagnostic from Pareto/minimum decisions.

Do not modify any other primary dimension unless a new review later reaches a defect there.

After the cost-contract successor is frozen, restart hostile review from Gate 1.

## Gate 6 — claim ceiling

State: `NOT_OPENED`

Gate 5 failed, so the claim ceiling is not reviewed in this pass.

## Terminal review state

```text
ORACLE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

ARCHITECTURE_ISOLATION:
PASS_AT_CONSTITUTION_LEVEL

GROUND_TRUTH_INTEGRITY:
PASS

ANTI_TRIVIALITY:
PASS

COST_SEPARABILITY:
FAIL

CLAIM_CEILING:
NOT_OPENED

IMPLEMENTATION:
NOT_ELIGIBLE

EXECUTION:
NOT_AUTHORIZED

ASSAY OBSERVATIONS:
0
```

Next admissible action:

```text
MINIMAL GATE-5 COST-CONTRACT CORRECTION ONLY
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
