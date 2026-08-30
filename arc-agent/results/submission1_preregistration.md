# Submission-1 preregistration: context-scoped consequence authority

Status: **LOCKED BEFORE S1 CODE CHANGE**

Competition lane only. The frozen research lineage is not modified by this experiment.

## Baseline

- Hidden Kaggle score: `S0 = 0.19`
- Leaderboard snapshot at measurement: `#1690 / 2628`
- Baseline repository commit: `845dbbc3c9838b4e41d1bef84cab791197204720`
- Baseline `arc-agent/agent/my_agent.py` blob SHA: `57c65e72434912efbd9a2f1480b7efdb604bec10`
- Public aggregate score under the frozen 25-environment, 220-action evaluation: `1.3756373256373253`

The S0 agent already contains one-action consequence checking and surgical REOPEN bookkeeping. S1 does **not** add that reflex. The intervention changes only the scope at which consequence evidence is allowed to acquire predictive/policy authority.

## Hypothesis

`H1`: **Scoping consequence authority to observed context improves unseen transfer relative to action-global authority.**

Hidden prediction: `S1 > S0`.

Secondary predictions:

- cross-context false transfer decreases;
- post-contradiction persistence of a defeated prediction decreases.

A flat or negative hidden result is admissible evidence that fragmentation costs outweigh the protection gained by contextualization under this agent architecture.

## Only conceptual intervention

S0:

`P(o | a)`

S1:

`P(o | c, a)`

with hierarchical backoff:

`exact visible state -> level -> global -> unknown`

### Immutable context definition

S1 reuses the state identifier already present in S0:

`state_key = f"{levels_completed}:{BLAKE2(frame_bytes)}"`

Both `levels_completed` and the current frame are available to the agent at decision time. The context identifier may not use future outcomes, hidden engine state, post-hoc clustering, source access, or any information unavailable at the action decision.

Formally:

`c_t = f(agent-visible history <= t)`

and never `f(future outcome, hidden state, post-hoc grouping)`.

## Authority hierarchy

### Local authority

An observation updates only the exact `(state_key, action)` bucket first.

Repetition in the same state may increase local confidence but cannot itself justify broader authority.

`n x (c1, a) !=> (c2, a)`

### Level promotion

A level-scoped claim is available only after compatible evidence exists across at least **two distinct state keys in that level**.

All currently observed local dominant outcomes for that `(level, action)` must agree. A contrary local observation revokes the level promotion while preserving the local observations.

### Global promotion

A global claim is available only after compatible level promotions exist across at least **two distinct levels**.

All supporting level promotions must agree, and any contrary observed local dominant outcome in any level defeats the global promotion. Revoking the global claim does not erase supporting local evidence.

Thus:

`local evidence -> cross-state invariance -> cross-level invariance -> global authority`

with no shortcut from repetition.

## Prediction/use rule

For an action in the current state, use the narrowest justified source:

1. exact `(state_key, action)` evidence;
2. earned level promotion;
3. earned global promotion;
4. otherwise `unknown` / existing exploration behavior.

## Contradiction rule

A contradiction revokes the authority of the claim that predicted incorrectly at its earned scope. It does not erase unaffected narrower observations.

`falsify generalization != erase observations`

## Frozen components

S1 may not change:

- exploration policy structure;
- coordinate candidate generation;
- the earned `ft09` solver;
- state construction;
- action budget;
- terminal / give-up logic;
- stochastic seed policy;
- proposer machinery;
- game-family portfolio routing;
- hidden-interface access.

Only existing uses of consequence evidence may be changed from action-global aggregation to the declared context hierarchy.

## Behaviorally inert S0 microscope check

Before S1 modification, S0 was run on all 25 public environments with and without an external logging wrapper under the same deterministic per-game seed policy.

Result:

- aggregate score without microscope: `1.3756373256373253`
- aggregate score with microscope: `1.3756373256373253`
- total environment actions compared: `4450`
- action-trace mismatches: `0`

Therefore the microscope was behaviorally inert on this public evaluation.

## S0 microscope snapshot

Across `4425` observed post-action consequences:

- non-unknown S0 predictions: `2925`
- contradictions among non-unknown predictions: `468` (`16.0%`)
- predictions made in an exact state/action context with no prior local observation but with action-global evidence from elsewhere: `2753`
- false transfers among those cross-context predictions: `424` (`15.401380312386487%`)
- repeated exact `(state, action)` consequences: `173`
- outcome counts: `noop=732`, `local=2519`, `global=1119`, `death=50`, `level=5`

These are diagnostic public measurements, not evidence about which mechanism produced the hidden `0.19`.

## Submission discipline

The experiment terminates at one hidden submission of the S1 candidate.

No second conceptual change may be bundled before that measurement.

`Delta S_hidden = S1 - 0.19`
