# Cross-Compressor Replication v0.1 — Result

Terminal: `CROSS_COMPRESSOR_REPLICATION_PASS`

Contract SHA-256: `e2af94cd07a418e67533566633bd0fb42e11a4f57931ea946e13a3aa7eb4113b`

Runner SHA-256 (frozen before execution): `02be6afceadc8c03cfdd6d074731ecac03c6b1e1c906af21f4a354caadc81e57`

## Frozen question

Does the selective correction footprint replicate across materially different present-only compression mechanisms?

The two new compressors were Ward-like hierarchical agglomeration and greedy k-medoids / prototype compression. Both optimized only present reward-vector distortion under the same 18-object budget. Neither received a correction objective or future-defeater data.

## Present gate

Reference: current policy accuracy `1.000`, logical model slots `192`, reward objects `48`.

Agglomerative compression: current policy accuracy `1.000`, logical slots `120`, objects `18`, present gate `PASS`, prospective class-realization gate `PASS`.

K-medoids compression: current policy accuracy `1.000`, logical slots `120`, objects `18`, present gate `PASS`, prospective class-realization gate `PASS`.

## Selective correction footprint

Agglomerative:

- local deltas: `[0, 0, 0, 0, 0, 0, 0, 0]`
- structural deltas: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`
- mean local ΔC*: `0.000`
- mean structural ΔC*: `1.000`

K-medoids:

- local deltas: `[0, 0, 0, 0, 0, 0, 0, 0]`
- structural deltas: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`
- mean local ΔC*: `0.000`
- mean structural ΔC*: `1.000`

All independently validated correction endpoints passed.

For both compressors, `ΔC*(local) = 0` for 8/8 prospective local defeaters and `ΔC*(structural) = +1` for 10/10 prospective structural defeaters. The additional cost appears only when future evidence requires reopening a raw-state distinction that the present-only compressor merged.

## Custody

The complete runner was written and hashed before execution. Post-execution hashes for the contract, manifest, defeater specification, validator, and runner all match their frozen values.

## Claim ceiling

This is a **cross-compressor replication within one synthetic learned-state world**. It supports the narrower statement that the selective local-vs-structural correction-cost footprint is not specific to k-means geometry in this world: it also appeared under hierarchical agglomeration and medoid/prototype compression.

It does not establish that compression in general causes future corrective debt. All three compression mechanisms operated on the same deliberately transparent reward-vector substrate, and all three learned the same coarse topology because the present equivalence structure is strong.
