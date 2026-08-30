# Submission-0 local public scorecard

These are **local public-environment engineering results**, not Kaggle leaderboard results and not research evidence for the frozen construction-capability frontier.

All three runs used the 25 bundled public ARC-AGI-3 environments, `arc-agi` 0.9.8, a 220 action cap, and stable per-game BLAKE2 seeding.

| condition | aggregate local score | salient completed levels |
|---|---:|---|
| stable stochastic control | `0.16005291005291003` | `r11l` L1 |
| generic consequence-checking explorer, `ft09` specialization disabled | `0.07272727272727272` | `lf52` L1 |
| Submission-0 score-first portfolio | `1.3756373256373253` | `ft09` L1-L3; `lf52` L1; `r11l` L1 |

The Submission-0 gain is **not** evidence that the generic REOPEN explorer broadly beats random exploration. The generic ablation underperforms this single stable stochastic control. The score-first portfolio therefore keeps:

- the earned `ft09` relational closed-loop specialization;
- the generic explorer on `lf52`, where it earns a level in this public run;
- reproducible stochastic fallback elsewhere, while still recording consequence predictions and local defeaters.

`ft09` details in the final portfolio:

```text
Level 1: 4 actions  -> score cap 115
Level 2: 7 actions  -> score cap 115
Level 3: 14 actions -> score cap 115
```

The solver intentionally stops being trusted once its relational model becomes internally inconsistent in the next context; the competition lane is free to replace that later.
