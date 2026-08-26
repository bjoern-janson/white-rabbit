# Authority-Propagation Inventory v0.1

Version: `AUTHORITY_PROPAGATION_INVENTORY_V0.1`

Status: `FROZEN_INVENTORY / REPOSITORY_OBSERVATION / NON_SCIENTIFIC / NON_AUTHORIZING`

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

## Question

```text
When an authority-bearing source changes status,
what actually happens to each dependent surface?
```

Inventory object:

```text
I(a) = (a, A_t(a), D(a), rho(a, Delta A))
```

where:

- `a` is an authority-bearing source artifact/state;
- `A_t(a)` is its current authority disposition;
- `D(a)` is the declared/live dependent set;
- `rho(a, Delta A)` is the observed downstream response after authority changes.

The inventory does not assume a universal propagation mechanism.

## Cross-cutting diagnostic

```text
A_t(a) != A_assumed(d)
AND d in D(a)
=>
d may not silently remain CURRENT
```

Possible observed states include, but are not limited to:

```text
UPDATED
STALE_MARKED
REQUIRES_REVIEW
SOURCE_UNRESOLVED
OPERATIVELY_BLOCKED
UNCHANGED_BUT_DEPENDENT
BYPASSABLE
```

## Case 1 — result authority -> rendered scientific claim

Source authority change:

```text
G7 neutral-control robustness panel
historical panel authority
->
PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN
```

Cause:

```text
B4/B5 tuple + grammar + frozen-hash authority
!=
displayed "exact source"

executor followed displayed source
->
H_executed != H_frozen
```

Dependent:

`assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md`

Observed pre-remediation response:

```text
UNCHANGED_BUT_DEPENDENT
silently rendered ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED
```

Remediation in this checkpoint:

```text
STALE_MARKED / AUTHORITY_WITHDRAWN
```

Historical observations and old analyzer terminal are preserved as history, but the result surface no
longer presents them as current panel authority.

## Case 2 — state authority -> orientation surface

Source authority change:

```text
repository progressed through:
G7 v0.3 execution
robustness execution + identity invalidation
Q1/Q3 constitutions
MII implementation/runtime conformance
```

Dependents:

```text
README.md
program/STATE.md
program/ROADMAP.md
```

Observed pre-remediation response:

```text
orientation still described an old pre-execution Gate 7 frontier
```

Classification:

```text
STALE_ORIENTATION
```

Remediation in this checkpoint:

```text
UPDATED
```

All current orientation surfaces carry:

```text
Authority checkpoint: WR_AUTHORITY_2026_08_26_V1
```

and point to `program/CURRENT_AUTHORITY_STATE.json`.

This update fixes the current stale instance. It does **not** prove future staleness will automatically
be prevented.

## Case 3 — evidence authority -> dependent claim

Source assertion:

```text
fresh Q2 replication
```

Repository source status:

```text
SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
```

Dependents:

```text
historical G7_Q1_REPLICATION_ASSAY_V0.1 motivation
historical G7_Q3_REPLICATION_ASSAY_V0.1 motivation
```

Observed pre-remediation response:

```text
derived assertion present
without repository-resolvable upstream Q2 constitution/result/custody
```

Classification:

```text
SOURCE_UNRESOLVED
```

Remediation:

```text
G7_Q1_REPLICATION_ASSAY_V0.1.1
G7_Q3_REPLICATION_ASSAY_V0.1.1
```

The successor constitutions explicitly downgrade Q2 to unresolved motivation. Q2 supplies no sample
observations, no evidential authority, and no execution authority.

## Case 4 — execution authority -> operative transition

Historical source state:

```text
constitution = NON_AUTHORIZING
execution authority = absent
```

Observed historical downstream response:

```text
scientific result commit could follow directly
```

Repository-governance state at inventory start:

```text
main protected: false
required status checks: off
rulesets: none
```

Classification:

```text
DECLARED_AUTHORITY_GRAPH != OPERATIVE_GITHUB_GRAPH
BYPASSABLE
```

Repository-level remediation:

```text
constitution/authority_propagation.md
schema/execution_authorization.schema.json
authority/execution/*.json
program/CURRENT_AUTHORITY_STATE.json
tools/validate_authority_propagation.py
.github/workflows/authority-propagation.yml
```

Current open scientific lanes have machine-readable:

```text
authorized = false
```

Residual:

```text
GitHub main remains unprotected.
Repository checks can detect a bypass but cannot make direct push unreachable.
```

Current classification:

```text
MACHINE_CHECKED / PLATFORM_BYPASSABLE
```

A full `OPERATIVELY_BLOCKED` classification is not earned until branch protection/rulesets require
the check and review.

## Current topology result

The four cases share the abstract symptom:

```text
Delta E -> Delta A
does not automatically imply
Delta downstream system
```

But their realized response mechanisms are materially different:

```text
result rendering       -> stale/current status surface
orientation            -> state projection
dependent claim        -> resolvable provenance edge
execution transition   -> permission/enforcement graph
```

Therefore this inventory does **not** yet earn one universal propagation primitive.

Terminal:

```text
COMMON_SYMPTOM_OBSERVED
MECHANISM_HETEROGENEITY_OBSERVED
UNIVERSAL_PROPAGATION_MECHANISM_NOT_EARNED
```

## Next admissible edge

```text
verify these classifications against future repository changes
-> add new cases only when independently evidenced
-> build a shared propagation mechanism only if a common failure topology is earned
```

No MII assay, Q1/Q3 assay, or other scientific execution is authorized by this inventory.
