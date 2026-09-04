# Fixed-Substrate Effective Capability Assay v0.1.1 — Hostile Technical Re-review

Status: `HOSTILE_TECHNICAL_REREVIEW_PASS / LOCAL_SUBSTRATE_GATE_NOT_SATISFIED / REVIEWER_INDEPENDENCE_NOT_ESTABLISHED / NOT_EXECUTED / NON_AUTHORIZING`

Scientific observations: `0`

Implementation: `NOT_OPENED`

Scientific execution: `NOT_OPENED`

Execution authorized: `false`

Reviewed repaired artifacts:

- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_TASKSET_V0_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_CONDITIONS_V0_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_SUBSTRATE_CAPTURE_V0_1.md`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_EXECUTION_SCHEDULE_V0_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ADJUDICATION_V0_1_1.json`
- `assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0_1_1.md`

This re-review was performed in the same assistant workflow that authored the repair. It is adversarial in method but does not claim independent reviewer provenance.

## Review terminal

```text
SUBSTANTIVE_HOSTILE_TECHNICAL_REREVIEW: PASS
LOCAL_SUBSTRATE_MANIFEST: NOT_CAPTURED
INDEPENDENT_REVIEWER_PROVENANCE: NOT_ESTABLISHED
IMPLEMENTATION: NOT_OPENED
SCIENTIFIC_EXECUTION: NOT_OPENED
SCIENTIFIC_OBSERVATIONS: 0
```

## R1 — Repair scope preservation

**PASS.**

The v0.1.1 successor changes only:

```text
primary latency authority
within-budget feasibility rule
global execution order
```

The task bank, task roles, B/R/C condition construction, acquisition protocol, 30/60/120 second budgets, proper-superset endpoint, acquisition-cost firewall, and claim ceiling are unchanged.

## R2 — Primary latency authority

**PASS.**

`L_primary` is now prospectively defined as an external monotonic wall-clock interval with explicit request-send and full-response-receipt boundaries.

Backend/server timing fields remain secondary literal measurements and cannot silently substitute for the feasibility clock.

Missing/invalid primary timing is explicitly inadmissible.

This resolves the v0.1 timing-source ambiguity.

## R3 — Reliable within-budget feasibility

**PASS.**

For every condition/task/budget, v0.1.1 requires:

```text
3/3 admissible
3/3 exact-grade success
3/3 L_primary <= tau
```

Equivalently, after admissibility and success:

```text
max(L_primary) <= tau
```

Therefore a task called feasible under the frozen contract actually completed correctly within the budget on every constituted replicate. The failed median-only semantics are no longer operative.

## R4 — Global execution order

**PASS.**

The complete 108-observation order is frozen by deterministic rule before implementation:

```text
rep 1: Q01->Q12; B,R,C
rep 2: Q12->Q01; R,C,B
rep 3: Q01->Q12; C,B,R
```

Every observation starts a fresh backend/recorder; R/C acquisition occurs inside its own slot. No outcome-dependent reorder or immediate unscheduled replacement is permitted.

This resolves the v0.1 global-order gap without introducing a larger factorial.

## R5 — Task oracle / novelty firewall

**PASS.**

Q01-Q03 remain historical controls only. Q04-Q12 remain the sole primary frontier set. Their exact mechanical answers were reviewed for correctness; the constrained-ordering and subset tasks were checked for uniqueness under their frozen statements.

No prior White Rabbit outcome for Q04-Q12 is used by the assay.

## R6 — B/R causal identity

**PASS at specification layer.**

B and R share the same neutral prelude and same frozen task; measured-request construction is required to be byte-identical for a fixed task. Their intended difference is prior warm/runtime state.

Actual full serialized request hashes remain a future implementation-review burden and must be checked before scientific execution.

## R7 — R/C scope

**PASS with existing ceiling.**

R and C use the same one-acquisition/one-measurement protocol. Their preludes differ prospectively. `C-R` therefore remains a total candidate-path effect under a common acquisition protocol, not a pure semantic effect at fixed token burden or an assertion of identical realized warm state.

No stronger causal label has been added.

## R8 — Runtime-state control

**PASS as constituted burden.**

`R-B` remains a generic warm-runtime-state contrast. The documents explicitly deny that it isolates KV cache from thermal/JIT/allocator/other warm-state consequences.

Runtime-state realization must still be evidenced by the future implementation; failure produces inadmissibility rather than interpretation.

## R9 — Frontier terminal logic

**PASS.**

The primary positive condition remains:

```text
exists tau in {30,60,120} such that F_R(tau) is a proper subset of F_C(tau)
```

A negative crossing prevents proper-superset status at that budget. Mixed task-level states and all raw Q/L/W/T/M/F evidence remain preserved.

The repair did not weaken the frontier criterion.

## R10 — Acquisition-cost firewall

**PASS.**

Acquisition cost remains separately preserved and excluded from the frontier terminal. No amortization or lifecycle-cost conclusion is opened.

## R11 — Substrate capture contract

**PASS as capture specification / GATE NOT SATISFIED.**

The capture contract correctly treats the local machine as part of the scientific object, requires exact model/runtime hashes and current machine-derived identities, and prevents historical repository names from standing in for current substrate evidence.

It also avoids requiring publication of raw host/user/GPU UUID identifiers when a digest plus sanitized scientific fields is sufficient.

However, the actual machine-derived substrate manifest does not exist yet.

Therefore:

```text
SUBSTRATE_MANIFEST_FROZEN = NO
IMPLEMENTATION_OPEN = NO
```

## R12 — Sampling / seed discipline

**PASS as pre-implementation requirement.**

The completed substrate/execution manifest must freeze all decoding settings and a replicate seed schedule matched across B/R/C within replicate before implementation. No outcome-conditioned seed selection is allowed.

## R13 — Claim ceiling

**PASS.**

A future positive result remains local to the exact frozen substrate/task/path/time-budget contract and does not claim explanation of WR-OBS-001, general White Rabbit mechanism, persistent learning, transfer, amortization, compounding, or cross-substrate generality.

## R14 — Execution non-authorization

**PASS.**

No scientific runner, local model request, acquisition request, measured observation, or result has been produced.

## Reviewer-independence note

This re-review does **not** satisfy any requirement for independent reviewer provenance because the same assistant workflow authored the repair.

It establishes only:

```text
SUBSTANTIVE_TECHNICAL_REPAIR_SURVIVED_HOSTILE_REREVIEW
```

not:

```text
INDEPENDENT_REVIEW_PASS
```

## Current authority state

```text
artifact: FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1.1
task set: FROZEN
B/R/C contract: FROZEN
latency/feasibility adjudication: FROZEN
global schedule: FROZEN
substrate capture contract: FROZEN
substantive hostile technical rereview: PASS
actual local substrate manifest: NOT_CAPTURED
independent reviewer provenance: NOT_ESTABLISHED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
next action: CAPTURE ACTUAL LOCAL SUBSTRATE
```

**STOP AT THE MACHINE.**
