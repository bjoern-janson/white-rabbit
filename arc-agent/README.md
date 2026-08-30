# White Rabbit ARC-AGI-3 Competition Agent

> **COMPETITION LANE — SCORE-OPTIMIZING.**
>
> This directory is deliberately separate from `experiments/`. Changes here do **not** change the frozen White Rabbit research claims.

## Submission-0

Submission-0 converts already-earned engineering lessons into an offline Kaggle agent:

```text
observe
-> predict consequence class
-> take exactly one action
-> compare prediction with consequence
-> contract only the falsified action-effect commitment
-> choose the next action
```

The per-game agent retains:

- exact observation/action history through an online transition graph;
- action-effect outcome distributions (`noop`, `local`, `global`, `level`, `death`);
- defeated prediction records;
- state visitation counts;
- coordinate probe history;
- level-transfer state.

The competition implementation is intentionally pragmatic. It currently uses a **score-first portfolio**:

1. `ft09`: the relational frame model earned from the source-firewalled/audited real trajectory, replanned after every action;
2. `lf52`: generic transition/coordinate exploration because that policy earns a public level in the local run;
3. other game families: reproducible stochastic fallback, while consequence bookkeeping remains active.

This is not C3, autonomous ontology construction, or a research-frontier claim.

## Local public result

Using the 25 bundled public environments with `arc-agi` 0.9.8 and a 220-action cap:

```text
stable stochastic control:  0.16005291005291003
generic explorer ablation:  0.07272727272727272
Submission-0 portfolio:      1.3756373256373253
```

The improvement is dominated by `ft09`; see [`results/README.md`](results/README.md) and [`results/local_public_summary.json`](results/local_public_summary.json) for the claim ceiling and machine-readable score summary.

## Kaggle notebook

`notebooks/submission.ipynb` is **generated build output** from `agent/my_agent.py` using the official starter pattern. It is intentionally gitignored so source and notebook cannot drift.

The generated notebook:

- installs only from the competition's offline wheel directory;
- has internet disabled;
- uses the CPU accelerator;
- copies the competition-provided agent framework into `/kaggle/working`;
- registers `MyAgent` with a slim framework initializer;
- lets the ARC gateway generate `submission.parquet` on competition rerun.

Generate it with:

```bash
make notebook
```

`make submit` always regenerates it before pushing to Kaggle.

## Local setup

Requires Python 3.12.

```bash
make setup
make play-local GAME=ft09
make play-local
```

The setup follows the official `arcprize/ARC-AGI-3-Kaggle-Starter` workflow.

## Kaggle push

Before the first push:

```bash
mkdir -p .kaggle
# put the one-line Kaggle API token in .kaggle/access_token
# replace REPLACE_WITH_YOUR_USERNAME in notebooks/kernel-metadata.json
make submit
make status
```

Pushing the notebook is not the same as spending a competition submission; after the Kaggle run completes, select the generated `submission.parquet` in the competition UI.

## Submission-0 limits

- No offline LLM/model is packaged yet.
- Generic exploration is not competitive across the public suite yet.
- Public score is not a hidden-set estimate.
- The `ft09` specialization is intentionally exploited in this score lane and must not be cited as evidence for the frozen research frontier.
- No Kaggle leaderboard score is recorded here until an actual competition rerun is submitted.

## Next score work

The highest-value engineering work is now empirical and competition-only:

```text
public trajectory failures
-> game-family policy portfolio
-> fewer wasted actions
-> better cross-level transfer
-> package an offline multimodal/world-model component if it earns score
```

The research frontier remains frozen in `experiments/arc-reopening-lineage/FROZEN_FRONTIER.md`.
