# Phenomenon Hunt 🐇

Purpose: **make the weird local-machine effect happen again.**

This is exploration, not confirmation. Adapt the task difficulty as you learn.

## Compare

```text
B = practical old / baseline path
C = practical new / candidate path
```

Use the same machine when practical, but do not turn the hunt into a metadata project.

## Good tasks

Prefer work where practical reasoning matters:

- debugging and root-cause analysis
- difficult coding changes
- architecture/design problems
- multi-constraint synthesis
- contradiction finding
- unfamiliar multi-step reasoning

Avoid optimizing the hunt around toy formatting tasks.

## Record per run

```text
task
condition B or C
output / result
useful? (yes/no/partial)
wall-clock time
TTFT
decode rate
output-token count
failure mode / short note
```

## Search rule

```text
both succeed -> increase difficulty
both fail -> reduce difficulty or change family
B and C separate -> probe neighboring tasks
```

Keep negative results.

## What counts as prey?

Interesting:

```text
same or better quality, much lower latency
```

Strong:

```text
C quality > B quality AND C latency < B latency
```

Rabbit:

```text
B is practically unusable AND C is practically useful
```

A single anecdote is a lead. A similar separation on nearby tasks or repeated attempts is a specimen worth dissecting.

## First mechanistic fork

If decode throughput jumps dramatically, investigate runtime acceleration first.

If decode throughput stays roughly similar while C reaches equal/better answers with much less output work or lower total latency, investigate the computational path / representation.

If quality rises while latency falls without a giant raw-throughput shift, stop broad searching and dissect that case.

## Stop condition

When a repeatable discontinuity appears:

```text
hunt -> mechanism dissection -> formal confirmation
```

Do not drag formal confirmation machinery into the hunt before there is prey.
