# Gate 7 Neutral-Control Reconstitution Search v0.1

Version: `G7_NEUTRAL_CONTROL_RECONSTITUTION_SEARCH_V0.1`

Status: `NO_ADMISSIBLE_TOKEN_MATCH / LANE_BLOCKED / NON_SCIENTIFIC / NON_AUTHORIZING`

Terminal state:

```text
NO_ADMISSIBLE_TOKEN_MATCH
```

```text
N_scientific_runs = 0
```

This artifact reports the exhaustive token-only search authorized by `G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.1`. It is not an independent pre-open certification, Gate 7 scientific observation, generated-output comparison, capability result, work result, or White Rabbit claim.

## Authority

```text
starting HEAD: d85c42cab4375beefeee9640a08a7ecb5739f460
contract version: G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.1
contract commit: d85c42cab4375beefeee9640a08a7ecb5739f460
contract SHA-256: 76ff861ac2004e759cdd9822f9fbfb7685392280f8af58878e66f5f3b3cad1fd
implementation: tools/g7_neutral_control_search_v0_1.py
implementation SHA-256: 68496f55765d028dc916951010fa0964484750c0ff8b2ab409dd1a951184d9e8
```

The historical `G7_MATCHED_CONTEXT_ASSAY_V0.1.1`, `B0`, C, Q1-Q3, separator, runtime, template/tokenizer semantics, and mismatch artifacts were not modified.

## Phase A — complete source-family materialization

Phase A was completed and the manifest frozen before any tokenizer/template process was started.

```text
theoretical positions: 15,625
positions processed: 15,625
source-admissible: 15,625
rejected: 0
early stop: NO
```

Manifest custody:

```text
path: assays/G7_NEUTRAL_CONTROL_SOURCE_MANIFEST_V0_1.json
manifest payload SHA-256: 860325766811324f94fbc7f42b81513e29d0d6bce44cd4f237308c84eb5e73bf
manifest file SHA-256: 158f330644a7c068ca2d92f6a631d82b135c7c825f2393e3bf072afc223ae362
```

The manifest preserves every survivor and would have preserved every rejection and its complete mechanical reason set. No candidate was invented, edited, removed, reordered, or relabeled after the manifest freeze.

## Phase B — exact native non-generating search

A dedicated controlled inspection process was used:

```text
PID: 21800
endpoint: 127.0.0.2:8097
llama.cpp: 0.2.0-dev, build 10603, commit c060ca974
server executable SHA-256: a1d19e3c770512de76c1d101e2bcf0f6bd9b2d33b94cbda5e775be69ec02a124
model: Qwen3.8-27B-Q2_K.gguf
model SHA-256: 8d7bd72140ff0936fd8b7049917f028c91099c8896c2e4e16f0e664e6d5adb39
model alias: qwen38-27b
GPU layers: 50
context size: 8192
parallel slots: 1
Jinja: enabled
reasoning format: deepseek
chat-template SHA-256: c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041
```

Only these native operations were used:

```text
GET /health: 1 startup readiness check
GET /props: 1 search-custodied call
POST /apply-template: 46,878
POST /tokenize: 46,878
completion/generation routes: 0
```

The 46,878 template/tokenization pairs comprise three recomputed C reference contexts plus all `15,625 × 3 = 46,875` admissible candidate/task contexts.

The unrelated pre-existing llama-server process at PID `37648` was not queried, stopped, modified, or reused.

## Frozen C reproduction

The dedicated process reproduced the historical C token counts exactly:

| Task | Frozen C count | Recomputed C count | Status |
| --- | ---: | ---: | --- |
| Q1 | 142 | 142 | exact |
| Q2 | 135 | 135 | exact |
| Q3 | 153 | 153 | exact |

Any disagreement would have produced `RECONSTITUTION_UNDETERMINABLE`; none occurred.

## Exhaustive exact-match result

Every source-admissible candidate was processed on Q1, Q2, and Q3. No early stopping occurred.

Observed candidate token-count vectors were:

| `(Q1, Q2, Q3)` | Candidate count |
| --- | ---: |
| `(139, 132, 150)` | 10,000 |
| `(140, 133, 151)` | 5,000 |
| `(141, 134, 152)` | 625 |

The required exact vector was:

```text
(142, 135, 153)
```

Therefore:

```text
exact-match candidate count: 0
complete MATCH_SET: empty
B1 selected: NO
B1 artifact created: NO
terminal state: NO_ADMISSIBLE_TOKEN_MATCH
```

No tolerance, averaging, `±1`, padding, offset correction, task tradeoff, family expansion, or semantic preference was applied.

## Token and search custody

```text
token custody path: assays/G7_NEUTRAL_CONTROL_TOKEN_CUSTODY_V0_1.jsonl
token custody SHA-256: 5a4dedca2428890cf2d471ca64ffb570ae9e65a7893721e347b3bc96820430aa
token context records: 46,875

machine search path: assays/G7_NEUTRAL_CONTROL_RECONSTITUTION_SEARCH_V0_1.json
machine search SHA-256: a9409b50de385e9d4f529e03772efdaafc58c344c0aa811fdf736b55094814f5
```

The token-custody JSONL preserves, for every candidate/task context, assembled-message hash, rendered-prompt hash and byte count, exact token IDs, canonical token-sequence hash, and total prompt-token count. The machine search artifact preserves all candidate count vectors, complete match set, runtime custody, C reproduction, route counts, and zero-generation attestation.

## Process closure and firewall

```text
dedicated process stopped: YES
listeners on inspection port 8097 after stop: 0
llama.cpp task log lines: 0
sampled/generated tokens: 0
assistant output observed: NO
White Rabbit Recorder started: NO
capability observed: NO
N_generated observed: NO
latency comparison performed: NO
scientific runs: 0
White Rabbit claim emitted: NO
```

## Claim ceiling and stop state

This result establishes only:

> **The complete frozen `B_neutral` family contained no source-admissible candidate whose exact native prompt-token counts equaled C on all three frozen tasks.**

It does not establish that no neutral control can ever match, that C has a behavioral effect, semantic inequality, capability change, work change, or any White Rabbit property.

```text
neutral-control search: NO_ADMISSIBLE_TOKEN_MATCH / LANE_BLOCKED
CONTROL_RECONSTITUTED: NOT EMITTED
PREOPEN_TOKEN_MATCH_MATCH: NOT EMITTED
G7 v0.1.2: NOT CREATED
independent re-match: NOT AUTHORIZED / NOT OPENED
Gate 7 execution: NOT AUTHORIZED / NOT OPENED
N_scientific_runs: 0
```

The frozen family is not expanded by this result. Any successor search family would require a separate reviewed constitution and authorization.

