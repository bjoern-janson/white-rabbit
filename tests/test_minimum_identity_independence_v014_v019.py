from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v019 as m

A = b"mii-persistence-conformance:v1\ncondition=ALPHA\npayload=A"


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


class PersistenceCompletionConformance(unittest.TestCase):
    def test_01_full_write_counts_exact_bytes_and_is_complete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("evidence.bin", b"abc")
            self.assertEqual(cost.C_persist_bytes, 3)
            self.assertTrue(cost.complete["C_persist_bytes"])
            self.assertEqual(store.read("evidence.bin"), b"abc")

    def test_02_short_write_retains_actual_count_and_is_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)

            def short(path, data, mode):
                with path.open(mode) as stream:
                    return stream.write(data[:2])

            with mock.patch.object(m, "_persistence_write_once", side_effect=short):
                with self.assertRaises(m.ConformanceError):
                    store.write("evidence.bin", b"abc")
            self.assertEqual(cost.C_persist_bytes, 2)
            self.assertFalse(cost.complete["C_persist_bytes"])
            self.assertEqual(store.read("evidence.bin"), b"ab")

    def test_03_zero_byte_short_write_is_zero_but_incomplete(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            with mock.patch.object(m, "_persistence_write_once", return_value=0):
                with self.assertRaises(m.ConformanceError):
                    store.write("evidence.bin", b"abc")
            self.assertEqual(cost.C_persist_bytes, 0)
            self.assertFalse(cost.complete["C_persist_bytes"])

    def test_04_unknown_transfer_exception_never_invents_count(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("prior.bin", b"xy")
            before = cost.C_persist_bytes

            def writes_then_raises(path, data, mode):
                with path.open(mode) as stream:
                    stream.write(data[:1])
                raise OSError("count unavailable to instrument")

            with mock.patch.object(
                m, "_persistence_write_once", side_effect=writes_then_raises
            ):
                with self.assertRaises(OSError):
                    store.write("unknown.bin", b"abc")
            self.assertEqual(cost.C_persist_bytes, before)
            self.assertFalse(cost.complete["C_persist_bytes"])

    def test_05_repeated_overwrite_writes_are_cumulative_not_terminal_size(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("evidence.bin", b"abcd")
            store.write("evidence.bin", b"xy")
            self.assertEqual(cost.C_persist_bytes, 6)
            self.assertEqual(store.retained(), 2)
            self.assertTrue(cost.complete["C_persist_bytes"])

    def test_06_append_uses_same_cumulative_write_currency(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("evidence.bin", b"ab")
            store.append("evidence.bin", b"cde")
            self.assertEqual(cost.C_persist_bytes, 5)
            self.assertEqual(store.read("evidence.bin"), b"abcde")
            self.assertTrue(cost.complete["C_persist_bytes"])

    def test_07_truncate_and_delete_do_not_erase_prior_write_cost(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("evidence.bin", b"abcd")
            self.assertEqual(cost.C_persist_bytes, 4)
            store.truncate("evidence.bin", 1)
            self.assertEqual(cost.C_persist_bytes, 4)
            store.delete("evidence.bin")
            self.assertEqual(cost.C_persist_bytes, 4)
            self.assertTrue(cost.complete["C_persist_bytes"])

    def test_08_delete_then_replacement_write_keeps_prior_and_new_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("evidence.bin", b"abc")
            store.delete("evidence.bin")
            store.write("evidence.bin", b"wxyz")
            self.assertEqual(cost.C_persist_bytes, 7)
            self.assertEqual(store.retained(), 4)

    def test_09_incompleteness_is_sticky_after_later_success(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)

            def short(path, data, mode):
                with path.open(mode) as stream:
                    return stream.write(data[:1])

            with mock.patch.object(m, "_persistence_write_once", side_effect=short):
                with self.assertRaises(m.ConformanceError):
                    store.write("bad.bin", b"abc")
            self.assertEqual(cost.C_persist_bytes, 1)
            self.assertFalse(cost.complete["C_persist_bytes"])

            store.write("later.bin", b"zz")
            self.assertEqual(cost.C_persist_bytes, 3)
            self.assertFalse(cost.complete["C_persist_bytes"])

    def test_10_chi2_prepare_persists_exact_executed_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_2", case(), Path(td))
        self.assertEqual(prepared.cost.C_persist_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])

    def test_11_chi0_no_persistence_path_is_complete_zero(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        self.assertEqual(prepared.cost.C_persist_bytes, 0)
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])

    def test_12_aggregate_rejects_incomplete_persistence(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.mark_view(b"abc")
            m._capture._sha._complete._set_operation_measurement_complete(cost, True)
            costs.append(cost)
        costs[4].complete["C_persist_bytes"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)


if __name__ == "__main__":
    unittest.main()
