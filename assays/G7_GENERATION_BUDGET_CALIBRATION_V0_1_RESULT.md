# G7 Generation-Budget Calibration v0.1 Result

Status: `GENERATION_BUDGET_CALIBRATION_PASS`

Calibration constitution commit: `23cd33dad0fad7e91d1a9ebe06e7cf0f28c33c99`

Canonical B* SHA-256: `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663`

Raw custody: `observations/G7-generation-budget-calibration-v0.1/`

Raw-custody archive SHA-256: `d72f900b06f9d08f751828cd21b66952f9b061f587da3cee8456a9f296d1069d`

## Frozen executor identity

- llama.cpp: build `b10603`, commit `c060ca974`
- model: `Qwen3.8-27B-Q2_K.gguf`; alias `qwen38-27b`
- GPU layers: `50`; context size: `8192`; parallel slots: `1`
- Jinja: enabled; reasoning format: `deepseek`
- backend: `127.0.0.2:8086`; recorder: `127.0.0.1:8085`
- recorder: `v0.1.0`, commit `80cddb26a7b851d218f95317cd3c5b0593acd831`
- stream: `false`; sampling overrides: absent
- `max_tokens`: `512`

## Execution accounting

- Planned observations: `15`
- Original observations attempted: `15`
- Calibration requests issued: `15`
- Admissible observations: `15`
- Inadmissible observations: `0`
- Replacement observations: `0`
- Condition C executed: `NO`

## Per-run evidence

| Run | Rep | Task | Adm | Success | N_prompt | N_prompt,new | N_generated | finish | T_prompt ms | T_gen ms | T_total ms | graphs_reused | f_sim_best | f_keep | cached tokens | failure reason |
| ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 01 | 1 | Q1 | YES | 1 | 142 | 142 | 143 | stop | 21622.55 | 47432.32 | 69054.88 | 141 | MISSING | MISSING | MISSING | MISSING |
| 02 | 1 | Q2 | YES | 1 | 135 | 135 | 78 | stop | 22461.94 | 25964.46 | 48426.4 | 77 | MISSING | MISSING | MISSING | MISSING |
| 03 | 1 | Q3 | YES | 1 | 153 | 153 | 135 | stop | 22815.63 | 44044.07 | 66859.7 | 133 | MISSING | MISSING | MISSING | MISSING |
| 04 | 2 | Q1 | YES | 1 | 142 | 142 | 230 | stop | 21562.81 | 74984.62 | 96547.44 | 228 | MISSING | MISSING | MISSING | MISSING |
| 05 | 2 | Q2 | YES | 1 | 135 | 135 | 108 | stop | 22683.87 | 35335.67 | 58019.54 | 107 | MISSING | MISSING | MISSING | MISSING |
| 06 | 2 | Q3 | YES | 1 | 153 | 153 | 108 | stop | 21712.65 | 35289.8 | 57002.44 | 106 | MISSING | MISSING | MISSING | MISSING |
| 07 | 3 | Q1 | YES | 1 | 142 | 142 | 147 | stop | 21674.02 | 48034.38 | 69708.41 | 145 | MISSING | MISSING | MISSING | MISSING |
| 08 | 3 | Q2 | YES | 1 | 135 | 135 | 74 | stop | 21362.63 | 24264.39 | 45627.02 | 73 | MISSING | MISSING | MISSING | MISSING |
| 09 | 3 | Q3 | YES | 1 | 153 | 153 | 188 | stop | 21739.8 | 61046.93 | 82786.73 | 186 | MISSING | MISSING | MISSING | MISSING |
| 10 | 4 | Q1 | YES | 1 | 142 | 142 | 85 | stop | 21409.13 | 27908.0 | 49317.13 | 84 | MISSING | MISSING | MISSING | MISSING |
| 11 | 4 | Q2 | YES | 1 | 135 | 135 | 106 | stop | 21423.71 | 34705.49 | 56129.2 | 105 | MISSING | MISSING | MISSING | MISSING |
| 12 | 4 | Q3 | YES | 1 | 153 | 153 | 181 | stop | 22096.2 | 59412.61 | 81508.81 | 179 | MISSING | MISSING | MISSING | MISSING |
| 13 | 5 | Q1 | YES | 1 | 142 | 142 | 146 | stop | 21240.18 | 47629.84 | 68870.02 | 144 | MISSING | MISSING | MISSING | MISSING |
| 14 | 5 | Q2 | YES | 1 | 135 | 135 | 111 | stop | 22050.56 | 36486.33 | 58536.89 | 110 | MISSING | MISSING | MISSING | MISSING |
| 15 | 5 | Q3 | YES | 1 | 153 | 153 | 140 | stop | 21996.67 | 45517.47 | 67514.14 | 138 | MISSING | MISSING | MISSING | MISSING |

Each row traces to its recorder run ID, exact request/response hashes, backend PID, recorder PID, startup snapshot, cold-state checks, and exact correlation record in `derived-results.json`. Missing literal fields remain `MISSING`.

## Mechanical task results

- Q1 B* successes: `5/5`
- Q2 B* successes: `5/5`
- Q3 B* successes: `5/5`
- Length-terminated observations: `0`
- Natural-stop observations: `15`

## Frozen state progression

1. Completeness/admissibility: `CALIBRATION_COMPLETE`
2. Generation-budget non-binding: `GENERATION_BUDGET_NONBINDING`
3. Baseline completion: `BASELINE_COMPLETION_OBSERVED`

## Terminal interpretation

`GENERATION_BUDGET_CALIBRATION_PASS`

Successor `max_tokens = 512` earned: `YES`

G7 v0.3 created: `NO`

Condition C executed: `NO`

## Historical firewall

No G7 v0.2 observation was reused or counted. The historical terminal state remains `CONTROL_ADEQUACY_FAIL`; historical capability non-regression, censoring, and work comparison remain unopened.

## Claim ceiling

A calibration pass establishes only that, under the frozen executor and canonical B*, `max_tokens = 512` was non-binding across these 15 calibration observations and permitted mechanically correct natural completion of the three frozen tasks.

It does not establish a C_improve effect, generation-work reduction, whole-run work reduction, lifecycle economics, compilation, amortization, reuse, or White Rabbit. Calibration observations are not successor-assay observations.
