# Gate 7 Neutral-Control Robustness Assay v0.1.1 Result

Status: ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED

Parent constitution: 0b41a175fcf047ff3d0ec313cdb0e11485f12741
Verification correction: 90dbdadbbb5d2c974707787b83d865b72f6c599c

Original observations attempted: 105/105
Admissible: 105; inadmissible: 0; replacements: 0

Raw archive SHA-256: 1f7772de7754c754b6df37d227453e6e71d0dbe16f4ab17156971ca91a1f7617

## Frozen precedence

1. Completeness/admissibility: PASS
2. Panel control adequacy: PANEL_CONTROL_ADEQUACY_OBSERVED
3. C capability: CAPABILITY_NONREGRESSION_OBSERVED
4. Censoring: NO_REQUIRED_WORK_CENSORING_OBSERVED
5. Pairwise comparisons opened: YES

## Per-condition/task summaries

| Condition | Task | Values | Mean | Median | Min | Max |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| B0 | Q1 | [128, 138, 136, 135, 111] | 129.6 | 135 | 111 | 138 |
| B0 | Q2 | [48, 73, 79, 81, 92] | 74.6 | 79 | 48 | 92 |
| B0 | Q3 | [145, 103, 145, 127, 147] | 133.4 | 145 | 103 | 147 |
| B1 | Q1 | [104, 117, 108, 188, 147] | 132.8 | 117 | 104 | 188 |
| B1 | Q2 | [84, 113, 83, 109, 121] | 102 | 109 | 83 | 121 |
| B1 | Q3 | [146, 141, 85, 160, 128] | 132 | 141 | 85 | 160 |
| B2 | Q1 | [149, 196, 161, 154, 188] | 169.6 | 161 | 149 | 196 |
| B2 | Q2 | [75, 79, 115, 122, 85] | 95.2 | 85 | 75 | 122 |
| B2 | Q3 | [111, 154, 104, 119, 97] | 117 | 111 | 97 | 154 |
| B3 | Q1 | [109, 125, 122, 121, 200] | 135.4 | 122 | 109 | 200 |
| B3 | Q2 | [108, 107, 118, 77, 85] | 99 | 107 | 77 | 118 |
| B3 | Q3 | [110, 92, 123, 184, 111] | 124 | 111 | 92 | 184 |
| B4 | Q1 | [160, 186, 151, 121, 146] | 152.8 | 151 | 121 | 186 |
| B4 | Q2 | [78, 84, 92, 91, 126] | 94.2 | 91 | 78 | 126 |
| B4 | Q3 | [120, 113, 108, 87, 170] | 119.6 | 113 | 87 | 170 |
| B5 | Q1 | [110, 110, 170, 143, 115] | 129.6 | 115 | 110 | 170 |
| B5 | Q2 | [102, 110, 127, 101, 67] | 101.4 | 102 | 67 | 127 |
| B5 | Q3 | [115, 94, 133, 94, 173] | 121.8 | 115 | 94 | 173 |
| C | Q1 | [118, 113, 86, 104, 137] | 111.6 | 113 | 86 | 137 |
| C | Q2 | [185, 126, 147, 92, 78] | 125.6 | 126 | 78 | 185 |
| C | Q3 | [102, 98, 124, 127, 91] | 108.4 | 102 | 91 | 127 |

## Pairwise robustness

| Control | Task differences C-Bi | Pooled difference | PASS |
| --- | --- | ---: | --- |
| B0 | {'Q1': -18.0, 'Q2': 51.0, 'Q3': -25.0} | 2.6666666666666714 | FAIL |
| B1 | {'Q1': -21.200000000000017, 'Q2': 23.599999999999994, 'Q3': -23.599999999999994} | -7.066666666666663 | FAIL |
| B2 | {'Q1': -58.0, 'Q2': 30.39999999999999, 'Q3': -8.599999999999994} | -12.066666666666663 | FAIL |
| B3 | {'Q1': -23.80000000000001, 'Q2': 26.599999999999994, 'Q3': -15.599999999999994} | -4.266666666666666 | FAIL |
| B4 | {'Q1': -41.20000000000002, 'Q2': 31.39999999999999, 'Q3': -11.199999999999989} | -7.0 | FAIL |
| B5 | {'Q1': -18.0, 'Q2': 24.19999999999999, 'Q3': -13.399999999999991} | -2.3999999999999915 | FAIL |

K / 6: 0/6

## FINAL TERMINAL STATE

ROBUST_CONTROL_REALIZATION_ADVANTAGE_NOT_OBSERVED

All 105 observations are fresh. No historical observation was reused. Delta W_gen does not authorize Delta W_run or Delta C_H. No White Rabbit claim is emitted.

Literal secondary fields, run IDs, hashes, PIDs, and checks are in observations/G7-neutral-control-robustness-v0.1.1/derived-results.json. Missing fields remain missing.

## Claim ceiling

Any positive result is conditional on the exact six-control structural panel, frozen tasks, executor, cold-run protocol, and N_generated currency. It does not establish robustness across all 729 controls, a family-average effect, other tasks/models, persistent learning, whole-run compute reduction, lifecycle economics, or White Rabbit.
