# ARC-AGI-2 R0 + R1 conservative-router candidate

Status: **frozen competition candidate, not submitted**.

## Architecture

`R0/B2 fixed representations + R1.0 task-local anonymous role induction + conservative route allocation`

Router policy:

1. Preserve distinct admitted R0 outputs first.
2. Fill unused attempt capacity with the highest-ranked distinct R1 output.
3. If R0 has zero admitted candidates, let R1 supply attempts.
4. If neither source has an admitted route, inherit R0's schema-safe fallback.
5. Emit exactly two attempts per test input.

No representation-construction, synthesis, execution, or ranking mechanism changes.

Frozen hashes:

- R0/B2: `92db3a4ec0f0484773b6b19f1e65e87b84fabf5a38ba1e6698888f332e678c66`
- R1.0: `7d61faa79c8989738f72df38dd6d74800c9b8ca25435f06f0d6fb473e493b42a`

## Evidence

Prospective Mini-ARC test: R0 `27/149`, R1 `32/149`, conservative router `34/149`, with zero observed regressions of either component.

Development-only measurement on the already-spent ARC-AGI-2 120-task evaluation set: R0 `0/172` outputs, R1 `0/172`, router `0/172`. R1 induced at least one task-local representation on 20/120 tasks but frozen B2 synthesized zero exact-fit R1 candidates on all 120.

Therefore this architecture is retained as a research/engineering result, but the spent-120 measurement does **not** justify a Kaggle hidden submission by itself.

## Kaggle contract

The candidate is packaged separately as a self-contained notebook that reads `arc-agi_test_challenges.json` and writes `submission.json` with exactly `attempt_1` and `attempt_2` for every test output. The notebook has been executed against the local 240-task placeholder only as a schema/runtime check; that placeholder is not generalization evidence.
