from __future__ import annotations

from pathlib import Path

from tools.minimum_identity_independence_v014_v020 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v020 as _view

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle, view/capture/persistence/SHA/compare semantics,
# scoring, cost dimensions, missingness rules, and Pareto rules remain unchanged.
# The sole repair is semantic realization of C_extract_ops.
#
# Frozen cost-contract interpretation (not a new contract):
#   C_extract_ops counts completed authority-bearing recovery of executed raw
#   custody into bytes used as identity authority. Diagnostic custody access and
#   ordinary serialized-field reconstruction are not primary extraction units.

_complete = _view._complete
_ops = _view._ops

_CHILD_EXTRACT_BLOCK = '''def extract(text):\n    result=text.encode()\n    emit("EXTRACT_OPERATION")\n    return result\n'''
_CHILD_RECONSTRUCT_BLOCK = '''def reconstruct_serialized_bytes(text):\n    return text.encode()\n'''
_CHILD_CHI3_OLD = 'executed_hash=digest(extract(view["executed_raw_bytes_utf8"]))'
_CHILD_CHI3_NEW = 'executed_hash=digest(reconstruct_serialized_bytes(view["executed_raw_bytes_utf8"]))'


class Store(_view.Store):
    """Custody store with explicit semantic read roles.

    A low-level filesystem read is not sufficient to earn C_extract_ops. The
    caller must select the constituted semantic role explicitly.
    """

    def read(self, name: str) -> bytes:
        raise ConformanceError(
            "ambiguous custody read forbidden; choose diagnostic or authority extraction"
        )

    def read_diagnostic(self, name: str) -> bytes:
        """Retrieve custody for a non-authoritative/diagnostic role; no extract cost."""
        return self.p(name).read_bytes()

    def extract_authority_bytes(self, name: str) -> bytes:
        """Complete one authority-bearing raw-custody extraction or fail closed."""
        # The total extraction dimension is not complete until all architecture
        # instrumentation for the evaluation has closed. A required extraction
        # failure therefore remains incomplete and earns no completed-op count.
        self.cost.complete["C_extract_ops"] = False
        raw = self.p(name).read_bytes()
        if not isinstance(raw, bytes):
            raise ConformanceError("authority extraction must return bytes")
        self.cost.C_extract_ops += 1
        return raw


def architecture_source(chi: str) -> str:
    """Return reviewed child source with serialization reconstruction unmetered.

    C_extract_ops authority exists at the chi_3 raw-custody recovery boundary in
    the parent. The later UTF-8 string -> bytes reconstruction is representation
    conversion over already architecture-visible V_i, not another primary
    extraction operation.
    """
    source = _ops.architecture_source(chi)
    occurrences = source.count(_CHILD_EXTRACT_BLOCK)
    if occurrences != 1:
        raise ConformanceError(
            f"semantic extraction patch expected one child extract block, found {occurrences}"
        )
    source = source.replace(_CHILD_EXTRACT_BLOCK, _CHILD_RECONSTRUCT_BLOCK, 1)
    if chi == "chi_3":
        if source.count(_CHILD_CHI3_OLD) != 1:
            raise ConformanceError("chi_3 extraction call site not uniquely found")
        source = source.replace(_CHILD_CHI3_OLD, _CHILD_CHI3_NEW, 1)
    elif _CHILD_CHI3_OLD in source or _CHILD_CHI3_NEW in source:
        raise ConformanceError("chi_3 reconstruction leaked into other architecture")
    return source


def _decode_child_operation_events(event_bytes: bytes) -> ArchitectureDelta:
    """Decode child events while forbidding a second extraction definition."""
    delta = _ops._decode_events(event_bytes)
    if delta.extract_ops != 0:
        raise ConformanceError(
            "child EXTRACT_OPERATION is not a constituted primary extraction boundary"
        )
    return delta


def _merge_child_events_fail_closed(cost: Cost, event_bytes: bytes) -> ArchitectureDelta:
    """Close total operation measurement only after the child stream is valid."""
    _complete._set_operation_measurement_complete(cost, False)
    try:
        delta = _decode_child_operation_events(event_bytes)
        cost.merge_architecture_delta(delta)
    except Exception:
        _complete._set_operation_measurement_complete(cost, False)
        raise
    _complete._set_operation_measurement_complete(cost, True)
    return delta


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct exact V_i with extraction cost attached to semantic authority."""
    verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = __import__("secrets").token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()
    cost._view_pending()

    if chi in {"chi_2", "chi_3"}:
        cost.complete["C_capture_bytes"] = False
        cost.complete["C_persist_bytes"] = False
    else:
        cost.complete["C_capture_bytes"] = True
        cost.complete["C_persist_bytes"] = True

    # Extraction is semantically required only by chi_3's independent H_e path.
    # chi_0/chi_1 have no raw custody. chi_2 may carry raw custody diagnostically
    # but may not use it as alternate identity authority.
    if chi == "chi_3":
        cost.complete["C_extract_ops"] = False
    else:
        cost.complete["C_extract_ops"] = True

    store = Store(root, cost)
    schema_id = SCHEMAS[chi]["schema_id"]
    view: dict[str, object] = {
        "schema_version": schema_id,
        "case_handle": handle,
        "declared_object_id": case.declared_object_id,
        "convenience_identity_match": case.convenience_identity_match,
    }
    if chi != "chi_0":
        view |= {
            "frozen_bytes_utf8": case.frozen_bytes.decode(),
            "frozen_sha256": cost.projection_sha(case.frozen_bytes),
            "materialized_bytes_utf8": case.materialized_bytes.decode(),
            "materialized_sha256": cost.projection_sha(case.materialized_bytes),
        }
    if chi in {"chi_2", "chi_3"}:
        captured = cost.capture(case.executed_bytes)
        store.write("executed.raw", captured)
        if chi == "chi_3":
            raw = store.extract_authority_bytes("executed.raw")
        else:
            raw = store.read_diagnostic("executed.raw")
        view["executed_raw_bytes_utf8"] = raw.decode()
        view["custody_reported_executed_sha256"] = (
            case.custody_override or cost.projection_sha(raw)
        )

    names = [field[0] for field in SCHEMAS[chi]["fields_in_order"]]
    ordered = {name: view[name] for name in names}
    data = serialize(chi, ordered)

    attestation = {
        "case_handle": handle,
        "schema_id": schema_id,
        "schema_sha256": SCHEMA_SHA[chi],
        "dispatched_view_sha256": shared_sha(data),
        "schema_validation": "PASS",
    }

    # Total SHA/extract/compare measurement remains fail-closed until the child
    # operation stream closes. Parent chi_3 extraction counts are retained while
    # completeness remains pending.
    _complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def _invoke_architecture_with_life(
    chi: str,
    view_bytes: bytes,
    cost: Cost,
    life: Life,
) -> ArchitectureResult:
    parse(chi, view_bytes)
    output_bytes, event_bytes = _view._spawn(
        architecture_source(chi),
        view_bytes,
        cost=cost,
        life=life,
    )
    return _ops._parse_architecture_result(output_bytes, event_bytes)


def run(chi: str, prepared: Prepared) -> Frozen:
    """Production path with one semantic definition of C_extract_ops."""
    prepared.life.through(Life.ORDER[1])
    result = _invoke_architecture_with_life(
        chi,
        prepared.view_bytes,
        prepared.cost,
        prepared.life,
    )
    prepared.life.through(Life.ORDER[2])

    output_bytes = bytes(result.output_bytes)
    frozen = Frozen(
        result.terminal,
        output_bytes,
        shared_sha(output_bytes),
    )
    prepared.life.mark(Life.ORDER[3])

    _merge_child_events_fail_closed(prepared.cost, result.event_bytes)
    return frozen


def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    """Engineering-only evaluation through the repaired semantic child source."""
    parse(chi, view_bytes)
    output_bytes, event_bytes = _view._spawn(
        architecture_source(chi), view_bytes, cost=None, life=None
    )
    return _ops._parse_architecture_result(output_bytes, event_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    return _view.capability_probe(action, payload)
