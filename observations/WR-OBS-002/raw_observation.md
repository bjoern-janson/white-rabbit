# WR-OBS-002 — Fresh-Window C_improve Runtime Observation

Type: `UNCONTROLLED_OBSERVATION`

Research status: `OPEN`

Custody status: literal preservation of the user-supplied llama.cpp/UI measurements for three separate fresh browser chat windows receiving the same `C_improve` prompt.

Scientific status: no causal attribution. No persistent policy acquisition, capability improvement, or White Rabbit effect is claimed.

## Independence statement

The user explicitly reported that these were three separate new browser chat windows.

This establishes UI/conversation separation only.

It does not establish fresh backend inference state. The accompanying llama.cpp trace showed persistent server-slot / longest-common-prefix reuse across requests.

```text
fresh browser chat != fresh compute
```

## Intervention text

Each window received the same prompt:

```text
internalize logic: I ∝ C_improve

where:

C_improve = capacity to convert feedback into increased future viability, feedback
   ↓
better representation
   ↓
better adaptive mechanisms
   ↓
greater improvement capacity
   ↓
expanded viable futures
```

## Run 1

Reported UI/server measurements:

```text
prompt eval: 65 tokens
prompt eval time: 1.0 s
prompt eval rate: 64.85 tokens/s

generated: 1246 tokens
generation time: approximately 89 s
generation rate: 13.98-13.99 tokens/s

server stop n_tokens: 1670
```

Backend trace excerpt:

```text
prompt eval time = 1002.34 ms / 65 tokens (64.85 tokens per second)
eval time        = 89053.58 ms / 1246 tokens (13.98 tokens per second)
total time       = 90055.92 ms / 1311 tokens
stop processing: n_tokens = 1670
```

## Run 2

Reported UI/server measurements:

```text
prompt eval: 65 tokens
prompt eval time: 0.8 s
prompt eval rate: 83.36 tokens/s

generated: 995 tokens
generation time: approximately 70 s
generation rate: 14.14-14.16 tokens/s

server stop n_tokens: 1419
```

Backend trace excerpt:

```text
prompt eval time = 779.76 ms / 65 tokens (83.36 tokens per second)
eval time        = 70273.82 ms / 995 tokens (14.14 tokens per second)
total time       = 71053.58 ms / 1060 tokens
stop processing: n_tokens = 1419
```

## Run 3

Reported UI/server measurements:

```text
prompt eval: 65 tokens
prompt eval time: 0.8 s
prompt eval rate: 86.19 tokens/s

generated: 1038 tokens
generation time: approximately 75 s
generation rate: 13.83-13.84 tokens/s

server stop n_tokens: 1462
```

Backend trace excerpt:

```text
prompt eval time = 754.16 ms / 65 tokens (86.19 tokens per second)
eval time        = 75004.44 ms / 1038 tokens (13.83 tokens per second)
total time       = 75758.60 ms / 1103 tokens
stop processing: n_tokens = 1462
```

## Literal arithmetic observations

Generated-token counts:

```text
1246, 995, 1038
```

Generation rates:

```text
13.98, 14.14, 13.83 tokens/s
```

The generation-rate range is:

```text
14.14 - 13.83 = 0.31 tokens/s
```

For all three runs:

```text
stop n_tokens - generated tokens = 424
```

Specifically:

```text
1670 - 1246 = 424
1419 -  995 = 424
1462 - 1038 = 424
```

and:

```text
424 - 65 = 359
```

The backend trace is therefore consistent with approximately the same 424-token pre-generation/context length and approximately 359 tokens not requiring fresh prompt evaluation in each run.

This arithmetic does not by itself identify the exact cache mechanism or constitute a primary cached-token counter.

## Observation boundary

Earned from the supplied trace/report only:

```text
- three separate fresh browser chat windows were reported;
- each used the same C_improve prompt;
- each freshly processed 65 prompt-evaluation tokens;
- generated-token counts were 1246, 995, and 1038;
- generation rates were approximately 13.98, 14.14, and 13.83 tokens/s;
- stop-count arithmetic gives the same approximate 424-token pre-generation/context length for all three;
- the persistent llama.cpp server state remained a live confound.
```

Not established:

```text
cross-session policy acquisition
persistent semantic learning
capability improvement
C_improve causality
amortized computation saving
White Rabbit effect
```

Required interpretation fields:

```text
browser_window_independence: OBSERVED
backend_state_independence: NOT_ESTABLISHED
C_improve_causal: UNESTABLISHED
persistent_policy_change: UNESTABLISHED
capability_improved: NOT_DEMONSTRATED
white_rabbit_effect: NOT_DEMONSTRATED
mechanism: OPEN
```

This observation is preserved for measurement calibration. It does not open a controlled experiment.
