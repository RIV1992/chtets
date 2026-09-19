# Research influence and boundaries

Chtets combines evidence discipline, editorial judgment, and an optional author profile. These components have different foundations and should be assessed separately.

## What QuestBench contributed

[Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work](https://arxiv.org/abs/2605.21413v2) describes a course-built benchmark for research answers. Its value to this project is the demand for a bounded question, explicit acceptance criteria, and verifiable evidence. It is not a study of prose quality or an experiment on Chtets.

The companion [dataset](https://huggingface.co/datasets/PKUAIWeb/QuestBench/tree/9fb523b20fb89cbd0cbd15c07086394a91c5be54) was examined at a fixed revision. Its 256 records cover 14 domain labels. A structural pass and model-assisted reading of every question, answer, and rubric informed the design; this was not an independent external fact-check of every reference answer.

## Why the reference answer also needs scrutiny

A concrete example shows the value of checking the evaluation itself. Record 137 and the paper's Appendix C.2 identify FRUS document 64 as the expected archive reference. The official archive shows that [document 64](https://history.state.gov/historicaldocuments/frus1961-63v11/d64) is a Kennedy–Ball telephone conversation. [Document 80](https://history.state.gov/historicaldocuments/frus1961-63v11/d80) is Scali's memorandum describing a lunch with Fomin. The latter page is undated, so its identity and the full chronology must be treated as separate questions. The contents are sufficient to reject the supplied document 64 match.

Internal inconsistencies were also visible without solving the underlying research tasks: record 27 asks for a price but supplies names; record 94 announces 100 points while its stated positive components total at most 70; record 198 pairs Chinese occupational labels with contradictory English translations. These are scoped observations about those records, not an estimate of the dataset's overall factual error rate.

The practical lesson is to inspect the task, evidence, output, and assessment criterion separately. Matching a reference is useful only when the reference and the task are sound.

## What is an editorial design choice

Chtets adds composition, paragraph function, sentence transitions, rhythm, compression, genre, and author voice. These are the project's editorial guidance. They are not findings established by the QuestBench experiment.

| Observation or need | Chtets design choice | A useful check |
| --- | --- | --- |
| A plausible answer may address a different question | Establish the reader's goal and required content | Compare the finished text with the request |
| A citation may support only part of a claim | Check the specific claim against its source and context | Inspect the supporting passage |
| An older term may be treated as the only correct one | Track date, edition, and scope | Verify which version the task needs |
| An answer key may be wrong | Allow evidence to correct the reference | Resolve the conflict without forcing a match |
| Correct facts can still form a disjointed draft | Give paragraphs a function and inspect transitions | Explain how the next sentence follows |
| A polished draft can lose the author's voice | Use supplied preferences and actual experience | Let the author judge whether the thought is theirs |

Research benchmarks often make retrieval deliberately difficult. Everyday writing benefits from a direct path to adequate evidence. Chtets does not require extra searches or elaborate reasoning chains when the task is already clear.

## Complementary research corpus

The [September 19 corpus](../research/2026-09-19/README.md) contains 34 original annotations covering coherence, factual fidelity, revision, author voice, and evaluation. Each card records inspected source sections, findings, limits, a candidate instruction, and a way to test it. The [methodology](../research/2026-09-19/methodology.md) distinguishes direct writing research, transfer from adjacent tasks, conceptual foundations, and synthesis.

The sources motivate checking population and comparison boundaries, sentence dependencies after an edit, and whether a proposed repair improves an identified defect. They also motivate evidence-aware revision and caution with author-voice judgments. These are hypotheses for Chtets, not effects established by those papers. Several already overlap the existing workflow; adding another wording is not automatically an improvement.

The corpus and its public development scenarios are source documentation, excluded from the skill archive and both manual prompts. See [development](development.md) for implementation criteria and [evaluation](evaluation.md) for the observed results and untested questions.

## Source snapshot

- Paper: arXiv `2605.21413v2`, dated May 21, 2026.
- Dataset repository: `PKUAIWeb/QuestBench`.
- Dataset revision: `9fb523b20fb89cbd0cbd15c07086394a91c5be54`.
- File: `questbench.jsonl`, 187,696 bytes.
- SHA-256: `5429d4f3fc2ea51b9bf3e6e351e7a079c75d5d00d068bf2830960444d35587dd`.
- Audit date: September 19, 2026.

This repository includes original instructions and analysis, not the paper, dataset corpus, or third-party execution code. The MIT license applies to this repository's original material. See [evaluation](evaluation.md) for the limits of the testing performed on Chtets itself.
