# White Rabbit Measurement Model

Status: `FROZEN_CURRENT_MEASUREMENT_DOCTRINE / NON_AUTHORIZING`

This document defines the measurement vocabulary needed to distinguish capability, current-run execution, reusable state, derived reconstruction, and interpretation. It does not authorize model calls or scientific treatment.

## Measurement doctrine

The mandatory evidence order is:

```text
RAW MEASUREMENT
    -> DERIVED RECONSTRUCTION
    -> INTERPRETATION
```

These are distinct epistemic layers.

- **RAW MEASUREMENT**: literal bytes, counters, timings, identifiers, and backend fields actually observed.
- **DERIVED RECONSTRUCTION**: arithmetic or deterministic reconstruction from raw measurements.
- **INTERPRETATION**: semantic, causal, capability, independence, or White Rabbit claims.

A derived value must never be presented as if it were backend-reported. An interpretation must never be presented as if it were a measurement.

## Three quantities that must remain separate

```text
C_latent != C_realized(R, q) != C_work(R, q)
```

`C_latent` is not directly measured by the current apparatus. It is a conceptual quantity describing capability available in a fixed model/substrate.

`C_realized(R, q)` must eventually be operationalized by a separately constituted evaluation layer. The recorder must not infer it from response length, style, confidence, or subjective impressiveness.

`C_work(R, q)` is the computational-work side. The first recorder preserves backend evidence relevant to this quantity but does not itself adjudicate work elimination.

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

## LCP / retained-prefix firewall

Literal llama.cpp reuse indicators must remain distinct:

```text
f_sim_best != f_keep
```

They have different reference populations and must never be interpreted in isolation.

At the current evidence boundary:

- `f_sim_best` is preserved as the backend's reported similarity of the incoming context to selected prior state;
- `f_keep` is preserved as the backend's reported retained fraction associated with prior state;
- neither field is relabeled as an explicit cached-token count;
- interpretation requires the relevant token populations and surrounding backend evidence.

The recorder should preserve, where available:

```text
f_sim_best
f_keep
previous slot token count
N_prompt,new
N_generated
final slot token count
slot/task identifiers
```

A reconstruction such as:

```text
3667 retained + 2228 new ~= 5895 pre-generation context
```

is a **DERIVED RECONSTRUCTION** when supported by the raw counters. It is not a backend-reported cache meter.

> **Never interpret LCP similarity without retained-prefix size and its reference population.**

## Elimination firewall

The measurement layer must distinguish:

```text
work executed now
work executed earlier and reused now
work never required because of candidate structure
```

Only the third category is direct evidence that a candidate eliminated previously required computation. Reuse can still produce favorable total economics, but its acquisition cost must be included.

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

## Raw observables for the recorder

The recorder preserves, where explicitly exposed:

```text
raw HTTP request body
raw HTTP response body
server invocation/build/PID/session
N_prompt,new
N_prompt,cached (only if explicitly exposed)
N_generated
N_slot / final slot count when explicitly exposed
T_prompt
T_generation
T_total
slot/task identifiers
f_sim_best
f_keep
graphs_reused
backend logs
```

Missing fields remain missing. Defaults and cached-token counts are never guessed in the primary measurement layer.

`graphs_reused` remains a literal backend counter. It is not a cached-token counter unless a separately established backend definition says so.

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

## White Rabbit gates

The general White Rabbit burden is:

```text
G1: C_realized(M, q) >= C_realized(R0, q)
G2: independent reproduction
G3: C_work(M, q) < C_work(R0, q)
G4: acquisition cost is repaid over reuse
```

with optional stronger capability gain:

```text
G1+: C_realized(M, q) > C_realized(R0, q)
```

A measurement at one gate does not earn any later gate.

Examples:

```text
good answer        != compute saving
cache hit          != capability improvement
one-off reduction  != independent reproduction
reuse              != amortization
```

## Scientific boundary

This measurement model does not establish:

```text
general capability
C_improve causality
independent replication
persistent policy acquisition
computation elimination
amortized savings
White Rabbit effect
```

It exists so those claims can later be tested without conflating interface presentation, caching, runtime throughput, derived reconstruction, and scientific interpretation.
