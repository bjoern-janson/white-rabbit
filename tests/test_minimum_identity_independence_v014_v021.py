from __future__ import annotations

import inspect
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v021 as m

A = b"mii-extraction-conformance:v1\ncondition=ALPHA\npayload=A"


def case() -> m.Case:
    return m.Case(
        semantic_case_id="SYNTHETIC_ONLY",
        frozen_bytes=A,
        materialized_bytes=A,
        executed_bytes=A,
        declared_object_id="ALPHA",
        convenience_identity_match=True,
        custody_override=None,
    )


class SemanticExtractionConformance(unittest.TestCase):
    def test_01_same_low_level_read_diagnostic_role_does_not_count(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("executed.raw", b"abc")
            before = cost.C_extract_ops
            got = store.read_diagnostic("executed.raw")
        self.assertEqual(got, b"abc")
        self.assertEqual(cost.C_extract_ops, before)

    def test_02_same_low_level_read_authority_role_counts_exactly_one(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("executed.raw", b"abc")
            before = cost.C_extract_ops
            got = store.extract_authority_bytes("executed.raw")
        self.assertEqual(got, b"abc")
        self.assertEqual(cost.C_extract_ops, before + 1)
        self.assertFalse(cost.complete["C_extract_ops"])

    def test_03_failed_authority_extraction_does_not_count_and_is_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("executed.raw", b"abc")
            before = cost.C_extract_ops
            with mock.patch.object(Path, "read_bytes", side_effect=OSError("forced read failure")):
                with self.assertRaises(OSError):
                    store.extract_authority_bytes("executed.raw")
        self.assertEqual(cost.C_extract_ops, before)
        self.assertFalse(cost.complete["C_extract_ops"])

    def test_04_ambiguous_untyped_custody_read_is_forbidden(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("executed.raw", b"abc")
            with self.assertRaises(m.ConformanceError):
                store.read("executed.raw")

    def test_05_chi3_prepare_counts_one_authority_extraction(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(prepared.cost.C_extract_ops, 1)
        self.assertFalse(prepared.cost.complete["C_extract_ops"])
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])

    def test_06_chi2_prepare_diagnostic_read_does_not_count_extraction(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_2", case(), Path(td))
        self.assertEqual(prepared.cost.C_extract_ops, 0)
        self.assertFalse(prepared.cost.complete["C_extract_ops"])

    def test_07_child_serialized_reconstruction_emits_no_extract_event(self):
        source = m.architecture_source("chi_3")
        self.assertIn("def reconstruct_serialized_bytes(text):", source)
        self.assertIn(
            'executed_hash=digest(reconstruct_serialized_bytes(view["executed_raw_bytes_utf8"]))',
            source,
        )
        self.assertNotIn('emit("EXTRACT_OPERATION")', source)

    def test_08_child_extract_event_is_rejected_as_second_definition(self):
        with self.assertRaises(m.ConformanceError):
            m._decode_child_operation_events(b"EXTRACT_OPERATION\n")

    def test_09_valid_child_stream_preserves_parent_extraction_count(self):
        cost = m.Cost()
        cost.C_extract_ops = 1
        m._complete._set_operation_measurement_complete(cost, False)
        stream = (
            b"IDENTITY_COMPARE_OPERATION\n"
            b"SHA256_OPERATION\n"
            b"IDENTITY_COMPARE_OPERATION\n"
        )
        delta = m._merge_child_events_fail_closed(cost, stream)
        self.assertEqual(delta.extract_ops, 0)
        self.assertEqual(cost.C_extract_ops, 1)
        self.assertTrue(cost.complete["C_extract_ops"])

    def test_10_invalid_child_extract_event_fails_total_extraction_closed(self):
        cost = m.Cost()
        cost.C_extract_ops = 1
        with self.assertRaises(m.ConformanceError):
            m._merge_child_events_fail_closed(cost, b"EXTRACT_OPERATION\n")
        self.assertEqual(cost.C_extract_ops, 1)
        self.assertFalse(cost.complete["C_extract_ops"])

    def test_11_semantic_role_not_low_level_primitive_controls_count(self):
        source = inspect.getsource(m.Store)
        self.assertIn("read_diagnostic", source)
        self.assertIn("extract_authority_bytes", source)
        self.assertIn('self.cost.C_extract_ops += 1', source)
        # Exactly one semantic increment site in the successor Store.
        self.assertEqual(source.count('self.cost.C_extract_ops += 1'), 1)

    def test_12_chi3_authority_extraction_failure_during_prepare_never_becomes_zero_complete(self):
        tracking = m.Cost()
        original_store = m.Store

        class FailingStore(original_store):
            def extract_authority_bytes(self, name: str) -> bytes:
                self.cost.complete["C_extract_ops"] = False
                raise OSError("forced authority extraction failure")

        with tempfile.TemporaryDirectory() as td:
            with mock.patch.object(m, "Cost", return_value=tracking):
                with mock.patch.object(m, "Store", FailingStore):
                    with self.assertRaises(OSError):
                        m.prepare("chi_3", case(), Path(td))
        self.assertEqual(tracking.C_extract_ops, 0)
        self.assertFalse(tracking.complete["C_extract_ops"])

    def test_13_aggregate_rejects_incomplete_extraction_measurement(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.C_view_bytes = 3
            cost.complete["C_view_bytes"] = True
            m._complete._set_operation_measurement_complete(cost, True)
            costs.append(cost)
        costs[1].complete["C_extract_ops"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)

    def test_14_view_capture_persistence_and_sha_repairs_are_retained(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertIsNone(prepared.cost.C_view_bytes)
        self.assertFalse(prepared.cost.complete["C_view_bytes"])
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])
        self.assertEqual(prepared.cost.C_persist_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])
        self.assertGreaterEqual(prepared.cost.C_sha256_ops, 2)


if __name__ == "__main__":
    unittest.main()
