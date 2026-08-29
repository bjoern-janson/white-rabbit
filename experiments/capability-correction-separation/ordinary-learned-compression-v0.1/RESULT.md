# Ordinary Compression / Learned State Abstraction v0.1 — Result

Terminal: `SELECTIVE_CORRECTION_FOOTPRINT_OBSERVED`

Contract SHA-256: `00ed56a0d3a0299db795c3edadf453b191d78a6400ccf33b4188a4f7e0ebdd2b`

## Frozen question

Does ordinary present-only state compression create a selective future correction-cost footprint?

Primary prediction:

`mean ΔC*(local) ≈ 0` and `mean ΔC*(structural) > 0`.

## Present-only compression gate

Both conditions learned from the same noisy present-task observations.

- reference current policy accuracy: `1.000`
- compressed current policy accuracy: `1.000`
- reference logical model slots: `192`
- compressed logical model slots: `120`
- compressed/reference slot ratio: `0.625`
- reference reward objects: `48`
- compressed reward objects: `18`
- present gate: `PASS`

The compressor was ordinary k-means over learned present reward vectors, minimizing present reconstruction error subject to 18 reward objects. It received no correction objective and no future defeater data.

## Prospective defeater-class realization

The defeater targets and construction rule were frozen before learning.

- all 8 local targets realized as singleton compressed objects: `PASS`
- all 10 structural targets realized inside non-singleton compressed objects: `PASS`

No surprise was relabeled after seeing the learned abstraction.

## Minimum independently validated correction cost

- mean `ΔC* = C*_compressed - C*_reference` for local defeaters: `0.000`
- mean `ΔC*` for structural defeaters: `1.000`

Local paired deltas: `[0, 0, 0, 0, 0, 0, 0, 0]`

Structural paired deltas: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`

All `36` minimum-path endpoints passed the separate batch validator: `PASS`.

## Selective footprint

`ΔC*(local) = 0` for every frozen local defeater.

`ΔC*(structural) = +1` for every frozen structural defeater.

The reference repaired either class with one object-level update. For a structural defeater, the compressed representation first had to split the implicated raw state out of its learned multi-state abstraction, then update the resulting singleton object.

## Claim ceiling

This is a local result in one learned contextual-state abstraction substrate.

It establishes that an ordinary present-only k-means compression procedure, with no correction objective and no access to future defeaters, produced a selective later correction-cost penalty exactly on the prospectively frozen cases that required reopening a distinction the learned abstraction had merged, while leaving corrections to prospectively frozen singleton states unchanged.

It does not establish that compression generally causes corrective debt, that learned abstraction in other systems behaves this way, or that the effect occurs in LLMs or agentic systems.

## Execution custody correction

The first execution was performed in a notebook cell whose exact executable bytes were not prospectively saved; the initial `run.py` was only a stub. That initial execution therefore did not independently satisfy hard executable custody.

A standalone confirmation runner was subsequently frozen and hashed **before execution** and reproduced the present metrics, learned object topology, all local/structural correction-cost deltas, and independent-validation status exactly. Confirmation status: `PROSPECTIVE_EXECUTABLE_CONFIRMATION_PASS`.
