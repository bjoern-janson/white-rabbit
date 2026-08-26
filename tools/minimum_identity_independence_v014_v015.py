from __future__ import annotations

import json
from dataclasses import dataclass

from tools.minimum_identity_independence_v014_v014 import *  # re-export frozen parent surfaces
import tools.minimum_identity_independence_v014_v014 as _life

# Gate-5-only successor. Constitution, oracle, schemas, architecture authority,
# sandbox, lifecycle, scoring, and cost contract are unchanged.
# The sole repair is that primary operation events are emitted only after the
# counted operation has completed successfully.

_OLD_PRIMITIVE_BLOCK = '''def emit(event,_err=_stderr):\n    _err.write(event+"\\n");_err.flush();return None\n\ndef compare(a,b): emit("IDENTITY_COMPARE_OPERATION");return a==b\n\ndef extract(text): emit("EXTRACT_OPERATION");return text.encode()\n\ndef digest(data,_h=_sha256): emit("SHA256_OPERATION");return _h(data).hexdigest()\n'''

_COMPLETED_PRIMITIVE_BLOCK = '''def emit(event,_err=_stderr):\n    _err.write(event+"\\n");_err.flush();return None\n\ndef compare(a,b):\n    result=a==b\n    emit("IDENTITY_COMPARE_OPERATION")\n    return result\n\ndef extract(text):\n    result=text.encode()\n    emit("EXTRACT_OPERATION")\n    return result\n\ndef digest(data,_h=_sha256):\n    result=_h(data).hexdigest()\n    emit("SHA256_OPERATION")\n    return result\n'''


def architecture_source(chi: str) -> str:
    """Return the unchanged hardened child source with post-completion events."""
    source = _life._base.architecture_source(chi)
    occurrences = source.count(_OLD_PRIMITIVE_BLOCK)
    if occurrences != 1:
        raise ConformanceError(
            f"completed-operation primitive patch expected 1 block, found {occurrences}"
        )
    return source.replace(
        _OLD_PRIMITIVE_BLOCK, _COMPLETED_PRIMITIVE_BLOCK, 1
    )


@dataclass(frozen=True)
class ArchitectureResult:
    terminal: str
    output_bytes: bytes
    event_bytes: bytes


def _parse_architecture_result(output_bytes: bytes, event_bytes: bytes) -> ArchitectureResult:
    try:
        output = json.loads(output_bytes.decode(), object_pairs_hook=dict)
    except Exception as exc:
        raise ConformanceError("invalid architecture output") from exc
    if list(output) != ["terminal"] or output.get("terminal") not in TERMINALS:
        raise ConformanceError("invalid architecture terminal")
    if json.dumps(output, separators=(",", ":")).encode() != output_bytes:
        raise ConformanceError("noncanonical architecture output")
    return ArchitectureResult(output["terminal"], output_bytes, event_bytes)


def _invoke_architecture_with_life(
    chi: str, view_bytes: bytes, life: Life
) -> ArchitectureResult:
    parse(chi, view_bytes)
    output_bytes, event_bytes = _life._spawn(
        architecture_source(chi), view_bytes, life=life
    )
    return _parse_architecture_result(output_bytes, event_bytes)


def evaluate(chi: str, view_bytes: bytes) -> ArchitectureResult:
    """Engineering/conformance evaluation without assay lifecycle authority."""
    parse(chi, view_bytes)
    output_bytes, event_bytes = _life._spawn(
        architecture_source(chi), view_bytes, life=None
    )
    return _parse_architecture_result(output_bytes, event_bytes)


def chi_0(view_bytes: bytes) -> str:
    return evaluate("chi_0", view_bytes).terminal


def chi_1(view_bytes: bytes) -> str:
    return evaluate("chi_1", view_bytes).terminal


def chi_2(view_bytes: bytes) -> str:
    return evaluate("chi_2", view_bytes).terminal


def chi_3(view_bytes: bytes) -> str:
    return evaluate("chi_3", view_bytes).terminal


def _decode_events(event_bytes: bytes) -> ArchitectureDelta:
    return _life._base._decode_events(event_bytes)


def capability_probe(action: str, payload: dict[str, str]) -> str:
    """Retain the exact reviewed v0.1.4 sandbox/capability-probe path."""
    return _life.capability_probe(action, payload)


def run(chi: str, prepared: Prepared) -> Frozen:
    """Production path: unchanged T2/T3 lifecycle, repaired event semantics."""
    prepared.life.through(Life.ORDER[1])
    result = _invoke_architecture_with_life(
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

    # Completed-operation events are interpreted only after terminal freeze/T3.
    prepared.cost.merge_architecture_delta(_decode_events(result.event_bytes))
    return frozen
