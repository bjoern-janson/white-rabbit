import copy
import json
import unittest
from pathlib import Path

from validator import OUTCOMES, validate_file, validate_state


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def load_fixture(name="valid_state.json"):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


class ResearchStateConstitutionTests(unittest.TestCase):
    def test_all_frozen_schemas_are_parseable_json_schema_documents(self):
        expected = {
            "source.schema.json",
            "claim.schema.json",
            "status.schema.json",
            "relation.schema.json",
            "experiment.schema.json",
            "artifact.schema.json",
            "research_state.schema.json",
        }
        self.assertEqual(expected, {path.name for path in (ROOT / "schema").glob("*.json")})
        for name in expected:
            schema = json.loads((ROOT / "schema" / name).read_text(encoding="utf-8"))
            self.assertEqual("https://json-schema.org/draft/2020-12/schema", schema["$schema"])
            self.assertEqual(name, schema["$id"])

    def test_source_normalized_derived_path_is_valid_and_deterministic(self):
        state = load_fixture()
        first = validate_state(state)
        second = validate_state(copy.deepcopy(state))
        self.assertEqual("PROVENANCE_VALID", first.outcome)
        self.assertEqual(first, second)

    def test_missing_source_is_unresolved_source(self):
        state = load_fixture()
        state["provenance"][0]["source_refs"][0]["source_id"] = "source:missing"
        self.assertEqual("UNRESOLVED_SOURCE", validate_state(state).outcome)

    def test_missing_normalized_parent_is_provenance_invalid(self):
        state = load_fixture()
        state["provenance"][1]["parent_normalized_ids"] = ["claim:missing"]
        report = validate_state(state)
        self.assertEqual("PROVENANCE_INVALID", report.outcome)
        self.assertIn("INVALID_NORMALIZED_PARENT", {issue.code for issue in report.issues})

    def test_broken_relation_is_unresolved_relation(self):
        state = load_fixture("explicit_supersession.json")
        state["relations"][0]["target_object_id"] = "claim:missing"
        self.assertEqual("UNRESOLVED_RELATION", validate_state(state).outcome)

    def test_malformed_object_is_schema_invalid(self):
        state = load_fixture()
        del state["claims"][0]["proposition"]
        self.assertEqual("SCHEMA_INVALID", validate_state(state).outcome)

    def test_status_missing_effective_commit_is_schema_invalid(self):
        state = load_fixture()
        del state["statuses"][0]["effective_commit"]
        self.assertEqual("SCHEMA_INVALID", validate_state(state).outcome)

    def test_status_without_provenance_record_is_provenance_invalid(self):
        state = load_fixture()
        state["provenance"] = [
            record for record in state["provenance"]
            if record["subject_id"] != "status:normalized:v1"
        ]
        report = validate_state(state)
        self.assertEqual("PROVENANCE_INVALID", report.outcome)
        self.assertIn("PROVENANCE_CARDINALITY", {issue.code for issue in report.issues})

    def test_claim_cannot_borrow_another_objects_status(self):
        state = load_fixture()
        state["claims"][0]["status_id"] = "status:derived:v1"
        report = validate_state(state)
        self.assertEqual("PROVENANCE_INVALID", report.outcome)
        self.assertIn("STATUS_SUBJECT_MISMATCH", {issue.code for issue in report.issues})

    def test_duplicate_stable_id_rejects_silent_replacement(self):
        state = load_fixture()
        replacement = copy.deepcopy(state["claims"][0])
        replacement["proposition"] = "A silently changed proposition."
        state["claims"].append(replacement)
        report = validate_state(state)
        self.assertEqual("PROVENANCE_INVALID", report.outcome)
        self.assertIn("DUPLICATE_STABLE_ID", {issue.code for issue in report.issues})

    def test_explicit_supersession_fixture_preserves_both_versions(self):
        state = load_fixture("explicit_supersession.json")
        self.assertEqual("PROVENANCE_VALID", validate_state(state).outcome)
        self.assertEqual(
            {"claim:history:v1", "claim:history:v2"},
            {claim["id"] for claim in state["claims"]},
        )
        relation = state["relations"][0]
        self.assertEqual("SUPERSEDES", relation["relation_type"])
        self.assertNotEqual(relation["source_object_id"], relation["target_object_id"])

    def test_authority_firewall_contains_no_scientific_success_outcome(self):
        forbidden = {
            "WARRANT_SUFFICIENT",
            "SCIENTIFICALLY_VALID",
            "TRUE",
            "CORRECT",
            "SUPPORTED",
            "PROVEN",
        }
        self.assertTrue(forbidden.isdisjoint(OUTCOMES))
        self.assertEqual("PROVENANCE_VALID", validate_file(FIXTURES / "valid_state.json").outcome)


if __name__ == "__main__":
    unittest.main()
