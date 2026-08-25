# Gate 7 Neutral-Control Selection Specification v0.1

Version: `G7_NEUTRAL_CONTROL_SELECTION_SPEC_V0.1`

Status: `B_STAR_FROZEN / ORDINAL_1 / SOURCE_ADMISSIBLE / EXECUTOR_UNMEASURED / NON_EXECUTING`

Verified starting remote `main`:

```text
83f921110b70a9ce996765eac71bd9ecfbd86b66
```

```text
N_scientific_runs = 0
```

This artifact selects, materializes, and freezes exactly one canonical neutral realization from the already frozen `B_neutral^(v0.2)` family. It does not constitute a successor Gate 7 assay, tokenize the control, contact an executor, or authorize execution.

## Immutable upstream authority

| Object | Path | Published commit | Git blob |
| --- | --- | --- | --- |
| `Theta_G7` | `assays/G7_ESTIMAND_SPEC_V0_1.md` | `11c69c5a0ce4b02f75f1f0403869a4031b65502d` | `495048de467c4a1197c888eeb2e9bd29d59b8e40` |
| `E_repr` | `assays/G7_ASSAY_RELATIVE_REPRESENTATION_SPEC_V0_1.md` | `85a4b6b5fee11e5d2c0ea8e8a0649f61c782ea16` | `51233d6526554d0d1e6f48b045cff5d4a00cde8f` |
| `R2` and `B_neutral^(v0.2)` | `assays/G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0_2.md` | `2b4933b798745aff1fff6241d5a34386bf8d944d` | `428eb6cf43be782f83cfc22a55c07f6459424582` |
| `E_measurement` | `assays/G7_MEASUREMENT_EQUIVALENCE_SPEC_V0_1.md` | `83f921110b70a9ce996765eac71bd9ecfbd86b66` | `d18eb7dba5a465185b594fa62d8a3aa93304d286` |

All four upstream artifacts remain byte-unchanged. Their estimand, representation partition, grammar, family, admissibility rules, and measurement classification are immutable inputs.

## Prospective selection rule

The sole selection rule is:

```text
B* = arg min ordinal(B_k)
     over B_k in B_neutral^(v0.2)
```

Equivalently:

```text
select the unique family member with frozen ordinal = 1
```

This is a convention, not an optimization. It does not claim that ordinal 1 is scientifically superior, behaviorally more neutral, executor-optimal, or representative of the full family.

The rule uses only the enumeration frozen prospectively in `G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.2`, before candidate tokenization, latency, model behavior, capability, prompt burden, generated work, or scientific outcomes.

Therefore the selection is:

```text
deterministic
prospective
executor-blind
outcome-blind
```

## Algebraic derivation of ordinal 1

The frozen ordinal rule for tuple `(i0, i1, i2, i3, i4, i5)` is:

```text
ordinal = (((((i0 × 3 + i1) × 3 + i2) × 3 + i3) × 3 + i4) × 3 + i5) + 1
```

Each index is in `{0, 1, 2}`. Substitution of the minimum index at every position gives:

```text
ordinal(0,0,0,0,0,0)
    = (((((0 × 3 + 0) × 3 + 0) × 3 + 0) × 3 + 0) × 3 + 0) + 1
    = 1
```

Conversely, every nonzero index contributes a positive radix-three place value, so no other tuple has ordinal 1.

Frozen selection:

```text
ordinal: 1
six-index tuple: (0,0,0,0,0,0)
```

No family enumeration, search, or inspection of another tuple was performed.

## Mechanical derivation from the frozen grammar

The ordinal-1 tuple selects index `0` from each frozen slot:

| Slot | Selected frozen primitive |
| --- | --- |
| `RELATION_LINE[0]` | `S = L_catalog` |
| `DEFINITION_LINE[0]` | `catalog = fixed convention pairing a symbol with a label, symbol` |
| `STAGE_1[0]` | `fixed catalog relation` |
| `STAGE_2[0]` | `corresponding catalog label` |
| `STAGE_3[0]` | `unchanged catalog entry` |
| `STAGE_4[0]` | `same descriptive mapping` |

These six primitives were substituted once into the exact frozen `Build` skeleton. The result was then compared byte-for-byte with the supplied expected reconstruction. They agree.

```text
derived from frozen grammar rather than copied: YES
derived reconstruction equals expected reconstruction: YES
```

## Frozen canonical control `B*`

Exact source text, excluding code-fence delimiters, using LF line endings and no trailing LF:

```text
internalize logic: S = L_catalog

where:

catalog = fixed convention pairing a symbol with a label, symbol
   ↓
fixed catalog relation
   ↓
corresponding catalog label
   ↓
unchanged catalog entry
   ↓
same descriptive mapping
```

Every down-arrow line begins with exactly three ASCII spaces followed by `↓` (`U+2193`).

## Exact custody

```text
family identifier: B_neutral^(v0.2)
selection identifier: B*
ordinal: 1
six-index tuple: (0,0,0,0,0,0)
Unicode code points: 226
UTF-8 bytes: 234
UTF-8 SHA-256: 37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663
line endings: LF only
UTF-8 BOM: absent
trailing LF: absent
upstream R2 commit: 2b4933b798745aff1fff6241d5a34386bf8d944d
upstream R2 git blob: 428eb6cf43be782f83cfc22a55c07f6459424582
```

The code-point count, UTF-8 byte count, and SHA-256 were derived independently from the grammar-produced source and matched the supplied verification targets exactly.

```text
B_STAR_DERIVATION_MISMATCH: NOT_TRIGGERED
B_STAR_CUSTODY_MISMATCH: NOT_TRIGGERED
```

## Frozen R2 source-admissibility result

Every predicate was applied in the order frozen by R2. In this table, `PASS` means the rejection condition was absent.

| Order | Frozen predicate / rejection code | Result | Evidence |
| ---: | --- | --- | --- |
| 1 | `R2_UTF8_INVALID` | `PASS` | Source encodes and decodes as valid UTF-8 |
| 2 | `R2_BOM_PRESENT` | `PASS` | UTF-8 BOM absent |
| 3 | `R2_LINE_ENDING_INVALID` | `PASS` | LF only; no CR |
| 4 | `R2_TRAILING_LF` | `PASS` | No trailing LF |
| 5 | `R2_SKELETON_MISMATCH` | `PASS` | Exact frozen 13-line skeleton |
| 6 | `R2_DIRECTIVE_MISMATCH` | `PASS` | Exact `internalize logic: ` operator and ASCII space |
| 7 | `R2_SLOT_NOT_MEMBER` | `PASS` | Every selected value is index 0 of its frozen slot |
| 8 | `R2_TARGET_TEXT_PRESENT` | `PASS` | No complete frozen target occurs |
| 9 | `R2_EXPECTED_ANSWER_PRESENT` | `PASS` | No frozen expected answer occurs |
| 10 | `R2_TREATMENT_LITERAL_PRESENT` | `PASS` | No case-insensitive literal `C_improve` occurs |
| 11 | `R2_FORBIDDEN_TREATMENT_SUBSTRING` | `PASS` | No frozen treatment-guard substring occurs after the frozen normalized scan |
| 12 | `R2_FORBIDDEN_TASK_HELP_SUBSTRING` | `PASS` | No frozen task-help substring occurs after the frozen normalized scan |
| 13 | `R2_UNEXPECTED_DUPLICATE` | `PASS` | Unique slot strings at fixed unique positions make `Build` injective; the tuple is recoverable from the source |

```text
all frozen R2 source-level admissibility predicates: PASS
B_STAR_SOURCE_INADMISSIBLE: NOT_TRIGGERED
```

Predicate 13 was established algebraically from the frozen unique-slot construction. No other candidate was materialized or hashed.

No new semantic test, forbidden substring, compatibility rule, or reinterpretation was introduced.

## Selection firewall

`B*` selection did not use and must never be justified by:

```text
tokenizer measurements
prompt-token counts
prompt time
absolute target token position
cache or reuse fields
model behavior
generated work
capability
latency
anticipated assay result
historical token observations
```

```text
B* selection does not depend on executor realization.
```

## Relationship to `E_measurement`

The frozen measurement classifications remain unchanged:

```text
N_prompt = MEASURE
absolute target token position = MEASURE
prompt time = MEASURE
N_prompt,new = MEASURE
N_generated = MEASURE
execution-time reuse/cache fields = MEASURE, if exposed
```

None was measured in this task. Exact prompt-token matching is not resurrected as a selection rule.

## Claim ceiling

This artifact establishes only:

```text
B* is the unique canonical neutral realization selected by the
prospectively frozen minimum-ordinal rule from B_neutral^(v0.2),
and B* satisfies the already frozen source-level R2 admissibility rules.
```

It does not establish:

```text
behavioral neutrality
executor equivalence
token equality
prompt-work equality
control adequacy
causal identification
capability preservation
generation-work reduction
C_improve causality
White Rabbit
robustness across the full neutral family
execution evidence
```

```text
comparison against B* != comparison against all admissible neutral realizations
```

Any future Gate 7 result using `B*` is conditional on this prospectively selected canonical control.

## Forbidden operations and preserved non-events

This task did not:

```text
enumerate the full neutral family
materialize another candidate
hash another candidate
tokenize anything
contact llama-server
call /props
call /apply-template
call /tokenize
start the recorder
inspect prompt tokens or model-visible token sequences
generate output
run B*
run C
run Gate 7
create G7_MATCHED_CONTEXT_ASSAY_V0.2
modify the historical v0.1.1 assay
```

```text
N_scientific_runs = 0
```

## Frozen terminal state

```text
B_STAR_FROZEN
ORDINAL_1
SOURCE_ADMISSIBLE
EXECUTOR_UNMEASURED
NON_EXECUTING
```

The only authorized next edge is:

```text
B* FROZEN
    ->
STOP + REVIEW
```

A later, separately authorized task may constitute `G7_MATCHED_CONTEXT_ASSAY_V0.2`. This artifact does not create it, and no transition is automatic.

> **Select by constitution, not by behavior.**

> **Minimum ordinal is a convention, not an optimization.**

> **Freeze one control without looking at what the executor does with it.**

> **B* is canonical for this assay; it is not universal over neutral wording.**
