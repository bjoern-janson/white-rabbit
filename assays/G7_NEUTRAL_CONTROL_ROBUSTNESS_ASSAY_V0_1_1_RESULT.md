# Gate 7 Neutral-Control Robustness Assay v0.1.1 Result

## CURRENT SCIENTIFIC AUTHORITY

```text
PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN
HISTORICAL_RESULT_PRESERVED
CURRENT_USE = DIAGNOSTIC / TARGET_SELECTION / FORENSIC ONLY
```

Authority checkpoint: `WR_AUTHORITY_2026_08_26_V1`

Historical result blob before authority withdrawal notice:

```text
b2863253d355d9aee40c2f7cbbca16506114749b
```

The historical analyzer output was:

```text
ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED
```

That terminal is **not a current panel-level scientific conclusion**.

## Why authority was withdrawn

The panel's B4/B5 condition identity failed at the constituted-object boundary.

The frozen tuple/hash authority and the displayed “exact source” disagreed about Stage-3 wording.
The executor followed the displayed source branch, so for B4/B5:

```text
H_executed != H_frozen
```

This invalidates panel-level scientific authority even though the observations themselves remain
preserved.

The relevant general lesson is:

```text
marginal lexical balance != exact condition identity
```

## Historical execution snapshot

The historical execution remains preserved as data:

```text
original observations attempted: 105/105
historically classified admissible: 105
replacements: 0
historical panel control adequacy: OBSERVED
historical C capability non-regression: OBSERVED
historical censoring state: NO_REQUIRED_WORK_CENSORING_OBSERVED
historical K / 6: 0/6
```

Historical per-task means:

| Condition | Q1 | Q2 | Q3 |
| --- | ---: | ---: | ---: |
| B0 | 129.6 | 74.6 | 133.4 |
| B1 | 132.8 | 102.0 | 132.0 |
| B2 | 169.6 | 95.2 | 117.0 |
| B3 | 135.4 | 99.0 | 124.0 |
| B4 | 152.8 | 94.2 | 119.6 |
| B5 | 129.6 | 101.4 | 121.8 |
| C | 111.6 | 125.6 | 108.4 |

B0 diagnostic differences `C-B0`:

```text
Q1: -18.0
Q2: +51.0
Q3: -25.0
```

These values may be used for target selection/diagnosis. They are not evidence of a valid six-control
robustness comparison because panel identity was not established.

## Raw custody

Historical observation directory:

`observations/G7-neutral-control-robustness-v0.1.1/`

The committed historical raw-custody checksum is preserved. The third-pass audit found no evidence
that the currently committed archive drifted.

However, the historical analyzer's archive builder is non-idempotent under rerun because it can
recursively ingest previously generated derived artifacts and archive metadata is not normalized.

Therefore:

```text
DO NOT REGENERATE RAW CUSTODY WITH tools/g7_analyze_robustness_v011.py
```

Deterministic engineering successor:

`tools/g7_analyze_robustness_v012.py`

The successor does not restore panel scientific authority; it only repairs future archive-generation
semantics.

## Current claim ceiling

The robustness panel currently establishes **no** valid panel-level conclusion about whether the C
realization advantage is robust across the six controls.

It does not establish:

- robust generation-work reduction;
- robust absence of generation-work reduction;
- family-average effects;
- whole-run compute reduction;
- lifecycle economics;
- White Rabbit.

## Authority propagation

This file is intentionally a current authority surface rather than a silent copy of the historical
terminal.

```text
new evidence
-> panel authority withdrawn
-> rendered result updated
```

See:

- `program/AUTHORITY_PROPAGATION_INVENTORY_V0_1.md`
- `program/CURRENT_AUTHORITY_STATE.json`
