# White Rabbit 🐇⚡

White Rabbit started with a simple anomaly:

> On the same local RTX 3080 Ti, Qwen went from slow and not very useful to surprisingly capable reasoning at a usable pace.

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

## Rule of thumb

**Find where the machine suddenly stops having to struggle.**

Then figure out why.
