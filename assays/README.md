# Assay Authority Index

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

This index reports **current authority**, not merely historical filenames.

| Artifact / lane | Current authority | Execution |
| --- | --- | --- |
| G7 v0.3 matched-context result | `HISTORICAL_LOCAL_OBSERVATION / PROSPECTIVE_EXECUTION_PROVENANCE_LIMIT` | historical execution only |
| G7 neutral-control robustness v0.1.1 | `PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN` | no new execution authorized |
| Q2 replication source | `SOURCE_UNRESOLVED_IN_THIS_REPOSITORY` | none |
| Q1 replication v0.1.1 | `CONSTITUTED / REVIEW_REQUIRED / NON_AUTHORIZING` | `authorized=false` |
| Q3 replication v0.1.1 | `CONSTITUTED / REVIEW_REQUIRED / NON_AUTHORIZING` | `authorized=false` |
| MII v0.1.4 | `IMPLEMENTATION_REVIEW_PASS` | scientific assay `authorized=false`, `N_assay=0` |

## Current pointers

### G7 v0.3

Current result surface:

`G7_MATCHED_CONTEXT_ASSAY_V0_3_RESULT.md`

The historical generation-work reduction remains a local observation. The current surface records its
prospective execution-provenance limit.

### Robustness

Current result surface:

`G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md`

Panel-level scientific authority is withdrawn because B4/B5 did not preserve exact constituted
condition identity.

### Q1 / Q3

Historical parents:

```text
G7_Q1_REPLICATION_ASSAY_V0_1.md
G7_Q3_REPLICATION_ASSAY_V0_1.md
```

Current effective successors:

```text
G7_Q1_REPLICATION_ASSAY_V0_1_1.md
G7_Q3_REPLICATION_ASSAY_V0_1_1.md
```

The successors override only the unresolved Q2 provenance premise and its sample-size justification.
No scientific observations exist under either Q1/Q3 constitution.

### MII

Implementation runtime review:

`MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_12_RUNTIME_REVIEW.md`

Current:

```text
IMPLEMENTATION_REVIEW_PASS
122/122 non-assay conformance tests PASS
N_assay=0
scientific execution authorized=false
```

## Rule

```text
historical result != current authority
```

When a later correction changes an artifact's authority, use this index and
`../program/CURRENT_AUTHORITY_STATE.json` before treating a historical terminal as current.
