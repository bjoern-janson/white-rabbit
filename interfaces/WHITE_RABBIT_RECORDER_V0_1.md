# White Rabbit Recorder v0.1 — Interface Contract

Status: `SPECIFIED / NOT_IMPLEMENTED / EXECUTION_NOT_AUTHORIZED`

This is a handoff contract for a future sibling component, preferably `white-rabbit-recorder`. It is intentionally non-runnable in this repository.

The recorder is a microscope, not a treatment.

## Objective

Establish:

```text
raw HTTP custody
+
backend execution custody
```

for local Qwen / llama.cpp inference without evaluating capability or executing a White Rabbit treatment.

The acceptance question is:

> **Can one recorded run prove exactly what HTTP body was delivered to llama-server, exactly what HTTP response body returned, which server configuration/PID processed it, and what llama.cpp explicitly reports it executed?**

The recorder does not yet establish the exact post-Jinja token sequence seen by the neural network.

## Topology

```text
browser
   |
   v
recorder 127.0.0.1:8085
   |
   v
llama-server 127.0.0.1:8086
```

The recorder must transparently proxy all HTTP routes because the llama.cpp browser UI may be served by the same server. Only inference endpoints such as `/v1/chat/completions` create measured run artifacts.

It must not replace the chat UI.

## Source/derived firewall

Authoritative artifacts:

```text
request/body.raw
response/body.raw
server/log.raw
```

Derived conveniences may include hashes, parsed JSON/JSONL, metadata, and mechanically extracted timing fields.

```text
RAW != PARSED != INTERPRETED
```

Never reconstruct raw custody from parsed JSON.

Never normalize request bytes before forwarding.

Never fill absent fields with guessed backend defaults.

## Request identity

For a measured inference request:

```text
SHA256(proxy_received_body) == SHA256(proxy_forwarded_body)
```

must hold.

The body must be forwarded byte-identically. Changes to transport framing may be recorded but must not be confused with HTTP-body identity.

The recorder should preserve method, path/query, relevant headers, timestamps, exact body bytes, and SHA-256.

Derived parsing should expose every field actually supplied, including unknown properties. Missing fields remain explicitly absent.

Malformed JSON is preserved raw and receives a parse-failure derivative; it is never repaired.

## Response custody

The recorder must preserve upstream response bytes in received order, including streaming/SSE responses.

Derived parsing may fail without affecting raw custody.

Capture status, relevant headers, first-byte/final-byte timing, and body hash.

## Server-session custody

A future launcher should be able to start the historical configuration on `:8086`:

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

The model path must be configuration/environment, not a hard-coded user path.

Preserve:

```text
exact invocation
llama-server --version
PID
process start time
recorder session ID
stdout/stderr
```

Backend identity must be recorded from evidence, not assumption. Historical evidence showed Vulkan participation, but a future run must classify its own backend.

## Backend extraction

Parse only explicitly reported llama.cpp fields. Where present:

```text
n_prompt_new
n_generated
t_prompt_ms
t_generation_ms
t_total_ms
slot_id
task_id
truncated
slot selection
f_sim_best
f_keep
graphs_reused
```

If an explicit cached-prompt-token counter exists, preserve it. Otherwise `n_prompt_cached` remains absent.

`graphs_reused` remains a literal backend counter and must not be renamed cached tokens.

Primary measurement must not infer cached-token counts by subtraction.

## Freshness/correlation firewall

> **Fresh chat is not fresh compute.**

Record server session ID, PID, start time, and number of prior measured requests in the session.

A new browser tab must never automatically become `COLD`, `FRESH`, or `INDEPENDENT`.

Because the historical setup uses `-np 1`, v0.1 may serialize or reject concurrent measured inference requests. Correlate request-to-task mechanically. If ambiguous:

```text
correlation_status = AMBIGUOUS
```

Never guess a task ID.

## Immutable run package

Suggested layout:

```text
runs/<run_id>/
  manifest.json
  request/
    body.raw
    body.sha256
    parsed.json
    metadata.json
  response/
    body.raw
    body.sha256
    parsed.jsonl
    metadata.json
  server/
    invocation.txt
    version.txt
    pid.txt
    session.json
    log.raw
  backend/
    timing.json
    cache.json
    correlation.json
```

Existing run IDs may never be overwritten.

The manifest contains custody metadata and hashes, never scientific conclusions.

## Forbidden scope

v0.1 must not add or execute:

```text
C_improve treatment
neutral prelude treatment
Cold A/B/C comparison
capability scoring
LLM judge
White Rabbit policy
prompt optimization
adaptive prompting
retrieval
embeddings/vector DB
fine-tuning
scientific adjudication
```

It must not modify `white-rabbit` or `RD_HARNESS` when implemented as the sibling recorder.

## Fake-upstream acceptance

Implementation acceptance must use a deterministic fake upstream server. No real Qwen request is required.

Required properties include:

1. request bytes survive forwarding byte-for-byte;
2. request SHA matches the exact fake-upstream body;
3. whitespace/key order/Unicode representation are not normalized;
4. unknown fields survive;
5. missing fields remain absent;
6. malformed JSON remains raw with explicit parse failure;
7. response/SSE bytes remain in upstream order;
8. parser failures preserve raw source;
9. run directories are immutable and unique;
10. non-inference routes proxy transparently;
11. server invocation/build/PID/session custody is implemented;
12. backend timing/LCP fields parse literally;
13. missing backend metrics remain absent;
14. ambiguous task correlation fails explicitly;
15. concurrent measured requests are controlled;
16. no treatment/capability/White Rabbit conclusion is emitted.

The only v0.1 engineering claim ceiling should be equivalent to:

```text
IMPLEMENTED
+
FAKE-UPSTREAM BYTE-CUSTODY ACCEPTANCE PASS
```

No scientific result follows.

## Stop condition

After fake-upstream acceptance:

```text
STOP
```

Do not run Qwen, `C_improve`, Cold A/B/C, a neutral prelude, or a capability comparison without a separately authorized transition.

## Governing rule

> **Measure what ran before interpreting what it means.**
