# White Rabbit 🐇⚡

The project asks one question:

**What changed in the computational path that made the same machine dramatically more useful?**

## Workflow

```text
find the discontinuity -> explain the discontinuity -> prove the explanation
```

### 1. Phenomenon hunt — active

Use the real baseline and candidate setups on hard, meaningful tasks. Adjust task difficulty while searching.

Record only what helps locate the effect:

```text
quality / usefulness
wall-clock time
TTFT
decode rate
output tokens
failure mode
```

The interesting signal is not “a few fewer tokens.” It is a regime change:

```text
baseline: practically unusable
candidate: practically useful
```

Keep failed hunts too. They tell us where the boundary is not.

See [`HUNT.md`](HUNT.md) and [`hunt/log.csv`](hunt/log.csv).

### 2. Formal confirmation — frozen until needed

Once the hunt finds a repeatable discontinuity, freeze the exact setup and test it properly.

The previous formal machinery is preserved in Git history and on the dedicated formal-assay branch / PR. It is intentionally not the active face of this repository.

See [`FORMAL.md`](FORMAL.md).

## Historical anomaly

The original observation and its important runtime correction are preserved under [`observations/`](observations/).

The correction matters: part of the apparent speedup was consistent with retained-prefix / KV reuse, while another runtime-performance shift remained unexplained. That is why the current project hunts the phenomenon first instead of assuming a mechanism.

## Split program

```text
RESEARCH FRONTIER:  FROZEN
COMPETITION AGENT:  SCORE-OPTIMIZING
```

The scientific record remains under [`experiments/`](experiments/). Its claim ceilings, negative controls, and frozen frontier are not modified by competition engineering.

The ARC-AGI-3 score lane lives under [`arc-agent/`](arc-agent/). It is explicitly allowed to use heuristics, game-family specializations, stochastic fallbacks, and other score-seeking engineering without acquiring research authority.

Current Submission-0 local public engineering score: `1.3756373256373253` on the 25 bundled public environments. This is not a Kaggle leaderboard score or a hidden-set estimate; see [`arc-agent/results/`](arc-agent/results/) for the bounded comparison.

## Preserved research lineages

These records are kept under `experiments/` without changing the active phenomenon-first face of the repository:

- [`capability-correction-separation/`](experiments/capability-correction-separation/) — frozen synthetic lineage on selective future correction cost, learned abstraction, dormant recoverability, and operation-relative adequacy.
- [`arc-reopening-lineage/`](experiments/arc-reopening-lineage/) — synthetic reopening instruments followed by real ARC pressure tests, ending at the current upstream state-construction boundary exposed by an untouched prospective transfer failure.
  - [`FROZEN_FRONTIER.md`](experiments/arc-reopening-lineage/FROZEN_FRONTIER.md) — final separation of selection, reachability, and construction-capability change, including the dormant-constructor null hypotheses required for any future positive.

The second lineage deliberately preserves positive controls, contaminated development results, and prospective negatives as different authority classes.

## Rule of thumb

**Find where the machine suddenly stops having to struggle.**

Then figure out why.
