# Preservation-Cost Sweep v0.1 — Result

Contract SHA-256:

```text
c96064ce808af9cdfe8108e402f8a5c567caf6f288fd98b0d5f2e86aef335cbb
```

## Frozen question

Does the v0.2 correction-cost separation persist across a preservation-cost sweep?

## Execution validity

The completed sweep evaluated:

```text
8 accumulation states x 16 prospective surprises = 128 correction evaluations
```

All 128 discovered shortest-path endpoints passed the independent validation rule.

## Sweep

| State | lambda | Present V | Compiled groups | Mean C* | Max C* | Surprises with C*>1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P anchor | — | 653 | 8 | 4.500 | 8 | 8/16 |
| C_lambda_0 | 0 | 653 | 8 | 1.500 | 2 | 8/16 |
| C_lambda_1 | 1 | 552 | 6 | 1.375 | 2 | 6/16 |
| C_lambda_2 | 2 | 552 | 6 | 1.375 | 2 | 6/16 |
| C_lambda_3 | 3 | 507 | 5 | 1.3125 | 2 | 5/16 |
| C_lambda_4 | 4 | 465 | 4 | 1.250 | 2 | 4/16 |
| C_lambda_6 | 6 | 465 | 4 | 1.250 | 2 | 4/16 |
| C_lambda_8 | 8 | 427 | 3 | 1.1875 | 2 | 3/16 |

Within this substrate, increasing the resource cost of preserving source structure caused the productive optimizer to compile fewer groups. Present productive capability fell while mean future validated correction cost also fell.

## Lambda = 0 control

At `lambda=0`, preservation is free in the frozen accounting:

```text
V(C_0) = V(P) = 653
```

but:

```text
mean C*(C_0,e) = 1.5
mean C*(P,e)   = 4.5
```

Thus the productive capability gap does not appear when preserving the source representation carries no resource price, while the correction-cost disadvantage of discarding it remains.

## Structural locality / internal null region

Under the no-preservation P anchor, accumulation compiled eight groups and discarded their source rules.

Exactly those eight surprise locations produced `C*>1`.

The eight surprises hitting source-only groups remained one-action corrections.

The effect therefore does not appear as generic global brittleness. In this substrate, the future correction burden tracks whether the future shock interrogates structure actually changed by accumulation.

## Earned result boundary

> **A synthetic capability–correction frontier was observed under finite-resource productive accumulation, and the future correction burden tracked the structures actually changed by accumulation.**

This is still a compilation-substrate result.

## Execution-custody correction

The original sweep execution occurred in an interactive notebook harness. The frozen contract, exact accumulation states, surprise family, validator, derived sweep rows, and result were preserved, but the exact notebook execution code was not prospectively saved as a standalone runner. Therefore the original `execution identity PASS` wording was too strong at the code-custody layer.

A standalone successor reproduction was later run against the unchanged contract. It reproduced every checked sweep quantity exactly for all eight states, including:

- present capability;
- memory use;
- number of compiled groups;
- mean, minimum, and maximum `C*`;
- number of surprises with `C*>1`;
- 128/128 independent validations.

Successor runner SHA-256:

```text
bb2665a6cc06e74198db01cf3e0453f50bc2bbd04b115ce16b973247c13ada0d
```

This reproduction increases reproducibility but does **not** retroactively make the original notebook cell prospectively byte-custodied.

## Claim ceiling

This is a synthetic local frontier over one explicit compilation/memory substrate.

It does not establish a universal capability–correction law, a general compression result, an effect in real AI systems, or a general mechanism involving provenance, authority, jurisdiction, or reasoning capital.

The next evidential boundary is to change the accumulation substrate while preserving the assay discipline.
