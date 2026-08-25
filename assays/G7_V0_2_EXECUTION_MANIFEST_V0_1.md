# Gate 7 v0.2 Operational Execution Manifest v0.1

Version: `G7_V0_2_EXECUTION_MANIFEST_V0.1`

Status: `FROZEN_PROSPECTIVE / NOT_STARTED / OPERATIONAL_ONLY / NON_AMENDING`

Assay authority: `assays/G7_MATCHED_CONTEXT_ASSAY_V0_2.md`

Assay commit: `72b3f639a829cea5a033874f0f814d80e8d3055a`

This manifest binds the 30 already-constituted assay slots before scientific run 01. It cannot change the assay, authorize extra requests, replace a failed slot, or contain an outcome.

## Frozen sources

| Object | UTF-8 SHA-256 |
| --- | --- |
| canonical neutral control `B*` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` |
| literal `C_improve` treatment `C` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` |
| Q1 target | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` |
| Q2 target | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` |
| Q3 target | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` |

## Frozen executor expectation

```text
llama.cpp build: b10603
llama.cpp commit: c060ca974
model: Qwen3.8-27B-Q2_K.gguf
model alias: qwen38-27b
GPU layers: 50
context size: 8192
parallel slots: 1
Jinja: enabled
reasoning format: deepseek
backend: 127.0.0.2:8086
recorder: 127.0.0.1:8085
recorder version: 0.1.0
recorder reported commit: 80cddb26a7b851d218f95317cd3c5b0593acd831
endpoint: POST /v1/chat/completions
stream: false
max_tokens: 64
sampling overrides: absent
```

Every slot requires its own new backend PID, new recorder PID/session, zero prior measured requests, exact cold-state evidence, exactly one scientific request, one exact task/slot correlation block, raw-byte/hash custody, and process teardown before the next slot.

## Frozen slots

| Run | Pair | Replicate | Task | Condition | Target SHA-256 | Prelude SHA-256 | Expected runtime | Prospective status |
| ---: | ---: | ---: | --- | --- | --- | --- | --- | --- |
| 01 | 1 | 1 | Q1 | `B*` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 02 | 1 | 1 | Q1 | `C` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 03 | 2 | 1 | Q2 | `C` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 04 | 2 | 1 | Q2 | `B*` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 05 | 3 | 1 | Q3 | `B*` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 06 | 3 | 1 | Q3 | `C` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 07 | 4 | 2 | Q1 | `C` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 08 | 4 | 2 | Q1 | `B*` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 09 | 5 | 2 | Q2 | `B*` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 10 | 5 | 2 | Q2 | `C` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 11 | 6 | 2 | Q3 | `C` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 12 | 6 | 2 | Q3 | `B*` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 13 | 7 | 3 | Q1 | `B*` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 14 | 7 | 3 | Q1 | `C` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 15 | 8 | 3 | Q2 | `C` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 16 | 8 | 3 | Q2 | `B*` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 17 | 9 | 3 | Q3 | `B*` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 18 | 9 | 3 | Q3 | `C` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 19 | 10 | 4 | Q1 | `C` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 20 | 10 | 4 | Q1 | `B*` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 21 | 11 | 4 | Q2 | `B*` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 22 | 11 | 4 | Q2 | `C` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 23 | 12 | 4 | Q3 | `C` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 24 | 12 | 4 | Q3 | `B*` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 25 | 13 | 5 | Q1 | `B*` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 26 | 13 | 5 | Q1 | `C` | `eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 27 | 14 | 5 | Q2 | `C` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 28 | 14 | 5 | Q2 | `B*` | `3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 29 | 15 | 5 | Q3 | `B*` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `37e85197d6c68dcf9bc0027cc4b9e5900041af6e0f5cbe77b954a209349c5663` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |
| 30 | 15 | 5 | Q3 | `C` | `886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400` | `62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a` | `G7_V0_2_FROZEN_EXECUTOR` | `NOT_STARTED` |

No adaptive ordering, early stop, silent rerun, or 31st request is authorized. An inadmissible original slot remains preserved; replacement observations require a separate outcome-blind authorization.

