# WR-OBS-001 — Backend Measurement Correction

Type: `MEASUREMENT_CORRECTION`

Status: `OPEN_LEAD / INTERPRETATION_CORRECTED`

This record preserves the correction induced by the later llama.cpp server trace. It does not delete or rewrite the original UI custody record.

## Runtime configuration evidenced by the supplied PowerShell trace

The server was launched successfully with:

```text
llama.cpp version: 0.2.0-dev
build: 10603
commit: c060ca974
model: Qwen3.8-27B-Q2_K.gguf
alias: qwen38-27b
host: 127.0.0.1
port: 8085
n_gpu_layers: 50
context: 8192
parallel slots: 1
jinja: enabled
reasoning format: deepseek
```

The trace directly shows Vulkan participation during the failed higher-memory launch:

```text
ggml_vulkan: Device memory allocation ... failed
vk::Device::allocateMemory: ErrorOutOfDeviceMemory
```

Therefore this historical execution must not be labeled CUDA-only from the available evidence. `VULKAN_PARTICIPATION_OBSERVED` is the bounded runtime statement.

## Correction to Pair A — `hi`

Earlier request:

```text
prompt eval time = 28449.71 ms / 371 tokens
       eval time =  3069.07 ms /  44 tokens
      total time = 31518.78 ms / 415 tokens
stop processing: n_tokens = 414
```

Later request:

```text
selected slot by LCP similarity, f_sim_best = 0.978 (> 0.100 thold), f_keep = 0.217
prompt eval time = 442.02 ms / 11 tokens
       eval time = 6140.30 ms / 88 tokens
      total time = 6582.32 ms / 99 tokens
stop processing: n_tokens = 458
```

### Corrected classification

The `371` and `11` counts belong to llama.cpp `prompt eval` accounting: prompt tokens freshly processed for those requests after any retained-prefix reuse. They are not generated reasoning-token counts.

The generated-token counts are `44` and `88` respectively.

Using the slot totals as an approximate context accounting:

```text
earlier: 414 - 44 = 370 pre-generation/context tokens
later:   458 - 88 = 370 pre-generation/context tokens
```

So the available trace is consistent with approximately the same full prompt/context size in both `hi` runs while the later request required only 11 freshly evaluated prompt tokens.

The later request explicitly selected the slot by longest-common-prefix similarity with:

```text
f_sim_best = 0.978
```

This is direct evidence that substantial prefix/KV reuse was active. Approximately `370 - 11 = 359` prompt/context tokens did not require fresh prompt evaluation in the later request under this accounting.

### Timing decomposition

Earlier:

```text
prompt evaluation: ~28.45 s
generation:        ~3.07 s
generated tokens:   44
```

Later:

```text
prompt evaluation: ~0.44 s
generation:        ~6.14 s
generated tokens:   88
```

The later request generated more tokens and spent more time in generation. The large latency reduction occurred in prompt-prefill work, consistent with prefix/KV reuse.

Therefore the earlier interpretation:

```text
371 -> 11 = reasoning-token disappearance
```

is superseded.

The corrected claim ceiling is:

```text
UI observation: PRESERVED
371->11 reasoning-reduction interpretation: SUPERSEDED
371 and 11: freshly processed prompt-token counts
approximately equal full prompt/context length: OBSERVED
prefix/KV reuse: OBSERVED
C_improve causal effect: UNESTABLISHED
reasoning-work reduction: NOT_DEMONSTRATED
White Rabbit effect: NOT_DEMONSTRATED
```

## Repeated C_improve presentations

The same trace records three later presentations of the C_improve prompt. Their server accounting is:

```text
run 1:
  prompt eval = 65 tokens @ 64.85 tokens/s
  generation  = 1246 tokens @ 13.98 tokens/s
  stop n_tokens = 1670

run 2:
  prompt eval = 65 tokens @ 83.36 tokens/s
  generation  = 995 tokens @ 14.14 tokens/s
  stop n_tokens = 1419

run 3:
  prompt eval = 65 tokens @ 86.19 tokens/s
  generation  = 1038 tokens @ 13.83 tokens/s
  stop n_tokens = 1462
```

For all three:

```text
stop n_tokens - generated tokens = 424
```

and:

```text
424 - 65 = 359
```

so the trace is consistent with the same approximately 359-token retained/common prefix plus 65 freshly evaluated prompt tokens across these requests.

The generation throughput remains in the ordinary ~14 tokens/s regime. These observations do not establish a C_improve-specific policy effect.

## Neural-network throughput correction

The earlier neural-network request generated at approximately `1.37 tokens/s`, but the surrounding server trace contains other unrelated requests generating at approximately the same `1.37 tokens/s` regime before later requests returned to roughly `13-14 tokens/s`.

Therefore the neural-network before/after throughput contrast must not be attributed to C_improve from this evidence. A broader runtime-performance regime was present; its cause remains unknown.

## Measurement lesson

The authoritative distinction for future White Rabbit accounting is:

```text
fresh browser chat != fresh compute
```

A computation-saving claim must account for the cost of creating any reusable state that makes the saving possible.

Current-run execution should be recorded as:

```text
C_run = C_prompt,new + C_generation + C_other
```

Reusable state is tracked separately:

```text
K_reused = previously constituted state reused by this run
```

Across a reuse horizon:

```text
C_total = C_cache,acquire + sum_i C_run,i
```

Do not call computation eliminated until it is known who paid for the reusable state, when that cost was paid, and whether the apparent saving was merely cache/prefix reuse.

## Scientific boundary

This correction establishes a measurement reinterpretation, not a White Rabbit result.

```text
C_improve_causal: UNESTABLISHED
persistent_policy_change: UNESTABLISHED
reasoning_work_reduction: NOT_DEMONSTRATED
white_rabbit_effect: NOT_DEMONSTRATED
mechanism_of_runtime_slow_period: UNKNOWN
```

The original raw UI custody remains preserved unchanged as historical evidence of the initial observation and initial interpretation context.