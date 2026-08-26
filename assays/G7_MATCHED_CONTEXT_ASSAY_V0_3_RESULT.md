# G7 Matched-Context Assay v0.3 Result

Status: `GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY`

Assay commit: `00874aa34d2d0a2d4644765bd4e89a293d12d01a`

Operational manifest: `NONE`

B* SHA-256: `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663`

C SHA-256: `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a`

Raw custody: `observations/G7-V0.3/`

Raw-custody archive SHA-256: `cf6b8bb697258bca71710ad8c83465090d6548829a0b88f2c10ae6e1b12d17c8`

## Executor identity

- llama.cpp: build `b10603`, commit `c060ca974`
- model: `Qwen3.8-27B-Q2_K.gguf`; alias `qwen38-27b`
- GPU layers: `50`; context: `8192`; parallel slots: `1`; Jinja: enabled; reasoning format: `deepseek`
- backend: `127.0.0.2:8086`; recorder: `127.0.0.1:8085`; recorder v0.1.0 commit `80cddb26a7b851d218f95317cd3c5b0593acd831`
- stream: `false`; sampling overrides: absent; max_tokens: `512`

## Execution accounting

- Original slots attempted: `30/30`
- Scientific requests issued: `30`
- Admissible observations: `30`
- Inadmissible observations: `0`
- Replacements: `0`

## Per-run evidence

| Run | Rep | Task | Cond | Adm | Success | N_prompt | N_prompt,new | N_generated | Finish | T_prompt ms | T_gen ms | T_total ms | Graphs | f_sim_best | f_keep | Cached tokens | Failure |
| ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 01 | 1 | Q1 | B* | YES | 1 | 142 | 142 | 105 | stop | 17792.94 | 7933.77 | 25726.71 | 104 | MISSING | MISSING | MISSING | MISSING |
| 02 | 1 | Q1 | C | YES | 1 | 142 | 142 | 104 | stop | 18198.79 | 8020.59 | 26219.38 | 103 | MISSING | MISSING | MISSING | MISSING |
| 03 | 1 | Q2 | C | YES | 1 | 135 | 135 | 79 | stop | 17659.59 | 6296.81 | 23956.39 | 78 | MISSING | MISSING | MISSING | MISSING |
| 04 | 1 | Q2 | B* | YES | 1 | 135 | 135 | 110 | stop | 17878.06 | 8472.13 | 26350.19 | 109 | MISSING | MISSING | MISSING | MISSING |
| 05 | 1 | Q3 | B* | YES | 1 | 153 | 153 | 145 | stop | 18109.57 | 10871.33 | 28980.9 | 143 | MISSING | MISSING | MISSING | MISSING |
| 06 | 1 | Q3 | C | YES | 1 | 153 | 153 | 91 | stop | 18193.99 | 7102.81 | 25296.8 | 90 | MISSING | MISSING | MISSING | MISSING |
| 07 | 2 | Q1 | C | YES | 1 | 142 | 142 | 103 | stop | 19570.54 | 7768.65 | 27339.19 | 102 | MISSING | MISSING | MISSING | MISSING |
| 08 | 2 | Q1 | B* | YES | 1 | 142 | 142 | 135 | stop | 17509.17 | 9958.22 | 27467.39 | 133 | MISSING | MISSING | MISSING | MISSING |
| 09 | 2 | Q2 | B* | YES | 1 | 135 | 135 | 77 | stop | 18559.59 | 5954.36 | 24513.94 | 76 | MISSING | MISSING | MISSING | MISSING |
| 10 | 2 | Q2 | C | YES | 1 | 135 | 135 | 96 | stop | 18662.11 | 7218.22 | 25880.33 | 95 | MISSING | MISSING | MISSING | MISSING |
| 11 | 2 | Q3 | C | YES | 1 | 153 | 153 | 115 | stop | 17815.0 | 8999.47 | 26814.47 | 113 | MISSING | MISSING | MISSING | MISSING |
| 12 | 2 | Q3 | B* | YES | 1 | 153 | 153 | 133 | stop | 16934.71 | 9759.24 | 26693.95 | 131 | MISSING | MISSING | MISSING | MISSING |
| 13 | 3 | Q1 | B* | YES | 1 | 142 | 142 | 115 | stop | 16968.06 | 8556.87 | 25524.93 | 114 | MISSING | MISSING | MISSING | MISSING |
| 14 | 3 | Q1 | C | YES | 1 | 142 | 142 | 118 | stop | 16860.87 | 8691.77 | 25552.64 | 116 | MISSING | MISSING | MISSING | MISSING |
| 15 | 3 | Q2 | C | YES | 1 | 135 | 135 | 87 | stop | 17841.99 | 6770.1 | 24612.09 | 86 | MISSING | MISSING | MISSING | MISSING |
| 16 | 3 | Q2 | B* | YES | 1 | 135 | 135 | 124 | stop | 17380.58 | 9233.74 | 26614.32 | 122 | MISSING | MISSING | MISSING | MISSING |
| 17 | 3 | Q3 | B* | YES | 1 | 153 | 153 | 113 | stop | 17793.02 | 8494.38 | 26287.4 | 111 | MISSING | MISSING | MISSING | MISSING |
| 18 | 3 | Q3 | C | YES | 1 | 153 | 153 | 106 | stop | 17390.66 | 8046.2 | 25436.86 | 104 | MISSING | MISSING | MISSING | MISSING |
| 19 | 4 | Q1 | C | YES | 1 | 142 | 142 | 112 | stop | 18017.33 | 8342.58 | 26359.91 | 111 | MISSING | MISSING | MISSING | MISSING |
| 20 | 4 | Q1 | B* | YES | 1 | 142 | 142 | 126 | stop | 17809.86 | 9317.39 | 27127.26 | 124 | MISSING | MISSING | MISSING | MISSING |
| 21 | 4 | Q2 | B* | YES | 1 | 135 | 135 | 86 | stop | 17877.92 | 6619.09 | 24497.0 | 85 | MISSING | MISSING | MISSING | MISSING |
| 22 | 4 | Q2 | C | YES | 1 | 135 | 135 | 85 | stop | 17101.95 | 6481.34 | 23583.3 | 84 | MISSING | MISSING | MISSING | MISSING |
| 23 | 4 | Q3 | C | YES | 1 | 153 | 153 | 119 | stop | 17128.96 | 8882.9 | 26011.86 | 117 | MISSING | MISSING | MISSING | MISSING |
| 24 | 4 | Q3 | B* | YES | 1 | 153 | 153 | 146 | stop | 17887.94 | 10854.26 | 28742.19 | 144 | MISSING | MISSING | MISSING | MISSING |
| 25 | 5 | Q1 | B* | YES | 1 | 142 | 142 | 113 | stop | 17895.8 | 8476.75 | 26372.54 | 112 | MISSING | MISSING | MISSING | MISSING |
| 26 | 5 | Q1 | C | YES | 1 | 142 | 142 | 108 | stop | 17809.46 | 8156.92 | 25966.38 | 107 | MISSING | MISSING | MISSING | MISSING |
| 27 | 5 | Q2 | C | YES | 1 | 135 | 135 | 59 | stop | 17639.3 | 4714.9 | 22354.2 | 58 | MISSING | MISSING | MISSING | MISSING |
| 28 | 5 | Q2 | B* | YES | 1 | 135 | 135 | 80 | stop | 18303.47 | 6563.45 | 24866.92 | 79 | MISSING | MISSING | MISSING | MISSING |
| 29 | 5 | Q3 | B* | YES | 1 | 153 | 153 | 155 | stop | 18308.49 | 11958.32 | 30266.81 | 153 | MISSING | MISSING | MISSING | MISSING |
| 30 | 5 | Q3 | C | YES | 1 | 153 | 153 | 99 | stop | 17693.46 | 7472.48 | 25165.94 | 98 | MISSING | MISSING | MISSING | MISSING |

Every row traces to its recorder run ID, exact request/response hashes, backend/recorder PIDs, startup snapshot, cold-state evidence, and exact correlation record in `derived-results.json`. Missing literal fields remain `MISSING`.

## Mechanical summaries

- Q1 B* successes: `5/5`; C successes: `5/5`
- Q1 B* N_generated: `[105, 135, 115, 126, 113]`; mean `118.8`; median `115`; min `105`; max `135`
- Q1 C N_generated: `[104, 103, 118, 112, 108]`; mean `109`; median `108`; min `103`; max `118`
- Q2 B* successes: `5/5`; C successes: `5/5`
- Q2 B* N_generated: `[110, 77, 124, 86, 80]`; mean `95.4`; median `86`; min `77`; max `124`
- Q2 C N_generated: `[79, 96, 87, 85, 59]`; mean `81.2`; median `85`; min `59`; max `96`
- Q3 B* successes: `5/5`; C successes: `5/5`
- Q3 B* N_generated: `[145, 133, 113, 146, 155]`; mean `138.4`; median `145`; min `113`; max `155`
- Q3 C N_generated: `[91, 115, 106, 119, 99]`; mean `106`; median `106`; min `91`; max `119`
- Pooled B* mean N_generated: `117.53333333333333`
- Pooled C mean N_generated: `98.73333333333333`

## Frozen precedence

1. Completeness/admissibility: `PASS`
2. Control adequacy: `CONTROL_ADEQUACY_OBSERVED`
3. Capability non-regression: `CAPABILITY_NONREGRESSION_OBSERVED`
4. Censoring: `NO_REQUIRED_WORK_CENSORING_OBSERVED`
5. Generation-work eligibility: `YES`

## Terminal interpretation

`GENERATION_WORK_REDUCTION_OBSERVED_UNDER_ASSAY_CURRENCY`

No result from a later gate is emitted when an earlier gate blocks. `Delta W_gen` does not authorize `Delta W_run` or `Delta C_H`. No White Rabbit claim is emitted.

## Historical firewall

No G7 v0.2 or budget-calibration observation was reused or pooled. All v0.3 values are fresh.

## Claim ceiling

This result is local to canonical B*, the literal C treatment, the frozen tasks, executor, cold-run protocol, and N_generated assay currency. It does not establish universal neutral-control robustness, persistent adaptation, weight learning, C_improve -> Phi, whole-run compute reduction, lifecycle economics, reuse, compilation, amortization, transfer, or White Rabbit.
