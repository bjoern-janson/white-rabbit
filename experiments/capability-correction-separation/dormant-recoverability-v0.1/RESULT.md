# Dormant Recoverability v0.1 — Result

Terminal: `DORMANT_RECOVERABILITY_RESCUE_OBSERVED`

Contract SHA-256: `c1280fecc4a07d5584a52f0cdcba4baf4e387f844b32ad68b75b8c0c6ed171ea`

Runner SHA-256 (frozen before execution): `5cf3e768b5f2892c79c6545e1e9a63622d253109c4a974fcdd30ce728befa1b6`

## Frozen question

Does dormant recoverability remove the structural correction-cost penalty while leaving present computation unchanged?

## Present-use invisibility

The `C` and `D` conditions used byte-identical operative compressed representations.

- present policy outputs identical: `PASS`
- active logical slots identical: `120` vs `120`
- active inference usage identical: `PASS`
- dormant reads during D present inference: `0`
- accumulation/training trace identical: `PASS`
- operative canonical content hash identical: `PASS`
- current compressed policy accuracy: `1.000`
- present-use invisibility gate: `PASS`

The dormant sidecar does consume physical storage. Its exact serialized size is `4271` bytes. That storage overhead is disclosed separately and was not available to present inference or optimization.

## Future correction

Local defeaters:

- `C*_reference`: `[1, 1, 1, 1, 1, 1, 1, 1]`
- `C*_C`: `[1, 1, 1, 1, 1, 1, 1, 1]`
- `C*_D`: `[1, 1, 1, 1, 1, 1, 1, 1]`

Structural defeaters:

- `C*_reference`: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`
- `C*_C`: `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`
- `C*_D`: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`

Mean deltas relative to reference:

- local compressed `C-reference`: `0.000`
- local dormant `D-reference`: `0.000`
- structural compressed `C-reference`: `1.000`
- structural dormant `D-reference`: `0.000`

All independently validated endpoints passed: `PASS`.

## Bounded interpretation

The dormant condition preserved exactly the same operative abstraction used for present computation. The dormant sidecar was inaccessible to present policy, reward computation, optimization, and accumulation.

For local defeaters, all three conditions required the same one-step correction.

For structural defeaters, the ordinary compressed condition required two actions: create a target singleton, then write the future evidence. The dormant condition matched the reference at one action because the same `WRITE_TARGET_EVIDENCE` operation could promote an already-retained target-specific dormant record rather than first reconstructing that distinction.

## Claim ceiling

This is a local recoverability-isolation result in one synthetic learned-state abstraction world.

It supports the narrower statement that, in this substrate, the previously observed structural correction-cost penalty is not caused by using an abstraction for present computation alone. The penalty disappears when the future-relevant raw-state distinction remains dormant but cheaply reopenable, while present operative computation stays unchanged.

It does not establish a general law of irrecoverability, compression, memory, or corrigibility. The dormant sidecar has nonzero storage cost, explicitly reported above, so this experiment isolates **present-use invisibility and correction reachability**, not zero total physical resource cost.
