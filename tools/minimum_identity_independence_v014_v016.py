from __future__ import annotations

from pathlib import Path

from tools.minimum_identity_independence_v014_v015 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v015 as _ops

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# sandbox, lifecycle, scoring, operation-event semantics, cost dimensions, and
# Pareto rules are unchanged. The sole repair is fail-closed completeness for
# the three architecture operation-measurement dimensions.

_OPERATION_FIELDS = (
    "C_sha256_ops",
    "C_extract_ops",
    "C_identity_compare_ops",
)


def _set_operation_measurement_complete(cost: Cost, value: bool) -> None:
    for field in _OPERATION_FIELDS:
        cost.complete[field] = value


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Prepare the frozen V_i with operation measurement still pending.

    Projection-side values may already have been measured, but the total
    operation dimensions cannot be authoritative until the T2->T3 one-way
    event stream has been acquired and decoded successfully.
    """
    prepared = _ops.prepare(chi, case, root)
    _set_operation_measurement_complete(prepared.cost, False)
    return prepared


def _merge_operation_events_fail_closed(
    cost: Cost, event_bytes: bytes
) -> ArchitectureDelta:
    """Decode and merge a complete operation stream or leave it incomplete.

    Empty bytes are a valid complete zero-event stream. Any malformed,
    truncated, unknown, non-ASCII, or otherwise undecodable stream propagates
    its error while the mandatory operation dimensions remain incomplete.
    """
    _set_operation_measurement_complete(cost, False)
    try:
        delta = _ops._decode_events(event_bytes)
        cost.merge_architecture_delta(delta)
    except Exception:
        _set_operation_measurement_complete(cost, False)
        raise
    _set_operation_measurement_complete(cost, True)
    return delta


def run(chi: str, prepared: Prepared) -> Frozen:
    """Production path with fail-closed operation-measurement completeness."""
    prepared.life.through(Life.ORDER[1])
    result = _ops._invoke_architecture_with_life(
        chi, prepared.view_bytes, prepared.life
    )
    prepared.life.through(Life.ORDER[2])

    output_bytes = bytes(result.output_bytes)
    frozen = Frozen(
        result.terminal,
        output_bytes,
        shared_sha(output_bytes),
    )
    prepared.life.mark(Life.ORDER[3])

    # T3 freezes the architecture verdict. The primary operation dimensions
    # become complete only if the one-way event stream is then acquired,
    # decoded, and merged successfully. Failure propagates with complete=false.
    _merge_operation_events_fail_closed(prepared.cost, result.event_bytes)
    return frozen
