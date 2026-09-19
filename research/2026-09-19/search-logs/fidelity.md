# Fidelity search log

Checked: 2026-09-19. Scope: complementary research for the public English Chtets skill. This is a curated evidence register, not a systematic review or a redistributed training corpus. No skill or repository was edited.

## Search process

Web search queries included:

- `FActScore Fine-grained Atomic Evaluation Factual Precision Long Form Text Generation ACL 2023`
- `ALCE Enabling Large Language Models Generate Text Citations EMNLP 2023`
- `RARR Researching and Revising What Language Models Say Using Language Models ACL 2023`
- `FRANK A Benchmark for Factuality Metrics Summarization ACL 2021 dataset github`
- `Long-form factuality in large language models SAFE LongFact ICLR 2024 2025 github`
- `uncertainty preserving hedging editing scientific summarization factuality dataset modality`
- `"FRANK" "A Benchmark" factuality` (ACL domain filter)
- `"FActScore" "2023.emnlp"` (ACL domain filter)
- `"uncertainty" "summarization" "hedging"` (ACL domain filter)
- `"Measuring the Uncertainty" "Scientific"`
- `"hedging" "scientific" "summarization" LLM`
- `"Long-form factuality in large language models" conference`
- `"Generalization Bias in Large Language Model Summarization of Scientific Research"`

Some broad and domain-filtered searches returned irrelevant or root-page results. The workflow then opened canonical publication pages and followed official paper/repository links. LongFact venue was corrected from a search hypothesis to verified NeurIPS 2024. The anchor QuestBench abstract was opened to check topic alignment; it is not duplicated in this subcorpus.

## Selection rationale

Six complementary sources were retained: atomic factual support, citation support, controlled correction, discourse-level errors, long-form evaluation, and scope preservation. All six have verified peer-reviewed publication records. Selected full-text sections were read; the register lists their locators. “Editorial transfer” means a proposed skill rule inspired by evidence, not a demonstrated Chtets intervention.

FActScore and SAFE distinguish source support from universal truth. ALCE offers two citation checks but does not certify source trustworthiness. RARR gives an especially useful check against needless corrections. FRANK catches errors in causal/temporal links and modality. The generalization study adds a failure type not captured by checking isolated entities. Its historical model comparisons are not portable to September 2026 model rankings.

## Exclusions and deferrals

- FaStFACT (arXiv:2510.12839), FactReasoner (arXiv:2502.18573), and FactAlign (arXiv:2410.01691) surfaced in search. Deferred: pipeline efficiency/probabilistic evaluation/training are less directly useful to a portable editorial procedure; abstracts alone are insufficient for inclusion.
- SciZoom (arXiv:2603.16131) surfaced indirectly. Deferred without full-text verification; no claim made about its findings or release status.
- TruthfulQA and HaluEval are useful for broader factuality testing but their short-answer focus adds less to this six-source writing subset.
- A remembered uncertainty-study title could not be reliably retrieved; excluded instead of inventing metadata.
- Aggregator summaries, social posts and generated paper explanations were discovery leads only, never evidence for final annotations.

## Access and licensing checks

- ACL paper PDFs and official GitHub repositories were accessible. MIT LICENSE files were read for FActScore, ALCE and FRANK. These licenses were not extended by assumption to external datasets or copyrighted source articles.
- LongFact's official README explicitly separates software (Apache-2.0) from other repository materials (CC BY 4.0).
- RARR's inspected root and README showed no license declaration; mark unverified, not “openly reusable”. Historical API instructions were not installation-tested.
- Generalization Bias: PubMed verifies journal/date/DOI. Publisher and DOI access failed; PMC returned a bot challenge. The arXiv author PDF was read. Two OSF targets were extracted from the PDF hyperlinks; canonical project URLs returned 403. The PDF includes view-only variants, which are deliberately not copied into the public register. Dataset contents and license remain unverified.
- ALCE arXiv HTML request failed; ACL PDF supplied full text. Generalization Bias arXiv HTML failed; PDF supplied full text. No browser fallback or access-control bypass was used.
- Full benchmark rows were not downloaded, redistributed, or used for training. Resource availability means the stated page/repository was inspected, not that every linked download was fetched or executed.

## Guardrails for integration

Use original synthetic editing tests with explicit source facts. Score faithfulness, useful coverage, citation support and voice separately. Do not improve a factuality score by deleting all difficult content. Preserve uncertainty when present; do not add uncertainty mechanically to well-supported claims. Verification should distinguish supported, contradicted, unresolved and source-conflicted cases rather than conflate every unsuccessful search with falsity. These are editorial synthesis recommendations, not paper-tested Chtets improvements.
