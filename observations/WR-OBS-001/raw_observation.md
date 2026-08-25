# WR-OBS-001 — Raw Observation Custody

Type: `UNCONTROLLED_OBSERVATION`

Custody status: literal transcription of user-reported local Qwen UI observations preserved before controlled reproduction.

Scientific status: no causal attribution. No White Rabbit effect is claimed.

## Source limitation

This file preserves the observation as reported in conversation. Original local screenshots/runtime logs are not attached here. Exact wall-clock timestamps were not supplied. Server restart state was not established. Conversation/session/KV/runtime state therefore remains a live confound.

Visible model label in the supplied UI excerpts: `qwen38` / `27B`.

## Intervention text

The user reported sending the following prompt before the later measurements:

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

The supplied UI excerpt for that interaction reported:

```text
65 tokens
1.0s
64.85 tokens/s
```

The model response was reported as beginning:

```text
Internalized. Here's the model as I hold it:

Core relation: I ∝ C_improve — intelligence is not stored capability, it's conversion rate. The ability to turn feedback into increased future viability.
```

The complete pasted response also described the feedback → representation → adaptive mechanisms → improvement capacity → expanded viable futures loop, proposed `I ≈ dV/dF`, and discussed bottlenecks, proxy failure, representation rigidity, and loop fidelity.

The supplied UI excerpt reported the response as:

```text
1,246 tokens
1min 29s
```

No inference is made here from the reported throughput or wall time.

## Pair A — `hi`

### Earlier observation, reported as "last night"

Prompt:

```text
hi
```

Reasoning display:

```text
371 tokens
28s
13.04 tokens/s
```

Final answer:

```text
Hi! 👋 How can I help you today?
```

Final-generation display:

```text
44 tokens
3.1s
14.34 t/s
```

### Later observation, after the C_improve interaction

Prompt:

```text
hi
```

Reasoning display:

```text
11 tokens
0.4s
24.89 tokens/s
```

Final answer:

```text
Hi! How can I help you today?
```

Final-generation display:

```text
88 tokens
6.1s
14.33 t/s
```

### Literal arithmetic difference

Displayed reasoning-token count changed from `371` to `11`, a difference of `360` displayed reasoning tokens.

Final-generation throughput was reported as `14.34 t/s` versus `14.33 t/s`, approximately unchanged at the precision shown by the UI.

This arithmetic observation does not establish why the work changed.

## Pair B — one-sentence neural-network explanation

This pair is preserved separately because the reported throughput changed strongly as well as the latency, leaving a substantial runtime/session/accounting confound.

### Earlier observation, reported as "last night"

Prompt:

```text
Explain in one sentence what a neural network is.
```

Reasoning display:

```text
21 tokens
16s
1.25 tokens/s
```

Final answer:

```text
A neural network is a mathematical model inspired by the brain, composed of layers of connected artificial neurons that learn to map inputs to outputs by adjusting weighted parameters through training.
```

Final-generation display:

```text
60 tokens
43s
1.39 t/s
```

### Later observation, after the C_improve interaction

Prompt:

```text
explain in one sentence what a neural network is
```

Reasoning display:

```text
19 tokens
0.6s
32.49 tokens/s
```

Final answer:

```text
A neural network is a computing system inspired by the brain, made of many simple artificial "neurons" that pass signals to each other, with adjustable connection strengths (weights) that are tuned through training to learn patterns in data.
```

Final-generation display:

```text
78 tokens
5.4s
14.54 t/s
```

## Observation boundary

Earned from the supplied report only:

```text
O1: observed reasoning work differed between the reported earlier and later measurements.
```

Not established:

```text
O2: C_improve caused the change.
O3: the change persists, transfers, or amortizes.
```

Required interpretation fields:

```text
C_improve_causal: UNESTABLISHED
persistent_policy_change: UNESTABLISHED
white_rabbit_effect: NOT_DEMONSTRATED
amortization: UNMEASURED
mechanism: UNKNOWN
```

Methodological constraint:

> Preserve anomaly != explain anomaly != optimize anomaly.

> Follow the footprint. Don't manufacture a trail.
