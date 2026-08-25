import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "tools" / "g7_neutral_control_search_v0_1.py"
SPEC = importlib.util.spec_from_file_location("g7_search", MODULE_PATH)
assert SPEC and SPEC.loader
g7 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(g7)


class Gate7NeutralControlSearchTests(unittest.TestCase):
    def test_cartesian_product_order_and_product_index(self):
        tuples = list(g7.iter_option_tuples())
        self.assertEqual(15625, len(tuples))
        self.assertEqual((0, 0, 0, 0, 0, 0), tuples[0])
        self.assertEqual((0, 0, 0, 0, 0, 1), tuples[1])
        self.assertEqual((4, 4, 4, 4, 4, 4), tuples[-1])
        self.assertEqual(1, g7.product_index(tuples[0]))
        self.assertEqual(2, g7.product_index(tuples[1]))
        self.assertEqual(15625, g7.product_index(tuples[-1]))

    def test_source_construction_reproduces_B0(self):
        source = g7.construct_candidate((0, 0, 0, 0, 0, 0))
        self.assertEqual(g7.B0, source)
        self.assertEqual([], g7.source_rejection_codes(source, (0, 0, 0, 0, 0, 0)))

    def test_forbidden_ascii_folding_and_filter(self):
        self.assertEqual("c_improve", g7.ascii_fold("C_Improve"))
        codes = g7.source_rejection_codes(
            g7.B0 + " C_Improve", (0, 0, 0, 0, 0, 0)
        )
        self.assertIn("FORBIDDEN_SUBSTRING:c_improve", codes)

    def test_structural_admissibility_detects_changes(self):
        source = g7.B0.replace("   ↓", "↓", 1)
        codes = g7.source_rejection_codes(source, (0, 0, 0, 0, 0, 0))
        self.assertIn("ARROW_LINE_COUNT", codes)
        self.assertIn("STRUCTURAL_TEMPLATE_MISMATCH", codes)

    def test_codepoint_byte_and_sha_custody(self):
        self.assertEqual(246, len(g7.B0))
        self.assertEqual(256, len(g7.B0.encode("utf-8")))
        self.assertEqual(g7.EXPECTED_HASHES["B0"], g7.sha256_text(g7.B0))

    def test_unicode_levenshtein_definition(self):
        self.assertEqual(0, g7.levenshtein_codepoints("∝", "∝"))
        self.assertEqual(1, g7.levenshtein_codepoints("↓", "∝"))
        self.assertEqual(3, g7.levenshtein_codepoints("kitten", "sitting"))

    def test_deterministic_tie_break_prefers_B0(self):
        b0 = {"source": g7.B0, "source_sha256": g7.sha256_text(g7.B0)}
        changed_source = g7.B0.replace("pattern", "relation", 1)
        changed = {
            "source": changed_source,
            "source_sha256": g7.sha256_text(changed_source),
        }
        self.assertIs(b0, sorted([changed, b0], key=g7.ranking_key)[0])


if __name__ == "__main__":
    unittest.main()
