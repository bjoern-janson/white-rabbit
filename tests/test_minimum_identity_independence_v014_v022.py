from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v022 as m

A = b"mii-capture-boundary-conformance:v1\ncondition=ALPHA\npayload=A"


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


class CaptureBoundaryConformance(unittest.TestCase):
    def test_01_old_memory_helper_capture_authority_is_disabled(self):
        cost = m.Cost()
        with self.assertRaises(m.ConformanceError):
            cost.capture(b"abc")
        self.assertEqual(cost.C_capture_bytes, 0)

    def test_02_full_evidence_channel_transfer_counts_capture_and_persistence(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.capture_into_evidence("executed.raw", b"abc")
            self.assertEqual(cost.C_capture_bytes, 3)
            self.assertTrue(cost.complete["C_capture_bytes"])
            self.assertEqual(cost.C_persist_bytes, 3)
            self.assertTrue(cost.complete["C_persist_bytes"])
            self.assertEqual(store.read_diagnostic("executed.raw"), b"abc")

    def test_03_partial_channel_transfer_retains_known_work_and_is_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)

            def short(path, data, mode):
                with path.open(mode) as stream:
                    return stream.write(data[:2])

            with mock.patch.object(m._persist, "_persistence_write_once", side_effect=short):
                with self.assertRaises(m.ConformanceError):
                    store.capture_into_evidence("executed.raw", b"abc")
            self.assertEqual(cost.C_capture_bytes, 2)
            self.assertFalse(cost.complete["C_capture_bytes"])
            self.assertEqual(cost.C_persist_bytes, 2)
            self.assertFalse(cost.complete["C_persist_bytes"])

    def test_04_unknown_channel_transfer_never_invents_capture_count(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)

            def writes_then_raises(path, data, mode):
                with path.open(mode) as stream:
                    stream.write(data[:1])
                raise OSError("authoritative count unavailable")

            with mock.patch.object(
                m._persist, "_persistence_write_once", side_effect=writes_then_raises
            ):
                with self.assertRaises(OSError):
                    store.capture_into_evidence("executed.raw", b"abc")
            self.assertIsNone(cost.C_capture_bytes)
            self.assertFalse(cost.complete["C_capture_bytes"])
            self.assertEqual(cost.C_persist_bytes, 0)
            self.assertFalse(cost.complete["C_persist_bytes"])

    def test_05_prepared_memory_value_without_channel_transfer_is_not_capture(self):
        source = b"abc"
        prepared = bytes(source)
        self.assertEqual(prepared, source)
        cost = m.Cost()
        self.assertEqual(cost.C_capture_bytes, 0)
        self.assertTrue(cost.complete["C_capture_bytes"])

    def test_06_successful_memory_preparation_then_failed_channel_write_is_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            prepared = bytes(b"abc")
            with mock.patch.object(
                m._persist,
                "_persistence_write_once",
                side_effect=OSError("channel write failed"),
            ):
                with self.assertRaises(OSError):
                    store.capture_into_evidence("executed.raw", prepared)
            self.assertIsNone(cost.C_capture_bytes)
            self.assertFalse(cost.complete["C_capture_bytes"])

    def test_07_later_rewrite_adds_persistence_but_never_capture(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.capture_into_evidence("executed.raw", b"abc")
            capture_before = cost.C_capture_bytes
            store.write("executed.raw", b"wxyz")
            self.assertEqual(cost.C_capture_bytes, capture_before)
            self.assertEqual(cost.C_persist_bytes, 7)

    def test_08_delete_replacement_preserves_capture_single_event(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.capture_into_evidence("executed.raw", b"abc")
            store.delete("executed.raw")
            store.write("executed.raw", b"zz")
            self.assertEqual(cost.C_capture_bytes, 3)
            self.assertEqual(cost.C_persist_bytes, 5)

    def test_09_chi2_prepare_capture_is_exact_custody_transfer(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_2", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])
        self.assertEqual(prepared.cost.C_persist_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])
        self.assertEqual(prepared.cost.C_extract_ops, 0)

    def test_10_chi3_prepare_capture_and_authority_extraction_are_distinct(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])
        self.assertEqual(prepared.cost.C_persist_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])
        self.assertEqual(prepared.cost.C_extract_ops, 1)
        self.assertFalse(prepared.cost.complete["C_extract_ops"])

    def test_11_chi0_and_chi1_no_capture_paths_are_complete_zero(self):
        for chi in ("chi_0", "chi_1"):
            with self.subTest(chi=chi):
                with tempfile.TemporaryDirectory() as td:
                    prepared = m.prepare(chi, case(), Path(td))
                self.assertEqual(prepared.cost.C_capture_bytes, 0)
                self.assertTrue(prepared.cost.complete["C_capture_bytes"])

    def test_12_incomplete_capture_blocks_aggregate(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.C_view_bytes = 3
            cost.complete["C_view_bytes"] = True
            m._complete._set_operation_measurement_complete(cost, True)
            costs.append(cost)
        costs[3].C_capture_bytes = 2
        costs[3].complete["C_capture_bytes"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)

    def test_13_semantic_extraction_rules_are_retained(self):
        source = m.architecture_source("chi_3")
        self.assertNotIn('emit("EXTRACT_OPERATION")', source)
        self.assertIn("reconstruct_serialized_bytes", source)

    def test_14_view_dispatch_authority_remains_pending_after_prepare(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertIsNone(prepared.cost.C_view_bytes)
        self.assertFalse(prepared.cost.complete["C_view_bytes"])
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])


if __name__ == "__main__":
    unittest.main()
