"""Preserve published v1.2.0 evidence independently of the evolving skill."""

import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "evaluations/meaning-map-v1"
# Captured from the published v1.2.0 source; new runs belong in separate folders.
FROZEN_HASHES = {
    "inputs.jsonl": "a65991f4d667ed6b708a5ea44987d18d43e7e206166b010fe19da5fdf75fd023",
    "rubrics.jsonl": "dd2f5c8826d9f331ad9ece4af36db66fff8489afd3e856202ad8d35afddd1263",
    "outputs/A.jsonl": "3899b5cc061687009d0e1537d06cfd8de4bce6b212e143977b67b42d133e81a0",
    "outputs/B.jsonl": "502721742a6a0644eda269adc7e8a309437e0c25d1798ed33b1575faac8ad351",
    "judgments.jsonl": "e3dc2190f35931cf25ace46012d2ac76a0abe36e0926d303e00f519d00619641",
    "pair-key.json": "5c26857a1ecde3b6b4ad40489a9cc055cff1f08203b82c1085b34864cffd2855",
    "conditions.json": "9524aa82be861ab2fdb399fa1c975fc2f502411227dacf464a6b0d9b26993af8",
    "read-inventory.json": "a5fea7728833939dc89172ffa2e0f11eb9460f8f1379bff023b8544d7541983b",
}


class MeaningMapArtifactTests(unittest.TestCase):
    def rows(self, name):
        rows = [json.loads(line) for line in (ROOT / name).read_text(encoding="utf-8").splitlines() if line.strip()]
        ids = [row["id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)), f"duplicate IDs in {name}")
        return {row["id"]: row for row in rows}

    def test_frozen_records_unchanged(self):
        for name, expected in FROZEN_HASHES.items():
            with self.subTest(file=name):
                # Ignore checkout line endings, as the release builder does.
                data = (ROOT / name).read_text(encoding="utf-8").encode("utf-8")
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected, f"published evidence changed: {name}")
        maintenance = ROOT.parent / "maintenance-v1.2.1/results.json"
        self.assertEqual(
            hashlib.sha256(maintenance.read_text(encoding="utf-8").encode("utf-8")).hexdigest(),
            "476bdcec50477cf36b0a9dd3272217fa9d22b01a711bea75770f58bbd4a3e265",
            "v1.2.1 functional-check record changed; preserve it and add a new run separately",
        )

    def test_every_input_has_its_rubric_outputs_and_judgment(self):
        inputs = self.rows("inputs.jsonl")
        self.assertTrue(inputs)
        for name in ("rubrics.jsonl", "outputs/A.jsonl", "outputs/B.jsonl", "judgments.jsonl"):
            with self.subTest(file=name):
                rows = self.rows(name)
                self.assertEqual(set(rows), set(inputs), f"case coverage differs in {name}")
                if name.startswith("outputs/"):
                    self.assertTrue(all(isinstance(row["output"], str) and row["output"].strip() for row in rows.values()))

    def test_anonymous_pairs_resolve_to_both_conditions(self):
        judgments = self.rows("judgments.jsonl")
        key = json.loads((ROOT / "pair-key.json").read_text(encoding="utf-8"))
        conditions = json.loads((ROOT / "conditions.json").read_text(encoding="utf-8"))
        self.assertEqual(set(key), set(judgments))
        for case_id, mapping in key.items():
            with self.subTest(case=case_id):
                self.assertEqual(set(mapping), {"x", "y"})
                self.assertEqual(set(mapping.values()), set(conditions))
                self.assertIn(judgments[case_id]["preference"], {"x", "y", "tie"})
                for label in ("x", "y"):
                    self.assertIsInstance(judgments[case_id][label]["critical_failures"], list)


if __name__ == "__main__":
    unittest.main()
