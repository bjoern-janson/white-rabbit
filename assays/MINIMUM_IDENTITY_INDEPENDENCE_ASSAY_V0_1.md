# Minimum Identity Independence Assay v0.1

Version: `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1`

Status: `CONSTITUTED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Engineering observations executed under this constitution: `0`

This artifact constitutes a synthetic, non-model identity-evidence experiment. It does not authorize execution.

It does not modify Gate 7, Q1/Q2/Q3 replication constitutions, the White Rabbit conceptual freeze, or any scientific result.

## 1. Absolute scope

Primary question:

> **How much independent identity-evidence machinery is required, among the tested architectures, to preserve executed-object identity over a prospectively frozen family of critical mismatch cases?**

The experimental object is:

```text
identity-evidence architecture chi
    ->
critical identity-failure detectability
```

This assay is limited to executed-object identity evidence.

It does NOT authorize or establish:

- Q1, Q2, or Q3 execution;
- model inference of any kind;
- Gate 7 scientific execution;
- robustness-panel repair or rerun;
- semantic-validity challenge sufficiency (`G_C`);
- operative revision (`G_R`);
- general corrigibility;
- correctable compression;
- White Rabbit existence;
- amortization or compounding;
- mechanism claims;
- a universal theorem about independence.

The strongest possible result is contract-relative and architecture-relative.

## 2. Frozen oracle authority

The sole oracle fixture authority is:

`assays/MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0_1.json`

The oracle freezes:

- exact identity-bearing synthetic byte objects;
- exact SHA-256 values;
- two critical clean controls;
- four critical mismatch cases;
- three diagnostic cases;
- oracle mismatch truth;
- expected mismatch class.

The oracle must remain unavailable to every architecture under test during evaluation.

Architecture outputs must be finalized and hashed before the referee opens the oracle for scoring.

The experiment must not ask an architecture whether its own answer was correct.

```text
system under test
    !=
ground-truth authority
```

## 3. Synthetic identity domain

No scientific prompt, model request, B0, C, Q1, Q2, or Q3 object is used.

The identity domain consists only of the three frozen synthetic objects in the oracle:

```text
ALPHA
ALPHA_MUT
BETA
```

Each has exact frozen UTF-8 bytes and exact SHA-256 authority.

The experiment uses the three identity stages:

```text
H_f = frozen / constituted object identity
H_m = materialized / intended object identity
H_e = executed / externally observed object identity
```

Full identity is:

```text
H_f = H_m = H_e
```

The assay studies what evidence path is required to establish or reject that equality.

## 4. Independent variable

The only intended independent variable is the identity-evidence path `chi_i`.

Everything else must be common across architectures:

- synthetic object bytes;
- perturbation generation;
- case order;
- process/runtime environment;
- serialization;
- common terminal-state vocabulary;
- common referee;
- oracle truth;
- cost instrumentation;
- output schema;
- hash function;
- case identifiers.

No architecture may receive:

- a different fixture;
- a different perturbation;
- a different oracle;
- a different parser unless parser independence is itself the constituted difference;
- hidden ground-truth fields;
- extra retries;
- architecture-specific case repair.

## 5. Architecture ladder

The tested architectures are frozen as evidence-access contracts, not as assumed quality rankings.

### `chi_0` — self-report only

Available identity evidence:

- declared condition/object identifier;
- executor/self-reported identity state;
- convenience field such as `condition_identity_match` when present.

Unavailable:

- independent frozen/materialized comparison;
- independent raw executed-object custody;
- independent executed-byte hash recomputation.

`chi_0` may emit only from its allowed evidence. It may not open hidden fixture/oracle bytes.

### `chi_1` — independent preflight identity

Available identity evidence:

- frozen authority bytes/hash;
- materialized bytes/hash;
- independent computation of `H_f` and `H_m` before synthetic dispatch;
- declared object identifier and convenience metadata.

Unavailable:

- authoritative raw executed-object custody;
- independent `H_e` from the executed object.

If execution identity cannot be established from permitted evidence, `chi_1` must emit `IDENTITY_UNRESOLVED`, not silently substitute `H_m` for `H_e`.

### `chi_2` — independent raw custody with recorded executed identity

Available identity evidence:

- all `chi_1` evidence;
- externally persisted raw executed-object bytes;
- recorder/custody-layer reported executed-object hash or extracted identity;
- common comparison logic over `H_f`, `H_m`, and recorded `H_e`.

Constraint:

`chi_2` may trust the custody layer's reported/extracted `H_e` and does not independently recompute `H_e` from the raw bytes.

This is deliberate. It separates raw custody availability from independent recomputation.

### `chi_3` — raw custody plus independent recomputation

Available identity evidence:

- all raw custody available to `chi_2`;
- independent byte extraction from authoritative raw custody;
- independent SHA-256 recomputation from the extracted executed bytes;
- comparison against frozen authority and materialized identity without trusting convenience predicates or recorder-reported `H_e`.

The independent recomputation path must not call the same convenience predicate or merely copy the custody layer's claimed hash.

## 6. Common evaluator boundary

Architectures must use the same terminal vocabulary:

```text
IDENTITY_PASS
IDENTITY_MISMATCH
IDENTITY_UNRESOLVED
```

They may additionally emit a diagnostic mismatch class, but exact class attribution is secondary.

Primary scoring asks only whether the architecture correctly distinguishes:

```text
mismatch
vs
clean identity
```

`IDENTITY_UNRESOLVED` is conservative but does not count as successful detection or successful clean admission for the primary sufficiency gate.

This prevents an architecture from passing merely by refusing every case.

Likewise, an architecture that always emits `IDENTITY_MISMATCH` fails the critical clean controls.

## 7. Frozen critical cases

The critical contract contains two kinds of cases.

### Critical clean controls

The architecture must correctly accept:

```text
C0_ALPHA_CLEAN
C1_BETA_CLEAN
```

These exist specifically to prevent the trivial always-reject detector from satisfying the assay.

### Critical mismatch cases

The architecture must detect all four:

```text
E1_FROZEN_MATERIALIZED_MISMATCH
E2_MATERIALIZED_EXECUTED_MISMATCH
E3_CROSS_OBJECT_SUBSTITUTION
E4_LYING_CONVENIENCE_PREDICATE
```

Their exact frozen bytes, hashes, metadata, and oracle relations are defined only by the oracle manifest.

No additional critical case may be added after execution begins.

No critical case may be downgraded after observing results.

## 8. Diagnostic cases

The oracle also freezes three non-gating diagnostic cases:

```text
D1_MISSING_CONVENIENCE_FIELD
D2_IRRELEVANT_METADATA_CHANGE
D3_CORRUPTED_RECORDED_HASH_RAW_BYTES_CLEAN
```

Diagnostic performance must be reported but does not determine critical contract sufficiency in v0.1.

This prevents the architecture from being driven by an unbounded parser-torture corpus.

A future assay may promote a diagnostic case to critical only prospectively in a successor constitution.

## 9. Case generation and hidden ground truth

For each frozen case, a common synthetic harness constructs:

```text
X_frozen
X_materialized
X_actual
```

according to the oracle manifest.

The harness maintains ground truth outside the architecture evidence path.

Architecture-specific views are generated only after the actual synthetic object is fixed.

The clean causal graph is:

```text
frozen case
    -> synthetic actual object
    -> architecture-specific evidence view chi_i
    -> architecture terminal classification
```

Separately:

```text
frozen oracle
    -> referee
```

Only after all architecture outputs for the case are frozen may the referee compare architecture output to oracle truth.

## 10. Primary detection score

For architecture `chi_i` and critical case `k`, define:

```text
D(i,k) = 1
```

iff:

- oracle says mismatch and architecture emits `IDENTITY_MISMATCH`; or
- oracle says clean and architecture emits `IDENTITY_PASS`.

Otherwise:

```text
D(i,k) = 0
```

including `IDENTITY_UNRESOLVED`.

Exact failure-class agreement is reported separately and does not substitute for primary correctness.

## 11. Critical sufficiency gate

Architecture `chi_i` is contract-sufficient iff:

```text
D(i,k) = 1
for every critical clean control and every critical mismatch case.
```

Equivalently:

```text
all critical mismatches detected
AND
all critical clean controls accepted
```

There is no averaging away a missed critical case.

A 5/6 or otherwise incomplete critical result is insufficient regardless of diagnostic performance.

## 12. Detection matrix

The primary result artifact must report the literal matrix:

| architecture | C0 | C1 | E1 | E2 | E3 | E4 | critical sufficient |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `chi_0` | ? | ? | ? | ? | ? | ? | ? |
| `chi_1` | ? | ? | ? | ? | ? | ? | ? |
| `chi_2` | ? | ? | ? | ? | ? | ? | ? |
| `chi_3` | ? | ? | ? | ? | ? | ? | ? |

Diagnostic cases must be reported in a separate matrix and cannot change the critical-sufficiency state.

## 13. Cost ledger

Cost is measured only after critical detection outputs are frozen.

Do not define a synthetic scalar called `independence cost`.

Record literal architecture-specific quantities over the same constituted case horizon, including where available:

```text
bytes of authoritative evidence persisted
number of persisted evidence artifacts
SHA-256 computations
independent parse/extraction operations
identity comparisons
process/runtime elapsed time
CPU time if authoritatively exposed
peak or total storage bytes where available
```

Oracle-generation and referee costs are experiment scaffolding and must be reported separately from architecture cost because every architecture shares them.

Missing cost fields remain missing.

Do not infer FLOPs, dollars, energy, or lifecycle economics from these measurements.

## 14. No invented scalarization

This constitution freezes no weighting function over cost dimensions.

Among critically sufficient architectures, report componentwise dominance and the Pareto set.

A unique `least costly tested architecture` may be emitted only if one critically sufficient architecture weakly dominates every other critically sufficient architecture across all frozen primary cost dimensions and strictly improves at least one dimension.

Otherwise emit the Pareto set without forcing a total ranking.

## 15. Result states

Permitted terminal states include:

```text
NO_TESTED_ARCHITECTURE_CRITICALLY_SUFFICIENT

CRITICAL_IDENTITY_SUFFICIENCY_OBSERVED_FOR_SUBSET

UNIQUE_MINIMUM_TESTED_IDENTITY_ARCHITECTURE_OBSERVED

IDENTITY_ARCHITECTURE_PARETO_SET_REPORTED

ASSAY_INCOMPLETE
```

The exact detection matrix and literal cost ledger are primary. Terminal labels summarize; they do not replace the data.

## 16. Execution order

Use deterministic case-major order:

```text
C0: chi_0, chi_1, chi_2, chi_3
C1: chi_0, chi_1, chi_2, chi_3
E1: chi_0, chi_1, chi_2, chi_3
E2: chi_0, chi_1, chi_2, chi_3
E3: chi_0, chi_1, chi_2, chi_3
E4: chi_0, chi_1, chi_2, chi_3
D1: chi_0, chi_1, chi_2, chi_3
D2: chi_0, chi_1, chi_2, chi_3
D3: chi_0, chi_1, chi_2, chi_3
```

Total constituted architecture-case evaluations:

```text
9 cases x 4 architectures = 36 evaluations
```

Because this is a deterministic synthetic identity assay, no outcome-conditioned repetitions, replacements, or sample-size extensions are constituted.

If an evaluation is operationally incomplete, preserve it as incomplete and stop for separate review rather than silently retrying until a desired matrix is obtained.

## 17. Implementation firewall

Before execution authorization, independent review must verify that the four implementations differ only in their constituted identity-evidence path.

The review must reject implementations that accidentally vary:

- fixture bytes;
- oracle access;
- failure injection;
- serialization;
- case ordering;
- output semantics;
- runtime environment;
- hidden state;
- common comparison semantics, except where independent recomputation is the explicit `chi_3` treatment.

The oracle path must not be readable by architecture code during evaluation.

The architecture code must not branch on case IDs to produce expected answers.

## 18. Historical Gate 7 relation

Gate 7 motivates the failure family but supplies no observations to this assay.

The motivating pattern is the distinction between:

```text
constituted identity
materialized identity
executed identity
```

and the requirement that executed identity not be inferred merely from intended/materialized identity.

No historical B4/B5 row is replayed or counted as an assay observation.

This v0.1 experiment uses synthetic identity fixtures only.

Therefore:

```text
Gate 7 motivation
    !=
Gate 7 sample reuse
```

## 19. Claim ceiling

A successful result may establish at most a statement of the form:

> For the prospectively frozen v0.1 identity case contract, the specified tested architecture(s) correctly distinguished every critical mismatch from every critical clean control, with the reported literal evidence-cost vector.

If a unique componentwise cost minimum exists among critically sufficient architectures, the result may additionally state:

> Among the tested v0.1 architectures and frozen cost dimensions, `chi_k` was the unique componentwise minimum architecture satisfying the critical identity contract.

The assay does NOT establish:

```text
universal identity sufficiency
minimum independence in all systems
semantic challenge sufficiency
operative corrigibility
correctable compression
White Rabbit
amortization
compounding
```

## 20. Review requirements

Independent review must verify before any execution authorization:

1. exact oracle file bytes and blob identity;
2. exact synthetic object bytes and SHA-256 values;
3. exact critical-clean / critical-failure / diagnostic partition;
4. exact `chi_0..chi_3` evidence contracts;
5. oracle non-availability to architectures;
6. common harness equality outside the evidence-path treatment;
7. primary `D(i,k)` scoring rule;
8. anti-triviality controls against always-pass and always-fail strategies;
9. deterministic 36-evaluation order;
10. cost ledger and no-scalarization rule;
11. claim ceiling;
12. no model inference and no Gate 7 scientific execution.

## 21. Stop rule

This constitution authorizes no execution.

Do not implement and run the 36 evaluations merely because this document exists.

Next permitted action:

```text
INDEPENDENT CONSTITUTION + ORACLE REVIEW
```

After review, any execution requires separate explicit authorization.

## Terminal constitution state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1

status:
CONSTITUTED
NOT_EXECUTED
REVIEW_REQUIRED
NON_AUTHORIZING

oracle:
MINIMUM_IDENTITY_INDEPENDENCE_ORACLE_V0.1

model inference:
0

Gate 7 scientific observations:
0

critical clean controls:
2

critical mismatch cases:
4

diagnostic cases:
3

architectures:
4

constituted evaluations:
36

next action:
INDEPENDENT REVIEW ONLY
```

> **Do not test corrigibility in the abstract. First measure how much independent machinery is required to keep one authority-bearing distinction recoverable.**
