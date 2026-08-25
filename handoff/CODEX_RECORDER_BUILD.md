# Codex Handoff — White Rabbit Recorder v0.1

Status: `IMPLEMENTATION_HANDOFF / NOT_EXECUTED / NON_SCIENTIFIC`

Codex must read first:

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
RAW != PARSED != INTERPRETED
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

## Completion report

Return:

```text
White Rabbit Recorder version:
repository:
parent commit:
implementation commit:

files added:
files changed:

dependencies added:

test command:
test result:

all-route transparent proxy: YES/NO
inference-route recording: YES/NO
request raw-byte custody: YES/NO
request forwarded byte-identically: YES/NO
request SHA verified against fake upstream: YES/NO
unknown fields preserved: YES/NO
missing fields left absent: YES/NO
malformed JSON preserved: YES/NO
response raw-byte custody: YES/NO
streaming response preserved: YES/NO
response parse failure preserves raw source: YES/NO
server invocation capture implemented: YES/NO
server version capture implemented: YES/NO
server PID/session capture implemented: YES/NO
backend prompt-new extraction: YES/NO
backend generated-token extraction: YES/NO
backend timing extraction: YES/NO
LCP fields preserved literally: YES/NO
graphs-reused field preserved literally: YES/NO
cached-token count guessed anywhere: YES/NO
task/request correlation implemented: YES/NO
ambiguous correlation fails explicitly: YES/NO
concurrent measured requests controlled: YES/NO
post-template model token stream claimed: YES/NO
C_improve treatment added: YES/NO
neutral prelude added: YES/NO
capability evaluator added: YES/NO
White Rabbit policy added: YES/NO
white-rabbit repo modified by recorder implementation: YES/NO
RD_HARNESS modified: YES/NO
real Qwen request executed: YES/NO
scientific comparison executed: YES/NO
known limitations:
scientific ambiguities encountered:
working tree clean: YES/NO
```

Then stop.

## Governing rule

> **Measure what ran before interpreting what it means.**
