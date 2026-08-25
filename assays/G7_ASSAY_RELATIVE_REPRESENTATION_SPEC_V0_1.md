# Gate 7 Assay-Relative Representation Specification v0.1

Status: `REVIEWED / REPRESENTATION_PARTITION_FROZEN / NON_CONSTRUCTIVE / EXECUTION_NOT_AUTHORIZED`

Artifact identifier:

```text
G7_ASSAY_RELATIVE_REPRESENTATION_SPEC_V0_1
```

This artifact defines only the assay-relative representation partition required for a future neutral control under the frozen Gate 7 estimand. It does not construct that control or modify any existing Gate 7 artifact.

## Immutable input

The sole controlling estimand is the already frozen:

```text
C_improve-content effect under matched instructional form
```

Source:

```text
assays/G7_ESTIMAND_SPEC_V0_1.md
published commit: 11c69c5a0ce4b02f75f1f0403869a4031b65502d
git blob: 495048de467c4a1197c888eeb2e9bd29d59b8e40
SHA-256: 24582e94052acb47dae77cc44bf35f108f506833a24c2f8523a5aa82f9cc22eb
```

This artifact cannot revise, broaden, or select a different estimand.

## Scope

The representation of a Gate 7 prelude is partitioned, relative to the frozen estimand, into three disjoint semantic/pragmatic classes:

```text
D_repr = D_preserve ⊔ D_treatment ⊔ D_free
```

where `⊔` denotes an assay-relative disjoint classification. If an apparent feature contains separable components, the components must be classified separately rather than assigning the same component to multiple classes.

A separate layer:

```text
D_measurement
```

records or tests properties of concrete realizations. It is not a fourth member of the representation partition and cannot redefine which dimensions carry the treatment.

This partition is sufficient only to state what a future neutral control would have to preserve, remove, and remain free to realize. It supplies no control text, candidate family, matching result, or execution authority.

## Classification rule

For each representational dimension `d`:

```text
d ∈ D_preserve
```

iff changing `d` would change the matched instructional form on which the frozen estimand conditions.

```text
d ∈ D_treatment
```

iff `d` conveys the `C_improve` content whose causal contribution the frozen estimand asks to vary.

```text
d ∈ D_free
```

iff `d` may vary without changing either the matched instructional form or the presence/absence of `C_improve` content, subject to the neutrality and task-independence boundaries below.

The classification is determined by historical intent and causal meaning. Surface convenience, later feasibility, and observed behavior are not classification criteria.

## `D_preserve` — matched instructional form

`D_preserve` contains the representational dimensions that must remain invariant in causal role across treatment and neutral control.

| Preserved dimension | Required invariant | Reason |
| --- | --- | --- |
| **Speech act** | `PRESERVE`: an instruction/directive, not a description, question, report, warning, or suggestion | The frozen estimand explicitly conditions on matched instructional form. |
| Directive force | Active and comparably strong direction to the addressee | Weakening a directive into optional or descriptive language changes the intervention form. |
| Addressee | The model/system receiving the forthcoming target task | Redirecting the instruction to an external person or abstract audience changes who is acted upon. |
| Requested operation class | Internalize, adopt, or use a presented logic/principle | Replacing cognitive uptake with passive reading, summarization, quotation, or critique changes the operative instruction. |
| Temporal/task relation | The instruction is presented as a prelude governing processing of the subsequent target | Moving it after the target or making it unrelated to the ensuing task changes its causal position. |
| Message role and conversational position | User-provided prelude in the same role and pre-target position | These are expressly fixed by the frozen estimand's meaning of matched instructional form. |
| Object type | A general logic/principle offered for use, rather than a direct answer to the target task | The control must match the kind of instructional object without supplying task-specific help. |
| Task independence | No answer, solution fragment, domain hint, or task-specific capability aid | Such content would create a second treatment and contaminate the intended contrast. |
| Illocutionary polarity | Affirmative enactment of the instruction rather than negation, refusal, prohibition, or ironic quotation | An anti-instruction or quoted instruction is not the same speech act. |

Speech act is therefore unambiguously classified as:

```text
speech_act ∈ D_preserve
speech_act = PRESERVE
```

The exact words used to realize the preserved speech act are not themselves frozen by this classification. What is preserved is their pragmatic function and comparable force.

## `D_treatment` — `C_improve` content

`D_treatment` contains the dimensions that constitute or semantically transmit the candidate content whose effect Gate 7 intends to estimate.

| Treatment-bearing dimension | Treatment content |
| --- | --- |
| Named construct | `C_improve` as the capacity under consideration |
| Proportional claim | The presented relation `I ∝ C_improve` or its semantic equivalent |
| Definitional content | Improvement capacity as the capacity to convert feedback into increased future viability |
| Feedback role | Feedback as input to recursive improvement rather than as an inert observation |
| Representational transition | Better representation as a consequence in the improvement pathway |
| Mechanism transition | Better adaptive mechanisms as a consequence in the improvement pathway |
| Recursive capacity transition | Greater improvement capacity produced by improved representation/mechanisms |
| Viability consequence | Expansion of viable futures as the terminal direction of the pathway |
| Integrated causal logic | The overall feedback-to-representation-to-adaptation-to-improvement-to-viability structure |
| Semantic equivalents | Paraphrases, aliases, examples, or implications that materially reproduce the same candidate logic |

For a future control to be neutral with respect to the selected estimand, it must not assert, entail, presuppose, exemplify, or instruct adoption of the treatment-bearing logic.

Neutrality means absence of the `C_improve` content, not inversion of it. An anti-`C_improve` claim, a claim that feedback reduces viability, or an instruction to reject improvement would introduce a distinct active treatment rather than a neutral control.

The instruction to internalize or use a logic is not itself in `D_treatment`; that speech act belongs to `D_preserve`. The particular logic being offered for internalization is what belongs to `D_treatment`.

## `D_free` — unconstrained realization dimensions

`D_free` contains dimensions that are not part of the selected causal treatment and need not be semantically identical, provided they neither change `D_preserve` nor carry `D_treatment`.

Examples include:

```text
exact lexical choices used to realize the preserved directive
the name of a neutral placeholder construct
neutral subject matter that carries no C_improve-equivalent logic
non-treatment examples or labels
exact notation and variable names for neutral content
punctuation and capitalization
line wrapping, indentation, and typographic ornament
choice of arrows, bullets, or equivalent visual connectors
mnemonic or stylistic phrasing
surface length and formatting particulars
```

`D_free` means free relative to the causal representation partition, not unrestricted in the final assay. A concrete realization may later be constrained by an independently constituted measurement or matching contract.

No `D_free` choice may:

```text
weaken or strengthen the preserved speech act;
change the addressee, requested operation class, or pre-target role;
encode C_improve or a semantic proxy for it;
encode an anti-C_improve treatment;
answer or materially assist a target task;
introduce another capability-changing or metacognitive optimization instruction.
```

If a nominally free feature acquires one of those functions in context, it must be reclassified by causal meaning before any control is constituted.

## `D_measurement` — separate realization-audit layer

`D_measurement` contains observables and checks used to describe or audit concrete treatment/control realizations. It does not determine semantic membership in `D_preserve`, `D_treatment`, or `D_free`.

Its permissible scope includes, if separately constituted later:

| Measurement class | What it may observe |
| --- | --- |
| Custody | Exact source, bytes, hashes, and assembly identity |
| Context realization | Message count, role, order, prelude position, separator, and target identity |
| Surface realization | Characters, bytes, lines, blocks, symbols, and other literal structure |
| Model-visible burden | Template-mediated input burden under a separately frozen measurement procedure |
| Partition audit | Whether a realized control actually preserves `D_preserve` and excludes `D_treatment` |

The measurement layer may reveal that a proposed realization is incomparable or inadmissible. It may not make semantically different speech acts equivalent, declare treatment-bearing content neutral, or move a dimension between partition classes to obtain a convenient match.

No values, thresholds, equivalence rules, token-matching procedure, runtime settings, or candidate evaluations are defined here.

## Control eligibility implied by the partition

Without constructing a control, this specification defines the necessary semantic conditions for a future `B`:

```text
1. match C on every D_preserve dimension;
2. contain none of the D_treatment content or its semantic equivalents;
3. choose D_free realizations only within the neutrality and task-independence boundaries;
4. undergo any D_measurement checks only under a separately frozen authorization.
```

Satisfying these conditions would make a candidate eligible for further review. It would not by itself establish measurement equivalence, control adequacy, identifiability, or execution readiness.

## Provenance

This partition is derived from the following historical causal record:

| Source | Anchor | Contribution |
| --- | --- | --- |
| `assays/G7_ESTIMAND_SPEC_V0_1.md` | published `11c69c5a0ce4b02f75f1f0403869a4031b65502d` | Immutable selection of the `C_improve`-content effect under matched instructional form; expressly fixes instructional character, role, placement, and comparable directive force. |
| `observations/WR-OBS-002/raw_observation.md` | `70e8c46fba0a9a070a7a0aeba5664c3f8039cecf` | Literal source of the instruction and `C_improve` candidate logic; records its causal role as unestablished. |
| `handoff/CODEX_G7_CONSTITUTION.md` | `20d5b3c6f545abc0d464a5377c5d2418f866faba` | Historical requirement for a matched-context neutral control, task independence, fixed role/position, and literal source treatment. |
| `assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md` | original constitution `7696bf90452cb13f86fe8e22cc860ff6e9d09dee` | Preserves the historical distinction between prelude content, common target/context, source treatment, and neutral control assumption. |
| `program/GATE7_PREOPEN_CONSTITUTION_REVIEW.md` | `9b48052b4814e784e56a764c35187c21d6a88d7f` | Confirms that `C_improve` is one candidate intervention and is not equivalent to the wider White Rabbit hypothesis. |

## Excluded classification inputs

The following were excluded from every partition decision:

```text
the +3 token mismatch
the failed v0.1 control family or its search result
all token counts
runtime behavior
observed model outputs
anticipated outcomes
ease or difficulty of constructing a replacement control
```

These may bear on later feasibility or admissibility. They cannot determine which dimensions the frozen causal estimand requires preserved or varied.

## Review findings

The partition was reviewed against the immutable estimand for:

```text
estimand fidelity: PASS
speech-act classification as PRESERVE: PASS
treatment-content isolation: PASS
neutrality versus anti-treatment distinction: PASS
semantic partition versus measurement-layer separation: PASS
non-construction boundary: PASS
execution firewall: PASS
```

This is a conceptual/constitutional review only. It is not empirical or scientific validation.

## Rationale

The selected estimand asks for the effect of `C_improve` content while conditioning on matched instructional form. Causal identification therefore requires the pragmatic act of instructing the system to adopt/use a logic to be common across conditions. If one condition instructs while the other merely describes, the contrast bundles speech-act and content effects and no longer answers the frozen question.

The semantic content of `C_improve` must consequently be the varied dimension. Incidental wording and presentation can remain free at the representation level, while a distinct measurement layer may later constrain concrete realizations to protect comparability. Keeping that layer separate prevents surface metrics from retroactively defining semantic neutrality.

## Relationship to existing artifacts

All existing Gate 7 artifacts remain byte-untouched and retain their recorded authority and status.

This specification does not:

```text
amend the frozen estimand;
amend the existing Gate 7 assay;
reinterpret the existing B prelude;
repair or supersede a control;
amend token/context artifacts;
amend a search artifact or reconstitution contract;
authorize any next transition.
```

## Claim ceiling

This artifact establishes only an assay-relative classification of representation dimensions for the already frozen estimand:

```text
D_preserve: matched instructional form, including speech act
D_treatment: C_improve candidate content
D_free: non-treatment realization choices within neutrality boundaries
D_measurement: a separate future audit layer
```

It does not establish:

```text
a valid or instantiated neutral control
a control payload or candidate family
representation equivalence for any concrete text
measurement or token equivalence
identification or estimability
control adequacy
runtime admissibility
capability preservation or improvement
work reduction
C_improve causality
a White Rabbit effect
execution evidence
```

## STOP conditions

This task stops after this reviewed artifact is frozen and the existing repository tests and validator are run.

The following remain expressly unauthorized:

```text
construct B1
create or modify R2
create a candidate family
perform token matching or token search
change runtime configuration
start llama-server or the recorder
execute any prelude, B condition, or C condition
run or modify the Gate 7 assay
compare outputs
draw a scientific conclusion
```

Any control construction, representation realization, measurement contract, or execution requires a new prospective authorization.

```text
REPRESENTATION_PARTITIONED != CONTROL_CONSTRUCTED
CONTROL_CONSTRUCTED != MATCHED
MATCHED != EXECUTED
```

> **Preserve the instructional act; vary only the candidate content; measure realization separately.**
