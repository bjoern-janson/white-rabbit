from __future__ import annotations

import json
import unittest
from pathlib import Path

from tools.validate_authority_propagation import CHECKPOINT, validate


ROOT = Path(__file__).resolve().parents[1]


class AuthorityPropagationTests(unittest.TestCase):
    def test_current_repository_authority_surfaces_validate(self):
        self.assertEqual(validate(ROOT), [])

    def test_open_scientific_lanes_are_explicitly_unauthorized(self):
        state = json.loads((ROOT / "program/CURRENT_AUTHORITY_STATE.json").read_text())
        self.assertFalse(state["gate7"]["q1_replication"]["authorized"])
        self.assertFalse(state["gate7"]["q3_replication"]["authorized"])
        self.assertFalse(state["mii"]["authorized"])
        self.assertEqual(state["mii"]["n_assay"], 0)

    def test_orientation_epoch_is_single_valued(self):
        marker = f"Authority checkpoint: `{CHECKPOINT}`"
        for rel in (
            "README.md",
            "program/STATE.md",
            "program/ROADMAP.md",
            "assays/README.md",
        ):
            text = (ROOT / rel).read_text()
            self.assertIn(marker, text)

    def test_robustness_current_surface_withdraws_panel_authority(self):
        text = (ROOT / "assays/G7_NEUTRAL_CONTROL_ROBUSTNESS_ASSAY_V0_1_1_RESULT.md").read_text()
        self.assertIn("PANEL_SCIENTIFIC_AUTHORITY_WITHDRAWN", text)
        self.assertIn("not a current panel-level scientific conclusion", text)

    def test_q2_is_not_silently_promoted(self):
        for rel in (
            "assays/G7_Q1_REPLICATION_ASSAY_V0_1_1.md",
            "assays/G7_Q3_REPLICATION_ASSAY_V0_1_1.md",
        ):
            text = (ROOT / rel).read_text()
            self.assertIn("SOURCE_UNRESOLVED_IN_THIS_REPOSITORY", text)
            self.assertIn("Q2_OBSERVATIONS_ENTERING_", text)

    def test_platform_residual_is_not_hidden(self):
        state = json.loads((ROOT / "program/CURRENT_AUTHORITY_STATE.json").read_text())
        platform = state["platform_enforcement"]
        self.assertFalse(platform["main_branch_protected"])
        self.assertFalse(platform["rulesets_present"])
        self.assertEqual(platform["status"], "MACHINE_CHECKED / PLATFORM_BYPASSABLE")


if __name__ == "__main__":
    unittest.main()
