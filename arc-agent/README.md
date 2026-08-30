# White Rabbit ARC-AGI-3 Competition Agent

> **COMPETITION LANE — SCORE-OPTIMIZING.**
>
> This directory is deliberately separate from `experiments/`. Changes here do **not** change the frozen White Rabbit research claims.

## Submit from Kaggle

The ready-to-run competition notebook is committed at:

```text
notebooks/submission.ipynb
```

The intended submission workflow is simply:

```text
Kaggle
-> Import Notebook
-> select notebooks/submission.ipynb
-> Save Version / Run All
-> Submit to Competition
```

No local machine setup is required. Do **not** run `make setup` inside Kaggle.

The notebook is self-contained for the competition rerun: it embeds Submission-0, uses the competition-provided offline wheel directory and ARC agent framework, runs with internet disabled and CPU only, and lets the ARC gateway produce `submission.parquet`.

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

The improvement is dominated by `ft09`; see [`results/README.md`](results/README.md) and [`results/local_public_summary.json`](results/local_public_summary.json) for the bounded comparison.

## Source of truth

`agent/my_agent.py` remains the editable source. `notebooks/submission.ipynb` is the committed ready-to-run Kaggle artifact generated from that source by `scripts/build_notebook.py`.

If the agent changes, regenerate the notebook before committing:

```bash
python3 scripts/build_notebook.py
```

This regeneration step is for maintainers of the repo; it is **not required to submit the already-committed notebook from Kaggle**.

## Optional developer tooling

The `Makefile`, local runner, and setup scripts remain for development and regression testing. They are not part of the Kaggle submission path.

## Submission-0 limits

- No offline LLM/model is packaged yet.
- Generic exploration is not competitive across the public suite yet.
- Public score is not a hidden-set estimate.
- The `ft09` specialization is intentionally exploited in this score lane and must not be cited as evidence for the frozen research frontier.
- No Kaggle leaderboard score is recorded here until an actual competition rerun is submitted.

The research frontier remains frozen in `experiments/arc-reopening-lineage/FROZEN_FRONTIER.md`.
