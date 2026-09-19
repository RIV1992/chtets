"""Recompute descriptive pilot totals; this does not rejudge text quality."""
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def aggregate(rows, key, id_field):
    preferences = Counter()
    failures = Counter()
    for row in rows:
        mapping = key[row[id_field]]
        preference = row["preference"]
        preferences["tie" if preference == "tie" else mapping[preference]] += 1
        for label in ("X", "Y"):
            failures[mapping[label]] += bool(row[label]["critical_failures"])
    return {"pairs": len(rows), "preferences": dict(preferences), "critical_failure_outputs": dict(failures)}


def main():
    key = json.loads((ROOT / "work/blind-key.json").read_text(encoding="utf-8"))
    result = {language: aggregate(read_rows(ROOT / f"blind/judgments-{language}.jsonl"), key, "id")
              for language in ("en", "fr", "ru")}
    probe_key = json.loads((ROOT / "work/probe-key.json").read_text(encoding="utf-8"))
    probe_rows = read_rows(ROOT / "blind/judgments-probes.jsonl")
    probes = {condition: aggregate([row for row in probe_rows if probe_key[row["pair_id"]]["condition"] == condition], probe_key, "pair_id")
              for condition in ("C1", "C2", "C3")}
    print(json.dumps({"A_vs_B": result, "individual_probes": probes}, indent=2))


if __name__ == "__main__":
    main()
