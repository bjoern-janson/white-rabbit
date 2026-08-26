# Gate 7 Neutral-Control Robustness Assay v0.1.1

Version: `G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0.1.1`

Status: `CONSTITUTED / PANEL_FROZEN / SCHEDULE_VERIFIED / NOT_EXECUTED / REVIEW_REQUIRED / NON_AUTHORIZING`

Scientific requests: `0`

## Authority and correction scope

Repository: `bjoern-janson/white-rabbit`.

Required starting remote `main`: `0b41a175fcf047ff3d0ec313cdb0e11485f12741`.

Parent: `assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1.md`, commit `0b41a175fcf047ff3d0ec313cdb0e11485f12741`.

`G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0.1` remains an immutable historical constitution. It contains no scientific observations. Its reported task-local schedule blocker was an arithmetic verification error. This artifact corrects verification only.

The v0.1 and v0.1.1 schedule, panel, conditions, decision rules, executor, measurement rules, and claim ceiling are identical. No scientific design dimension is changed. The sole correction is `task-local schedule verification: FAIL -> PASS`.

## Immutable inherited design

Preserved unchanged: the six-control panel B0–B5; tuples, labels, R2 ordinals, exact source text and hashes; literal treatment C and hash; Q1/Q2/Q3 wording, answers, and hashes; executor and `max_tokens = 512`; `N_prompt = MEASURE`; token-matching prohibition; 14-row order library; `R15 = R01`; condition-number mapping; exact 15-block assignment and run numbers 001–105; cold-run doctrine; capability gates; censoring gate; pairwise robustness criterion; panel terminal states; result precedence; and claim ceiling.

The panel remains a predeclared structural robustness panel, not a random sample, representative sample, exhaustive family estimate, or population probability. Planned observations remain `7 × 3 × 5 = 105` fresh observations. Historical observations remain excluded.

## Correct task-local verification

Condition mapping is unchanged: `1=B0`, `2=B1`, `3=C`, `4=B2`, `5=B3`, `6=B4`, `7=B5`.

Serial positions were recomputed from the existing frozen 15-block schedule. The authoritative integer sums and means are:

| Task | B0 | B1 | C | B2 | B3 | B4 | B5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Q1 sums | 19 | 19 | 20 | 20 | 21 | 21 | 20 |
| Q1 means | 3.8 | 3.8 | 4.0 | 4.0 | 4.2 | 4.2 | 4.0 |
| Q2 sums | 19 | 20 | 20 | 21 | 21 | 20 | 19 |
| Q2 means | 3.8 | 4.0 | 4.0 | 4.2 | 4.2 | 4.0 | 3.8 |
| Q3 sums | 19 | 19 | 20 | 21 | 21 | 20 | 20 |
| Q3 means | 3.8 | 3.8 | 4.0 | 4.2 | 4.2 | 4.0 | 4.0 |

Every condition/task mean lies in `[3.8, 4.2]`; C has mean `4.0` for Q1, Q2, and Q3. Task-local schedule verification: **PASS**.

Explicit C arithmetic:

- Q1, blocks 01/04/07/10/13: positions `4, 2, 2, 7, 5`, sum `20`, mean `4.0`.
- Q2, blocks 02/05/08/11/14: positions `3, 6, 1, 6, 4`, sum `20`, mean `4.0`.
- Q3, blocks 03/06/09/12/15: positions `1, 3, 4, 7, 5`, sum `20`, mean `4.0`.

The prior blocker resulted from associating the wrong library rows with the task blocks; the frozen schedule itself was not defective and is not repaired here.

## First-14 balance verification

Recomputation from unchanged R01–R14 verifies:

- each of the seven conditions occupies each of the seven serial positions exactly twice;
- all `7 × 6 = 42` ordered adjacent pairs of distinct conditions occur exactly twice.

The row library is unchanged.

## Execution boundary

This is a verification-only correction. Do not start llama-server or the recorder, send requests, tokenize for matching, generate observations, execute B0–B5 or C, evaluate `N_generated`, or emit any scientific or White Rabbit result. Execution authority remains absent pending independent review.

## Completion record

- version: `G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0.1.1`
- path: `assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1.md`
- starting remote main: `0b41a175fcf047ff3d0ec313cdb0e11485f12741`
- parent v0.1 preserved: YES
- scientific design changed: NO
- schedule changed: NO
- panel changed: NO
- verification failure locus: arithmetic / schedule-verification inference
- first-14 position balance: PASS
- first-14 adjacency balance: PASS
- task-local position sums: verified as tabulated
- task-local position means: verified as tabulated
- C Q1/Q2/Q3 means: `4.0 / 4.0 / 4.0`
- task-local requirement: PASS
- scientific requests: `0`
- execution authorized: NO
- unit tests: run after artifact creation
- validator: run after artifact creation
- files added: this artifact only
- files changed: none
- ambiguities: none after corrected row-to-task association
- blockers: execution remains unauthorized; independent review required

STOP.
