from __future__ import annotations

import inspect
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tools.minimum_identity_independence_v014_v020 as m

A = b"mii-view-dispatch-conformance:v1\ncondition=ALPHA\npayload=A"


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


def life_at_t1() -> m.Life:
    life = m.Life()
    life.mark(m.Life.ORDER[0])
    life.mark(m.Life.ORDER[1])
    return life


class SequenceWriter:
    def __init__(self, actions, flush_error: Exception | None = None) -> None:
        self.actions = list(actions)
        self.flush_error = flush_error
        self.data = bytearray()
        self.closed = False

    def write(self, payload) -> int:
        if not self.actions:
            n = len(payload)
        else:
            action = self.actions.pop(0)
            if isinstance(action, Exception):
                raise action
            n = action
        if n > 0:
            self.data.extend(bytes(payload[:n]))
        return n

    def flush(self) -> None:
        if self.flush_error is not None:
            raise self.flush_error

    def close(self) -> None:
        self.closed = True


class FakeProc:
    def __init__(self) -> None:
        self.stderr = object()
        self.stdin = SequenceWriter([])
        self.stdout = object()
        self.returncode = None
        self.killed = False

    def kill(self) -> None:
        self.killed = True
        self.returncode = -9

    def wait(self, timeout=None):
        if self.returncode is None:
            self.returncode = 0
        return self.returncode

    def poll(self):
        return self.returncode


class ExactViewDispatchAccountingConformance(unittest.TestCase):
    def test_01_prepare_leaves_view_measurement_pending(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        self.assertIsNone(prepared.cost.C_view_bytes)
        self.assertFalse(prepared.cost.complete["C_view_bytes"])
        self.assertEqual(tuple(prepared.life.events), m.Life.ORDER[:2])

    def test_02_historical_prepare_time_mark_view_authority_is_disabled(self):
        cost = m.Cost()
        with self.assertRaises(m.ConformanceError):
            cost.mark_view(b"prepared-not-dispatched")
        self.assertIsNone(cost.C_view_bytes)
        self.assertFalse(cost.complete["C_view_bytes"])

    def test_03_full_exact_transfer_records_full_bytes_then_t2_and_complete(self):
        cost = m.Cost()
        life = life_at_t1()
        writer = SequenceWriter([2, 3])
        m._write_exact_view_account_and_mark_t2(writer, b"abcde", cost, life)
        self.assertEqual(bytes(writer.data), b"abcde")
        self.assertTrue(writer.closed)
        self.assertEqual(cost.C_view_bytes, 5)
        self.assertTrue(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:3])

    def test_04_known_partial_transfer_retains_actual_prefix_and_never_emits_t2(self):
        cost = m.Cost()
        life = life_at_t1()
        writer = SequenceWriter([2, 0])
        with self.assertRaises(m.ConformanceError):
            m._write_exact_view_account_and_mark_t2(writer, b"abcde", cost, life)
        self.assertEqual(bytes(writer.data), b"ab")
        self.assertEqual(cost.C_view_bytes, 2)
        self.assertFalse(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_05_unknown_transfer_exception_never_invents_byte_count_or_t2(self):
        cost = m.Cost()
        life = life_at_t1()
        writer = SequenceWriter([OSError("unknown transfer")])
        with self.assertRaises(m.ConformanceError):
            m._write_exact_view_account_and_mark_t2(writer, b"abc", cost, life)
        self.assertIsNone(cost.C_view_bytes)
        self.assertFalse(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_06_flush_failure_after_write_fails_closed_and_never_emits_t2(self):
        cost = m.Cost()
        life = life_at_t1()
        writer = SequenceWriter([3], flush_error=OSError("flush failed"))
        with self.assertRaises(m.ConformanceError):
            m._write_exact_view_account_and_mark_t2(writer, b"abc", cost, life)
        self.assertIsNone(cost.C_view_bytes)
        self.assertFalse(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_07_readiness_failure_leaves_view_pending_and_t2_absent(self):
        cost = m.Cost()
        cost._view_pending()
        life = life_at_t1()
        proc = FakeProc()
        with mock.patch.object(m._life._base, "_launcher", return_value=["sandbox"]):
            with mock.patch.object(m.subprocess, "Popen", return_value=proc):
                with mock.patch.object(m.select, "select", return_value=([], [], [])):
                    with self.assertRaises(m.ConformanceError):
                        m._spawn("source", b"abc", cost=cost, life=life)
        self.assertTrue(proc.killed)
        self.assertIsNone(cost.C_view_bytes)
        self.assertFalse(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_08_view_completion_cannot_be_granted_without_t2(self):
        cost = m.Cost()
        life = life_at_t1()
        with self.assertRaises(m.ConformanceError):
            cost._view_complete_after_t2(3, life)
        self.assertFalse(cost.complete["C_view_bytes"])
        self.assertEqual(tuple(life.events), m.Life.ORDER[:2])

    def test_09_successor_has_single_production_complete_true_assignment(self):
        source = inspect.getsource(m)
        self.assertEqual(source.count('complete["C_view_bytes"] = True'), 1)
        self.assertIn("life.through(Life.ORDER[2])", source)

    def test_10_production_spawn_uses_unbuffered_stdin_transfer_primitive(self):
        source = inspect.getsource(m._spawn)
        self.assertIn("bufsize=0", source)
        self.assertIn("_write_exact_view_account_and_mark_t2", source)

    def test_11_aggregate_rejects_incomplete_view_measurement(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.C_view_bytes = 3
            cost.complete["C_view_bytes"] = True
            m._persist._capture._sha._complete._set_operation_measurement_complete(
                cost, True
            )
            costs.append(cost)
        costs[2].complete["C_view_bytes"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)

    def test_12_persistence_and_capture_repairs_are_retained(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
        self.assertEqual(prepared.cost.C_capture_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_capture_bytes"])
        self.assertEqual(prepared.cost.C_persist_bytes, len(A))
        self.assertTrue(prepared.cost.complete["C_persist_bytes"])
        self.assertIsNone(prepared.cost.C_view_bytes)
        self.assertFalse(prepared.cost.complete["C_view_bytes"])

    def test_13_projection_and_child_operation_completion_semantics_are_retained(self):
        cost = m.Cost()
        before = cost.C_sha256_ops
        cost.projection_sha(b"abc")
        self.assertEqual(cost.C_sha256_ops, before + 1)
        child_source = m._ops.architecture_source("chi_3")
        self.assertIn(
            'result=_h(data).hexdigest()\n    emit("SHA256_OPERATION")\n    return result',
            child_source,
        )


if __name__ == "__main__":
    unittest.main()
