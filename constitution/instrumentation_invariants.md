# White Rabbit Instrumentation Invariants

Version: `0.1`

Status: `ACTIVE_MEASUREMENT_BOUNDARY`

This document extends the founding research-state constitution with measurement constraints learned from `WR-OBS-001`. It does not modify the frozen founding constitution and does not authorize a White Rabbit experiment.

## WR-I-CACHE-001 — Reusable-state acquisition must be charged

> **A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.**

Current-run execution is accounted separately from reusable state:

```text
C_run = C_prompt,new + C_generation + C_other
```

where:

- `C_prompt,new` is prompt/prefill computation newly executed for the run;
- `C_generation` is generation/decoding computation executed for the run;
- `C_other` is any other explicitly measured current-run work.

Reusable state is recorded separately:

```text
K_reused = previously constituted state reused by this run
```

Across a reuse horizon:

```text
C_total = C_cache,acquire + sum_i C_run,i
```

A treatment may not receive uncharged credit for reusable state that was created outside the run accounting window.

For a controlled comparison, either:

```text
K_baseline = K_treatment
```

at the constituted start boundary, or the cost of creating the differing reusable state must be included in the treatment accounting.

## WR-I-FRESH-001 — Fresh chat is not fresh compute

> **A new browser conversation does not constitute an independent inference state.**

Freshness must be defined at the backend state boundary relevant to the measured mechanism, including retained KV/prefix/cache state where applicable.

A UI/session reset is insufficient evidence of computational independence.

## WR-I-SEMANTICS-001 — Backend-confirm measurement categories

> **UI-visible token categories must not be assigned computational semantics without backend confirmation.**

In particular, prompt-evaluation tokens, generated tokens, reasoning-content tokens, cached-prefix tokens, and total context tokens must remain distinct unless an instrument explicitly establishes equivalence.

## WR-I-ELIMINATION-001 — Do not misclassify cached work as eliminated work

> **Never call computation eliminated until it is known who paid for it, when they paid for it, and whether it was merely cached.**

A valid computation-saving claim requires an accounting boundary that distinguishes:

```text
work executed now
work executed earlier and reused now
work never required because of the candidate structure
```

Only the third category is evidence of computation eliminated by the candidate structure itself, unless the acquisition-and-reuse economics are explicitly included and favorable.

## Scope

These are instrumentation invariants only.

They do not establish:

```text
C_improve causality
persistent computational-policy change
representation learning
amortized savings
White Rabbit effect
```

They constrain how future claims may be measured.