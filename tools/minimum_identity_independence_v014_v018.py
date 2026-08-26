from __future__ import annotations

import secrets
from pathlib import Path

from tools.minimum_identity_independence_v014_v017 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v017 as _sha

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# runtime sandbox, lifecycle, completed-operation SHA/extract/compare semantics,
# scoring, cost dimensions, missingness rules, and Pareto rules remain unchanged.
# The sole repair is capture-byte completed-work accounting during T1->T2.


def _capture_identity_bytes(data: bytes) -> bytes:
    """Uninstrumented capture body used only by the instrumented capture wrapper."""
    return bytes(data)


class Cost(_sha.Cost):
    """Successor ledger with fail-closed completed capture-byte accounting."""

    def capture(self, data: bytes) -> bytes:
        # A required capture is not authoritative until the actual returned
        # bytes are known. Never pre-credit the intended input length.
        self.complete["C_capture_bytes"] = False
        captured = _capture_identity_bytes(data)
        if not isinstance(captured, bytes):
            raise ConformanceError("capture result must be bytes")

        # Count only bytes that the capture body actually returned.
        self.C_capture_bytes += len(captured)

        # This assay requires exact executed-object custody. A partial returned
        # capture is real copied work, but it cannot establish a complete
        # primary capture measurement for the required evidence path.
        if len(captured) != len(data):
            raise ConformanceError("required capture incomplete")

        self.complete["C_capture_bytes"] = True
        return captured


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct exact V_i with repaired capture accounting only.

    chi_0/chi_1 require no executed-byte capture, so their zero capture is a
    known complete zero. chi_2/chi_3 require capture, so that dimension is
    pending from T1 until the capture succeeds exactly.
    """
    verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = secrets.token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()
    if chi in {"chi_2", "chi_3"}:
        cost.complete["C_capture_bytes"] = False
    else:
        cost.complete["C_capture_bytes"] = True

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
        raw = store.read("executed.raw")
        view["executed_raw_bytes_utf8"] = raw.decode()
        view["custody_reported_executed_sha256"] = (
            case.custody_override or cost.projection_sha(raw)
        )

    names = [field[0] for field in SCHEMAS[chi]["fields_in_order"]]
    ordered = {name: view[name] for name in names}
    data = serialize(chi, ordered)
    cost.mark_view(data)
    attestation = {
        "case_handle": handle,
        "schema_id": schema_id,
        "schema_sha256": SCHEMA_SHA[chi],
        "dispatched_view_sha256": shared_sha(data),
        "schema_validation": "PASS",
    }

    # Preserve v0.1.6/v0.1.7 fail-closed total operation semantics.
    _sha._complete._set_operation_measurement_complete(cost, False)
    return Prepared(data, attestation, cost, life)


def run(chi: str, prepared: Prepared) -> Frozen:
    return _sha.run(chi, prepared)


def evaluate(chi: str, view_bytes: bytes):
    return _sha.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    return _sha.capability_probe(action, payload)
