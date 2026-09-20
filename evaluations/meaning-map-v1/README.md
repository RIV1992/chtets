# Meaning-map functional release check

Date: September 20, 2026. This is a small synthetic check before field use of v1.2.0, not an efficacy study or a real standards assessment.

## Conditions and method

- **A:** public v1.1.1 at `9eeb3bc6d1b7a2efd9f1b32ea1d95c93b4fbc2f8`.
- **B:** v1.2.0 candidate, identified by the exact runtime file hashes in [conditions.json](conditions.json).
- Eight new synthetic requests: three Russian, two French, and three English inputs, with translation into English in one request. The set covers standards applicability, denominator changes, commitments, shortening, translation, limited proofreading, intentional ambiguity, and ordinary correspondence.
- One fresh writer per condition, one eight-request batch each. Both used the same inherited model and reasoning configuration in the same host; exact model internals, computation, token use, and comparable latency were not exposed. Neither writer saw the rubrics or the other condition.
- A fresh model reviewer saw the original requests, frozen rubrics, and anonymous x/y outputs in alternating order. It did not receive condition identities. Preference was assessed after correctness; ties were allowed.

The [protocol](protocol.md) records the scope change from the larger proposed experiment. Inputs and rubrics were frozen before either writer ran. No skill instruction was changed after these candidate outputs were generated.

## Observations

| Observation | Baseline A | Candidate B |
| --- | ---: | ---: |
| Requests without a reviewer-reported critical failure | 8 / 8 | 8 / 8 |
| Editorial preferences | 0 | 1 |

Seven pairs tied. In the standards case, the reviewer slightly preferred B because the concluding protocol condition retained its explicit 2024-edition qualifier. A had established that qualification earlier, so the reviewer treated its shorter conclusion as a minor ambiguity, not a critical failure. This is one model preference, not a demonstrated general improvement.

Both outputs also passed direct checks of the 65-word shortening limit, unchanged lexical sequence in punctuation-only editing, exact preserved French quotation, the requested keep-as-written response, and the final `Merci,` sign-off. These checks assess explicit constraints rather than literary quality.

The candidate's observed reads included the core, meaning map, evidence, and review; baseline reads included the core, evidence, and review. The [inventory](read-inventory.json) records batch-level reads. It cannot establish whether each routine request would avoid loading optional references in a fresh session. The candidates' routine outputs did not expose unnecessary maps or audits.

## Artifacts and interpretation

- [Inputs](inputs.jsonl) and [frozen acceptance rubrics](rubrics.jsonl).
- [Baseline outputs](outputs/A.jsonl) and [candidate outputs](outputs/B.jsonl).
- [Anonymous judgments](judgments.jsonl), [pair key](pair-key.json), and [runtime hashes](conditions.json).

For any judgment, resolve x/y through `pair-key.json`, then read that condition's matching output ID. Recompute preference totals from these records; the temporary anonymous joined bundle is not duplicated in the repository.

Package validation and all 11 repository tests passed, including extended-reference resolution, archive boundaries, and deterministic packaging. The core is 798 whitespace words; the compact prompt 842; the optional meaning-map reference 428; the extended prompt 3,555. These counts are not model tokens. The installed personal copy retains its private voice file and interface metadata; none is included here.

The release is accepted for field use with an optional procedure. The larger 24-case comparison, C2 reminder ablation, repeated runs, human voice judgment, actual GOST source reading, and full-length report evaluation have **not** been performed. All cases are now public development material, not a held-out set. Preserve concrete failures and useful interventions from future work without publishing private project material. An apparent dependency remains a hypothesis to check against the source; revert or narrow the procedure if it creates errors or unnecessary work.
