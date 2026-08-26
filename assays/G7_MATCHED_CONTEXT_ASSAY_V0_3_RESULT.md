# G7 Matched-Context Assay v0.3 Result

## CURRENT AUTHORITY

```text
HISTORICAL_LOCAL_OBSERVATION
PROSPECTIVE_EXECUTION_PROVENANCE_LIMIT
```

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

Historical result blob before this authority-surface update:

```text
518c30b7791bb57bf487182c7c88ddb9e8b995b9
```

Historical analyzer terminal:

```text
GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY
```

The numerical observation is preserved. Its prospective execution provenance is explicitly weaker
than later assay doctrine.

## Preserved local observation

Historical execution:

```text
30/30 scientific requests
30/30 historically admissible
capability success: 5/5 in B* and C for Q1/Q2/Q3
required-work censoring: not observed
```

Historical `N_generated` summaries:

| Task | B* values | B* mean | C values | C mean | C-B* |
| --- | --- | ---: | --- | ---: | ---: |
| Q1 | 105, 135, 115, 126, 113 | 118.8 | 104, 103, 118, 112, 108 | 109.0 | -9.8 |
| Q2 | 110, 77, 124, 86, 80 | 95.4 | 79, 96, 87, 85, 59 | 81.2 | -14.2 |
| Q3 | 145, 133, 113, 146, 155 | 138.4 | 91, 115, 106, 119, 99 | 106.0 | -32.4 |

Pooled historical means:

```text
B*: 117.53333333333333
C:   98.73333333333333
```

Prompt-token burden was equal within every task in this execution.

Raw/derived custody remains under:

`observations/G7-V0.3/`

## Provenance limitation

The third-pass audit confirmed that the local numerical observation survives, but the prospective
execution-authority chain is weaker than later doctrine.

Specifically:

```text
constitution said NOT_EXECUTED / REVIEW_REQUIRED
no intervening independent review artifact was frozen
no separate execution-authorization artifact was frozen
operational manifest: NONE
executor first appears with the result commit
```

The v0.3 identity path also did not establish the later invariant:

```text
H_frozen = H_materialized = H_executed
```

and the execution identity record did not independently hash-bind all concrete model/runtime/
tokenizer/template artifacts required by the later measurement doctrine.

No evidence currently shows that the wrong B*/C conditions actually ran. The limitation is that
identity/equality was not proved at the later required authority layer.

## Current use

This result may be cited as:

```text
strong local historical observation
+
weak prospective execution provenance
```

It may be used for target selection and context, with the provenance qualifier visible.

It must not be promoted to the authority of a fresh, prospectively reviewed, separately authorized
replication.

## Q2 replication boundary

A later fresh Q2 replication is described in research handoff/context, but this repository does not
currently contain a resolvable Q2 constitution/result/custody object.

Therefore:

```text
Q2_SOURCE_STATUS = SOURCE_UNRESOLVED_IN_THIS_REPOSITORY
```

The current Q1/Q3 successors do not treat Q2 as repository-verified evidence.

## Claim ceiling

This historical result does not establish:

- a general C effect;
- robust neutral-control independence;
- persistent adaptation or learning;
- `C_improve -> Phi`;
- whole-run compute reduction;
- lifecycle economics;
- compilation/amortization;
- White Rabbit.

Current authority map:

- `program/CURRENT_AUTHORITY_STATE.json`
- `assays/README.md`
