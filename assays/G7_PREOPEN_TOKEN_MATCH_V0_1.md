# Gate 7 PREOPEN TOKEN/CONTEXT MATCH v0.1

Status: `PREOPEN_TOKEN_MATCH_MISMATCH / ASSAY_BLOCKED`

Terminal result:

```text
PREOPEN_TOKEN_MATCH_MISMATCH
```

This is a deterministic pre-experimental template/tokenization result. It is not a Gate 7 observation, treatment inference, neutral-control inference, capability evaluation, work comparison, or White Rabbit result.

## Authority and frozen inputs

```text
starting repository HEAD: 079b524b8b0344bda1681f2f26ad23b929128ba0
assay constitution: G7_MATCHED_CONTEXT_ASSAY_V0.1.1
assay constitution commit: 079b524b8b0344bda1681f2f26ad23b929128ba0
conceptual-freeze commit: 1d7651a6c1e302eedc6c2680f574c2989af98391
authorized operation: PREOPEN_TOKEN_MATCH only
Gate 7 execution: NOT AUTHORIZED / NOT OPENED
```

The literal B and C preludes and Q1-Q3 targets were extracted from the frozen assay carrier. The Windows checkout carrier was normalized to the constitution's explicit LF source semantics before extraction. All five frozen UTF-8 SHA-256 values matched before rendering or tokenization:

| Source | UTF-8 bytes | SHA-256 |
| --- | ---: | --- |
| B prelude | 256 | `af2d192d9ce44c51190455b3434b55e0c676c9630c6a17af5d33d6c0d94f3a51` |
| C prelude | 256 | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` |
| Q1 | 84 | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` |
| Q2 | 109 | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` |
| Q3 | 155 | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` |

The literal separator SHA-256 was `7f31dacfc61dd598296a31789337fd1886023536222243b43e16a914886bf5f4`.

## Exact non-generating native path

The operation used the same frozen llama.cpp build and GGUF model as Gate 7, but on inspection-only port `8096`:

```text
executable: C:\Users\Mewn\Documents\Codex\2026-08-10\i-t-e-v-t-h\work\white-rabbit-recorder\.calibration-runtime\llama-b10603-verified\llama-server.exe
version: 0.2.0-dev (build 10603, commit c060ca974)
compiler: Clang 20.1.8 for Windows x86_64
build_info: b10603-c060ca974
model: C:\Users\Mewn\Models\Qwen3.8-27B\Qwen3.8-27B-Q2_K.gguf
model bytes: 10711665248
model SHA-256: 8d7bd72140ff0936fd8b7049917f028c91099c8896c2e4e16f0e664e6d5adb39
model alias: qwen38-27b
model ftype: Q2_K - Medium
GPU layers: 50
context size: 8192
parallel slots: 1
Jinja: enabled
reasoning format CLI: deepseek
```

Exact invocation:

```text
llama-server.exe -m C:\Users\Mewn\Models\Qwen3.8-27B\Qwen3.8-27B-Q2_K.gguf -a qwen38-27b --host 127.0.0.2 --port 8096 -ngl 50 -c 8192 -np 1 --jinja --reasoning-format deepseek
```

Native operations were limited to:

```text
GET /health
GET /props
POST /apply-template
POST /tokenize
```

No completion or generation endpoint was called. The server log contained zero task lines. The controlled process was stopped after custody, and port `8096` had zero listeners after shutdown.

## Template and tokenizer custody

The exact chat-template source was returned by the loaded frozen runtime at `/props`:

```text
chat-template UTF-8 bytes: 8952
chat-template SHA-256: c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041
```

Each single user message was passed to native `/apply-template` with `add_generation_prompt: true`. The observed suffix was:

```text
<|im_start|>assistant
<think>
```

The rendered prompt was passed to native `/tokenize` in the same loaded process with:

```json
{"add_special":true,"parse_special":true,"with_pieces":true}
```

Special-token custody:

```text
BOS: <|endoftext|> = 248044; not automatically prepended to the rendered chat prompt
EOS: <|im_end|> = 248046; not automatically appended after the generation-prompt suffix
<|im_start|> = 248045
<think> = 248068
```

The full template source, template capabilities, exact per-call request custody, rendered prompts, token IDs, token pieces, canonical token-ID JSON, server startup output, and executable hashes are preserved in `G7_PREOPEN_TOKEN_MATCH_V0_1.json`.

## Deterministic comparison

The frozen criterion is equality of total model-visible prompt-token burden for B and C within every task.

| Task | B prompt tokens | C prompt tokens | Delta C-B | Result |
| --- | ---: | ---: | ---: | --- |
| Q1 | 139 | 142 | +3 | mismatch |
| Q2 | 132 | 135 | +3 | mismatch |
| Q3 | 150 | 153 | +3 | mismatch |

All three token-count deltas zero: `NO`.

Therefore the mechanically assigned terminal result is:

```text
PREOPEN_TOKEN_MATCH_MISMATCH
```

## Per-context custody

| Context | Assembled UTF-8 bytes | Assembled SHA-256 | Rendered UTF-8 bytes | Rendered SHA-256 | Token count | Token-sequence SHA-256 |
| --- | ---: | --- | ---: | --- | ---: | --- |
| B_Q1 | 357 | `a42b103c516927f4a27cb904f874b1067bf284c9c0ef64349344a230c1100c72` | 652 | `5f51e54c3e9c1d2162893b6d032dc09d4aadae6ca44a96f42f0ea0663429b36d` | 139 | `863b5f14dc8d373cf9c0856840dfe2819571caf73285e7676f19d85a4404675d` |
| C_Q1 | 357 | `f0a6090f04d1cbca757352485c87910a044af404475c92b4f0afeed7e1d8e3e2` | 652 | `e5103154a6b518cdadfad92e67b9d4f1eda6329babd1dbdc24bbcdb1edcdfa5f` | 142 | `f1f78e1962890c55fdc24da42a74cd1636d6864c93ffaacc4b9aeeef94ee85f3` |
| B_Q2 | 382 | `727351e3ca23d862023709baf4ac4160c4c60ea478f37e3322e4efef913bb933` | 677 | `28804eb4c879eee8dc7e2a9153062c821cccdd4c555707f83e8cc7e53fd62531` | 132 | `4e8af1eb9d32c2d98f89535951f4399f403ed378b20fdc475657d02615a023cb` |
| C_Q2 | 382 | `e18548be37e23155942572febdf37fd053e41c1291ffef5768de9fdad0b13488` | 677 | `74f00ae0d14d2423e4cc1fb6e330f6a227c76d22e247043105f46ef93e93f392` | 135 | `ad0b312a3e2c71731d7e3031aa7dd278449fe826d6d3060c6458b7ec4ecaa38b` |
| B_Q3 | 428 | `7d27294719503ef82664b8d4d3ab0b7f1decf1f20a59c1ab7b0b2258a24131d6` | 723 | `939d0c73470b186ecb852c279d4d2366772922d46cf7e3f92185a63ef7de6100` | 150 | `8d10a8fef576b32807075977508ce08b99e64bf22ad4438e704d30c5ae25148f` |
| C_Q3 | 428 | `0213bd405977d731b59cd6e05950989952765e7f159d92fbecd09a094a1c4f3b` | 723 | `8959362a896cd58fd9e4839fd3be300da2c32b3c1b058dd8682d7d621a2139ba` | 153 | `dfd04ce76d0319093be895f668f8853e83afd060c2c53db099b27977d74f0da8` |

The B and C assembled and rendered byte lengths match within each task, but their token burdens do not. Byte-length equality is not promoted over the frozen token-count criterion.

## Firewall and claim ceiling

```text
generation performed: NO
sampled tokens: 0
White Rabbit Recorder started: NO
C_improve inference executed: NO
neutral-control inference executed: NO
Gate 7 assay observations executed: 0
capability grading performed: NO
scientific work comparison performed: NO
White Rabbit claim emitted: NO
```

This result supports only:

> **The frozen B/C contexts impose unequal prompt-token burden under the exact frozen pre-open template/tokenizer procedure: C is three tokens longer for Q1, Q2, and Q3.**

It does not establish semantic inequality, capability change, generated work, treatment effect, compute reduction, or any White Rabbit claim.

No source was edited or padded. The current assay is blocked pending separate review or reconstitution. Gate 7 execution remains `NOT AUTHORIZED / NOT OPENED`.

