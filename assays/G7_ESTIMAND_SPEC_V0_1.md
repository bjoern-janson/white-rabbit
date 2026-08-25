# Gate 7 Estimand Specification v0.1

Status: `FROZEN_ESTIMAND_SPEC / CONTENT_EFFECT_SELECTED / NON_EXECUTING / EXECUTION_NOT_AUTHORIZED`

Artifact identifier:

```text
G7_ESTIMAND_SPEC_V0.1
```

Repository parent at authoring:

```text
fa5e957b2296ea5fd54b5205bd7d969eef73d87d
```

This artifact resolves only the intended Gate 7 intervention contrast. It does not alter an existing Gate 7 artifact, constitute a replacement control, repair token/context matching, configure a runtime, or authorize an assay execution.

## Resolution

The intended Gate 7 estimand is:

```text
C_improve-content effect under matched instructional form
```

In causal notation, the intended contrast has the conceptual form:

```text
effect of setting content = C_improve rather than neutral content,
with instructional form fixed and matched across conditions
```

Equivalently, for each already constituted Gate 7 endpoint, the intended question is the difference between:

```text
do(content = C_improve, instructional_form = matched)
```

and:

```text
do(content = neutral, instructional_form = matched)
```

This notation identifies the causal question only. It does not assert that the contrast is currently identified, operationalized, estimable, executable, or validly controlled.

The other candidate resolutions are rejected for this Gate 7 estimand:

```text
package effect: NOT_SELECTED
factorial requirement: NOT_REQUIRED_FOR_THE_SELECTED_ESTIMAND
unresolved: NOT_SELECTED
```

## Meaning of the selected contrast

`C_improve content` refers to the candidate logic preserved in the literal source intervention, not to every incidental property of the complete prompt package.

`Matched instructional form` means that a future separately constituted contrast would have to hold fixed the intervention's instructional character, message role, placement, and comparable directive force while varying the candidate content. This specification does not create the matching representation or any control payload.

The literal source package includes both:

```text
1. an instructional act (for example, an instruction to internalize), and
2. the C_improve candidate content presented by that act.
```

A contrast between that whole package and a merely descriptive neutral package would identify, at most, the effect of the bundle. It would not isolate the causal contribution of `C_improve` content.

## Provenance

The resolution is grounded only in the pre-token historical statement of intent and the causal meaning of the competing contrasts.

| Source | Historical anchor | Relevant intent |
| --- | --- | --- |
| `observations/WR-OBS-002/raw_observation.md` | `70e8c46fba0a9a070a7a0aeba5664c3f8039cecf` | Preserves the source prompt as a `C_improve` intervention and records `C_improve causality` as unestablished. |
| `handoff/CODEX_G7_CONSTITUTION.md` | `20d5b3c6f545abc0d464a5377c5d2418f866faba` | Defines Gate 7 around a literal `C_improve` treatment and a matched neutral control, with tasks independent of `C_improve` content. |
| `assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md` | original constitution `7696bf90452cb13f86fe8e22cc860ff6e9d09dee` | Names condition C the literal source treatment and seeks a matched-context comparison without claiming causality. |
| `program/GATE7_PREOPEN_CONSTITUTION_REVIEW.md` | `9b48052b4814e784e56a764c35187c21d6a88d7f` | Explicitly records `C_improve treated as one candidate intervention` and `White Rabbit != C_improve effect`. |

These sources consistently make the scientific object the causal role of the `C_improve` candidate intervention while using matching to control context. They do not identify generic instructional framing or the complete literal prompt package as a co-primary scientific target.

## Excluded decision inputs

The following were not admissible evidence for choosing the estimand and did not determine this resolution:

```text
token counts
any +3 mismatch
the result of any failed control-family search
ease or difficulty of repair
anticipated treatment or control outcomes
```

Those facts could affect feasibility or future design admissibility. They cannot retroactively choose which causal question Gate 7 intended to ask.

## Rationale

### Why this is not a package-effect estimand

A package-effect estimand would treat every difference in the literal intervention package as part of the treatment, including instructional force and semantic content. That is a coherent possible estimand, but it answers:

```text
What is the effect of presenting this complete package?
```

The historical Gate 7 lineage instead repeatedly marks `C_improve` itself as the candidate intervention whose causal role remains unestablished. Therefore the complete package is the source of the candidate content, not the intended indivisible causal object.

### Why a factorial is not required by this estimand

A factorial design would be required if Gate 7 intended to estimate instructional-form effects, content effects, and their interaction as separate causal objects. The historical record does not establish those multiple estimands. It establishes one candidate-content question and a matched-context control requirement.

Accordingly, holding instructional form fixed is sufficient for the intended contrast. A future program may separately constitute a factorial assay, but such an assay would answer additional questions and is not authorized or required by this artifact.

### Why the estimand is not unresolved

The repeated historical phrases `C_improve causality`, `C_improve treated as one candidate intervention`, and `White Rabbit != C_improve effect` distinguish the candidate content effect from both the wider White Rabbit program and incidental package properties. That is sufficient to resolve the intended causal object without consulting later feasibility evidence.

## Relationship to existing Gate 7 artifacts

All existing Gate 7 artifacts remain unchanged and retain their recorded statuses.

In particular, this specification:

```text
does not reinterpret an existing B/C result;
does not amend G7_MATCHED_CONTEXT_ASSAY_V0.1.1;
does not amend the pre-open token-match artifacts;
does not amend the neutral-control reconstitution contract;
does not amend the neutral-control search artifacts;
does not create a successor assay or control;
does not open execution.
```

If an existing constituted contrast does not identify the selected estimand, this artifact does not silently repair it. Any successor design would require separate prospective constitution and authorization.

## Claim ceiling

This artifact establishes only:

```text
the intended Gate 7 causal contrast is the C_improve-content effect
under matched instructional form
```

It does not establish:

```text
a valid matched-form control
identification or estimability
token/context equivalence
control adequacy
capability preservation or improvement
work reduction
C_improve causality
a White Rabbit effect
persistence, transfer, or amortization
scientific execution evidence
```

No numerical or scientific result follows from this specification.

## STOP conditions

This task stops after this artifact is frozen and existing repository validation is run.

The following are explicitly outside authority and must not be created, modified, or executed under this specification:

```text
E_repr
R2
B1
token matching or token search
runtime configuration
llama-server or recorder startup
prelude execution
condition B or C execution
assay execution
output comparison
scientific interpretation
```

Any next transition requires separate prospective authorization. In particular, this artifact does not authorize constructing a matched-instructional control, modifying an assay, or running the selected contrast.

```text
ESTIMAND_RESOLVED != CONTRAST_CONSTITUTED
CONTRAST_CONSTITUTED != EXECUTED
```

> **Resolve the causal question before repairing its implementation.**
