from __future__ import annotations

import ast
import hashlib
import os
import tempfile
import unittest
from pathlib import Path

import tools.minimum_identity_independence_v014_v012 as m

A = b"mii-conformance:v2\ncondition=ALPHA\npayload=A"
B = b"mii-conformance:v2\ncondition=ALPHA\npayload=B"


def case(**overrides):
    data = dict(
        semantic_case_id="SYNTHETIC_ONLY",
        frozen_bytes=A,
        materialized_bytes=A,
        executed_bytes=A,
        declared_object_id="ALPHA",
        convenience_identity_match=True,
        custody_override=None,
    )
    data.update(overrides)
    return m.Case(**data)


class OneWayInstrumentationConformance(unittest.TestCase):
    def test_01_schema_hashes(self):
        m.verify_schemas()

    def test_02_alias_resolution_stays_referee_side(self):
        oracle = {
            "version": m.ORACLE_VERSION,
            "objects": {
                "VISIBLE": {"bytes": A.decode(), "sha256": hashlib.sha256(A).hexdigest()},
                "SECRET_ALIAS": {"bytes": B.decode(), "sha256": hashlib.sha256(B).hexdigest()},
            },
            "critical_clean_controls": [],
            "critical_failures": [
                {
                    "id": "SYNTH",
                    "frozen": "VISIBLE",
                    "materialized": "VISIBLE",
                    "executed": "SECRET_ALIAS",
                    "declared_condition": "ALPHA",
                    "convenience_identity_match": True,
                }
            ],
            "diagnostic_cases": [],
        }
        resolved = m.resolve_case(oracle, "SYNTH")
        self.assertEqual(resolved.executed_bytes, B)
        with tempfile.TemporaryDirectory() as td:
            view = m.prepare("chi_3", resolved, Path(td)).view_bytes
        self.assertNotIn(b"SECRET_ALIAS", view)
        self.assertNotIn(b"SYNTH", view)

    def test_03_forbidden_extra_field_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        import json
        view = json.loads(prepared.view_bytes)
        view["oracle_mismatch"] = True
        with self.assertRaises(m.ConformanceError):
            m.validate("chi_0", view)

    def test_04_handles_are_fresh_opaque_hex64(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            x = m.prepare("chi_0", case(), Path(a)).attestation["case_handle"]
            y = m.prepare("chi_0", case(), Path(b)).attestation["case_handle"]
        self.assertRegex(x, r"^[0-9a-f]{64}$")
        self.assertRegex(y, r"^[0-9a-f]{64}$")
        self.assertNotEqual(x, y)

    def test_05_child_environment_is_minimal(self):
        env = m._minimal_child_env()
        self.assertTrue(set(env).issubset({"SYSTEMROOT", "WINDIR"}))
        for forbidden in ("PYTHONPATH", "PWD", "HOME", "USER", "USERNAME", "MII_SECRET"):
            self.assertNotIn(forbidden, env)

    def test_06_architecture_source_contains_no_readable_meter_or_oracle_channel(self):
        forbidden = (
            "_ArchitectureMeter",
            "Cost(",
            "semantic_case_id",
            "oracle_mismatch",
            "oracle_class",
            "global_ordinal",
            "previous_state",
            "os.environ",
            "os.getenv",
            "open(",
            "socket",
            "subprocess",
        )
        for chi in ("chi_0", "chi_1", "chi_2", "chi_3"):
            source = m.architecture_source(chi)
            for token in forbidden:
                self.assertNotIn(token, source)

    def test_07_emit_is_one_way_and_returns_none(self):
        tree = ast.parse(m.architecture_source("chi_3"))
        emit = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "emit")
        returns = [n for n in ast.walk(emit) if isinstance(n, ast.Return)]
        self.assertEqual(len(returns), 1)
        self.assertIsInstance(returns[0].value, ast.Constant)
        self.assertIsNone(returns[0].value.value)
        self.assertFalse(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in {"input", "eval", "exec"} for n in ast.walk(emit)))

    def test_08_hidden_parent_environment_cannot_change_observable_behavior(self):
        with tempfile.TemporaryDirectory() as td:
            view = m.prepare("chi_3", case(), Path(td)).view_bytes
        old = os.environ.get("MII_SECRET")
        try:
            os.environ["MII_SECRET"] = "oracle-world-A"
            r1 = m.evaluate("chi_3", view)
            os.environ["MII_SECRET"] = "oracle-world-B-different"
            r2 = m.evaluate("chi_3", view)
        finally:
            if old is None:
                os.environ.pop("MII_SECRET", None)
            else:
                os.environ["MII_SECRET"] = old
        self.assertEqual(r1, r2)

    def test_09_hidden_pre_dispatch_ledgers_cannot_change_observable_behavior(self):
        with tempfile.TemporaryDirectory() as td:
            view = m.prepare("chi_3", case(), Path(td)).view_bytes
        hidden_a = m.Cost(C_view_bytes=1, C_sha256_ops=2, C_persist_bytes=7)
        hidden_b = m.Cost(C_view_bytes=999, C_sha256_ops=123, C_persist_bytes=4567)
        hidden_a.complete["C_view_bytes"] = True
        hidden_b.complete["C_view_bytes"] = True
        self.assertNotEqual(hidden_a.vector(), hidden_b.vector())
        self.assertEqual(m.evaluate("chi_3", view), m.evaluate("chi_3", view))

    def test_10_fresh_process_evaluation_is_repeatable(self):
        with tempfile.TemporaryDirectory() as td:
            view = m.prepare("chi_2", case(), Path(td)).view_bytes
        self.assertEqual(m.evaluate("chi_2", view), m.evaluate("chi_2", view))

    def test_11_chi1_does_not_substitute_hm_for_he(self):
        with tempfile.TemporaryDirectory() as td:
            view = m.prepare("chi_1", case(), Path(td)).view_bytes
        self.assertEqual(m.evaluate("chi_1", view).terminal, "IDENTITY_UNRESOLVED")

    def test_12_chi2_chi3_authority_split_survives_process_boundary(self):
        fake_clean = hashlib.sha256(A).hexdigest()
        perturbed = case(executed_bytes=B, custody_override=fake_clean)
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            v2 = m.prepare("chi_2", perturbed, Path(a)).view_bytes
            v3 = m.prepare("chi_3", perturbed, Path(b)).view_bytes
        self.assertEqual(m.evaluate("chi_2", v2).terminal, "IDENTITY_PASS")
        self.assertEqual(m.evaluate("chi_3", v3).terminal, "IDENTITY_MISMATCH")

    def test_13_event_stream_matches_constituted_operations(self):
        expected = {
            "chi_0": m.ArchitectureDelta(0, 0, 0),
            "chi_1": m.ArchitectureDelta(0, 0, 1),
            "chi_2": m.ArchitectureDelta(0, 0, 2),
            "chi_3": m.ArchitectureDelta(1, 1, 2),
        }
        for chi, want in expected.items():
            with tempfile.TemporaryDirectory() as td:
                view = m.prepare(chi, case(), Path(td)).view_bytes
            result = m.evaluate(chi, view)
            self.assertEqual(m._decode_events(result.event_bytes), want)

    def test_14_event_api_has_no_informative_return_channel(self):
        source = m.architecture_source("chi_3")
        self.assertIn("emit(\"SHA256_OPERATION\")", source)
        self.assertIn("emit(\"EXTRACT_OPERATION\")", source)
        self.assertIn("emit(\"IDENTITY_COMPARE_OPERATION\")", source)
        self.assertNotIn("sequence", source.lower())
        self.assertNotIn("timestamp", source.lower())
        self.assertNotIn("count", source.lower())
        self.assertNotIn("history", source.lower())

    def test_15_output_freezes_before_event_decode_and_merge(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_3", case(), Path(td))
            pre = prepared.cost.vector()
            frozen = m.run("chi_3", prepared)
            post = prepared.cost.vector()
        self.assertEqual(frozen.terminal, "IDENTITY_PASS")
        self.assertEqual(prepared.life.events[-1], m.Life.ORDER[3])
        self.assertGreater(post[3], pre[3])
        self.assertGreater(post[4], pre[4])
        self.assertGreater(post[5], pre[5])

    def test_16_referee_join_requires_t3(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        fake = m.Frozen("IDENTITY_PASS", b'{"terminal":"IDENTITY_PASS"}', hashlib.sha256(b'{"terminal":"IDENTITY_PASS"}').hexdigest())
        with self.assertRaises(m.ConformanceError):
            m.score(prepared, fake, False)

    def test_17_event_decoder_rejects_malformed_or_unknown_streams(self):
        with self.assertRaises(m.ConformanceError):
            m._decode_events(b"SHA256_OPERATION")
        with self.assertRaises(m.ConformanceError):
            m._decode_events(b"ORACLE_CLASS\n")
        with self.assertRaises(m.ConformanceError):
            m._decode_events(b"\xff\n")

    def test_18_persistence_is_cumulative_not_terminal(self):
        with tempfile.TemporaryDirectory() as td:
            cost = m.Cost()
            store = m.Store(Path(td), cost)
            store.write("x", b"abcde")
            store.write("x", b"xy")
            store.truncate("x", 1)
            self.assertEqual(store.retained(), 1)
            store.delete("x")
            self.assertEqual(store.retained(), 0)
            self.assertEqual(cost.C_persist_bytes, 7)

    def test_19_view_bytes_and_missingness_are_literal(self):
        with tempfile.TemporaryDirectory() as td:
            prepared = m.prepare("chi_0", case(), Path(td))
        self.assertEqual(prepared.cost.C_view_bytes, len(prepared.view_bytes))
        incomplete = m.Cost()
        self.assertFalse(incomplete.is_complete())

    def test_20_aggregate_and_pareto_contract(self):
        costs = []
        for _ in range(6):
            cost = m.Cost()
            cost.mark_view(b"abc")
            costs.append(cost)
        self.assertEqual(m.aggregate(costs), (18, 0, 0, 0, 0, 0))
        vectors = {
            "a": (1, 1, 1, 1, 1, 1),
            "b": (2, 2, 2, 2, 2, 2),
            "c": (0, 3, 1, 1, 1, 1),
        }
        self.assertTrue(m.dominates(vectors["a"], vectors["b"]))
        self.assertEqual(m.pareto(vectors), {"a", "c"})
        costs[0].complete["C_persist_bytes"] = False
        with self.assertRaises(m.ConformanceError):
            m.aggregate(costs)


if __name__ == "__main__":
    unittest.main()
