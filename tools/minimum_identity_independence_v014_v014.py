from __future__ import annotations

import json
import secrets
import select
import subprocess
import tempfile
from pathlib import Path
from typing import BinaryIO

from tools.minimum_identity_independence_v014_v013 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v013 as _base


# Gate-4-only successor. The sandbox, schemas, oracle, architecture logic,
# scoring, and cost definitions remain inherited from v0.1.3.


def prepare(chi: str, case: Case, root: Path) -> Prepared:
    """Construct the exact frozen V_i but stop lifecycle authority at T1.

    T2 is deliberately NOT emitted here. It is emitted only by the actual
    successful child-stdin dispatch path after SANDBOX_READY.
    """
    _base.verify_schemas()
    life = Life()
    life.mark(Life.ORDER[0])
    handle = secrets.token_hex(32)
    if not HEX64.fullmatch(handle):
        raise ConformanceError("handle")

    life.mark(Life.ORDER[1])
    cost = Cost()
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
        store.write("executed.raw", cost.capture(case.executed_bytes))
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
    return Prepared(data, attestation, cost, life)


def _write_exact_view_and_mark_t2(
    stream: BinaryIO, view_bytes: bytes, life: Life
) -> None:
    """Commit the exact V_i bytes to child stdin, then and only then mark T2."""
    life.through(Life.ORDER[1])
    if not view_bytes:
        raise ConformanceError("empty view dispatch")

    total = 0
    payload = memoryview(view_bytes)
    try:
        while total < len(payload):
            written = stream.write(payload[total:])
            if written is None or written <= 0:
                raise ConformanceError("view dispatch incomplete")
            total += written
        stream.flush()
        stream.close()
    except (BrokenPipeError, OSError, ValueError) as exc:
        raise ConformanceError("view dispatch failed") from exc

    if total != len(view_bytes):
        raise ConformanceError("view dispatch byte-count mismatch")
    life.mark(Life.ORDER[2])


def _spawn(
    source: str, input_bytes: bytes, life: Life | None = None
) -> tuple[bytes, bytes]:
    """Use the unchanged v0.1.3 sandbox; optionally bind actual dispatch to T2."""
    with tempfile.TemporaryDirectory(prefix="mii-sandbox-") as td:
        proc = subprocess.Popen(
            _base._launcher() + [source],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=td,
            env={},
            close_fds=True,
        )
        try:
            ready, _, _ = select.select([proc.stderr], [], [], 5)
            if not ready:
                proc.kill()
                proc.wait(timeout=2)
                raise ConformanceError("sandbox readiness timeout")
            line = proc.stderr.readline()
            if line != _base.SANDBOX_READY:
                out, err = proc.communicate(timeout=2)
                raise ConformanceError(
                    f"sandbox failed before readiness: {line!r} {out!r} {err!r}"
                )

            if life is None:
                # Probe/conformance path only; no assay lifecycle authority.
                out, err = proc.communicate(input=input_bytes, timeout=5)
            else:
                if proc.stdin is None:
                    raise ConformanceError("sandbox stdin unavailable")
                stdin = proc.stdin
                _write_exact_view_and_mark_t2(stdin, input_bytes, life)
                # communicate() must not attempt to flush the now-closed stdin.
                proc.stdin = None
                out, err = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired as exc:
            proc.kill()
            proc.wait(timeout=2)
            raise ConformanceError("sandbox execution timeout") from exc

    if proc.returncode != 0:
        raise ConformanceError(f"sandbox child nonzero exit {proc.returncode}: {err!r}")
    return bytes(out), bytes(err)


def _invoke_architecture_with_life(
    chi: str, view_bytes: bytes, life: Life
) -> ArchitectureResult:
    _base.parse(chi, view_bytes)
    output_bytes, event_bytes = _spawn(
        _base.architecture_source(chi), view_bytes, life=life
    )
    try:
        output = json.loads(output_bytes.decode(), object_pairs_hook=dict)
    except Exception as exc:
        raise ConformanceError("invalid architecture output") from exc
    if list(output) != ["terminal"] or output.get("terminal") not in TERMINALS:
        raise ConformanceError("invalid architecture terminal")
    if json.dumps(output, separators=(",", ":")).encode() != output_bytes:
        raise ConformanceError("noncanonical architecture output")
    return ArchitectureResult(output["terminal"], output_bytes, event_bytes)


def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    """Engineering/conformance evaluation without assay lifecycle authority."""
    return _base.evaluate(chi, view_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    """Capability probe through this successor's exact spawn/launcher path."""
    out, err = _spawn(
        _base._probe_source(action),
        json.dumps(payload, separators=(",", ":")).encode(),
        life=None,
    )
    if err:
        raise ConformanceError(f"unexpected probe event stream: {err!r}")
    return out.decode()


def run(chi: str, prepared: Prepared) -> Frozen:
    """Production lifecycle path: T2 at actual dispatch, T3 after output freeze."""
    prepared.life.through(Life.ORDER[1])
    result = _invoke_architecture_with_life(
        chi, prepared.view_bytes, prepared.life
    )
    prepared.life.through(Life.ORDER[2])

    # Freeze/copy terminal evidence before granting T3 authority.
    output_bytes = bytes(result.output_bytes)
    frozen = Frozen(
        result.terminal,
        output_bytes,
        shared_sha(output_bytes),
    )
    prepared.life.mark(Life.ORDER[3])

    # One-way instrumentation remains downstream of the frozen terminal output.
    prepared.cost.merge_architecture_delta(_base._decode_events(result.event_bytes))
    return frozen
