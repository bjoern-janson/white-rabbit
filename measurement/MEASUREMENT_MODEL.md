# White Rabbit Measurement Model

Status: `MEASUREMENT_SPECIFICATION / NON_AUTHORIZING`

This document defines the measurement vocabulary needed to distinguish capability, current-run execution, and reusable state. It does not authorize model calls or scientific treatment.

## Three quantities that must remain separate

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

`C_latent` is not directly measured by the current apparatus. It is a conceptual quantity describing capability available in a fixed model/substrate.

`C_realized(R, q)` must eventually be operationalized by a separately constituted evaluation layer. The recorder must not infer it from response length, style, confidence, or subjective impressiveness.

`C_work(R, q)` is the computational-work side. The first recorder is intended to preserve backend evidence relevant to this quantity.

## Current-run accounting

Current execution is represented as:

```text
C_run = C_prompt,new + C_generation + C_other
```

where:

- `C_prompt,new` is prompt/prefill work newly executed during the run;
- `C_generation` is generation/decoding work executed during the run;
- `C_other` is any separately measured current-run work.

No claim is made that token counts, wall time, energy, FLOPs, and cost are interchangeable currencies. A future experiment must freeze its accounting currency before comparison.

## Reusable state

Reusable state is tracked separately:

```text
K_reused = previously constituted state reused by this run
```

Examples may include KV/prefix cache state or a future compiled White Rabbit candidate, but the measurement layer must record what is actually evidenced rather than assigning a mechanism by analogy.

Across a reuse horizon:

```text
C_total = C_cache,acquire + sum_i C_run,i
```

For a general candidate `M`, the analogous program-level accounting is:

```text
C_total(M) = C_acquire(M) + C_compile(M) + sum_i C_run(M, q_i)
```

The exact decomposition used by a future experiment must be frozen before execution.

## Cache firewall

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

A controlled comparison must either begin with matched reusable state:

```text
K_baseline = K_treatment
```

or explicitly charge the differing acquisition cost.

> **Fresh chat is not fresh compute.**

A UI/session boundary is not sufficient evidence of independent backend state.

## Elimination firewall

The measurement layer must distinguish:

```text
work executed now
work executed earlier and reused now
work never required because of candidate structure
```

Only the third category is direct evidence that a candidate eliminated previously required computation. Reuse can still produce favorable total economics, but its acquisition cost must be included.

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

## Raw observables for the first recorder

The recorder should preserve, where explicitly exposed:

```text
raw HTTP request body
raw HTTP response body
server invocation/build/PID/session
N_prompt,new
N_prompt,cached (only if explicitly exposed)
N_generated
T_prompt
T_generation
T_total
slot/task identifiers
LCP/cache indicators
backend logs
```

Missing fields remain missing. Defaults and cached-token counts are never guessed in the primary measurement layer.

## Representation/context record

For each future measured run, the evidence package should make it possible to reconstruct at least:

```text
R
q
model/runtime configuration
K
C_prompt,new
C_generated
T
```

The recorder establishes HTTP/backend custody only. It does not establish the exact post-Jinja token sequence received by the neural network unless a later instrumentation layer explicitly captures it.

## Scientific boundary

This measurement model does not establish:

```text
capability improvement
C_improve causality
persistent policy acquisition
amortized savings
White Rabbit effect
```

It exists so those claims can later be tested without conflating interface presentation, caching, runtime throughput, and actual computation.
