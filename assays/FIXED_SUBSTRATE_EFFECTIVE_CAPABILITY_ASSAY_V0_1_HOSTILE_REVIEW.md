# Fixed-Substrate Effective Capability Assay v0.1 — Hostile Constitution Review

Status: `REVIEW_FAIL / NARROW_CONSTITUTION_REPAIR_REQUIRED / SUBSTRATE_MANIFEST_NOT_CAPTURED / NOT_EXECUTED / NON_AUTHORIZING`

Scientific observations: `0`

Implementation: `NOT_OPENED`

Scientific execution: `NOT_OPENED`

Execution authorized: `false`

Reviewed artifacts:

- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_TASKSET_V0_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_CONDITIONS_V0_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0_1.md`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_SUBSTRATE_CAPTURE_V0_1.md`

This review attacks the constituted design only. No model execution or local-machine inference was performed.

## Review terminal

```text
HOSTILE_CONSTITUTION_REVIEW: FAIL
REPAIR_SCOPE: NARROW
SUBSTRATE_GATE: NOT_SATISFIED
IMPLEMENTATION: NOT_OPENED
SCIENTIFIC_EXECUTION: NOT_OPENED
SCIENTIFIC_OBSERVATIONS: 0
```

## G1 — Phenomenon / causal target

**PASS.**

The assay correctly treats WR-OBS-001/002 as phenomenon-selection evidence rather than causal evidence. The primary controlled question is `C-R`; `R-B` is separately retained as a generic warm-runtime-state contrast.

The constitution also correctly refuses to call `R-B` a pure KV-cache effect.

## G2 — Task oracle correctness and historical-exposure firewall

**PASS.**

Q01-Q03 are explicitly marked historical floor controls and excluded from the primary frontier claim.

Q04-Q12 are prospectively frozen as the primary task family. The mechanical expected answers and uniqueness constraints were checked at review. No White Rabbit outcome for Q04-Q12 exists in the repository at freeze.

The prospective band labels are construction labels only; no empirical difficulty authority is claimed.

## G3 — B/R measured-request identity

**PASS at constitution layer.**

For each task, B and R use the same neutral prelude and the condition contract requires byte-identical measured requests. Their intended difference is prior warm/runtime state only.

Future implementation review must verify the actual serialized request bytes and hashes rather than relying on the prose contract.

## G4 — R/C protocol symmetry and candidate-path scope

**PASS with claim ceiling.**

R and C both begin from fresh processes, issue exactly one acquisition request, then one measured request without restart. The prelude differs prospectively.

The resulting `C-R` contrast is a total candidate-path contrast under a common acquisition protocol. It is **not** a pure semantic-content effect at fixed token burden or fixed realized warm state. The current claim ceiling correctly reflects that.

## G5 — Runtime-state observability

**PASS as a constitution requirement / OPEN as implementation evidence.**

The constitution correctly makes cold/warm realization an admissibility burden and forbids inferred cached-token counts. No implementation exists yet, so runtime-state realization has not been demonstrated.

This is not a constitution failure.

## G6 — Substrate identity

**NOT SATISFIED / EXPECTED BLOCK.**

The actual local RTX 3080 Ti substrate manifest does not yet exist. Historical names are insufficient. The newly frozen capture contract correctly requires machine-derived identities and hashes while avoiding unnecessary publication of raw device/host identifiers.

This gate must remain closed until actual local capture is supplied.

## G7 — Mechanical capability grader

**PASS.**

Success is exact UTF-8 byte equality after only frozen leading/trailing ASCII whitespace trim. No human or model judge exists.

## G8 — Primary latency authority

**FAIL.**

The primary frontier definition uses `L_total`, but v0.1 does not freeze which clock/measurement source has authority over `L_total`.

Possible candidates include backend-reported total time, recorder wall time, client elapsed time, or another timing field. Those can differ and need not share boundaries.

Because feasibility is defined by wall-clock budgets, this is a scientific-definition defect, not merely implementation metadata.

Required repair:

```text
L_primary := external monotonic wall-clock elapsed time
from measured-request send boundary to complete response-receipt boundary
```

or an equally explicit prospectively frozen authority. Backend timing fields may remain secondary measurements.

## G9 — Feasibility semantics

**FAIL.**

v0.1 defines a task as feasible when:

```text
all 3 runs succeed
AND
median(L_total) <= tau
```

With three runs, this permits one successful run to exceed the frozen time budget while the task is still called feasible. That does not support the constitution's repeated language of reliable feasibility *within* the time budget.

Required repair: either weaken the vocabulary or strengthen the criterion.

Recommended narrow repair:

```text
all 3 runs admissible
AND
all 3 exact-grade successes
AND
max(L_primary) <= tau
```

which directly means every constituted replicate completed correctly within the budget.

## G10 — Global execution order

**FAIL.**

v0.1 freezes condition order *within each task* by replicate, but it does not freeze the global ordering of the 12 tasks / 108 measured observations.

A future executor could therefore schedule easier/harder tasks or task blocks after observing earlier behavior, or unintentionally align task identity with thermal/time drift.

Required repair: freeze a complete outcome-independent global schedule before implementation. A simple deterministic schedule is sufficient; no new factorial is needed.

## G11 — Frontier-set logic

**PASS conditional on G8/G9 repair.**

The proper-superset rule is appropriately conservative:

```text
F_R(tau) proper subset F_C(tau)
```

requires at least one positive crossing and no negative crossing among the primary tasks at that budget.

Task-level mixed outcomes remain preserved.

## G12 — Acquisition-cost firewall

**PASS.**

R/C acquisition costs are preserved separately and are explicitly excluded from the v0.1 frontier terminal. No amortization claim is opened.

## G13 — Claim ceiling

**PASS.**

The positive terminal is local to the frozen substrate/task/condition/time-budget contract. It does not claim persistent learning, held-out reuse, amortization, compounding, general White Rabbit mechanism, or explanation of the original anecdote.

## G14 — Execution non-authorization

**PASS.**

No runner, local backend execution, acquisition request, or scientific result exists under this assay.

## Required narrow repair set

Before another constitution review:

1. Freeze one authoritative external monotonic wall-clock definition for `L_primary`.
2. Make practical feasibility actually require every constituted replicate to complete successfully within `tau` (or explicitly weaken the scientific vocabulary; preferred repair is `max(L_primary) <= tau`).
3. Freeze a complete outcome-independent global 108-observation schedule.
4. Keep the substrate manifest gate closed until actual machine-derived identities are supplied.

No other conceptual expansion is required.

## Current authority state

```text
artifact: FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1
constitution: REVIEW_FAILED / NARROW_REPAIR_REQUIRED
substrate capture contract: FROZEN
actual local substrate manifest: NOT_CAPTURED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
next action: v0.1.1 narrow constitution repair + local substrate capture
```

**STOP.**
