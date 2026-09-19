# Search and interpretation method

Research snapshot: 2026-09-19. Starting point: QuestBench, arXiv 2605.21413v2, and its public dataset repository. Purpose: identify material that can improve the design and evaluation of the personal Chtets writing skill.

This was a targeted, multi-stage literature search with parallel research strands, followed by full-text section reading, source-card checks and synthesis. It is not an exhaustive systematic review, a meta-analysis, a model experiment or a comprehensive dataset audit. No separate automated Deep Research report is claimed.

## Questions and search route

We asked what evidence can inform coherent progression, controlled revision, factual fidelity, author voice, multilingual adaptation and fair evaluation. Discovery used Web search, exact-title follow-ups, bibliographies and author-maintained resources. Broad searches were often noisy, even with domain filters. Unrelated results were discarded; primary pages and paper references supplied the final evidence.

| Strand | Included records | Search log |
| --- | --- | --- |
| Research accountability | RES01–RES03 | [research](search-logs/research.md) |
| Coherence and simplification | COH01–COH06 | [coherence](search-logs/coherence.md) |
| Factual fidelity | FID01–FID06 | [fidelity](search-logs/fidelity.md) |
| Revision and correction | REV01–REV06 | [revision](search-logs/revision.md) |
| Voice and collaboration | VOI01–VOI06 | [voice](search-logs/voice.md) |
| Evaluation | EVA01–EVA06 | [evaluation](search-logs/evaluation.md) |
| Editorial foundations | COM01 | [editorial foundation](search-logs/editorial-foundation.md) |

The logs preserve actual query families, selection decisions, access failures and deferred leads. They are not a complete timestamped search-engine result export. No exact count of all screened search hits is asserted.

## Inclusion

A retained source had to address a concrete writing or evaluation decision; have a verified primary publication or author-hosted version; and permit reading relevant sections beyond its abstract. We inspected methods, findings and limitations pertinent to the proposed use. Resource cards and license files were checked where accessible. Every card lists inspected locations and distinguishes a paper version from a changing release.

Empirical papers, datasets, one critical survey and conceptual editorial works are included for different purposes. A primary empirical paper supports claims about its own study. REV06 is explicitly a literature synthesis: its checklist is useful, but it is not an independent replication of its cited experiments. Conceptual works supply vocabulary and editorial hypotheses, not measured intervention effects.

Secondary summaries, product pages and generated explanations were not used to substantiate scientific findings. Abstract-only leads were deferred. Lack of a retrieved source or confirmed license is recorded rather than filled with assumed metadata. We did not bypass access controls.

## Evidence routes

| `evidence_route` | Meaning | Important boundary |
| --- | --- | --- |
| `direct_writing_research` | Studies writing, editing, text coherence or a closely defined writing quality | Often narrow domains or older systems; does not validate a prompt skill |
| `adjacent_task_transfer` | Research QA, factuality, personalization or general assistant evaluation informs a writing decision | The transfer to Chtets is proposed, not directly measured |
| `conceptual_foundation` | Descriptive or editorial framework | No causal improvement claim follows from the framework alone |
| `literature_synthesis` | Survey-based methodological context | Inherits the limits and overlap of underlying studies |

These labels describe the route of relevance, not a scientific quality ranking. Even direct writing research still requires a separate test before a Chtets efficacy claim. `priority` is a reading recommendation; it is not an evidence certainty score. The `year` is the publication/first-publication label shown in the card; inspected revision details remain in `venue_status` and the section locators.

## Independence, language and version limits

Thirty-four sources do not mean thirty-four independent confirmations. Some reuse datasets or annotations: FActScore and SAFE share an evaluation lineage; G-Eval uses SummEval; several resources depend on Wikipedia or the same news corpora. Keep related sources for distinct contributions without adding their results as independent replications.

English dominates. Chinese appears in research and writing benchmarks; XFORMAL provides French sentence-register evidence. We did not verify sufficiently direct Russian author-voice evidence in this selection. There are no Chtets comparative results for any language in this package.

Publication metadata and release metadata can differ. Preserve the CoEdIT, WritingBench, LitBench and DeepResearch Bench II version notes. Repository availability was observed on the snapshot date, not guaranteed indefinitely. No executable environment was reproduced, and not every linked file or dataset row was inspected.

## From source to proposed rule

Each card separates `finding`, `limitation`, `candidate_rule` and `evaluation_hook`. Rules are explicitly labelled transfer or inference. The development plan compares them with existing Chtets instructions, to avoid presenting established skill behavior as a new contribution.

The 12 evaluation seeds are original synthetic scenarios, not extracted examples. They are public development material. Their protected meanings are editorial judgments requiring calibration; no outputs or scores have been produced. Fresh held-out briefs are required for a subsequent comparative evaluation.

## Quality checks and reproducibility

A separate reviewing agent audited the initial 33 research cards for overclaims, versions, licensing and overlapping evidence, including targeted primary-source checks. COM01 was then added as an explicitly conceptual annotation and reviewed during assembly. This is editorial quality control within the same assistant workflow, not external peer review.

The assembled package is checked for JSON/schema validity, unique IDs, valid source references from examples, the four-per-language distribution, local link targets and archive contents. These checks establish structural integrity, not the truth of every source or the effectiveness of the proposals.

`manifest.json` records the final files and their SHA-256 hashes. It excludes itself to avoid a circular hash. The download archive includes only the named deliverables and search logs; temporary downloaded papers, extracted article text and screenshots are excluded. Repeat research should recheck the linked versions and resource terms instead of assuming the current snapshot remains current.
