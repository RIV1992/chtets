"""Recompute saved pilot totals or export anonymous pairs; never rejudge outputs."""
import argparse
from collections import Counter
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent
LANGUAGES = ("en", "fr", "ru")
PROBE_COUNTS = {"C1": 6, "C2": 6, "C3": 15}


def read_rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def index_rows(rows, id_field="id", *, expected=None, label="rows"):
    indexed = {}
    for row in rows:
        identifier = row[id_field]
        if identifier in indexed:
            raise ValueError(f"{label}: duplicate {id_field} {identifier}")
        indexed[identifier] = row
    if expected is not None and set(indexed) != set(expected):
        missing = sorted(set(expected) - set(indexed))
        extra = sorted(set(indexed) - set(expected))
        raise ValueError(f"{label}: missing ids {missing}; unexpected ids {extra}")
    return indexed


def source_data(root):
    inputs = index_rows(read_rows(root / "stimuli/inputs.jsonl"), label="inputs")
    if Counter(row["lang"] for row in inputs.values()) != Counter({language: 12 for language in LANGUAGES}):
        raise ValueError("inputs: expected 12 cases per language")
    rubrics = index_rows(read_rows(root / "stimuli/rubrics.jsonl"), expected=inputs, label="rubrics")
    key = json.loads((root / "work/blind-key.json").read_text(encoding="utf-8"))
    if set(key) != set(inputs) or any(set(mapping.values()) != {"A", "B"} or set(mapping) != {"X", "Y"} for mapping in key.values()):
        raise ValueError("blind key must map every input once to A/B")
    probe_key = json.loads((root / "work/probe-key.json").read_text(encoding="utf-8"))
    if set(probe_key) != {f"p{number:02d}" for number in range(1, 28)}:
        raise ValueError("probe key must contain p01 through p27")
    if Counter(mapping["condition"] for mapping in probe_key.values()) != Counter(PROBE_COUNTS):
        raise ValueError("probe key must contain 6 C1, 6 C2 and 15 C3 pairs")
    for mapping in probe_key.values():
        if mapping["case_id"] not in inputs or {mapping["X"], mapping["Y"]} != {"B", mapping["condition"]}:
            raise ValueError("probe key has an invalid case or condition mapping")
    outputs = {condition: {} for condition in ("A", "B", *PROBE_COUNTS)}
    for condition in ("A", "B"):
        for language in LANGUAGES:
            expected = {identifier for identifier, row in inputs.items() if row["lang"] == language}
            name = f"outputs/{condition}-{language}.jsonl"
            outputs[condition].update(index_rows(read_rows(root / name), expected=expected, label=name))
    for condition, count in PROBE_COUNTS.items():
        expected = {mapping["case_id"] for mapping in probe_key.values() if mapping["condition"] == condition}
        if len(expected) != count:
            raise ValueError(f"{condition}: repeated probe case")
        name = f"outputs/{condition}.jsonl"
        outputs[condition] = index_rows(read_rows(root / name), expected=expected, label=name)
    return inputs, rubrics, outputs, key, probe_key


def anonymous_pairs(root=ROOT):
    inputs, rubrics, outputs, key, probe_key = source_data(root)

    def pair(identifier, mapping):
        return {"input": inputs[identifier], "rubric": rubrics[identifier],
                **{label: outputs[mapping[label]][identifier]["text"] for label in ("X", "Y")}}

    result = {f"{language}.jsonl": [pair(identifier, key[identifier]) for identifier, row in inputs.items()
                                   if row["lang"] == language] for language in LANGUAGES}
    probes = [{"pair_id": identifier, **pair(probe_key[identifier]["case_id"], probe_key[identifier])}
              for identifier in sorted(probe_key)]
    # The original draw shuffled X/Y for all 27 pairs, then shuffled the rows.
    # Saved keys remain authoritative for X/Y; consume the same draws for order.
    generator = random.Random(88267)
    for _ in probes:
        labels = ["X", "Y"]
        generator.shuffle(labels)
    generator.shuffle(probes)
    result["probes.jsonl"] = probes
    return result


def aggregate(rows, key, id_field):
    index_rows(rows, id_field, expected=key, label="judgments")
    preferences = Counter()
    failures = Counter()
    for row in rows:
        mapping = key[row[id_field]]
        preference = row["preference"]
        if preference not in {"X", "Y", "tie"}:
            raise ValueError(f"judgment {row[id_field]}: invalid preference {preference}")
        preferences["tie" if preference == "tie" else mapping[preference]] += 1
        for label in ("X", "Y"):
            failures[mapping[label]] += bool(row[label]["critical_failures"])
    return {"pairs": len(rows), "preferences": dict(preferences), "critical_failure_outputs": dict(failures)}


def summarize(root=ROOT):
    inputs, _, _, key, probe_key = source_data(root)
    result = {language: aggregate(read_rows(root / f"blind/judgments-{language}.jsonl"),
                                  {identifier: key[identifier] for identifier, row in inputs.items() if row["lang"] == language}, "id")
              for language in LANGUAGES}
    probe_rows = read_rows(root / "blind/judgments-probes.jsonl")
    index_rows(probe_rows, "pair_id", expected=probe_key, label="probe judgments")
    if any(row["id"] != probe_key[row["pair_id"]]["case_id"] for row in probe_rows):
        raise ValueError("probe judgment case does not match its key")
    probes = {condition: aggregate([row for row in probe_rows if probe_key[row["pair_id"]]["condition"] == condition],
                                  {identifier: mapping for identifier, mapping in probe_key.items() if mapping["condition"] == condition}, "pair_id")
              for condition in PROBE_COUNTS}
    return {"A_vs_B": result, "individual_probes": probes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export-pairs", type=Path, metavar="DIR", help="reconstruct the four original anonymous JSONL bundles")
    args = parser.parse_args()
    try:
        result = summarize()
        if args.export_pairs is not None:
            pairs = anonymous_pairs()
            args.export_pairs.mkdir(parents=True, exist_ok=True)
            for name, rows in pairs.items():
                (args.export_pairs / name).write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8", newline="\n")
        print(json.dumps(result, indent=2))
    except (KeyError, ValueError, OSError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
