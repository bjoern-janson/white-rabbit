# ARC-2 PATH-OP0 preregistration

**Status:** FROZEN BEFORE READING THE FRESH EXTERNAL TEST CORPUS.

## Experimental question

Does a narrowly bounded operation-ready path representation create genuinely new executable A→B routes when layered on top of frozen R1.0 anonymous role induction?

Control:

    D -> X_role -> frozen B2

Intervention:

    D -> X_role -> X_operational^path -> fixed paint-path executor

R1.0 itself is unchanged.

## Fresh external corpus

ARC-AGI-1 public evaluation set (400 tasks), from the original ARC-AGI-1 repository.

Reason for selection:
- predates ARC-AGI-2 and this solver line;
- ARC-format compatible;
- not used in B0-B3, R1.0, ConceptARC, or Mini-ARC development in this program;
- scored once for this preregistered intervention, after which it is development evidence for this branch.

No task JSON contents may be inspected before this specification and implementation are frozen.

## X_operational^path

Given one R1-normalized anonymous-role grid:

1. Infer a background role as the modal role; deterministic tie-break = lowest role id.
2. Construct 4-connected components for every non-background role.
3. For each component, compute:
   - cells
   - role
   - size and within-grid component-size rank
   - bounding box
   - border contact
   - same-component 4-neighbor degree per cell
4. Construct terminals:
   - singleton component cells;
   - cells of thin components with same-component degree <= 1.
   A component is thin iff every cell has same-component degree <= 2.
5. Construct candidate path operands only from:
   - `segment`: straight horizontal/vertical terminal-to-terminal paths;
   - `elbow`: one-bend terminal-to-terminal paths, using either orthogonal bend;
   - `ray`: terminal-to-grid-boundary paths in N/E/S/W.
6. A candidate path is admissible only when all interior cells are background. Endpoints may be foreground.
7. Each path operand exposes only:
   - kind
   - source role / target role (`-1` for boundary ray)
   - source / target component-size rank
   - source / target border-contact flag
   - bend count
   - orientation class
   - path length

No connected-object semantic labels, shortest-path search, arbitrary graph search, obstacle routing with >1 bend, template matching, learned embeddings, or task IDs.

Resource bound fixed before external scoring:
- if a grid yields more than 128 terminals, PATH-OP0 abstains on that representation;
- if more than 4,096 admissible path operands are generated, retain the 4,096 shortest then lexically earliest operands.

## Fixed executor

The executor is deliberately trivial:

    paint_path(selector, paint_role)

It:
- selects preconstructed path operands by a conjunction of at most 2 equality predicates over operand metadata;
- paints only selected path cells that are currently background, using one existing anonymous role;
- preserves all pre-existing foreground cells, including terminals/endpoints;
- preserves every other input cell;
- never deletes, moves, crops, resizes, or recolors non-path cells;
- is simultaneous from the original role grid;
- is accepted only if it reproduces every demonstration output exactly.

The executor may not invent its own operands. If the required endpoint/path is absent from `X_operational^path`, the program does not exist.

Candidate ranking is deterministic:
1. fewer selector predicates;
2. fewer selected path operands across demonstrations;
3. shorter total painted path length across demonstrations;
4. lower paint role;
5. lexical program key.

Two attempts are the two strongest distinct predicted output grids.

## Scope restrictions

PATH-OP0 is same-shape only. If any demonstration changes grid shape, it produces no program.

No:
- deletion / distractor removal
- object movement or packing
- recoloring existing foreground objects
- multi-stage composition
- recursive generation
- path search with >1 bend
- learned ranking
- LLM
- task-specific code
- absolute coordinate predicates
- post-hoc family additions

## Primary diagnostics

Across the fresh corpus record:

- `N_role_active`: tasks with >=1 R1 role representation.
- `N_operationalized`: tasks with >=1 valid path operand representation.
- `N_executable`: tasks with >=1 exact-demo-fit PATH-OP0 program.
- `N_exact_top2`: tasks solved on all test outputs by PATH-OP0 top-2.
- `N_new_routes`: exact top-2 tasks for which neither frozen R0/B2 nor frozen R1.0 has a correct candidate route.
- `rho_path = N_exact_top2 / N_executable` when `N_executable > 0`.
- candidate inflation = executable tasks - exact top-2 tasks.
- regressions under conservative routing: frozen R0 routes first, then distinct R1 routes, then PATH-OP0 only in unused attempt slots.

Also report oracle-within-PATH-OP0 exact solves separately from top-2 ranking so coverage and ranking failures remain distinct.

## Decision rule

This is a hypothesis test, not automatic retention.

Evidence for the operationalization hypothesis requires:
- `N_new_routes > 0`, and
- no regression under conservative route allocation, and
- nontrivial transfer efficiency (`rho_path` reported, not hidden by raw coverage).

If PATH-OP0 merely increases exact-fit candidate coverage without held-out solves, reject it as another expressivity expansion.

## Claim ceiling

A positive result would support only:

> Explicitly constructing bounded path operands from task-local role coordinates can create executable routes unavailable to the frozen fixed-representation solver.

It would not establish a general graph ontology, general path reasoning, or autonomous representation invention.
