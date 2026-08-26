from __future__ import annotations

from pathlib import Path

from tools.minimum_identity_independence_v014_v021 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v021 as _extract

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle, view/persistence/SHA/extract/compare semantics,
# scoring, cost dimensions, missingness rules, and Pareto rules remain unchanged.
# The sole repair is semantic/physical realization of C_capture_bytes.
#
# Frozen implementation mapping of the existing cost contract:
#   CAPTURE is the successful transfer of fixed executed-object bytes across the
#   architecture-specific evidence-channel boundary into executed.raw custody.
#   C_capture_bytes counts the authoritative returned bytes transferred across
#   that boundary. The same physical write also contributes to C_persist_bytes,
#   which remains a distinct cumulative-write dimension.

_view = _extract._view
_persist = _view._persist
_complete = _extract._complete
_ops = _extract._ops


class Cost(_extract.Cost):
    """Successor ledger with no helper-return capture authority."""

    def capture(self, data: bytes) -> bytes:
        raise ConformanceError(
            "C_capture_bytes authority belongs only to evidence-channel transfer"
        )


class Store(_extract.Store):
    """Custody store whose initial source->executed.raw transfer is CAPTURE."""

    def __init__(self, root: Path, cost: Cost):
        super().__init__(root, cost)
        self._capture_measurement_valid = True

    def capture_into_evidence(self, name: str, source_bytes: bytes) -> None:
        """Transfer fixed source bytes into custody and jointly account capture/persist.

        One physical write has two constituted measurement roles:
          * capture: bytes transferred from fixed source into evidence channel;
          * persistence: bytes newly written to persistent evidence.
        Later writes may add persistence cost but never capture cost.
        """
        path = self.p(name)
        path.parent.mkdir(parents=True, exist_ok=True)

        self.cost.C_capture_bytes = 0
        self.cost.complete["C_capture_bytes"] = False
        self.cost.complete["C_persist_bytes"] = False

        try:
            written = _persist._persistence_write_once(path, source_bytes, "wb")
        except Exception:
            self._capture_measurement_valid = False
            self._persistence_measurement_valid = False
            # No authoritative returned transfer count exists. Capture value is
            # unknown rather than invented zero/full. Persistence retains any
            # previously known cumulative count but remains incomplete.
            self.cost.C_capture_bytes = None
            self.cost.complete["C_capture_bytes"] = False
            self.cost.complete["C_persist_bytes"] = False
            raise

        if (
            not isinstance(written, int)
            or isinstance(written, bool)
            or written < 0
            or written > len(source_bytes)
        ):
            self._capture_measurement_valid = False
            self._persistence_measurement_valid = False
            self.cost.C_capture_bytes = None
            self.cost.complete["C_capture_bytes"] = False
            self.cost.complete["C_persist_bytes"] = False
            raise ConformanceError("invalid evidence-channel transfer count")

        # The same authoritative returned byte count grounds two different
        # primary dimensions without conflating their semantics.
        self.cost.C_capture_bytes = written
        self.cost.C_persist_bytes += written

        if written != len(source_bytes):
            self._capture_measurement_valid = False
            self._persistence_measurement_valid = False
            self.cost.complete["C_capture_bytes"] = False
            self.cost.complete["C_persist_bytes"] = False
            raise ConformanceError("partial evidence-channel capture")

        if self._capture_measurement_valid:
            self.cost.complete["C_capture_bytes"] = True
        if self._persistence_measurement_valid:
            self.cost.complete["C_persist_bytes"] = True


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct exact V_i with capture authority at the custody boundary only."""
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
        cost.C_capture_bytes = 0
        cost.complete["C_capture_bytes"] = False
        cost.complete["C_persist_bytes"] = False
    else:
        cost.C_capture_bytes = 0
        cost.complete["C_capture_bytes"] = True
        cost.complete["C_persist_bytes"] = True

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
        # This is the sole production CAPTURE authority boundary.
        store.capture_into_evidence("executed.raw", case.executed_bytes)
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

    _complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def architecture_source(chi: str) -> str:
    return _extract.architecture_source(chi)


def _decode_child_operation_events(event_bytes: bytes) -> ArchitectureDelta:
    return _extract._decode_child_operation_events(event_bytes)


def _merge_child_events_fail_closed(cost: Cost, event_bytes: bytes) -> ArchitectureDelta:
    return _extract._merge_child_events_fail_closed(cost, event_bytes)


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
    return _extract.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    return _extract.capability_probe(action, payload)
