# Minimum Identity Independence View Boundary v0.1

Version: `MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0.1`

Status: `FROZEN_VIEW_BOUNDARY / NON_EXECUTED / NON_AUTHORIZING`

This artifact is the minimal Gate-1 repair for `MINIMUM_IDENTITY_INDEPENDENCE_ASSAY_V0.1` after hostile review found that prose-level oracle non-use was weaker than an explicit information boundary.

It does not modify the frozen oracle cases, case partition, scoring, cost ledger, claim ceiling, Gate 7, or any scientific result.

## 1. Isolation invariant

The architecture under test receives exactly one architecture-visible view `V_i` and no other case information:

```text
O --sealed projection P_i--> V_i --> chi_i
```

The referee alone joins architecture output back to oracle truth after the architecture output is frozen.

For every evaluation:

```text
architecture-visible input = exact serialized V_i bytes
```

No semantic case identity, oracle verdict, case class, or execution ordinal is architecture-visible.

## 2. Referee-only information

The following are forbidden from `V_i`, process arguments, environment, working-directory names, mounted files, network inputs, and persistent state visible to `chi_i`:

```text
semantic case ID
critical-clean / critical-failure / diagnostic membership
oracle_mismatch
oracle_class
global case ordinal
global architecture-case ordinal
semantic perturbation label
oracle-side substitution aliases including ALPHA_MUT
expected terminal classification
previous-case output or state
opaque-handle -> oracle-case mapping
complete oracle manifest
```

`declared_object_id` is not oracle truth. It is ordinary self-reported identity evidence already present in the frozen case and may therefore be visible where constituted below.

## 3. Opaque case handle

Every architecture-case evaluation receives a fresh handle generated independently from 256 CSPRNG bits and rendered as exactly 64 lowercase hexadecimal characters.

Requirements:

```text
fresh per evaluation
never reused in the assay
contains no case/class/architecture/ordinal encoding
mapping held only by referee
mapping unavailable to chi_0..chi_3
```

The same oracle case evaluated by different architectures receives different opaque handles.

## 4. Stateless evaluation boundary

Each `chi_i` evaluation is a fresh invocation with exactly one view input and exactly one result output.

The implementation must establish an equivalent of a pure function:

```text
result = chi_i(V_i)
```

The architecture evaluation context must have:

```text
no persistent state from previous evaluations
no shared mutable state
no oracle/repository/harness filesystem access
no network access
no semantic case information in argv/env/cwd
no previous-run outputs
no recoverable global case ordinal
```

A pure-function boundary is preferred. Any sandboxed process realization must be independently reviewed to show that clock/order/process metadata cannot reconstruct the constituted global case ordinal.

## 5. View serialization

Every `V_i` is serialized as:

```text
UTF-8
no BOM
compact JSON
keys exactly in fields_in_order
ensure_ascii = false
no terminal newline
no extra fields
```

Before invocation, the sealed projection layer validates exact schema conformance and computes:

```text
dispatched_view_sha256 = SHA256(exact serialized V_i bytes)
```

The projection-layer hash is authoritative. An architecture may echo an input hash diagnostically, but its self-report is not dispatch authority.

## 6. Frozen schema identity rule

For each architecture below:

```text
schema_sha256 = SHA256(UTF8(canonical_json(schema_contract)))
```

where:

```text
canonical_json:
  sort_keys = true
  separators = (",", ":")
  ensure_ascii = false
  terminal newline = absent
```

The canonical JSON shown for each architecture is exact schema-contract authority.

### chi_0

Canonical schema contract:

```json
{"authority":"self-report/convenience only; no H_f/H_m/H_e bytes or hashes","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI0_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"]],"schema_id":"MII_VIEW_CHI0_V0.1"}
```

```text
schema_sha256:
54214df3b4b02e8304d96a36629ac8ce6c851d61c4e5e58fcade382f28b739d3
```

### chi_1

Canonical schema contract:

```json
{"authority":"independent H_f/H_m only; H_e unavailable; H_m must not substitute for H_e","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal","executed_raw_bytes_utf8","custody_reported_executed_sha256"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI1_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"]],"schema_id":"MII_VIEW_CHI1_V0.1"}
```

```text
schema_sha256:
b873fad1d01af7c3c57d27d68cbab0df008248780fd397c5c548e2a9477c7056
```

### chi_2

Canonical schema contract:

```json
{"authority":"custody_reported_executed_sha256 is H_e authority; do not recompute SHA256(executed_raw_bytes_utf8)","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI2_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI2_V0.1"}
```

```text
schema_sha256:
61e1de0a04040172faa914813b86f8b31f7396f11db176e82e67e145f253c7a8
```

### chi_3

Canonical schema contract:

```json
{"authority":"independently recompute SHA256(executed_raw_bytes_utf8) as H_e authority; custody-reported H_e diagnostic only","forbidden":["semantic_case_id","case_partition","oracle_mismatch","oracle_class","global_ordinal","oracle_aliases","previous_state","expected_terminal"],"fields_in_order":[["schema_version","const:MII_VIEW_CHI3_V0.1"],["case_handle","hex64"],["declared_object_id","enum:ALPHA|BETA"],["convenience_identity_match","bool|null"],["frozen_bytes_utf8","string"],["frozen_sha256","hex64"],["materialized_bytes_utf8","string"],["materialized_sha256","hex64"],["executed_raw_bytes_utf8","string"],["custody_reported_executed_sha256","hex64"]],"schema_id":"MII_VIEW_CHI3_V0.1"}
```

```text
schema_sha256:
bf17650e576cbd28f7c2cbb12b039b60a2885794ae812031a929fe77a52c43b1
```

`chi_2` and `chi_3` intentionally receive equivalent identity evidence fields at the raw-custody level. Their constituted difference is the authority path: `chi_2` trusts custody-reported `H_e`; `chi_3` independently recomputes `H_e` from authoritative raw custody.

## 7. Sealed projection rules

Common projection code must:

1. resolve oracle-side symbolic aliases to exact bytes before view construction;
2. never emit `ALPHA_MUT` or any semantic perturbation label;
3. copy `declared_object_id` only from the ordinary declared identity evidence frozen in the case;
4. recompute visible `frozen_sha256` from visible frozen bytes;
5. recompute visible `materialized_sha256` from visible materialized bytes;
6. expose `executed_raw_bytes_utf8`, where constituted, only from the common authoritative synthetic custody path;
7. expose `custody_reported_executed_sha256`, where constituted, from an explicit frozen custody override if one exists, otherwise from the common custody layer's hash of the actual executed bytes;
8. add only the fresh opaque handle and fixed schema version;
9. reject any view containing an extra field.

The projection may know oracle truth because it is outside the architecture under test. It must not serialize that truth except through the evidence fields legitimately constituted for the selected `chi_i`.

## 8. Dispatch attestation

For every evaluation, before architecture execution, the sealed projection layer must record referee-side:

```text
opaque handle
schema_id
frozen schema_sha256
dispatched_view_sha256
schema validation PASS/FAIL
```

The semantic case mapping remains sealed on the referee side.

Architecture output is frozen and hashed before the referee joins it to oracle truth.

## 9. Scope of repair

This artifact repairs only the Gate-1 oracle/view boundary.

It does not revise:

```text
oracle object bytes
oracle SHA-256 values
C0/C1/E1/E2/E3/E4/D1/D2/D3 definitions
critical/diagnostic partition
D(i,k) scoring
cost ledger
no-scalarization rule
claim ceiling
execution authorization state
```

In particular, no later-gate observation or suspected defect is repaired here.

## Terminal state

```text
artifact:
MINIMUM_IDENTITY_INDEPENDENCE_VIEW_BOUNDARY_V0.1

status:
FROZEN_VIEW_BOUNDARY
NON_EXECUTED
NON_AUTHORIZING

repair scope:
ORACLE / ARCHITECTURE VIEW BOUNDARY ONLY

next action:
CONSTITUTE SUCCESSOR REFERENCE
THEN RESTART HOSTILE REVIEW FROM GATE 1
```
