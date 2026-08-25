# Codex Handoff — White Rabbit Recorder v0.1

Status: `HANDOFF_CLOSED / COMPLETION_REPORTED / NON_SCIENTIFIC`

This handoff has been consumed.

A user-supplied Codex completion report records:

```text
White Rabbit Recorder version: 0.1.0
local implementation commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
files added: 27
dependencies: none / Python standard library only
tests: 30/30 PASS
test upstream: deterministic fake only
real Qwen request: NO
scientific comparison: NO
working tree: clean
remote: none / local-only
```

This GitHub repository cannot independently inspect that local commit or rerun the reported tests.

The authoritative milestone record for current program state is:

```text
program/RECORDER_V0_1_MILESTONE.md
```

The original stop condition has been reached according to the supplied report:

```text
fake-upstream acceptance
-> STOP
```

Gate 5 — real-server recorder calibration — remains separately unauthorized.

---

## Historical implementation contract

Codex was instructed to read first:

1. `interfaces/WHITE_RABBIT_RECORDER_V0_1.md`
2. `measurement/MEASUREMENT_MODEL.md`
3. `constitution/instrumentation_invariants.md`
4. `constitution/authority.md`
5. `program/STATE.md`

## Build target

Implement a separate sibling component/repository:

```text
white-rabbit-recorder
```

Do not add recorder runtime code to `white-rabbit`.

Do not modify `RD_HARNESS`.

The component is a transparent reverse proxy / inference recorder:

```text
browser :8085
    -> recorder :8085
    -> llama-server :8086
```

It must proxy all routes and record inference routes such as `/v1/chat/completions`.

## Authoritative artifacts

```text
request/body.raw
response/body.raw
server/log.raw
```

Derived artifacts may include hashes, parsed JSON/JSONL, metadata, and literal backend timing extraction.

```text
RAW MEASUREMENT
-> DERIVED RECONSTRUCTION
-> INTERPRETATION
```

The request body forwarded upstream must be byte-identical to the request body received by the proxy.

Missing request/backend fields remain absent. Never infer defaults.

## Required engineering properties

The implementation must provide:

```text
all-route transparent proxying
raw request-body custody + SHA-256
raw response-body custody + SHA-256
streaming/SSE preservation
unknown-field preservation
malformed-JSON raw preservation
immutable run directories
server invocation/version/PID/session custody
literal llama.cpp timing extraction
literal LCP/cache-indicator extraction
explicit request/task correlation status
explicit ambiguous-correlation failure
concurrency control for measured inference
```

Do not infer `n_prompt_cached` by arithmetic when llama.cpp does not explicitly expose it.

Do not relabel `graphs_reused` as cached tokens.

Do not claim that the HTTP body is the exact post-Jinja model token stream.

## Historical server configuration for launcher support

```powershell
llama-server `
  -m "<MODEL_PATH>" `
  -a qwen38-27b `
  --host 127.0.0.1 `
  --port 8086 `
  -ngl 50 `
  -c 8192 `
  -np 1 `
  --jinja `
  --reasoning-format deepseek
```

The model path must be supplied through configuration/environment.

Backend identity must come from current runtime evidence, not assumptions about CUDA/Vulkan.

## Acceptance

Use a deterministic fake upstream only.

No real Qwen request is needed or authorized during v0.1 implementation acceptance.

Minimum acceptance checks:

```text
request bytes survive byte-for-byte
request SHA matches fake upstream received body
JSON whitespace/key order/Unicode representation are not normalized
unknown fields survive
missing fields stay absent
malformed JSON stays raw
normal + SSE response bytes survive in order
parse failure preserves raw source
non-inference routes transparently proxy
run directories cannot be overwritten
server command/version/PID/session capture works
backend fixture parser extracts literal timing/LCP fields
missing backend metrics stay absent
ambiguous correlation fails explicitly
concurrent measured inference is controlled
```

Claim ceiling after acceptance:

```text
IMPLEMENTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE PASS
```

Then `STOP`.

## Forbidden during this handoff

Do not add or execute:

```text
C_improve treatment
neutral prelude
Cold A/B/C
capability benchmark
capability judge
LLM judge
White Rabbit policy
prompt optimization
retrieval/embeddings/vector DB
fine-tuning
scientific treatment
real Qwen comparison
```

Do not change the White Rabbit scientific state merely because the recorder implementation succeeds.

## Reported completion against the contract

The supplied completion report states:

```text
all-route transparent proxy: YES
inference-route recording: YES
request raw-byte custody: YES
request forwarded byte-identically: YES
request SHA verified against fake upstream: YES
unknown fields preserved: YES
missing fields left absent: YES
malformed JSON preserved: YES
response raw-byte custody: YES
streaming response preserved: YES
response parse failure preserves raw source: YES
server invocation/version/PID/session capture: YES
backend prompt-new/generated/timing extraction: YES
LCP fields preserved literally: YES
graphs-reused preserved literally: YES
cached-token count guessed: NO
request/task correlation: YES
ambiguous correlation fails explicitly: YES
concurrent measured requests: HTTP 409
post-template model token stream claimed: NO
C_improve treatment added: NO
neutral prelude added: NO
capability evaluator added: NO
White Rabbit policy added: NO
white-rabbit modified by recorder task: NO
RD_HARNESS modified: NO
real Qwen request executed: NO
scientific comparison executed: NO
```

The reported limitations are preserved in `program/RECORDER_V0_1_MILESTONE.md`.

## Governing rule

> **Measure what ran before interpreting what it means.**
