# Gate 7 Neutral-Control Reconstitution Contract v0.1

Version: `G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.1`

Status: `CONSTITUTED / SEARCH_NOT_AUTHORIZED / ASSAY_BLOCKED / NON_AUTHORIZING`

Parent repository state: `e1a682275338a5792d0918e51bf217fa99cb6e2a`

```text
N_scientific_runs = 0
```

This document constitutes rules for a possible future token-only neutral-control search. It does not authorize or report that search, select a successor control, revise the Gate 7 assay, or authorize scientific execution.

```text
CONTROL_RECONSTITUTED
    !=
PREOPEN_TOKEN_MATCH_MATCH
    !=
EXECUTION_AUTHORIZED
```

## Governing purpose

> **Match the computational burden without optimizing the semantic control.**

The future search objective is exclusively to find a source-admissible `B1` in the finite family `B_neutral` such that:

```text
N_prompt(B1, Q1) = N_prompt(C, Q1)
AND
N_prompt(B1, Q2) = N_prompt(C, Q2)
AND
N_prompt(B1, Q3) = N_prompt(C, Q3)
```

The future selection procedure may use only:

```text
candidate source text
frozen structural properties
exact native chat-template rendering
rendered bytes
token IDs
token pieces, diagnostically
token counts
deterministic source-derived quantities
```

It may not use generated tokens, assistant responses, task success, capability, `N_generated`, generation or total inference latency, reasoning content, response quality, work-reduction outcomes, or any Gate 7 dependent variable.

Procedural independence principle:

> **`B1` must be constituted without access to `Y_assay`.**

This is a procedural firewall. This contract does not claim formal probabilistic independence.

## Authority and historical boundary

The immutable historical chain is:

```text
G7_MATCHED_CONTEXT_ASSAY_V0.1.1
    ->
G7_PREOPEN_TOKEN_MATCH_V0.1
    ->
PREOPEN_TOKEN_MATCH_MISMATCH / ASSAY_BLOCKED
```

Historical artifacts:

```text
assays/G7_MATCHED_CONTEXT_ASSAY_V0_1.md
assays/G7_PREOPEN_TOKEN_MATCH_V0_1.md
assays/G7_PREOPEN_TOKEN_MATCH_V0_1.json
```

They remain immutable. The earned result is only:

```text
equal source/rendered byte burden
    does not imply
equal prompt-token burden
```

under the frozen executor realization used by `G7_PREOPEN_TOKEN_MATCH_V0.1`. This is not a universal claim about all executors and is not a `C_improve` result.

## Immutable scientific objects

No future operation under this contract may modify:

```text
literal C_improve prelude or its SHA-256
Q1, Q2, or Q3 target or target SHA-256
separator
message role or message count
chat-template semantics
tokenizer
llama.cpp build or commit
model or model alias
GPU-layer, context-size, parallel-slot, Jinja, or reasoning-format configuration
request envelope
max_tokens = 64
mechanical grader
capability adequacy rule
capability non-regression rule
work-censoring rule
result-state precedence
n = 5 per condition per task
cold-independence criterion
primary work currency N_generated
scientific claim ceiling
```

Only a new neutral prelude may eventually be selected. That selection creates a new object; it never edits the historical control in place.

Frozen source and runtime identities remain:

```text
C_improve UTF-8 SHA-256: 62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a
Q1 UTF-8 SHA-256: eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23
Q2 UTF-8 SHA-256: 3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1
Q3 UTF-8 SHA-256: 886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400
separator UTF-8 SHA-256: 7f31dacfc61dd598296a31789337fd1886023536222243b43e16a914886bf5f4
llama.cpp build / commit: b10603 / c060ca974
model: Qwen3.8-27B-Q2_K.gguf
model alias: qwen38-27b
Jinja: enabled
reasoning format: deepseek
```

The future request remains one `user` message, `stream: false`, `max_tokens: 64`, and no sampling overrides, using the exact compact request envelope frozen in `G7_MATCHED_CONTEXT_ASSAY_V0.1.1`.

## Historical control B0

The original neutral control is frozen as `B0`, excluding code-fence delimiters, with LF line endings and no trailing LF:

```text
reference pattern: X ∝ Y_reference

where:

Y_reference = label for a static descriptive sequence, reference
   ↓
plain descriptive statement
   ↓
fixed reference notation
   ↓
ordinary descriptive sequence
   ↓
expanded neutral reference example
```

Custody:

```text
Unicode code points: 246
UTF-8 bytes: 256
UTF-8 SHA-256: af2d192d9ce44c51190455b3434b55e0c676c9630c6a17af5d33d6c0d94f3a51
```

`B0` remains immutable historical evidence. It may occur as one member of the constituted source grammar, but it may never be overwritten, relabeled as matched, or silently transformed into `B1`.

Frozen lineage:

```text
B0
    ->
PREOPEN_TOKEN_MATCH_MISMATCH
    ->
separately constituted reconstitution search
    ->
possible B1
```

Forbidden lineage: `B0 corrected into B1`.

Any future `B1` must receive its own exact text, UTF-8 SHA-256, measurements, provenance, and status.

## Closed family B_neutral

`B_neutral` is the finite set produced by the exact structural template and lexical option sets below, followed by the frozen source-admissibility filter. There is no free-text slot and no authority to add an option during or after token inspection.

### Fixed structural template

The placeholders are whole-line lexical slots. Every other character is fixed. The rendered candidate contains exactly the following 13 lines, joined by LF, with no trailing LF:

```text
{L1}

where:

{L5}
   ↓
{L7}
   ↓
{L9}
   ↓
{L11}
   ↓
{L13}
```

The literals `X`, `Y_reference`, `where:`, `∝`, and `↓` are preserved. Arrow lines contain exactly three ASCII spaces followed by `↓`.

### Lexical option set L1

Select exactly one whole line, in this frozen order:

```text
L1[0] = reference pattern: X ∝ Y_reference
L1[1] = reference relation: X ∝ Y_reference
L1[2] = reference mapping: X ∝ Y_reference
L1[3] = descriptive pattern: X ∝ Y_reference
L1[4] = static pattern: X ∝ Y_reference
```

### Lexical option set L5

Select exactly one whole line, in this frozen order:

```text
L5[0] = Y_reference = label for a static descriptive sequence, reference
L5[1] = Y_reference = marker for a fixed descriptive series, reference
L5[2] = Y_reference = name for an ordinary descriptive sequence, reference
L5[3] = Y_reference = symbol for a static reference series, reference
L5[4] = Y_reference = label for a fixed neutral sequence, reference
```

### Lexical option set L7

Select exactly one whole line, in this frozen order:

```text
L7[0] = plain descriptive statement
L7[1] = simple descriptive statement
L7[2] = plain reference statement
L7[3] = ordinary descriptive entry
L7[4] = neutral reference statement
```

### Lexical option set L9

Select exactly one whole line, in this frozen order:

```text
L9[0] = fixed reference notation
L9[1] = static reference notation
L9[2] = fixed descriptive notation
L9[3] = ordinary reference notation
L9[4] = neutral reference notation
```

### Lexical option set L11

Select exactly one whole line, in this frozen order:

```text
L11[0] = ordinary descriptive sequence
L11[1] = plain descriptive sequence
L11[2] = ordinary reference sequence
L11[3] = static descriptive sequence
L11[4] = neutral descriptive sequence
```

### Lexical option set L13

Select exactly one whole line, in this frozen order:

```text
L13[0] = expanded neutral reference example
L13[1] = extended neutral reference example
L13[2] = expanded static reference example
L13[3] = detailed neutral reference example
L13[4] = complete neutral reference example
```

### Theoretical family size

Before source filtering:

```text
|L1| × |L5| × |L7| × |L9| × |L11| × |L13|
= 5 × 5 × 5 × 5 × 5 × 5
= 15,625 theoretical candidates
```

This formula constitutes the family without materializing its Cartesian product. The actual candidate list, surviving count, hashes, or tokenization may be materialized only by a separately authorized search.

The family is intentionally restricted to ordinary static descriptive and reference language. That restriction is a frozen control-design assumption, not a scientific proof of semantic neutrality.

## Forbidden vocabulary

Every constructed candidate is checked after deterministic ASCII case folding: map `A`-`Z` (`U+0041`-`U+005A`) to `a`-`z` by adding 32; leave every other code point unchanged. No Unicode normalization is performed.

If the folded candidate contains any frozen substring below, it is mechanically inadmissible:

```text
c_improve
c-improve
improve
feedback
adapt
viability
future
representation
mechanism
learn
optim
reason
strategy
solve
capability
rabbit
corrig
efficient
compute
self-improv
metacogn
treatment
```

No human or LLM judgment may waive this filter. The finite lexical option sets are independently binding; passing the substring filter cannot authorize words outside those sets.

## Source-level admissibility

A future candidate `B_k` is source-admissible only if all requirements below pass mechanically:

1. It is a Unicode scalar-value sequence that encodes as valid UTF-8.
2. Its UTF-8 representation contains no BOM.
3. It uses LF line endings only, with no CR.
4. It has no trailing LF.
5. Splitting on LF yields exactly 13 lines.
6. Splitting on the exact delimiter `"\n\n"` yields exactly three non-empty blocks.
7. It contains exactly one `∝` code point.
8. Exactly four lines equal three ASCII spaces followed by `↓`.
9. It contains exactly one literal `where:` line.
10. It contains the literals `X` and `Y_reference` only in their positions fixed by the selected `L1` and `L5` options.
11. It is constructed from exactly one option from each frozen lexical set and the fixed structural template; no other character is present.
12. It contains none of the frozen forbidden substrings under the exact folding rule.
13. It contains none of the complete literal Q1, Q2, or Q3 target strings.
14. It contains none of the frozen expected-answer strings `486`, `9R2m7Q`, or `-4, 0, 9, 12, 17`.
15. It contains no literal `C_improve` substring under the folding rule.
16. It contains no White Rabbit terminology; the required `rabbit` filter is mechanically decisive for that phrase.
17. In future request construction it occupies the same sole-user-message prelude position and uses the unchanged frozen separator and target.

The `B0` Unicode code-point count and UTF-8 byte count are recorded for every candidate as diagnostic source-derived quantities. Equality to `B0` on either dimension is preferred only through the deterministic tie-break below and is **not mandatory** for membership in `B_neutral`.

```text
source-length equality: DESCRIPTIVE / NON-MANDATORY
executor prompt-token equality: FUTURE SELECTION CRITERION
```

No later fallback may relax or strengthen this source-length decision after candidate tokenization is observed.

## Deterministic future enumeration

The possible future search must execute these phases in order. This document defines them but does not execute them.

### Phase A — source-family materialization

1. Verify the contract file identity and the immutable `B0`, C, separator, and Q1-Q3 source hashes before construction.
2. Iterate the Cartesian product in tuple order `(i1, i5, i7, i9, i11, i13)`, where every index ranges from `0` through `4`, `i1` is the outermost loop, and `i13` varies fastest.
3. Assign the one-based theoretical product position:

```text
product_index = (((((i1 × 5 + i5) × 5 + i7) × 5 + i9) × 5 + i11) × 5 + i13) + 1
```

4. Construct the exact text from the fixed template and selected whole-line options.
5. Apply every source-admissibility rule.
6. Preserve every rejection with `product_index` and the complete set of mechanical rejection codes; do not tokenize rejected text.
7. Assign each surviving candidate a one-based `candidate_index` in encounter order.
8. For every survivor record exact source text, option-index tuple, `product_index`, `candidate_index`, UTF-8 SHA-256, Unicode code-point count, UTF-8 byte count, and differences from `B0` for the latter two counts.
9. Complete all 15,625 theoretical product positions. Early stopping is forbidden.
10. Freeze the complete source manifest and its UTF-8 SHA-256 before any template rendering or tokenization begins.

No candidate may be invented, edited, removed, reordered, or relabeled after Phase A is frozen. The future implementation must document and test its Unicode-scalar counting, UTF-8 encoding, hashing, structural checks, folding rule, and Cartesian-order implementation.

### Phase B — exact token-only search

Only after separate authorization and Phase A freeze, pass every source-admissible candidate to the exact native non-generating pipeline frozen by Gate 7:

```text
candidate source
    -> exact frozen message assembly
    -> exact frozen native Jinja chat-template rendering
    -> exact frozen GGUF tokenizer
    -> token IDs/count custody
```

For every candidate construct exactly:

```text
B_k + "\n\n--- TARGET ---\n" + Q1
B_k + "\n\n--- TARGET ---\n" + Q2
B_k + "\n\n--- TARGET ---\n" + Q3
```

The runtime identity remains:

```text
llama.cpp build: b10603
llama.cpp commit: c060ca974
model: Qwen3.8-27B-Q2_K.gguf
model alias: qwen38-27b
GPU layers: 50
context size: 8192
parallel slots: 1
Jinja: enabled
reasoning format: deepseek
message count: 1
role: user
stream: false
max_tokens: 64
sampling overrides: absent
```

The future operation must re-establish exact executable, model, template, tokenizer, special-token, BOS/EOS, and generation-prompt custody. It must preserve rendered prompt bytes/hashes, token IDs, canonical token-sequence hashes, and total prompt-token counts for every source-admissible candidate/task context.

A candidate enters the exact-match set if and only if:

```text
N_prompt(B_k, Q1) = N_prompt(C, Q1)
AND
N_prompt(B_k, Q2) = N_prompt(C, Q2)
AND
N_prompt(B_k, Q3) = N_prompt(C, Q3)
```

There is no averaging, tolerance, `±1` rule, offset correction, padding, early stop, or task tradeoff.

## No-generation firewall

The future search is prohibited from invoking:

```text
/v1/chat/completions
/completion
any generation or completion endpoint
decoder generation
token sampling
assistant output
response grading
N_generated observation
latency comparison
White Rabbit Recorder
```

Only exact native non-generating template/tokenizer inspection may be separately authorized. If the exact native path cannot be established without generation, the terminal state is `RECONSTITUTION_UNDETERMINABLE`; approximation is forbidden.

## Deterministic tie-break

If the exact-match set contains more than one candidate, rank the entire set by this ascending tuple:

```text
1. Unicode Levenshtein edit distance from B0
2. absolute UTF-8 byte-length difference from B0
3. absolute Unicode code-point-count difference from B0
4. UTF-8 byte sequence in lexicographic ascending order
5. UTF-8 SHA-256 as the final deterministic identifier
```

Levenshtein distance is defined over the unnormalized Unicode scalar/code-point sequence. Allowed operations are insertion, deletion, and substitution, each with unit cost `1`. No transposition operation exists. No normalization or case folding is applied for distance.

UTF-8 lexicographic ordering compares unsigned bytes from left to right; at the first difference, the lower byte sorts first; if one byte sequence is an exact prefix of another, the shorter sequence sorts first. SHA-256 is lowercase hexadecimal and serves as the final recorded identifier. No semantic preference may override this ranking after token counts are known.

The future implementation must include deterministic tests for the Levenshtein definition and ranking order before selection.

## Future terminal states

Exactly one future search terminal state must be emitted.

### `CONTROL_RECONSTITUTED`

Emit only if the complete frozen source family was mechanically materialized; every source-admissible candidate was processed by the exact native token-only pipeline; at least one candidate matched C token count exactly on Q1, Q2, and Q3; the deterministic tie-break selected exactly one `B1`; its source, hash, token custody, and lineage were frozen; and no generation occurred.

This state means only that the predeclared selection procedure produced a candidate control. It does not establish an independently certified token match and does not authorize Gate 7 execution.

### `NO_ADMISSIBLE_TOKEN_MATCH`

Emit only if the complete exact search processed every source-admissible candidate and none matched C token count on all three tasks. This blocks the current reconstitution lane. It does not authorize family expansion or relaxed matching inside the completed search.

### `RECONSTITUTION_UNDETERMINABLE`

Emit if the frozen family or search cannot be mechanically completed, custody is ambiguous, or exact native template/tokenizer equivalence cannot be established without generation. This blocks the lane. Uncertainty may not be resolved by approximation or judgment.

## Search is not certification

```text
CONTROL_RECONSTITUTED
    !=
PREOPEN_TOKEN_MATCH_MATCH
```

The search that selects `B1` is not its independent certification. If `CONTROL_RECONSTITUTED` is reached, the only possible lineage is:

```text
B1 exact source and SHA-256 frozen
    ->
G7 v0.1.2 may be separately constituted
    ->
a new independent native PREOPEN_TOKEN_MATCH may be separately authorized
    ->
MATCH | MISMATCH | UNDETERMINABLE
    ->
STOP
```

None of those arrows is authorized by this contract.

## Possible G7 v0.1.2 lineage

If a `B1` is eventually selected, a separately constituted assay revision must preserve:

```text
G7 v0.1.1
    ->
PREOPEN_TOKEN_MATCH_MISMATCH
    ->
neutral-control reconstitution
    ->
B1 frozen
    ->
G7 v0.1.2
```

`G7 v0.1.2` would be a new control design. It would not be a corrected historical v0.1.1, evidence that v0.1.1 matched, an assay result, or execution authorization. The historical artifacts remain untouched.

## Provenance requirements for a future search

Any separately authorized search must preserve at minimum:

```text
contract path, version, commit, and file SHA-256
implementation path, version, commit, and file hashes
exact runtime executable, model, template, and tokenizer custody
all exact commands and process purposes
Phase A complete source manifest and manifest SHA-256
all theoretical-product rejections and mechanical reasons
all source-admissible candidate records
all three rendered/tokenized contexts per source-admissible candidate
exact-match set
complete deterministic ranking values
selected B1, if any
terminal state and mechanically sufficient evidence
zero-generation attestation
```

Candidate-family materialization and token-only search must remain distinguishable provenance phases. Search results may not retroactively mutate this contract.

## Claim ceiling

This contract establishes only:

> **A predeclared finite procedure for constructing a token-matched neutral-control candidate without access to Gate 7 assay outcomes.**

It does not establish that `B1` exists, that token matching is achievable, that B and C are semantically equivalent, that the control is scientifically adequate, that `C_improve` has an effect, capability preservation, work reduction, White Rabbit, amortization, reuse, revocability, or transfer.

```text
N_scientific_runs = 0
candidate enumeration executed = NO
tokenization executed = NO
B1 selected = NO
G7 v0.1.2 created = NO
Gate 7 execution authorized = NO
```

## Current stop state

```text
G7_PREOPEN_TOKEN_MATCH_V0.1: MISMATCH / FROZEN / ASSAY_BLOCKED
G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.1: CONSTITUTED / SEARCH_NOT_AUTHORIZED
Gate 7 scientific execution: NOT AUTHORIZED / NOT OPENED
N_scientific_runs: 0
```

The next possible transition is only:

```text
review reconstitution contract
    ->
separately authorize token-only neutral-control search
    ->
STOP
```

> **Freeze the search space before searching it.**

> **Selection may see tokens. Selection may never see outcomes.**

> **Reconstitution is not certification. Certification is not execution.**
