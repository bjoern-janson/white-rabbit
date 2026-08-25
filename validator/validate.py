"""Mechanical validation for the White Rabbit research-state constitution.

This module deliberately has no scientific adjudication vocabulary. It checks
schema shape, stable identifiers, references, and typed provenance reachability.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping


OUTCOMES = (
    "PROVENANCE_VALID",
    "PROVENANCE_INVALID",
    "SCHEMA_INVALID",
    "UNRESOLVED_SOURCE",
    "UNRESOLVED_RELATION",
)

_SCHEMA_BY_COLLECTION = {
    "sources": "source.schema.json",
    "claims": "claim.schema.json",
    "relations": "relation.schema.json",
    "statuses": "status.schema.json",
    "experiments": "experiment.schema.json",
    "artifacts": "artifact.schema.json",
}

_HISTORY_RELATIONS = {"SUPERSEDES", "REVISES", "INVALIDATES"}


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    object_id: str
    detail: str

    def as_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "object_id": self.object_id,
            "detail": self.detail,
        }


@dataclass(frozen=True)
class ValidationReport:
    outcome: str
    issues: tuple[ValidationIssue, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "outcome": self.outcome,
            "issues": [issue.as_dict() for issue in self.issues],
        }


def _schema_directory() -> Path:
    return Path(__file__).resolve().parents[1] / "schema"


def _load_schema(name: str) -> dict[str, Any]:
    with (_schema_directory() / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _schema_issues(value: Any, schema: Mapping[str, Any], path: str) -> list[str]:
    """Validate the intentionally small JSON-Schema subset used by v0.1."""

    issues: list[str] = []
    expected = schema.get("type")
    if expected is not None and not _type_matches(value, expected):
        return [f"{path}: expected {expected}"]

    if "const" in schema and value != schema["const"]:
        issues.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        issues.append(f"{path}: value is outside the frozen vocabulary")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            issues.append(f"{path}: string is too short")
        pattern = schema.get("pattern")
        if pattern is not None and re.search(pattern, value) is None:
            issues.append(f"{path}: string does not match required pattern")

    if isinstance(value, list):
        minimum = schema.get("minItems")
        if minimum is not None and len(value) < minimum:
            issues.append(f"{path}: expected at least {minimum} item(s)")
        if schema.get("uniqueItems"):
            encoded = [json.dumps(item, sort_keys=True, separators=(",", ":")) for item in value]
            if len(encoded) != len(set(encoded)):
                issues.append(f"{path}: items must be unique")
        item_schema = schema.get("items")
        if item_schema is not None:
            for index, item in enumerate(value):
                issues.extend(_schema_issues(item, item_schema, f"{path}[{index}]"))

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                issues.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key in sorted(set(value) & set(properties)):
            issues.extend(_schema_issues(value[key], properties[key], f"{path}.{key}"))
        if schema.get("additionalProperties") is False:
            for key in sorted(set(value) - set(properties)):
                issues.append(f"{path}: unexpected property {key!r}")

    return issues


def _issue(code: str, object_id: Any, detail: str) -> ValidationIssue:
    return ValidationIssue(code=code, object_id=str(object_id or "<unknown>"), detail=detail)


def _sorted(issues: Iterable[ValidationIssue]) -> tuple[ValidationIssue, ...]:
    return tuple(sorted(issues, key=lambda item: (item.code, item.object_id, item.detail)))


def _all_records(state: Mapping[str, Any]) -> list[tuple[str, Mapping[str, Any]]]:
    records: list[tuple[str, Mapping[str, Any]]] = []
    for collection in (*_SCHEMA_BY_COLLECTION, "provenance"):
        for record in state.get(collection, []):
            if isinstance(record, dict):
                records.append((collection, record))
    return records


def _reference_values(record: Mapping[str, Any], field: str) -> list[str]:
    value = record.get(field, [])
    return [item for item in value if isinstance(item, str)] if isinstance(value, list) else []


def validate_state(state: Any) -> ValidationReport:
    """Validate one in-memory research state without repairing it."""

    top_schema = _load_schema("research_state.schema.json")
    schema_errors = _schema_issues(state, top_schema, "$")
    if isinstance(state, dict):
        for collection, schema_name in _SCHEMA_BY_COLLECTION.items():
            schema = _load_schema(schema_name)
            values = state.get(collection, [])
            if isinstance(values, list):
                for index, value in enumerate(values):
                    schema_errors.extend(_schema_issues(value, schema, f"$.{collection}[{index}]"))
    if schema_errors:
        return ValidationReport(
            "SCHEMA_INVALID",
            _sorted(_issue("SCHEMA_ERROR", "$", detail) for detail in schema_errors),
        )

    assert isinstance(state, dict)
    records = _all_records(state)
    ids: dict[str, tuple[str, Mapping[str, Any]]] = {}
    provenance_by_subject: dict[str, list[Mapping[str, Any]]] = {}
    provenance_by_id: dict[str, Mapping[str, Any]] = {}
    unresolved_sources: list[ValidationIssue] = []
    unresolved_relations: list[ValidationIssue] = []
    provenance_errors: list[ValidationIssue] = []

    for collection, record in records:
        record_id = record["id"]
        if record_id in ids:
            provenance_errors.append(
                _issue("DUPLICATE_STABLE_ID", record_id, f"also appears in {ids[record_id][0]}")
            )
        else:
            ids[record_id] = (collection, record)
        if collection == "provenance":
            provenance_by_id[record_id] = record
            provenance_by_subject.setdefault(record["subject_id"], []).append(record)

    source_ids = {source["id"] for source in state["sources"]}
    domain_ids = {
        record["id"]
        for collection, record in records
        if collection != "provenance"
    }

    def require_sources(owner: Mapping[str, Any], references: Iterable[str], context: str) -> None:
        for source_id in references:
            if source_id not in source_ids:
                unresolved_sources.append(
                    _issue("UNRESOLVED_SOURCE_REFERENCE", owner["id"], f"{context}: {source_id}")
                )

    for claim in state["claims"]:
        require_sources(claim, _reference_values(claim, "source_ids"), "claim source")
        status_id = claim["status_id"]
        if status_id not in ids or ids[status_id][0] != "statuses":
            provenance_errors.append(_issue("UNRESOLVED_STATUS", claim["id"], status_id))
        elif ids[status_id][1]["subject_id"] != claim["id"]:
            provenance_errors.append(
                _issue("STATUS_SUBJECT_MISMATCH", claim["id"], f"{status_id} names {ids[status_id][1]['subject_id']}")
            )

    for status in state["statuses"]:
        require_sources(status, _reference_values(status, "source_ids"), "status source")
        if status["subject_id"] not in domain_ids:
            provenance_errors.append(
                _issue("UNRESOLVED_STATUS_SUBJECT", status["id"], status["subject_id"])
            )

    for artifact in state["artifacts"]:
        require_sources(artifact, _reference_values(artifact, "source_ids"), "artifact source")

    for provenance in state["provenance"]:
        subject_id = provenance["subject_id"]
        if subject_id not in domain_ids:
            provenance_errors.append(_issue("UNRESOLVED_PROVENANCE_SUBJECT", provenance["id"], subject_id))
            continue
        subject = ids[subject_id][1]
        if provenance["subject_role"] != subject.get("epistemic_role"):
            provenance_errors.append(
                _issue("ROLE_MISMATCH", provenance["id"], "provenance role differs from subject role")
            )
        require_sources(
            provenance,
            (reference["source_id"] for reference in provenance["source_refs"]),
            "provenance source",
        )

    for relation in state["relations"]:
        for endpoint in ("source_object_id", "target_object_id"):
            if relation[endpoint] not in domain_ids:
                unresolved_relations.append(
                    _issue("UNRESOLVED_RELATION_ENDPOINT", relation["id"], f"{endpoint}: {relation[endpoint]}")
                )
        provenance_id = relation["provenance_id"]
        if provenance_id not in provenance_by_id:
            provenance_errors.append(_issue("UNRESOLVED_PROVENANCE", relation["id"], provenance_id))
        elif provenance_by_id[provenance_id]["subject_id"] != relation["id"]:
            provenance_errors.append(
                _issue("PROVENANCE_SUBJECT_MISMATCH", relation["id"], provenance_id)
            )
        if relation["relation_type"] in _HISTORY_RELATIONS and relation["source_object_id"] == relation["target_object_id"]:
            provenance_errors.append(
                _issue("SILENT_REPLACEMENT", relation["id"], "historical endpoints must have distinct stable IDs")
            )

    for experiment in state["experiments"]:
        provenance_id = experiment["provenance_id"]
        if provenance_id not in provenance_by_id:
            provenance_errors.append(_issue("UNRESOLVED_PROVENANCE", experiment["id"], provenance_id))
        elif provenance_by_id[provenance_id]["subject_id"] != experiment["id"]:
            provenance_errors.append(
                _issue("PROVENANCE_SUBJECT_MISMATCH", experiment["id"], provenance_id)
            )
        reference_fields = {
            "preregistration_artifact_id": "artifacts",
            "implementation_artifact_id": "artifacts",
        }
        for field, expected_collection in reference_fields.items():
            if field in experiment:
                target = experiment[field]
                if target not in ids or ids[target][0] != expected_collection:
                    provenance_errors.append(_issue("UNRESOLVED_EXPERIMENT_REFERENCE", experiment["id"], f"{field}: {target}"))
        for field, expected_collection in (
            ("result_artifact_ids", "artifacts"),
            ("status_ids", "statuses"),
            ("claim_ids", "claims"),
        ):
            for target in _reference_values(experiment, field):
                if target not in ids or ids[target][0] != expected_collection:
                    provenance_errors.append(_issue("UNRESOLVED_EXPERIMENT_REFERENCE", experiment["id"], f"{field}: {target}"))

    for collection, record in records:
        if collection == "provenance" or record.get("epistemic_role") == "SOURCE":
            continue
        attached = provenance_by_subject.get(record["id"], [])
        if len(attached) != 1:
            provenance_errors.append(
                _issue("PROVENANCE_CARDINALITY", record["id"], f"expected exactly one record, found {len(attached)}")
            )
            continue
        provenance = attached[0]
        if record["epistemic_role"] == "NORMALIZED":
            if not provenance["source_refs"]:
                provenance_errors.append(_issue("NORMALIZED_WITHOUT_SOURCE", record["id"], "source_refs is empty"))
            if provenance["parent_normalized_ids"]:
                provenance_errors.append(_issue("NORMALIZED_WITH_DERIVED_PARENTS", record["id"], "normalized state cannot use derived-parent semantics"))
        elif record["epistemic_role"] == "DERIVED":
            parents = provenance["parent_normalized_ids"]
            if not parents:
                provenance_errors.append(_issue("DERIVED_WITHOUT_NORMALIZED_PARENT", record["id"], "parent_normalized_ids is empty"))
            for parent_id in parents:
                parent_entry = ids.get(parent_id)
                if parent_entry is None or parent_entry[1].get("epistemic_role") != "NORMALIZED":
                    provenance_errors.append(_issue("INVALID_NORMALIZED_PARENT", record["id"], parent_id))
                    continue
                parent_provenance = provenance_by_subject.get(parent_id, [])
                if len(parent_provenance) != 1 or not parent_provenance[0]["source_refs"]:
                    provenance_errors.append(_issue("INCOMPLETE_TRANSITIVE_PATH", record["id"], parent_id))

    if unresolved_sources:
        return ValidationReport("UNRESOLVED_SOURCE", _sorted(unresolved_sources))
    if unresolved_relations:
        return ValidationReport("UNRESOLVED_RELATION", _sorted(unresolved_relations))
    if provenance_errors:
        return ValidationReport("PROVENANCE_INVALID", _sorted(provenance_errors))
    return ValidationReport("PROVENANCE_VALID", ())


def validate_file(path: str | Path) -> ValidationReport:
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            state = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return ValidationReport("SCHEMA_INVALID", (_issue("DOCUMENT_ERROR", str(path), str(exc)),))
    return validate_state(state)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate White Rabbit research-state provenance.")
    parser.add_argument("state", help="Path to a research-state JSON document")
    args = parser.parse_args(argv)
    report = validate_file(args.state)
    print(json.dumps(report.as_dict(), indent=2, sort_keys=True))
    return 0 if report.outcome == "PROVENANCE_VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())
