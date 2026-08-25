# White Rabbit Gate 6 — Cold Baseline Characterization Milestone

Status: `USER_REPORTED_PASS / PROTOCOL_CHARACTERIZATION / NON_SCIENTIFIC / NON_AUTHORIZING`

This file records the user-supplied result of the frozen five-replicate cold characterization protocol.

It is not an independent verification by this GitHub repository. The authoritative run artifacts and summary are reported to remain in the local calibration runtime.

## Earned statement

> **Cold baseline operationally characterized under the frozen five-replicate protocol.**

Explicit ceiling:

```text
five replicates characterize the frozen Gate 6 protocol
!=
the underlying stochastic distribution is fully known
```

## Reported common conditions

All five replicates reportedly satisfied:

```text
byte custody: PASS
exact request/task correlation: PASS
one-block measurement: PASS
cold-state acceptance: PASS
task / slot: 0 / 0
request SHA-256: ef7d718701d1122a83d77b5d0ff646ad74473ea29f3473455cc0873aac3dcf6c
unique backend PID: YES
zero pre-request task lines: YES
prior recorder requests: 0
first-slot evidence: selected slot by LRU, t_last = -1
```

## Reported replicates

| Replicate | Run ID suffix | Backend / Recorder PID | Prompt / Generated | Prompt / Generation / Total ms | `graphs_reused` |
| --- | --- | --- | --- | --- | ---: |
| 1 | `46ddd4…bcb8c9` | `38812 / 37072` | `53 / 3` | `14063.80 / 1281.79 / 15345.59` | 2 |
| 2 | `13fcbb…2091de` | `13084 / 32888` | `53 / 15` | `14088.28 / 5084.52 / 19172.80` | 14 |
| 3 | `b8857f…b8c8d8` | `2812 / 32384` | `53 / 24` | `14533.19 / 7922.67 / 22455.87` | 23 |
| 4 | `0ca03e…7a12dc` | `37708 / 27056` | `53 / 24` | `14667.45 / 7859.76 / 22527.22` | 23 |
| 5 | `5bd2b3…178c94` | `23768 / 26848` | `53 / 43` | `13796.69 / 13686.74 / 27483.44` | 42 |

## Mechanical summary

```text
N_prompt,new: mean 53, median 53, range 53-53
N_generated: mean 21.8, median 24, range 3-43
T_prompt: mean 14229.882 ms, median 14088.28 ms, range 13796.69-14667.45 ms
T_generation: mean 7167.096 ms, median 7859.76 ms, range 1281.79-13686.74 ms
T_total: mean 21396.984 ms, median 22455.87 ms, range 15345.59-27483.44 ms
graphs_reused: mean 20.8, median 23, range 2-42
```

Literal cache/LCP reporting:

```text
f_sim_best: NOT_EXPOSED in all five replicates
f_keep: NOT_EXPOSED in all five replicates
explicit cached-token field: NOT_EXPOSED in all five replicates
graphs_reused: preserved literally; not converted into cached tokens
```

Reported response variation:

```text
5 distinct raw response hashes
4 distinct assistant-content strings
replicates 3 and 4: identical visible content, different full response bytes
```

Reported summary artifact:

```text
white-rabbit-recorder.calibration-runtime/gate6-cold-characterization-20260825/gate6-summary.json
SHA-256: ffd58064d1f636d6b51bf50e7e3008b2a363fe5ca5148e7b4e870d6e92e8f32f
```

All controlled recorders/backends were reported stopped after the protocol.

## Methodological consequence

The frozen Gate 6 observations establish that under independently constituted cold runs with identical request bytes:

```text
N_prompt,new remained stable at 53
while
N_generated, T_generation, T_total, and response content varied materially
```

Therefore a future treatment effect must be evaluated against independently constituted baseline variability rather than against a privileged single baseline realization.

This is a protocol-level measurement constraint, not a scientific treatment result.

## Claim ceiling

```text
Gate 6 — five-replicate cold characterization: REPORTED PASS
Gate 7 — matched-context assay: NOT AUTHORIZED / NOT OPENED
White Rabbit G1-G4: NOT OPENED
```

No treatment, comparison, neutral prelude, benchmark, or capability evaluation was reported executed.
