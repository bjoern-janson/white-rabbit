from __future__ import annotations

import json
import sys
from pathlib import Path

CHECKPOINT = "WR_AUTHORITY_2026_08_26_V1"
ORIENTATION_FILES = (
    "README.md",
    "program/STATE.md",
    "program/ROADMAP.md",
    "assays/README.md",
)
AUTH_FILES = (
    "authority/execution/G7_Q1_REPLICATION_V0_1.json",
    "authority/execution/G7_Q3_REPLICATION_V0_1.json",
    "authority/execution/MINIMUM_IDENTITY_INDEPENDENCE_V0_1_4.json",
)


class AuthorityValidationError(RuntimeError):
    pass


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise AuthorityValidationError(f"invalid json: {path}") from exc


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []

    checkpoint_path = root / "program" / "CURRENT_AUTHORITY_STATE.json"
    if not checkpoint_path.is_file():
        return ["missing program/CURRENT_AUTHORITY_STATE.json"]

    state = load_json(checkpoint_path)
    if state.get("orientation_epoch") != CHECKPOINT:
        errors.append("authority checkpoint mismatch")

    marker = f"Authority checkpoint: `{CHECKPOINT}`"
    for rel in ORIENTATION_FILES:
        path = root / rel
        if not path.is_file():
            errors.append(f"missing orientation file: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if marker not in text:
            errors.append(f"stale/missing orientation checkpoint: {rel}")

    robustness = root / "assays" / "G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md"
    if not robustness.is_file():
        errors.append("missing robustness result")
    else:
        text = robustness.read_text(encoding="utf-8")
        if "PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN" not in text:
            errors.append("robustness result does not expose withdrawn authority")
        if "historical analyzer output" not in text.lower():
            errors.append("robustness historical terminal is not explicitly demoted")

    v03 = root / "assays" / "G7_MATCHED_CONTEXT_ASSAY_V0_3_RESULT.md"
    if not v03.is_file():
        errors.append("missing G7 v0.3 result")
    else:
        text = v03.read_text(encoding="utf-8")
        for required in (
            "HISTORICAL_LOCAL_OBSERVATION",
            "PROSPECTIVE_EXECUTION_PROVENANCE_LIMIT",
            "H_frozen = H_materialized = H_executed",
        ):
            if required not in text:
                errors.append(f"G7 v0.3 current-authority notice missing: {required}")

    for rel in (
        "assays/G7_Q1_REPLICATION_ASSAY_V0_1_1.md",
        "assays/G7_Q3_REPLICATION_ASSAY_V0_1_1.md",
    ):
        path = root / rel
        if not path.is_file():
            errors.append(f"missing successor constitution: {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "SOURCE_UNRESOLVED_IN_THIS_REPOSITORY" not in text:
            errors.append(f"Q2 source is not explicitly unresolved in {rel}")
        if "Scientific observations under parent or successor: `0`" not in text:
            errors.append(f"scientific observation firewall missing in {rel}")

    for rel in AUTH_FILES:
        path = root / rel
        if not path.is_file():
            errors.append(f"missing execution authorization object: {rel}")
            continue
        obj = load_json(path)
        if obj.get("schema_version") != "WHITE_RABBIT_EXECUTION_AUTHORIZATION_V0.1":
            errors.append(f"bad authorization schema version: {rel}")
        if obj.get("authority_checkpoint") != CHECKPOINT:
            errors.append(f"authorization checkpoint mismatch: {rel}")
        if obj.get("authorized") is not False:
            errors.append(f"open lane unexpectedly authorized: {rel}")

    mii_review = root / "assays" / "MINIMUM_IDENTITY_INDEPENDENCE_IMPLEMENTATION_V0_1_12_RUNTIME_REVIEW.md"
    if not mii_review.is_file():
        errors.append("missing MII runtime review")
    else:
        text = mii_review.read_text(encoding="utf-8")
        if "IMPLEMENTATION_REVIEW: PASS" not in text:
            errors.append("MII implementation pass missing")
        if "ASSAY_EXECUTION_AUTHORIZATION:" not in text or "NOT_GRANTED_BY_THIS_RECORD" not in text:
            errors.append("MII review does not preserve separate assay authorization")

    inventory = root / "program" / "AUTHORITY_PROPAGATION_INVENTORY_V0_1.md"
    if not inventory.is_file():
        errors.append("missing authority propagation inventory")
    else:
        text = inventory.read_text(encoding="utf-8")
        if "UNIVERSAL_PROPAGATION_MECHANISM_NOT_EARNED" not in text:
            errors.append("inventory overclaims common mechanism")

    platform = state.get("platform_enforcement", {})
    if platform.get("main_branch_protected") is not False:
        errors.append("checkpoint must not claim branch protection that was not observed")
    if platform.get("status") != "MACHINE_CHECKED / PLATFORM_BYPASSABLE":
        errors.append("platform enforcement residual missing")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("AUTHORITY_PROPAGATION_INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("AUTHORITY_PROPAGATION_VALID")
    print(f"authority_checkpoint={CHECKPOINT}")
    print("scientific_execution_authorized=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
