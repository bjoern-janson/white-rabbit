#!/usr/bin/env python3
"""Deterministic Gate 7 neutral-control source and token-only search.

This tool has no generation route. It materializes the contract-frozen source
family, then (under separate authorization) uses only native /props,
/apply-template, and /tokenize endpoints.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit


VERSION = "G7_NEUTRAL_CONTROL_SEARCH_IMPLEMENTATION_V0.1"
CONTRACT_VERSION = "G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0.1"
CONTRACT_COMMIT = "d85c42cab4375beefeee9640a08a7ecb5739f460"
EXPECTED_CONTRACT_SHA256 = "76ff861ac2004e759cdd9822f9fbfb7685392280f8af58878e66f5f3b3cad1fd"
STARTING_HEAD = CONTRACT_COMMIT

B0 = """reference pattern: X ∝ Y_reference

where:

Y_reference = label for a static descriptive sequence, reference
   ↓
plain descriptive statement
   ↓
fixed reference notation
   ↓
ordinary descriptive sequence
   ↓
expanded neutral reference example"""

C_IMPROVE = """internalize logic: I ∝ C_improve

where:

C_improve = capacity to convert feedback into increased future viability, feedback
   ↓
better representation
   ↓
better adaptive mechanisms
   ↓
greater improvement capacity
   ↓
expanded viable futures"""

TARGETS = {
    "Q1": "Compute (37 × 14) - (96 ÷ 3). Return exactly one base-10 integer and nothing else.",
    "Q2": "Reverse the character sequence `Q7m2R9`. Return exactly the reversed six-character sequence and nothing else.",
    "Q3": "Sort the integers 17, -4, 9, 0, 12 in strictly ascending numeric order. Return exactly a comma followed by a single space between values, and nothing else.",
}

EXPECTED_HASHES = {
    "B0": "af2d192d9ce44c51190455b3434b55e0c676c9630c6a17af5d33d6c0d94f3a51",
    "C": "62fda9b76bf6c5870ed63112b4fef021e227c933c8112755fc58dac27579109a",
    "Q1": "eb81d8205fe0a2215a3351f3743afbc6028c73b33ddbab238e6599c298142a23",
    "Q2": "3a2902cdad1a34cec5a1b8b1ab0684c0cf182fb867e861384d10034993c566f1",
    "Q3": "886d0318a6702db444cac8f63947f3cdcba7f8b23f93ee91a5c5c84366bea400",
    "separator": "7f31dacfc61dd598296a31789337fd1886023536222243b43e16a914886bf5f4",
}

SEPARATOR = "\n\n--- TARGET ---\n"
EXPECTED_C_COUNTS = {"Q1": 142, "Q2": 135, "Q3": 153}

OPTION_SETS = {
    "L1": [
        "reference pattern: X ∝ Y_reference",
        "reference relation: X ∝ Y_reference",
        "reference mapping: X ∝ Y_reference",
        "descriptive pattern: X ∝ Y_reference",
        "static pattern: X ∝ Y_reference",
    ],
    "L5": [
        "Y_reference = label for a static descriptive sequence, reference",
        "Y_reference = marker for a fixed descriptive series, reference",
        "Y_reference = name for an ordinary descriptive sequence, reference",
        "Y_reference = symbol for a static reference series, reference",
        "Y_reference = label for a fixed neutral sequence, reference",
    ],
    "L7": [
        "plain descriptive statement",
        "simple descriptive statement",
        "plain reference statement",
        "ordinary descriptive entry",
        "neutral reference statement",
    ],
    "L9": [
        "fixed reference notation",
        "static reference notation",
        "fixed descriptive notation",
        "ordinary reference notation",
        "neutral reference notation",
    ],
    "L11": [
        "ordinary descriptive sequence",
        "plain descriptive sequence",
        "ordinary reference sequence",
        "static descriptive sequence",
        "neutral descriptive sequence",
    ],
    "L13": [
        "expanded neutral reference example",
        "extended neutral reference example",
        "expanded static reference example",
        "detailed neutral reference example",
        "complete neutral reference example",
    ],
}

SLOT_ORDER = ("L1", "L5", "L7", "L9", "L11", "L13")
FORBIDDEN = (
    "c_improve",
    "c-improve",
    "improve",
    "feedback",
    "adapt",
    "viability",
    "future",
    "representation",
    "mechanism",
    "learn",
    "optim",
    "reason",
    "strategy",
    "solve",
    "capability",
    "rabbit",
    "corrig",
    "efficient",
    "compute",
    "self-improv",
    "metacogn",
    "treatment",
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def file_sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def ascii_fold(value: str) -> str:
    return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in value)


def product_index(option_tuple: tuple[int, int, int, int, int, int]) -> int:
    index = 0
    for value in option_tuple:
        if value < 0 or value > 4:
            raise ValueError("option index outside frozen range 0..4")
        index = index * 5 + value
    return index + 1


def iter_option_tuples() -> Iterable[tuple[int, int, int, int, int, int]]:
    for i1 in range(5):
        for i5 in range(5):
            for i7 in range(5):
                for i9 in range(5):
                    for i11 in range(5):
                        for i13 in range(5):
                            yield (i1, i5, i7, i9, i11, i13)


def construct_candidate(option_tuple: tuple[int, int, int, int, int, int]) -> str:
    values = {
        slot: OPTION_SETS[slot][index]
        for slot, index in zip(SLOT_ORDER, option_tuple, strict=True)
    }
    return "\n".join(
        (
            values["L1"],
            "",
            "where:",
            "",
            values["L5"],
            "   ↓",
            values["L7"],
            "   ↓",
            values["L9"],
            "   ↓",
            values["L11"],
            "   ↓",
            values["L13"],
        )
    )


def source_rejection_codes(
    candidate: str, option_tuple: tuple[int, int, int, int, int, int]
) -> list[str]:
    codes: list[str] = []
    if any(0xD800 <= ord(char) <= 0xDFFF for char in candidate):
        codes.append("NON_SCALAR_UNICODE")
    try:
        encoded = candidate.encode("utf-8")
    except UnicodeEncodeError:
        encoded = b""
        codes.append("INVALID_UTF8")
    if encoded.startswith(b"\xef\xbb\xbf"):
        codes.append("UTF8_BOM")
    if "\r" in candidate:
        codes.append("NON_LF_LINE_ENDING")
    if candidate.endswith("\n"):
        codes.append("TRAILING_LF")
    lines = candidate.split("\n")
    if len(lines) != 13:
        codes.append("LINE_COUNT")
    blocks = candidate.split("\n\n")
    if len(blocks) != 3 or any(block == "" for block in blocks):
        codes.append("BLOCK_COUNT")
    if candidate.count("∝") != 1:
        codes.append("PROPORTIONAL_SYMBOL_COUNT")
    if sum(line == "   ↓" for line in lines) != 4:
        codes.append("ARROW_LINE_COUNT")
    if sum(line == "where:" for line in lines) != 1:
        codes.append("WHERE_LINE_COUNT")
    if len(lines) == 13:
        selected = [lines[0], lines[4], lines[6], lines[8], lines[10], lines[12]]
        expected = [
            OPTION_SETS[slot][index]
            for slot, index in zip(SLOT_ORDER, option_tuple, strict=True)
        ]
        if selected != expected:
            codes.append("LEXICAL_OPTION_MISMATCH")
        fixed = {1: "", 2: "where:", 3: "", 5: "   ↓", 7: "   ↓", 9: "   ↓", 11: "   ↓"}
        if any(lines[index] != value for index, value in fixed.items()):
            codes.append("STRUCTURAL_TEMPLATE_MISMATCH")
    if candidate.count("X") != 1 or candidate.count("Y_reference") != 2:
        codes.append("FIXED_LITERAL_POSITION_COUNT")
    folded = ascii_fold(candidate)
    for term in FORBIDDEN:
        if term in folded:
            codes.append(f"FORBIDDEN_SUBSTRING:{term}")
    for task, target in TARGETS.items():
        if target in candidate:
            codes.append(f"TASK_TARGET:{task}")
    for answer in ("486", "9R2m7Q", "-4, 0, 9, 12, 17"):
        if answer in candidate:
            codes.append(f"EXPECTED_ANSWER:{answer}")
    return codes


def levenshtein_codepoints(left: str, right: str) -> int:
    if len(left) < len(right):
        left, right = right, left
    previous = list(range(len(right) + 1))
    for i, left_char in enumerate(left, start=1):
        current = [i]
        for j, right_char in enumerate(right, start=1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[j] + 1,
                    previous[j - 1] + (left_char != right_char),
                )
            )
        previous = current
    return previous[-1]


def ranking_key(candidate: dict[str, Any]) -> tuple[Any, ...]:
    source = candidate["source"]
    return (
        levenshtein_codepoints(B0, source),
        abs(len(source.encode("utf-8")) - len(B0.encode("utf-8"))),
        abs(len(source) - len(B0)),
        source.encode("utf-8"),
        candidate["source_sha256"],
    )


def verify_frozen_sources(contract_path: Path) -> dict[str, str]:
    actual = {
        "B0": sha256_text(B0),
        "C": sha256_text(C_IMPROVE),
        "Q1": sha256_text(TARGETS["Q1"]),
        "Q2": sha256_text(TARGETS["Q2"]),
        "Q3": sha256_text(TARGETS["Q3"]),
        "separator": sha256_text(SEPARATOR),
    }
    if actual != EXPECTED_HASHES:
        raise RuntimeError(f"frozen source hash mismatch: {actual!r}")
    contract_hash = file_sha256(contract_path)
    if contract_hash != EXPECTED_CONTRACT_SHA256:
        raise RuntimeError(
            f"contract hash mismatch: expected {EXPECTED_CONTRACT_SHA256}, got {contract_hash}"
        )
    actual["contract"] = contract_hash
    return actual


def materialize_phase_a(contract_path: Path, manifest_path: Path) -> dict[str, Any]:
    source_hashes = verify_frozen_sources(contract_path)
    survivors: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []
    for option_tuple in iter_option_tuples():
        p_index = product_index(option_tuple)
        source = construct_candidate(option_tuple)
        rejection_codes = source_rejection_codes(source, option_tuple)
        base_record = {
            "product_index": p_index,
            "option_tuple": list(option_tuple),
            "source": source,
            "source_sha256": sha256_text(source),
            "unicode_code_points": len(source),
            "utf8_bytes": len(source.encode("utf-8")),
            "delta_code_points_from_B0": len(source) - len(B0),
            "delta_utf8_bytes_from_B0": len(source.encode("utf-8")) - len(B0.encode("utf-8")),
        }
        if rejection_codes:
            rejections.append({**base_record, "rejection_codes": rejection_codes})
        else:
            survivors.append({**base_record, "candidate_index": len(survivors) + 1})

    if len(survivors) + len(rejections) != 15625:
        raise RuntimeError("Phase A did not process all 15,625 theoretical positions")
    payload = {
        "contract": {
            "version": CONTRACT_VERSION,
            "commit": CONTRACT_COMMIT,
            "path": contract_path.as_posix(),
            "sha256": source_hashes["contract"],
        },
        "implementation_version": VERSION,
        "starting_head": STARTING_HEAD,
        "source_hashes": source_hashes,
        "family": {
            "slot_order": list(SLOT_ORDER),
            "option_sets": OPTION_SETS,
            "theoretical_count_formula": "5*5*5*5*5*5",
            "total_theoretical_positions": 15625,
            "total_rejected": len(rejections),
            "total_source_admissible": len(survivors),
        },
        "rejections": rejections,
        "survivors": survivors,
        "phase_a_complete": True,
        "tokenization_started_before_manifest_freeze": False,
    }
    payload_hash = sha256_bytes(canonical_json_bytes(payload))
    document = {
        "schema_version": "G7_NEUTRAL_CONTROL_SOURCE_MANIFEST_V0.1",
        "hash_definition": "sha256(canonical UTF-8 JSON of manifest_payload; sort_keys=true; compact separators; ensure_ascii=false)",
        "manifest_sha256": payload_hash,
        "manifest_payload": payload,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    verify_manifest(manifest_path)
    return document


def verify_manifest(manifest_path: Path) -> dict[str, Any]:
    document = json.loads(manifest_path.read_text(encoding="utf-8"))
    actual = sha256_bytes(canonical_json_bytes(document["manifest_payload"]))
    if actual != document["manifest_sha256"]:
        raise RuntimeError("manifest payload hash mismatch")
    payload = document["manifest_payload"]
    family = payload["family"]
    if family["total_theoretical_positions"] != 15625:
        raise RuntimeError("manifest theoretical count mismatch")
    if family["total_rejected"] + family["total_source_admissible"] != 15625:
        raise RuntimeError("manifest rejected/admissible count mismatch")
    if not payload["phase_a_complete"]:
        raise RuntimeError("manifest does not attest complete Phase A")
    return document


class NativeInspectionClient:
    def __init__(self, base_url: str) -> None:
        parsed = urlsplit(base_url)
        if parsed.scheme != "http" or not parsed.hostname or not parsed.port:
            raise ValueError("inspection URL must be explicit http://host:port")
        self.host = parsed.hostname
        self.port = parsed.port
        self.connection = http.client.HTTPConnection(self.host, self.port, timeout=120)
        self.route_counts = {"GET /props": 0, "POST /apply-template": 0, "POST /tokenize": 0}

    def close(self) -> None:
        self.connection.close()

    def _request(self, method: str, path: str, body: bytes | None = None) -> tuple[bytes, dict[str, Any]]:
        headers = {"Content-Type": "application/json"} if body is not None else {}
        for attempt in range(2):
            try:
                self.connection.request(method, path, body=body, headers=headers)
                response = self.connection.getresponse()
                raw = response.read()
                if response.status != 200:
                    raise RuntimeError(f"{method} {path} returned {response.status}: {raw!r}")
                self.route_counts[f"{method} {path}"] += 1
                return raw, json.loads(raw.decode("utf-8"))
            except (ConnectionError, http.client.HTTPException):
                self.connection.close()
                if attempt:
                    raise
                self.connection = http.client.HTTPConnection(self.host, self.port, timeout=120)
        raise AssertionError("unreachable")

    def props(self) -> tuple[bytes, dict[str, Any]]:
        return self._request("GET", "/props")

    def render_and_tokenize(self, content: str) -> dict[str, Any]:
        template_body = canonical_json_bytes(
            {
                "messages": [{"role": "user", "content": content}],
                "add_generation_prompt": True,
            }
        )
        _, template_response = self._request("POST", "/apply-template", template_body)
        prompt = template_response["prompt"]
        tokenize_body = canonical_json_bytes(
            {
                "content": prompt,
                "add_special": True,
                "parse_special": True,
                "with_pieces": False,
            }
        )
        _, tokenize_response = self._request("POST", "/tokenize", tokenize_body)
        raw_tokens = tokenize_response["tokens"]
        token_ids = [item["id"] if isinstance(item, dict) else item for item in raw_tokens]
        canonical_tokens = json.dumps(token_ids, separators=(",", ":")).encode("ascii")
        return {
            "assembled_message_sha256": sha256_text(content),
            "rendered_prompt_sha256": sha256_text(prompt),
            "rendered_prompt_utf8_bytes": len(prompt.encode("utf-8")),
            "token_ids": token_ids,
            "canonical_token_sequence_sha256": sha256_bytes(canonical_tokens),
            "total_prompt_tokens": len(token_ids),
        }


def version_output(executable: Path) -> str:
    result = subprocess.run(
        [str(executable), "--version"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return (result.stdout + result.stderr).strip()


def execute_phase_b(args: argparse.Namespace) -> dict[str, Any]:
    manifest_path = Path(args.manifest)
    manifest = verify_manifest(manifest_path)
    payload = manifest["manifest_payload"]
    contract_path = Path(args.contract)
    source_hashes = verify_frozen_sources(contract_path)
    if payload["contract"]["sha256"] != source_hashes["contract"]:
        raise RuntimeError("manifest contract custody differs from current contract")

    implementation_path = Path(__file__).resolve()
    executable_path = Path(args.server_executable).resolve()
    model_path = Path(args.model).resolve()
    client = NativeInspectionClient(args.base_url)
    custody_path = Path(args.token_custody)
    custody_path.parent.mkdir(parents=True, exist_ok=True)
    custody_digest = hashlib.sha256()
    context_records = 0

    def write_custody(stream: Any, record: dict[str, Any]) -> None:
        nonlocal context_records
        raw = canonical_json_bytes(record) + b"\n"
        stream.write(raw)
        custody_digest.update(raw)
        context_records += 1

    try:
        props_raw, props = client.props()
        if props.get("build_info") != "b10603-c060ca974":
            raise RuntimeError(f"unexpected build_info: {props.get('build_info')!r}")
        if props.get("model_alias") != "qwen38-27b":
            raise RuntimeError(f"unexpected model alias: {props.get('model_alias')!r}")
        if Path(props.get("model_path", "")).resolve() != model_path:
            raise RuntimeError("loaded model path differs from frozen model")
        if props.get("default_generation_settings", {}).get("n_ctx") != 8192:
            raise RuntimeError("unexpected runtime context size")
        if props.get("total_slots") != 1:
            raise RuntimeError("unexpected slot count")
        chat_template = props.get("chat_template")
        if not isinstance(chat_template, str):
            raise RuntimeError("native props did not expose exact chat template")

        c_contexts: dict[str, dict[str, Any]] = {}
        for task, target in TARGETS.items():
            c_contexts[task] = client.render_and_tokenize(C_IMPROVE + SEPARATOR + target)
        recomputed_c_counts = {
            task: record["total_prompt_tokens"] for task, record in c_contexts.items()
        }
        if recomputed_c_counts != EXPECTED_C_COUNTS:
            raise RuntimeError(
                f"frozen C count reproduction failed: {recomputed_c_counts!r}"
            )

        candidate_counts: list[dict[str, Any]] = []
        match_candidates: list[dict[str, Any]] = []
        with custody_path.open("wb") as custody_stream:
            header = {
                "record_type": "header",
                "schema_version": "G7_NEUTRAL_CONTROL_TOKEN_CUSTODY_V0.1",
                "manifest_payload_sha256": manifest["manifest_sha256"],
                "manifest_file_sha256": file_sha256(manifest_path),
                "context_count_expected": payload["family"]["total_source_admissible"] * 3,
            }
            write_custody(custody_stream, header)
            for candidate in payload["survivors"]:
                counts: dict[str, int] = {}
                context_hashes: dict[str, dict[str, Any]] = {}
                for task, target in TARGETS.items():
                    record = client.render_and_tokenize(candidate["source"] + SEPARATOR + target)
                    counts[task] = record["total_prompt_tokens"]
                    context_hashes[task] = {
                        key: value for key, value in record.items() if key != "token_ids"
                    }
                    write_custody(
                        custody_stream,
                        {
                            "record_type": "context",
                            "candidate_index": candidate["candidate_index"],
                            "product_index": candidate["product_index"],
                            "task": task,
                            **record,
                        },
                    )
                count_record = {
                    "candidate_index": candidate["candidate_index"],
                    "product_index": candidate["product_index"],
                    "source_sha256": candidate["source_sha256"],
                    "token_counts": counts,
                    "context_hashes": context_hashes,
                }
                candidate_counts.append(count_record)
                if counts == EXPECTED_C_COUNTS:
                    match_candidates.append(candidate)

        expected_lines = payload["family"]["total_source_admissible"] * 3 + 1
        if context_records != expected_lines:
            raise RuntimeError(
                f"token custody record count mismatch: expected {expected_lines}, got {context_records}"
            )

        ranked_match_set: list[dict[str, Any]] = []
        for candidate in sorted(match_candidates, key=ranking_key):
            key = ranking_key(candidate)
            ranked_match_set.append(
                {
                    "rank": len(ranked_match_set) + 1,
                    "candidate_index": candidate["candidate_index"],
                    "product_index": candidate["product_index"],
                    "option_tuple": candidate["option_tuple"],
                    "source": candidate["source"],
                    "source_sha256": candidate["source_sha256"],
                    "unicode_code_points": candidate["unicode_code_points"],
                    "utf8_bytes": candidate["utf8_bytes"],
                    "levenshtein_from_B0": key[0],
                    "absolute_utf8_byte_difference_from_B0": key[1],
                    "absolute_code_point_difference_from_B0": key[2],
                    "utf8_hex": key[3].hex(),
                    "token_counts": EXPECTED_C_COUNTS,
                }
            )

        if ranked_match_set:
            terminal_state = "CONTROL_RECONSTITUTED"
            selected = ranked_match_set[0]
            Path(args.b1_output).write_bytes(selected["source"].encode("utf-8"))
            if file_sha256(Path(args.b1_output)) != selected["source_sha256"]:
                raise RuntimeError("B1 output hash mismatch")
        else:
            terminal_state = "NO_ADMISSIBLE_TOKEN_MATCH"
            selected = None

        server_argv = json.loads(args.server_argv_json)
        result = {
            "schema_version": "G7_NEUTRAL_CONTROL_RECONSTITUTION_SEARCH_V0.1",
            "terminal_state": terminal_state,
            "starting_head": STARTING_HEAD,
            "contract": {
                "version": CONTRACT_VERSION,
                "commit": CONTRACT_COMMIT,
                "path": contract_path.as_posix(),
                "sha256": source_hashes["contract"],
            },
            "implementation": {
                "version": VERSION,
                "path": implementation_path.as_posix(),
                "sha256": file_sha256(implementation_path),
                "phase_b_argv": sys.argv,
            },
            "source_manifest": {
                "path": manifest_path.as_posix(),
                "file_sha256": file_sha256(manifest_path),
                "payload_sha256": manifest["manifest_sha256"],
                "theoretical_positions": payload["family"]["total_theoretical_positions"],
                "rejected": payload["family"]["total_rejected"],
                "source_admissible": payload["family"]["total_source_admissible"],
                "phase_a_completed_before_tokenization": True,
            },
            "runtime_custody": {
                "base_url": args.base_url,
                "server_pid": args.server_pid,
                "server_executable": executable_path.as_posix(),
                "server_executable_sha256": file_sha256(executable_path),
                "server_version_output": version_output(executable_path),
                "server_argv": server_argv,
                "model_path": model_path.as_posix(),
                "model_filename": model_path.name,
                "model_bytes": model_path.stat().st_size,
                "model_sha256": file_sha256(model_path),
                "props_raw_sha256": sha256_bytes(props_raw),
                "build_info": props["build_info"],
                "model_alias": props["model_alias"],
                "model_ftype": props.get("model_ftype"),
                "context_size": props["default_generation_settings"]["n_ctx"],
                "parallel_slots": props["total_slots"],
                "chat_template": chat_template,
                "chat_template_sha256": sha256_text(chat_template),
                "chat_template_utf8_bytes": len(chat_template.encode("utf-8")),
                "chat_template_caps": props.get("chat_template_caps"),
                "bos_token": props.get("bos_token"),
                "eos_token": props.get("eos_token"),
                "add_generation_prompt": True,
                "tokenizer_options": {
                    "add_special": True,
                    "parse_special": True,
                    "with_pieces": False,
                },
                "native_routes_called": client.route_counts,
                "generation_routes_called": 0,
            },
            "c_reference": {
                "frozen_counts": EXPECTED_C_COUNTS,
                "recomputed_counts": recomputed_c_counts,
                "matched_frozen_counts": True,
                "contexts": c_contexts,
            },
            "token_custody": {
                "path": custody_path.as_posix(),
                "sha256": custody_digest.hexdigest(),
                "records_including_header": context_records,
                "context_records": context_records - 1,
            },
            "candidate_token_counts": candidate_counts,
            "exact_match_candidate_count": len(ranked_match_set),
            "complete_exact_match_set_ranked": ranked_match_set,
            "selected_B1": selected,
            "zero_generation_attestation": {
                "completion_or_generation_endpoint_called": False,
                "sampled_or_generated_tokens": 0,
                "assistant_output_observed": False,
                "white_rabbit_recorder_started": False,
                "scientific_runs": 0,
                "capability_observed": False,
                "N_generated_observed": False,
                "latency_comparison_performed": False,
                "white_rabbit_claim_emitted": False,
            },
            "limitations": [
                "Selection used token counts and is not independent PREOPEN_TOKEN_MATCH certification.",
                "CONTROL_RECONSTITUTED does not authorize G7 v0.1.2 or Gate 7 execution.",
                "No generated output, capability, work, latency, or scientific outcome was observed.",
            ],
        }
        Path(args.search_json).write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        return result
    finally:
        client.close()


def finalize_search(search_json: Path, server_log: Path, listeners_after_stop: int) -> None:
    result = json.loads(search_json.read_text(encoding="utf-8"))
    log_text = server_log.read_text(encoding="utf-8", errors="replace")
    result["post_run_process_custody"] = {
        "server_log_path": server_log.as_posix(),
        "server_log_sha256": file_sha256(server_log),
        "server_log_utf8_replacement_text": log_text,
        "task_log_lines": sum("task" in line.lower() for line in log_text.splitlines()),
        "controlled_process_stopped": True,
        "inspection_port_listeners_after_stop": listeners_after_stop,
    }
    result["artifact_hash_definition"] = (
        "search artifact file SHA-256 is recorded externally after this finalized JSON is frozen"
    )
    search_json.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def run_self_tests() -> None:
    verify_frozen_sources(Path("assays/G7_NEUTRAL_CONTROL_RECONSTITUTION_CONTRACT_V0_1.md"))
    tuples = list(iter_option_tuples())
    assert len(tuples) == 15625
    assert tuples[0] == (0, 0, 0, 0, 0, 0)
    assert tuples[1] == (0, 0, 0, 0, 0, 1)
    assert tuples[-1] == (4, 4, 4, 4, 4, 4)
    assert product_index(tuples[0]) == 1
    assert product_index(tuples[1]) == 2
    assert product_index(tuples[-1]) == 15625
    assert construct_candidate(tuples[0]) == B0
    assert source_rejection_codes(B0, tuples[0]) == []
    assert ascii_fold("C_Improve") == "c_improve"
    assert any(
        code.startswith("FORBIDDEN_SUBSTRING:c_improve")
        for code in source_rejection_codes(B0 + " C_Improve", tuples[0])
    )
    assert len(B0) == 246
    assert len(B0.encode("utf-8")) == 256
    assert sha256_text(B0) == EXPECTED_HASHES["B0"]
    assert levenshtein_codepoints("", "abc") == 3
    assert levenshtein_codepoints("kitten", "sitting") == 3
    a = {"source": B0, "source_sha256": sha256_text(B0)}
    b_source = B0.replace("pattern", "relation", 1)
    b = {"source": b_source, "source_sha256": sha256_text(b_source)}
    assert sorted([b, a], key=ranking_key)[0] is a
    print("deterministic self-tests: PASS")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("self-test")

    phase_a = subparsers.add_parser("phase-a")
    phase_a.add_argument("--contract", required=True)
    phase_a.add_argument("--manifest", required=True)

    phase_b = subparsers.add_parser("phase-b")
    phase_b.add_argument("--contract", required=True)
    phase_b.add_argument("--manifest", required=True)
    phase_b.add_argument("--base-url", required=True)
    phase_b.add_argument("--server-executable", required=True)
    phase_b.add_argument("--server-pid", required=True, type=int)
    phase_b.add_argument("--server-argv-json", required=True)
    phase_b.add_argument("--model", required=True)
    phase_b.add_argument("--token-custody", required=True)
    phase_b.add_argument("--search-json", required=True)
    phase_b.add_argument("--b1-output", required=True)

    finalize = subparsers.add_parser("finalize")
    finalize.add_argument("--search-json", required=True)
    finalize.add_argument("--server-log", required=True)
    finalize.add_argument("--listeners-after-stop", required=True, type=int)
    return parser.parse_args()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args()
    if args.command == "self-test":
        run_self_tests()
    elif args.command == "phase-a":
        document = materialize_phase_a(Path(args.contract), Path(args.manifest))
        family = document["manifest_payload"]["family"]
        print(
            json.dumps(
                {
                    "manifest_sha256": document["manifest_sha256"],
                    "theoretical": family["total_theoretical_positions"],
                    "rejected": family["total_rejected"],
                    "admissible": family["total_source_admissible"],
                },
                indent=2,
            )
        )
    elif args.command == "phase-b":
        result = execute_phase_b(args)
        print(
            json.dumps(
                {
                    "terminal_state": result["terminal_state"],
                    "exact_match_candidate_count": result["exact_match_candidate_count"],
                    "selected_B1": result["selected_B1"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif args.command == "finalize":
        finalize_search(
            Path(args.search_json),
            Path(args.server_log),
            args.listeners_after_stop,
        )
        print("search artifact finalization: PASS")


if __name__ == "__main__":
    main()
