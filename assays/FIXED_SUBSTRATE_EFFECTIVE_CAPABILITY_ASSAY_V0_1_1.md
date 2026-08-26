# Fixed-Substrate Effective Capability Assay v0.1.1 — Narrow Constitution Repair

Version: `FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1.1`

Status: `CONSTITUTED / SUBSTRATE_MANIFEST_REQUIRED / HOSTILE_REREVIEW_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

Scientific observations under this constitution: `0`

Parent constitution:

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0_1.md`

Parent hostile review:

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0_1_HOSTILE_REVIEW.md`

## 1. Repair scope

v0.1 failed hostile review on exactly three constituted definitions:

```text
primary wall-clock authority was ambiguous
median latency did not imply every replicate was within budget
global 108-observation order was not frozen
```

v0.1.1 repairs only those defects.

It does **not** alter:

```text
the phenomenon-selection anchor
Q01-Q12 task bytes or expected outputs
Q01-Q03 historical-floor-control status
Q04-Q12 primary frontier membership
B/R/C condition construction
canonical B* or C_improve preludes
warm acquisition protocol
30/60/120 second budgets
raw Q/L/W/T/M/F preservation
proper-superset frontier logic
acquisition-cost firewall
claim ceiling
```

The failed v0.1 constitution and review remain historical records.

## 2. Frozen effective upstream contract

The v0.1.1 assay is governed prospectively by:

### Task set

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_TASKSET_V0_1.json`

Frozen blob:

`88c1d7ad0de9051414608a52d5534e4eaeec70ee`

### B/R/C construction

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_CONDITIONS_V0_1.json`

Frozen blob:

`f069be6b5de80b386de897c05105a9057124583f`

### Substrate-capture contract

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_SUBSTRATE_CAPTURE_V0_1.md`

The actual local substrate manifest remains absent and must be captured from the real machine.

### Global execution schedule

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_EXECUTION_SCHEDULE_V0_1.json`

Freeze commit:

`f3404d1fdd2ed98677d189c54f595f1459698c9e`

### Adjudication repair

`assays/FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ADJUDICATION_V0_1_1.json`

Freeze commit:

`659cc87f5c9da2b9830b64f4bce221a9d84e8dad`

Where the v0.1 condition artifact's descriptive feasibility field conflicts with the v0.1.1 adjudication repair, the v0.1.1 adjudication artifact is authoritative for scientific feasibility. B/R/C request construction remains governed by the unchanged condition contract.

## 3. Primary latency authority

Freeze:

```text
L_primary := external monotonic wall-clock elapsed time
```

with boundaries:

```text
START: immediately before the client/recorder submits the complete measured request to the HTTP transport
STOP:  immediately after the complete measured response body has been received, before grading or post-processing
```

Backend-reported `total time`, prompt-eval time, generation time, TTFT, and related fields remain important secondary literal measurements but do not adjudicate practical feasibility.

If authoritative `L_primary` is missing or invalid:

```text
RUN_INADMISSIBLE_PRIMARY_LATENCY
```

## 4. Reliable within-budget feasibility

For every condition `X`, primary task `q`, and frozen budget `tau`:

```text
q in F_X(tau)
```

iff:

```text
all 3 constituted replicates are admissible
AND
all 3 exact-byte grades are SUCCESS = 1
AND
all 3 L_primary values are <= tau
```

Equivalently after admissibility/success:

```text
max(L_primary_1,L_primary_2,L_primary_3) <= tau
```

This replaces the failed v0.1 median criterion.

The primary tasks remain exactly:

```text
Q04,Q05,Q06,Q07,Q08,Q09,Q10,Q11,Q12
```

Q01-Q03 remain historical floor controls and do not enter the primary frontier set.

## 5. Complete global schedule

The exact global order is generated deterministically by the frozen schedule artifact.

Summary:

```text
replicate 1: tasks Q01->Q12; condition order B,R,C
replicate 2: tasks Q12->Q01; condition order R,C,B
replicate 3: tasks Q01->Q12; condition order C,B,R
```

Each emitted B/R/C measured observation starts its own fresh backend and recorder/session. R/C perform exactly one acquisition request inside that observation before the measured request.

No slot may be reordered because of outcomes, latency, thermal behavior, memory behavior, or prior observations.

No replacement schedule is constituted in v0.1.1.

## 6. Frontier endpoint unchanged

For every frozen `tau in {30,60,120}`:

```text
F_B(tau)
F_R(tau)
F_C(tau)
```

must be reported from the repaired feasibility rule.

The primary positive candidate condition remains:

```text
exists tau such that F_R(tau) is a proper subset of F_C(tau)
```

and only then may a separately authorized result emit:

```text
FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_FRONTIER_SHIFT_OBSERVED
```

Otherwise, after complete admissible execution:

```text
FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_FRONTIER_SHIFT_NOT_OBSERVED
```

All task-level crossings and raw Q/L/W/T/M/F measurements remain preserved irrespective of terminal.

## 7. Substrate gate remains hard

The exact local substrate is part of the scientific object.

No implementation may open until an actual machine-derived successor manifest has frozen the scientifically required identities defined by the capture contract, including exact model and runtime hashes and the local GPU/runtime selection.

```text
LOCAL SUBSTRATE MANIFEST ABSENT
=> IMPLEMENTATION NOT_OPENED
```

Historical repository names cannot satisfy this gate.

## 8. Sampling / seed gate

The completed substrate/execution manifest must prospectively freeze all request/decoding settings and a three-replicate seed schedule matched across B/R/C within replicate.

No post-outcome seed choice is admissible.

## 9. Claim ceiling unchanged

A positive result may establish only:

> Under the exact frozen local Qwen/RTX-3080-Ti substrate, B/R/C path contract, primary task set, runtime-state protocol, and frozen time budgets, the candidate structured path expanded the set of mechanically verified tasks reliably feasible within the budget relative to the warm neutral runtime-state control.

It does not establish:

```text
C_improve caused WR-OBS-001
a general White Rabbit mechanism
persistent learning
held-out transfer or reuse
amortization
lifecycle cost reduction
compounding improvement
general capability improvement across substrates
```

## 10. Authority boundary

This artifact authorizes none of:

```text
scientific runner implementation
local llama-server startup for this assay
acquisition requests
108 measured requests
frontier result generation
scientific interpretation
```

Current state:

```text
artifact: FIXED_SUBSTRATE_EFFECTIVE_CAPABILITY_ASSAY_V0.1.1
task set: FROZEN
B/R/C contract: FROZEN
latency/feasibility adjudication: FROZEN
global schedule: FROZEN
substrate capture contract: FROZEN
actual local substrate manifest: NOT_CAPTURED
hostile rereview: REQUIRED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
```

Next action:

```text
1. hostile technical re-review of exact v0.1.1 repair
2. capture and freeze actual local substrate manifest
3. independent review / implementation gate as separately required
4. STOP before scientific execution
```

**The frontier is the endpoint; the runtime counters explain it afterward.**
