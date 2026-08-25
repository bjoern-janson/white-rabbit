# White Rabbit Gate 5 — Real-Server Recorder Calibration Milestone

Status: `USER_REPORTED_PASS / INSTRUMENTAL_ONLY / NON_SCIENTIFIC / NON_AUTHORIZING`

This file records the user-supplied result of the first controlled cold real-server recorder calibration.

It is not an independent verification by this GitHub repository. The authoritative run artifacts are reported to remain in the local `white-rabbit-recorder` / calibration runtime.

## Reported run

```text
result: COLD BASELINE / REAL-SERVER CALIBRATION PASS
run_id: WRR-V01-20260825T121044.291824Z-e3b8cbcc977f4593a276431a1993b74f
backend PID: 36464
recorder PID: 31428
task / slot: 0 / 0
measurement blocks: 1
N_prompt,new: 53
N_generated: 48
T_prompt: 13829.56 ms
T_generation: 14514.73 ms
T_total: 28344.29 ms
graphs_reused: 47 (literal backend field)
f_sim_best: NOT_EXPOSED
f_keep: NOT_EXPOSED
explicit cached-token field: NOT_EXPOSED
```

Reported request SHA-256:

```text
ef7d718701d1122a83d77b5d0ff646ad74473ea29f3473455cc0873aac3dcf6c
```

Reported response SHA-256:

```text
fc470fd7b523a6963180c80ef062aa5b35a8e7c73de7436803a37f7bbb755c14
```

## Reported cold-state evidence

```text
fresh backend PID distinct from calibration predecessor
zero task lines before request
prior_recorded_inference_requests = 0
first slot selection: LRU, t_last = -1
startup snapshot: 1017 bytes, independently hashed
```

The recorder/backend were reported stopped after the run.

The only recorder implementation change reported before this run was literal llama.cpp b10603 log-format compatibility, covered by 15 passing custody/correlation/firewall tests.

## Claim ceiling

This milestone supports only the reported instrumental transition:

```text
Gate 5 — real-server recorder calibration: REPORTED PASS
```

It does not establish:

```text
capability effect
C_improve causality
compute reduction
cache independence beyond the constituted cold-state evidence
White Rabbit effect
```

No treatment, neutral prelude, comparison, benchmark, or capability evaluation was reported executed.

> **The microscope was reported to survive contact with the real llama.cpp/Qwen stack under a strongly evidenced cold start. No scientific treatment followed.**
