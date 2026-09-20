"""Check saved evidence integrity and exact reconstruction, without model runs."""

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1] / "evaluations/2026-09-19"
SPEC = importlib.util.spec_from_file_location("evaluation", ROOT / "summarize.py")
EVALUATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVALUATION)

# Captured from the original anonymous bundles before removing those duplicates.
ORIGINAL_PAIR_HASHES = {
    "en.jsonl": "e8d8f2ca68a965c6f169d6edc64e24b5e6adc1d7503676c682290048726c7fad",
    "fr.jsonl": "552def2c788bc1588a21cf316899028bbde583c5e31a56d1fed017f57dddae59",
    "ru.jsonl": "9c2210689e44305c35a2380bb631be2a64686852f6d7dea2f261c1b895ffb7ac",
    "probes.jsonl": "7372bc0d41c9a25b13abd9c5dabcd47a872cfa097b4132b061c97360e57f0d83",
}


class EvaluationArtifactTests(unittest.TestCase):
    def test_anonymous_exports_match_original_bytes(self):
        actual = {}
        for name, rows in EVALUATION.anonymous_pairs().items():
            data = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows).encode("utf-8")
            actual[name] = hashlib.sha256(data).hexdigest()
        self.assertEqual(actual, ORIGINAL_PAIR_HASHES)

    def test_missing_or_duplicate_judgment_is_rejected(self):
        rows = EVALUATION.read_rows(ROOT / "blind/judgments-en.jsonl")
        all_keys = json.loads((ROOT / "work/blind-key.json").read_text(encoding="utf-8"))
        key = {row["id"]: all_keys[row["id"]] for row in rows}
        for changed in (rows[:-1], rows + [rows[0]]):
            with self.subTest(count=len(changed)), self.assertRaises(ValueError):
                EVALUATION.aggregate(changed, key, "id")

    def test_missing_output_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "evaluation"
            shutil.copytree(ROOT, root)
            path = root / "outputs/B-en.jsonl"
            path.write_text("\n".join(path.read_text(encoding="utf-8").splitlines()[1:]) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing ids"):
                EVALUATION.summarize(root)

    def test_probe_case_must_match_saved_key(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "evaluation"
            shutil.copytree(ROOT, root)
            path = root / "blind/judgments-probes.jsonl"
            rows = EVALUATION.read_rows(path)
            rows[0]["id"] = "wrong-case"
            path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "case does not match"):
                EVALUATION.summarize(root)


if __name__ == "__main__":
    unittest.main()
