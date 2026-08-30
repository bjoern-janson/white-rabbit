# Fresh external test: conservative R0+R1 routing on Mini-ARC

Status: preregistered before reading any Mini-ARC task JSON contents or outputs.

## Frozen mechanisms

- R0/B2 SHA-256: `92db3a4ec0f0484773b6b19f1e65e87b84fabf5a38ba1e6698888f332e678c66`
- R1.0 SHA-256: `7d61faa79c8989738f72df38dd6d74800c9b8ca25435f06f0d6fb473e493b42a`
- No representation-construction, synthesis, execution, or ranking mechanism changes.

## Single intervention

Replace R1.0's implicit replacement routing with conservative route allocation:

1. If R0 has admitted candidates, preserve its distinct predicted outputs first.
2. Fill any unused attempt slot with the highest-ranked distinct R1 output.
3. If R0 has zero admitted candidates, let R1 supply the attempts.
4. If neither route source has an admitted route, inherit the existing schema-safe fallback.
5. Maximum two attempts. No truth-dependent choice. No task IDs. No confidence threshold tuning.

This is a routing intervention only. R0 and R1 remain frozen.

## Fresh corpus

Mini-ARC (`KSB21ST/MINI-ARC`, `data/MiniARC`), published with *Playgrounds for Abstraction and Reasoning* (2022). It has not been used in the B0-B3, R1.0, or ConceptARC development loops.

The corpus is cloned only inside the scoring workflow after this preregistration and router code are frozen.

## Primary comparison

`R1.0` versus `conservative(R0,R1)`.

Also report frozen R0 as a reference baseline.

Primary measurements:

- exact full-task solve rate
- exact output accuracy
- `N_R0_regressions`: tasks solved by R0 but not by the router
- `N_R1_regressions`: tasks solved by R1.0 but not by the router
- `N_router_gains_vs_R1`
- `N_R1_only_gains_retained`: R1.0-only full solves that remain solved by router
- `N_complementary_gains`: tasks solved by router where neither R0 nor R1.0 alone solves the complete task, with correct outputs supplied by materially distinct route sources
- number of test outputs whose attempt set differs between R1.0 and router

## Interpretation locked in advance

- Router improves with no R0 regressions: evidence that bounded route authority transfers to a fresh ARC-like corpus.
- Tie with no regressions: conservative routing preserves competence but has not bought fresh capability.
- Regression versus R0 or R1: router not retained.
- Complementary gains are counted separately from ordinary R1-only gains.

No solver changes are allowed between reading Mini-ARC task contents/results and recording this run.