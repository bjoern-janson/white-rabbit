# White Rabbit Authority-Propagation Boundary

Version: `AUTHORITY_PROPAGATION_BOUNDARY_V0.1`

Status: `FROZEN_REPOSITORY_CONTROL_CONSTITUTION / NON_SCIENTIFIC / NON_AUTHORIZING`

Parent founding authority constitution remains:

`constitution/authority.md`

This later constitution does not amend the founding validator's scientific ceiling. It governs only
repository authority state, dependent surfaces, and execution-disposition records.

## 1. Jurisdiction

This layer may:

- record current authority dispositions for repository artifacts;
- record declared/live dependency edges;
- mark a dependent artifact `UPDATED`, `STALE_MARKED`, `REQUIRES_REVIEW`,
  `SOURCE_UNRESOLVED`, `OPERATIVELY_BLOCKED`, or another explicit state;
- validate that current orientation surfaces point to the current authority checkpoint;
- validate that open scientific execution lanes have explicit machine-readable authorization state;
- fail closed when required authority/provenance references are unresolved.

Successful validation ceiling:

```text
AUTHORITY_PROPAGATION_VALID
```

This means the checked repository surfaces are internally consistent with the current checkpoint.
It does **not** establish scientific warrant or truth.

## 2. Current-authority invariant

For source artifact/state `a` and dependent `d`:

```text
A_t(a) != A_assumed(d)
AND d in D(a)
=>
d may not silently remain CURRENT
```

History may remain immutable. Current authority need not.

Acceptable responses include explicit staleness, review requirement, source-unresolved status, or
operative blocking. Automatic rewriting is not required.

## 3. Execution authority

Scientific execution requires a machine-readable authorization object conforming to:

`schema/execution_authorization.schema.json`

Minimum rule:

```text
authorized = true
```

is necessary but not sufficient. The authorization must also bind the exact target constitution,
review state, and scope required by that lane.

If:

```text
authorized = false
```

then repository tooling must classify scientific execution as unauthorized.

Current open lanes are recorded under:

`authority/execution/`

## 4. Separation of authority and history

Historical result bytes may be retained after authority withdrawal.

Therefore:

```text
historical terminal
!=
current scientific authority
```

A current result surface must make withdrawal/provenance limitation visible before presenting a
historical terminal as operative conclusion.

## 5. Unresolved source edges

If a dependent claim references a supporting artifact that cannot be resolved from the repository:

```text
SOURCE_UNRESOLVED
```

The dependent may preserve the historical assertion, but it may not use that assertion as current
evidential authority until the source edge is restored.

## 6. Orientation checkpoint

Current orientation surfaces must carry the current checkpoint identifier from:

`program/CURRENT_AUTHORITY_STATE.json`

Current required orientation surfaces:

```text
README.md
program/STATE.md
program/ROADMAP.md
assays/README.md
```

A mismatch is a validation failure.

## 7. Platform-enforcement ceiling

Repository validation is not equivalent to GitHub enforcement.

If branch protection/rulesets do not require the validator, the correct state is:

```text
MACHINE_CHECKED / PLATFORM_BYPASSABLE
```

not:

```text
OPERATIVELY_ENFORCED
```

The repository must report this residual explicitly.

## 8. No universal propagation mechanism

This constitution does not create `P_rev` or any general propagation engine.

The current inventory must first determine whether result rendering, orientation, provenance edges,
and execution permissions share a common failure topology.

## 9. Validation

Reference implementation:

`tools/validate_authority_propagation.py`

Tests:

`tests/test_authority_propagation.py`

CI definition:

`.github/workflows/authority-propagation.yml`

## Terminal state

```text
repository authority propagation: CONSTITUTED
scientific authority: NONE
scientific execution authorization: NONE
universal propagation mechanism: NOT EARNED
```
