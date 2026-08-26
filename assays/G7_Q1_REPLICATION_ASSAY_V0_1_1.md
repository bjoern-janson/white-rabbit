# G7 Q1 Replication Assay v0.1.1 — Provenance Repair

Version: `G7_Q1_REPLICATION_ASSAY_V0.1.1`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Parent constitution:

`assays/G7_Q1_REPLICATION_ASSAY_V0_1.md`

Parent blob:

`a83d10352d54d4361beb03c09d69682d7ecd1ed7`

Scientific observations under parent or successor: `0`

## Absolute scope of this successor

This successor changes **Q2 provenance only**.

All frozen Q1 treatment/control bytes, hashes, target bytes/hash, request construction, runtime,
cold/readiness doctrine, identity gate, mechanical grader, 20+20 replicate burden, order, gate
precedence, censoring rule, primary work currency, terminal vocabulary, claim ceiling, and execution
stop are inherited unchanged from the parent unless explicitly overridden below.

## Q2 provenance override

Parent Section 2 states that a fresh Q2 replication reported:

```text
Q2_GENERATION_WORK_REDUCTION_NOT_OBSERVED
```

The current repository does not contain a resolvable Q2 constitution, result, or custody object that
supports that assertion.

Therefore the effective successor state is:

```text
Q2_SOURCE_STATUS: SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
Q2_EVIDENTIAL_AUTHORITY_FOR_Q1: NONE
Q2_OBSERVATIONS_ENTERING_Q1: 0
```

The historical Q2 assertion may be retained only as unresolved motivational context.

It must not be represented as repository-verified evidence, used to authorize Q1, or used to
interpret a future Q1 result.

## Replicate-design clarification

The parent freezes:

```text
20 B0/B* + 20 C = 40 independently cold observations
```

That burden remains frozen as an **independent prospective Q1 design choice**.

Any parent wording that justifies the burden by saying it “matches the fresh Q2 replication burden”
is superseded. The Q1 sample size does not depend on a repository-resolvable Q2 result.

## Robustness authority

The parent already states that the robustness panel is scientifically non-authoritative at panel
level. That remains current.

Current result surface:

`assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md`

## Review addition

Independent review must explicitly verify:

```text
Q2_SOURCE_STATUS = SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
```

and confirm that no Q2 source object or Q2 outcome is required for Q1 execution or interpretation.

## Execution authority

Machine-readable disposition:

`authority/execution/G7_Q1_REPLICATION_V0_1.json`

Current:

```text
authorized = false
```

This successor does not authorize backend startup, recorder startup, or any scientific request.

## Precedence

For the effective Q1 constitution:

```text
this v0.1.1 successor
    overrides parent Section 2 Q2 evidential claims
    overrides the Q2-based sentence in parent Section 10
all other parent terms remain in force
```

## Terminal successor state

```text
artifact: G7_Q1_REPLICATION_ASSAY_V0.1.1
status: CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING
Q2 source: SOURCE_UNRESOLVED
scientific observations: 0
execution authorized: false
next action: independent constitution review
```
