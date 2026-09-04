# Fixed-Substrate Effective Capability — Substrate Capture Contract v0.1

Version: `FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_SUBSTRATE_CAPTURE_V0.1`

Status: `CAPTURE_CONTRACT_FROZEN / LOCAL_MANIFEST_NOT_CAPTURED / NON_AUTHORIZING / NOT_EXECUTED`

This artifact defines what must be captured from the actual local machine before implementation or scientific execution can open. It does **not** fill any machine-derived value from historical notes or repository inference.

## 1. Scientific role

The fixed substrate is part of the tested object:

```text
K_B = K_R = K_C
```

apart from the prospectively constituted B/R/C condition differences.

Historical names such as `RTX 3080 Ti`, `Qwen3.8-27B-Q2_K.gguf`, or `llama.cpp b10603` are lineage hints, not sufficient current identity.

## 2. Public manifest versus local raw custody

The repository-facing substrate manifest should contain scientific identities without unnecessarily publishing host/user identifiers.

Do **not** commit:

```text
Windows username
machine hostname
filesystem home path
raw GPU UUID / serial number
network addresses not required by the assay
other unrelated host identifiers
```

If a raw local capture contains a high-entropy device UUID or other machine-specific identifier, preserve the raw capture locally and bind it by SHA-256 in the public manifest. The public manifest may include a SHA-256 digest of the raw capture without publishing the raw identifier itself.

## 3. Required physical-substrate fields

Capture from the actual machine:

```text
GPU marketing name
GPU vendor/device identity as exposed by the selected backend
VRAM capacity
selected GPU/backend device index or selector
GPU driver version
OS name + build/version
CPU model
installed system RAM
externally controlled power/performance mode
GPU power limit if externally fixed
```

Instantaneous thermal/clock/power state is an execution-time measurement, not a static manifest identity. Preserve it per observation when available.

## 4. Required model identity

Capture:

```text
absolute local model path: LOCAL CUSTODY ONLY, do not publish if identifying
model filename
model file byte size
SHA-256 of exact model file
GGUF architecture / quantization metadata when exposed
model alias used by the server
```

The SHA-256 of the exact model file is authoritative for model-file identity.

## 5. Required runtime identity

Capture:

```text
llama.cpp version/build/commit reported by the binary
SHA-256 of exact server executable/binary
backend selected at runtime (e.g. Vulkan/CUDA as actually reported)
runtime command line after redacting only non-scientific local paths
n_gpu_layers
context size
parallel slots
threads / threads-batch
batch / ubatch
flash-attention setting when available
mmap/mlock settings when available
device/tensor split settings when available
reasoning-format configuration
Jinja/chat-template enablement
```

A runtime name or Git commit without the executable hash is not sufficient identity for the assay.

## 6. Tokenizer and chat-template identity

Capture the exact tokenizer/chat-template realization used by the server.

Where these are embedded in the model artifact, preserve the authoritative model metadata fields and a canonical hash of the extracted tokenizer/template metadata used for the assay.

Where an external template/config file is used, preserve its exact SHA-256.

## 7. Request/decoding identity

Before implementation review, freeze one common request/decoding contract for B/R/C:

```text
stream
max_tokens
temperature
top_p
top_k
min_p or equivalent when exposed
repeat/frequency/presence penalties when exposed
reasoning-format request fields
stop sequences
seed schedule
all other non-default decoding overrides
```

Replicate seeds must be prospectively frozen and matched across B/R/C within replicate. A permitted default schedule is:

```text
replicate 1: 1729
replicate 2: 2718
replicate 3: 3141
```

but those values acquire authority only when adopted in the completed substrate/execution manifest before implementation.

## 8. Recorder / timing identity

Capture:

```text
recorder/instrumentation version
recorder binary or source identity/hash
clock source used for primary wall latency
clock resolution when available
request-send and response-complete boundary definition
server-reported timing-field identities retained as secondary measurements
```

The primary feasibility clock must be an external monotonic wall clock around the measured request, not an ambiguously named backend timing field.

## 9. Warm-state observability

The eventual implementation must preserve enough literal evidence to distinguish:

```text
B: measured request is first inference on fresh backend
R/C: exactly one acquisition request preceded measured request on same fresh backend
```

Preserve when exposed:

```text
process IDs / session identifiers
request ordinal within process
N_prompt
N_prompt,new
prompt-evaluation time
f_sim_best
f_keep
graphs_reused
explicit cached-token field
```

Do not infer cached-token counts from proxy fields.

## 10. Local raw-capture binding

The completed public manifest should include SHA-256 identities for the exact local capture outputs used to populate it, for example:

```text
gpu/runtime inventory capture SHA-256
server --version/build capture SHA-256
server startup/device-selection capture SHA-256
model-hash capture SHA-256
model/tokenizer/template metadata capture SHA-256
```

Raw capture files may remain local if they contain identifying host/device details, provided their digests and scientifically relevant sanitized fields are frozen prospectively.

## 11. Manifest terminal

The completed successor artifact must be a separate file, for example:

```text
FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_SUBSTRATE_MANIFEST_V0_1.json
```

and may reach:

```text
SUBSTRATE_MANIFEST_FROZEN
```

only when every required scientific field is populated from actual local evidence.

Missing fields remain missing. Do not reconstruct them from historical notes.

## 12. Authority boundary

Current state:

```text
capture contract: FROZEN
actual local substrate manifest: NOT_CAPTURED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
```

**The manifest describes the machine that runs the experiment; it is not setup trivia.**
