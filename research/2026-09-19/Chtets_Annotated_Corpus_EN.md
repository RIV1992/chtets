# Chtets: Annotated Research Corpus

Checked 2026-09-19. 34 sources. Original annotations; linked primary material is not reproduced.

The collection supports research and editorial design. It does not demonstrate the effectiveness of Chtets. Findings, limitations, candidate rules and test ideas are kept separate. Full-text inspection was targeted; locators below state what was read.

Read [the methodology](methodology.md) for selection and evidence-route definitions, [the development plan](../../docs/development.md) for proposed integration, and [the resource register](resource-register.md) before obtaining external datasets.

## Index

| ID | Source | Year | Strand |
| --- | --- | --- | --- |
| [RES01](#res01) | Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work | 2026 | Research accountability |
| [RES02](#res02) | DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents | 2025 | Research accountability |
| [RES03](#res03) | DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports | 2026 | Research accountability |
| [COH01](#coh01) | Rhetorical Structure Theory: Toward a functional theory of text organization | 1988 | Coherence and simplification |
| [COH02](#coh02) | Modeling Local Coherence: An Entity-Based Approach | 2008 | Coherence and simplification |
| [COH03](#coh03) | Understanding Iterative Revision from Human-Written Text | 2022 | Coherence and simplification |
| [COH04](#coh04) | ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations | 2020 | Coherence and simplification |
| [COH05](#coh05) | SWiPE: A Dataset for Document-Level Simplification of Wikipedia Pages | 2023 | Coherence and simplification |
| [COH06](#coh06) | Dancing Between Success and Failure: Edit-level Simplification Evaluation using SALSA | 2023 | Coherence and simplification |
| [FID01](#fid01) | FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation | 2023 | Factual fidelity |
| [FID02](#fid02) | Enabling Large Language Models to Generate Text with Citations | 2023 | Factual fidelity |
| [FID03](#fid03) | RARR: Researching and Revising What Language Models Say, Using Language Models | 2023 | Factual fidelity |
| [FID04](#fid04) | Understanding Factuality in Abstractive Summarization with FRANK: A Benchmark for Factuality Metrics | 2021 | Factual fidelity |
| [FID05](#fid05) | Long-form factuality in large language models | 2024 | Factual fidelity |
| [FID06](#fid06) | Generalization bias in large language model summarization of scientific research | 2025 | Factual fidelity |
| [REV01](#rev01) | CoEdIT: Text Editing by Task-Specific Instruction Tuning | 2023 | Revision and correction |
| [REV02](#rev02) | EditEval: An Instruction-Based Benchmark for Text Improvements | 2022 | Revision and correction |
| [REV03](#rev03) | Self-Refine: Iterative Refinement with Self-Feedback | 2023 | Revision and correction |
| [REV04](#rev04) | CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing | 2024 | Revision and correction |
| [REV05](#rev05) | Large Language Models Cannot Self-Correct Reasoning Yet | 2024 | Revision and correction |
| [REV06](#rev06) | When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | 2024 | Revision and correction |
| [VOI01](#voi01) | CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities | 2022 | Voice and collaboration |
| [VOI02](#voi02) | Olá, Bonjour, Salve! XFORMAL: A Benchmark for Multilingual Formality Style Transfer | 2021 | Voice and collaboration |
| [VOI03](#voi03) | Dear Sir or Madam, May I Introduce the GYAFC Dataset: Corpus, Benchmarks and Metrics for Formality Style Transfer | 2018 | Voice and collaboration |
| [VOI04](#voi04) | Low-Resource Authorship Style Transfer: Can Non-Famous Authors Be Imitated? | 2022 | Voice and collaboration |
| [VOI05](#voi05) | LaMP: When Large Language Models Meet Personalization | 2024 | Voice and collaboration |
| [VOI06](#voi06) | Generative AI enhances individual creativity but reduces the collective diversity of novel content | 2024 | Voice and collaboration |
| [EVA01](#eva01) | WritingBench: A Comprehensive Benchmark for Generative Writing | 2025 | Evaluation |
| [EVA02](#eva02) | LitBench: A Benchmark and Dataset for Reliable Evaluation of Creative Writing | 2025 | Evaluation |
| [EVA03](#eva03) | SummEval: Re-evaluating Summarization Evaluation | 2021 | Evaluation |
| [EVA04](#eva04) | G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | 2023 | Evaluation |
| [EVA05](#eva05) | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | 2023 | Evaluation |
| [EVA06](#eva06) | Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators | 2024 | Evaluation |
| [COM01](#com01) | The Science of Scientific Writing | 1990 | Editorial foundations |

## RES01

**[Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work](https://arxiv.org/html/2605.21413v2)**

2026 · arXiv preprint, v2 (2026-05-21); peer-reviewed publication not verified

**Focus:** research_accountability. **Evidence:** Benchmark and course-practice report. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** QuestBench makes answer acceptance explicit through domain-specific questions, source checks, and reviewed rubrics. Its tasks assess research answers, not the quality of prose. The artifact contains 256 questions across 14 normalized domains.

**Limit.** The abstract’s 16.85% aggregate is not reconciled with Table 2: the unweighted mean of its 13 pass rates is 28.7169%. Different denominators may matter; this needs clarification, not an assumed correction.

**Candidate rule.** Editorial transfer: define acceptance criteria before drafting and audit both the answer and its reference standard.

**Test idea.** Include a deliberately flawed reference answer; prefer supported correction over blind reference matching.

**Language coverage:** Chinese task text; multilingual source retrieval.

**Reading depth:** full_text_selected_sections.

Inspected locations:

- Sections 3.4–3.6: task design and peer review
- Sections 4.1–4.4 and Table 2: evaluation scope and failures
- Appendices A–B: task requirements and review protocol

**Access:** Paper HTML and dataset repository public; dataset viewer reports a schema error. No dataset redistributed.

**Observed terms:** Paper: arXiv perpetual non-exclusive license displayed. Dataset reuse license not verified; package dependency licenses are not a dataset license.

**Additional primary resources:** [resource 1](https://arxiv.org/abs/2605.21413v2); [resource 2](https://huggingface.co/datasets/PKUAIWeb/QuestBench/tree/main).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## RES02

**[DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents](https://arxiv.org/html/2506.11763v1)**

2025 · arXiv preprint v1; later venue status not verified

**Focus:** research_accountability. **Evidence:** Research-report benchmark with human comparison. **Route:** `adjacent_task_transfer`. **Reading priority:** extended.

**Finding.** Separates report quality from citation-based grounding. RACE evaluates task-specific comprehensiveness, depth, instruction following, and readability; FACT checks statement–source pairs. The task set has 50 English and 50 Chinese research requests.

**Limit.** Relative scores depend on reference reports and judge configuration. Supporting a claim with a citation does not independently establish source truth. Human consistency was evaluated on a limited subset.

**Candidate rule.** Editorial transfer: review the argument and evidence separately, with task-specific criteria rather than a single fluent-writing score.

**Test idea.** Pair a readable unsupported report with a supported incomplete one; score evidence and coverage separately.

**Language coverage:** English; Chinese.

**Reading depth:** full_text_selected_sections.

Inspected locations:

- Section 2.2: task collection
- Sections 3.1–3.2: RACE and FACT
- Section 4.3: human consistency
- Appendices A–B: limitations and dimensions

**Access:** Paper, repository, tasks, and evaluation scripts public. Current repository changes evaluator configuration; pin a commit before replication.

**Observed terms:** Repository LICENSE inspected: Apache-2.0. Do not infer a blanket license for third-party webpages or all generated report inputs.

**Additional primary resources:** [resource 1](https://github.com/Ayanami0730/deep_research_bench); [resource 2](https://github.com/Ayanami0730/deep_research_bench/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## RES03

**[DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Reports](https://arxiv.org/abs/2601.08536)**

2026 · arXiv preprint; inspected v1 methods and current official resource terms

**Focus:** research_accountability. **Evidence:** Expert-report-derived benchmark and evaluation framework. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** Derives atomic, content-bearing rubrics from expert reports, separating information recall, analysis, and presentation. It offers a concrete model for evaluating whether a text contains and supports required substance.

**Limit.** Source-article leakage and annotator judgments affect scores. Presentation coverage does not fully evaluate adaptation to a particular reader. Meeting one reference-derived rubric is not the only legitimate way to write.

**Candidate rule.** Editorial transfer: make factual acceptance tests specific, but leave room for multiple valid structures and styles.

**Test idea.** Separate required facts from optional wording; test a correct answer with a different structure.

**Language coverage:** English; Chinese.

**Reading depth:** full_text_selected_sections.

Inspected locations:

- Sections 2.1–3.1: grounded rubric design
- Sections 5 and 7: presentation and leakage limits
- Current README License section and DATA_LICENSE

**Access:** Paper, task/rubric JSONL and code public; no third-party dataset copied into this package.

**Observed terms:** Current DATA_LICENSE: 129 tasks CC BY 4.0; idx26 and110 CC BY-NC 4.0; idx119 CC0. Code Apache-2.0. Current terms are more specific than the paper’s blanket noncommercial description.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2601.08536v1); [resource 2](https://github.com/imlrz/DeepResearch-Bench-II); [resource 3](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/DATA_LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH01

**[Rhetorical Structure Theory: Toward a functional theory of text organization](https://www.sfu.ca/rst/05bibliographies/bibs/Mann_Thompson_1988.pdf)**

1988 · Published journal article, Text 8(3), 243–281

**Focus:** Discourse relations and global coherence. **Evidence:** Descriptive linguistic framework; conceptual foundation, not a writing intervention trial. **Route:** `conceptual_foundation`. **Reading priority:** core.

**Finding.** Text spans can be described by their functions relative to other spans, including support, qualification, contrast and background. Relations can remain implicit. The framework makes interpretive judgments explicit rather than treating one structural analysis as certain.

**Limit.** Describes written monologue; relation assignment involves plausible interpretation of writer intent. It does not prove that explicit connectives or one preferred structure improve every text.

**Candidate rule.** Editorial transfer: identify each paragraph’s function and its relation to surrounding text; repair missing connections without inventing causal or evidential relations.

**Test idea.** Given shuffled or disconnected paragraphs, justify a coherent order; flag unsupported causal transitions instead of adding a misleading connective.

**Language coverage:** English examples; theory formulated abstractly.

**Reading depth:** Selected full-text sections visually inspected in scanned original; author-maintained introduction and definitions read.

Inspected locations:

- Original article §§1–2.2, printed pp.243–247 (PDF scans 1–3)
- Author-maintained introduction: Texts, Coherence and Structure; Nucleus::Satellite Relations; Observers and Definitions
- Definitions page: Background, Evidence, Condition and Contrast

**Access:** Author-hosted original PDF available as image-only scan; introductory and relation-definition pages accessible.

**Observed terms:** Original scan shows publisher copyright; author website states all rights reserved. No open redistribution license verified. Link and original annotations only.

**Additional primary resources:** [resource 1](https://www.sfu.ca/rst/01intro/intro.html); [resource 2](https://www.sfu.ca/rst/01intro/definitions.html); [resource 3](https://www.sfu.ca/rst/05bibliographies/publications.html).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH02

**[Modeling Local Coherence: An Entity-Based Approach](https://aclanthology.org/J08-1001/)**

2008 · Published journal article, Computational Linguistics 34(1), 1–34

**Focus:** Entity continuity and local coherence. **Evidence:** Computational model with empirical sentence-ordering, summary-coherence and readability evaluations. **Route:** `direct_writing_research`. **Reading priority:** extended.

**Finding.** Tracking recurring entities and their grammatical roles provides information about local coherence. Evaluation covers ordering, summary rating and readability. Performance depends on domain and text type; entity continuity and global rhetorical structure address different aspects of organization.

**Limit.** A local statistical representation, not a complete account of argument or global structure. Domain shifts and coreference errors affect performance; multilingual generalization was left for future work.

**Candidate rule.** Editorial transfer: trace who or what each sentence discusses, resolve ambiguous references, and explain topic shifts; do not mechanically repeat nouns.

**Test idea.** After compression or reordering, check pronoun antecedents, entity identity and unexplained subject changes across adjacent sentences.

**Language coverage:** English.

**Reading depth:** Selected full-text method, results and discussion sections read.

Inspected locations:

- §3.1 Entity-Grid Discourse Representation and Tables 1–2, pp.6–7
- §4 sentence ordering; Table 7 cross-domain evaluation, p.19
- §7 Discussion and Conclusions, pp.30–31

**Access:** Full paper openly readable through ACL Anthology; original experimental data/code license not investigated beyond paper.

**Observed terms:** ACL landing page states pre-2016 materials CC BY-NC-SA 3.0; original datasets/code license not verified. No redistribution included.

**Additional primary resources:** [resource 1](https://aclanthology.org/J08-1001.pdf).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH03

**[Understanding Iterative Revision from Human-Written Text](https://aclanthology.org/2022.acl-long.250/)**

2022 · Published ACL 2022 long paper, pp.3573–3590

**Focus:** Revision intent and controlled editing. **Evidence:** Human revision corpus, annotation taxonomy and empirical evaluations. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** IteraTeR distinguishes meaning-changing edits from fluency, coherence, clarity and style intents, using revisions from academic abstracts, Wikipedia and Wikinews. Annotation disagreement and weak coherence/style classifiers show that these categories require judgment; additional revision rounds are not automatically beneficial.

**Limit.** Formal English domains; most full-corpus labels are automatic. Small manual quality samples and moderate annotation agreement limit conclusions about universal revision order or optimum number of passes.

**Candidate rule.** Editorial transfer: name the intended improvement before revising; separate factual changes from expression edits, and retain another pass only when it fixes an identified problem.

**Test idea.** Label each substantive change by purpose and meaning impact; compare the final draft with the prior version and allow a no-change outcome.

**Language coverage:** English.

**Reading depth:** Selected full-text methods, annotation and quality-analysis sections read; repository and original dataset card checked.

Inspected locations:

- arXiv PDF §§3–4.3 and Tables 3–6, PDF pp.3–6
- §5.1–5.2 and Table 7, PDF pp.6–7
- Original repository: IteraTeR datasets and intention classifier; Hugging Face dataset card license

**Access:** Paper, repository raw files and original Hugging Face document dataset accessible; GitHub web fetch intermittently failed.

**Observed terms:** Repository LICENSE and original Hugging Face dataset card declare Apache-2.0. Underlying Wikipedia/Wikinews/arXiv text rights were not separately cleared for redistribution.

**Additional primary resources:** [resource 1](https://arxiv.org/abs/2203.03802); [resource 2](https://github.com/vipulraheja/IteraTeR); [resource 3](https://huggingface.co/datasets/wanyu/IteraTeR_human_doc); [resource 4](https://raw.githubusercontent.com/vipulraheja/IteraTeR/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH04

**[ASSET: A Dataset for Tuning and Evaluation of Sentence Simplification Models with Multiple Rewriting Transformations](https://aclanthology.org/2020.acl-main.424/)**

2020 · Published ACL 2020 paper, pp.4668–4679

**Focus:** Sentence simplification and meaning preservation. **Evidence:** Crowdsourced multi-reference dataset with human comparisons and metric-correlation study. **Route:** `direct_writing_research`. **Reading priority:** extended.

**Finding.** ASSET combines paraphrasing, splitting, reordering and deletion rather than testing one operation alone. Human judgments separate fluency, meaning and simplicity; preferences expose trade-offs. The collection permits removing information judged unimportant, so its references are not strict meaning-preservation targets.

**Limit.** English sentence-level Wikipedia material. Its deletion allowance conflicts with tasks requiring every factual commitment to survive. Correlations from older systems are not current-model quality guarantees.

**Candidate rule.** Editorial transfer: evaluate clarity and meaning separately; use splitting or reordering when helpful, and permit deletion only within the user’s stated scope.

**Test idea.** Simplify a dense sentence while preserving a checklist of names, quantities, conditions and exceptions; score comprehensibility independently from preservation.

**Language coverage:** English.

**Reading depth:** Selected full-text collection, comparison and evaluation sections read; original repository and license checked.

Inspected locations:

- §3.1–3.2, pp.4670–4671
- §5.1–5.2 and Table 4, pp.4674–4675
- §6.3 and Tables 5–6, p.4676
- Repository README and LICENSE

**Access:** Original repository supplies validation/test sentences, ten references per source, crowd instructions and human ratings; repository archived but readable.

**Observed terms:** Original repository LICENSE explicitly CC BY-NC 4.0. Do not incorporate raw examples into the MIT skill package without respecting separate terms.

**Additional primary resources:** [resource 1](https://aclanthology.org/2020.acl-main.424.pdf); [resource 2](https://github.com/facebookresearch/asset); [resource 3](https://github.com/facebookresearch/asset/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH05

**[SWiPE: A Dataset for Document-Level Simplification of Wikipedia Pages](https://arxiv.org/abs/2305.19204)**

2023 · Published ACL 2023 long paper; arXiv record confirms venue

**Focus:** Document-level simplification and edit dependencies. **Evidence:** Revision-aligned dataset with expert-informed edit taxonomy, manual annotations and model experiments. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** In the annotated sample, 43% of edits cross sentence boundaries. Discourse operations include reordering and anaphora changes. Revision matching reduces factual misalignment, but simplified Wikipedia versions still contain non-simplification edits and subjective choices. Simplification can require additional context, not just shorter sentences.

**Limit.** English Wikipedia introductions, not whole books or correspondence. Edit intent is reconstructed, agreement is moderate, and automatic alignment and silver labels remain fallible.

**Candidate rule.** Editorial transfer: revise with surrounding paragraphs visible; place prerequisite context before dependent ideas and recheck references after splitting, merging or moving text.

**Test idea.** Simplify a paragraph containing a delayed definition and pronouns; assess information order and reference continuity, then check added material against sources.

**Language coverage:** English.

**Reading depth:** Selected full-text dataset, annotation, limitations and edit-definition sections read; repository contents and license checked.

Inspected locations:

- §§3.2–3.4 revision matching and statistics
- §§4.1–4.4, Tables 1–2 and Figure 3
- §9 Limitations
- Appendix B.1–B.4 edit definitions

**Access:** Full text and repository accessible; data directory verified through GitHub API. Repository archived June 2026; dataset not downloaded or exhaustively audited.

**Observed terms:** Repository LICENSE.txt declares Apache-2.0. Separate clearance of source Wikipedia text rights not verified; no raw dataset redistribution included.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2305.19204v1); [resource 2](https://github.com/salesforce/simplification); [resource 3](https://github.com/salesforce/simplification/tree/master/data); [resource 4](https://github.com/salesforce/simplification/blob/master/LICENSE.txt).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COH06

**[Dancing Between Success and Failure: Edit-level Simplification Evaluation using SALSA](https://aclanthology.org/2023.emnlp-main.211/)**

2023 · Published EMNLP 2023 paper, pp.3466–3495

**Focus:** Edit-level evaluation and semantic regressions. **Evidence:** Human annotation framework, empirical model comparison and learned evaluation metrics. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** SALSA evaluates individual changes by information impact, edit type and efficacy or severity. Successful edits can coexist with damaging edits in the same simplification; identifying contradictions, bad deletions and reference errors makes a favorable overall impression insufficient as an evaluation.

**Limit.** Wikipedia sentence simplification; evaluation of document-level operations needs extension. Some edit boundaries are ambiguous. The advertised data directory is currently missing from the public main branch.

**Candidate rule.** Editorial transfer: inspect each substantive change for lost information, contradiction, reference damage and unsupported additions; do not let stylistic gains cancel a serious meaning error.

**Test idea.** Seed one severe semantic error among several fluent improvements; require the evaluator to locate it and reject the revision despite its smoother wording.

**Language coverage:** English.

**Reading depth:** Selected full-text framework, annotation, findings, limitations and error definitions read; repository and data availability checked.

Inspected locations:

- §§2.1–2.4 and Figure 3, arXiv PDF pp.2–4
- §§3.1–3.3 and Table 1, PDF p.4
- §4 and Figures 4–6, PDF pp.5–6
- Limitations; Appendix A.2–A.3 error types and severity

**Access:** Paper, code and interface configuration accessible. README data link fails; GitHub contents API confirms /data returns 404 as checked.

**Observed terms:** Repository LICENSE is Apache-2.0. Dataset download unavailable at checked path; any separate dataset and upstream-text terms remain unverified.

**Additional primary resources:** [resource 1](https://arxiv.org/abs/2305.14458); [resource 2](https://github.com/davidheineman/salsa); [resource 3](https://github.com/davidheineman/salsa/blob/main/LICENSE); [resource 4](https://github.com/davidheineman/salsa/tree/main/interface).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID01

**[FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://aclanthology.org/2023.emnlp-main.741/)**

2023 · Peer-reviewed: EMNLP 2023, pp. 12076–12100

**Focus:** Atomic factual support and coverage. **Evidence:** Metric definition; human-annotated biography evaluation; automated estimator. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** A sentence can mix supported and unsupported claims. FActScore evaluates individual factual units against a specified knowledge source. Its precision score does not measure whether the response retained the information needed to answer the question.

**Limit.** Main experiments use biographies and Wikipedia. Equal claim weights and nonconflicting evidence are assumptions; the estimator can err. Precision alone rewards omission or abstention.

**Candidate rule.** Editorial transfer: audit factual units against named evidence, then separately check whether editing removed facts essential to the reader's task.

**Test idea.** Score unsupported factual units and omitted required facts separately; preserve source-relative labels instead of declaring global truth.

**Language coverage:** English evaluation; cross-language transfer unvalidated here.

**Reading depth:** Selected full-text sections and official repository/license inspected.

Inspected locations:

- §3.1 Definition, PDF pp. 3–4
- §3.3 Data, PDF p. 4
- §4.1 Model, PDF p. 6
- Limitations, PDF pp. 9–10
- Official README: data release; LICENSE

**Access:** Paper and official repository public. README links human annotations and download tools; full data not downloaded or revalidated.

**Observed terms:** Repository software: MIT verified in LICENSE. Separate annotation and underlying Wikipedia redistribution terms not verified; do not treat the software license as a blanket dataset license.

**Additional primary resources:** [resource 1](https://aclanthology.org/2023.emnlp-main.741.pdf); [resource 2](https://github.com/shmsw25/FActScore); [resource 3](https://github.com/shmsw25/FActScore/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID02

**[Enabling Large Language Models to Generate Text with Citations](https://aclanthology.org/2023.emnlp-main.398/)**

2023 · Peer-reviewed: EMNLP 2023

**Focus:** Citation support, coverage and relevance. **Evidence:** ALCE benchmark: ASQA, QAMPARI and ELI5; automatic metrics compared with human judgments. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** ALCE separates fluency, answer correctness and citation quality. Citation recall checks support for statements; citation precision detects irrelevant references. Correct-looking answers and post-hoc citations can still have weak support, and compressing retrieved passages can lose evidence needed for attribution.

**Limit.** Citation entailment depends on the supplied passages and an imperfect inference model. It does not establish source reliability or resolve conflicting evidence; results concern English question answering.

**Candidate rule.** Editorial transfer: ensure each factual claim needing evidence is supported by its adjacent citation; remove irrelevant citations and inspect original passages after compression.

**Test idea.** Annotate unsupported claims, uncited claims requiring support, and irrelevant citations separately; review source trustworthiness independently.

**Language coverage:** English.

**Reading depth:** Selected full-text methods, analyses, human evaluation and repository/license inspected.

Inspected locations:

- §3 Automatic Evaluation, PDF pp. 3–5
- §3.3 Citation Quality and Figure 3, PDF pp. 4–5
- §5.1 post-hoc citations and compression analysis, PDF pp. 6–7
- §6 Human Evaluation, PDF pp. 8–9
- Official README: Data; LICENSE

**Access:** Paper and code public; repository provides download script and retrieval results. Underlying datasets were not downloaded in this review.

**Observed terms:** Repository software: MIT verified in LICENSE. ASQA, QAMPARI, ELI5 and retrieved third-party passages require separate terms; those dataset licenses were not verified here.

**Additional primary resources:** [resource 1](https://aclanthology.org/2023.emnlp-main.398.pdf); [resource 2](https://github.com/princeton-nlp/ALCE); [resource 3](https://github.com/princeton-nlp/ALCE/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID03

**[RARR: Researching and Revising What Language Models Say, Using Language Models](https://aclanthology.org/2023.acl-long.910/)**

2023 · Peer-reviewed: ACL 2023; initial preprint 2022

**Focus:** Evidence-driven correction with preservation. **Evidence:** Editing method; attribution/preservation evaluation; ablations and failure analysis. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** RARR treats factual correction and preservation as separate goals. Targeted evidence queries and a disagreement gate reduce unnecessary edits. Its analysis shows that improving attribution can change intent or discard useful content; a supporting source alone cannot establish correctness.

**Limit.** The method may retain unsupported claims, does not resolve conflicting sources, and is not validated for arbitrary long documents or poetry. Edit distance incompletely measures preservation.

**Candidate rule.** Editorial transfer: identify the precise evidence-backed correction before editing; preserve unaffected intent and wording, and record unresolved or conflicting claims rather than silently normalizing them.

**Test idea.** Measure corrected errors, newly introduced errors, lost intent and unnecessary changes; include a source that is relevant but does not contradict the draft.

**Language coverage:** English tasks and examples inspected.

**Reading depth:** Full-text task definition, method, relevant ablations, limitations and ethics; official repository inspected.

Inspected locations:

- §2.1 Measuring attribution and §2.2 Measuring preservation
- §3 Research and revision method
- §6.1 results and §6.2 query/agreement ablations
- §8 Limitations
- §9 Evidence trustworthiness and Conflicting evidence
- Official README: Agreement Gate and Editing

**Access:** Full paper and public implementation accessible. Evaluation-set redistribution and runtime API compatibility were not validated.

**Observed terms:** No LICENSE file or license declaration found in inspected official repository root/README. Data/code reuse license not verified; link and annotate only.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2210.08726v3); [resource 2](https://github.com/anthonywchen/RARR).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID04

**[Understanding Factuality in Abstractive Summarization with FRANK: A Benchmark for Factuality Metrics](https://aclanthology.org/2021.naacl-main.383/)**

2021 · Peer-reviewed: NAACL-HLT 2021, pp. 4812–4829

**Focus:** Source fidelity and discourse-level factual errors. **Evidence:** Human error taxonomy and annotated summary benchmark. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** FRANK distinguishes errors in predicates, entities, circumstances, references between sentences, discourse links and unverifiable additions. A summary may preserve individual names yet invent a causal connection, reverse event order or alter modality. Metrics vary in which error classes they detect.

**Limit.** News summaries and older summarization models constrain generalization. This measures consistency with an article, not the article's truth. Published metric rankings have a repository correction.

**Candidate rule.** Editorial transfer: verify who did what, when, where and with what modality; then separately inspect pronouns, causal links and event order.

**Test idea.** Use minimal-pair rewrites that alter one entity, modal, causal connector or temporal relation; report error types rather than one holistic score.

**Language coverage:** English CNN/DailyMail and XSum summaries.

**Reading depth:** Full-text taxonomy, data collection and metric analysis; official repository/license inspected.

Inspected locations:

- §2 Typology of Factual Errors and Table 1, PDF pp. 2–3
- §3 annotation data/collection, PDF pp. 3–4
- §5 metric strengths and weaknesses, PDF pp. 6–8
- Official README: Data, validation/test split and 2021 correction note; LICENSE

**Access:** Paper and annotation repository public. README reports 2,250 annotated outputs; current split counts total 2,246. No corpus rows redistributed.

**Observed terms:** Repository MIT LICENSE verified. Separate rights for underlying CNN/DailyMail and XSum source articles were not verified; repository license must not be assumed to relicense news text.

**Additional primary resources:** [resource 1](https://aclanthology.org/2021.naacl-main.383.pdf); [resource 2](https://github.com/artidoro/frank); [resource 3](https://github.com/artidoro/frank/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID05

**[Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/937ae0e83eb08d2cb8627fe1def8c751-Abstract-Conference.html)**

2024 · Peer-reviewed: NeurIPS 2024, main conference track

**Focus:** Long-form verification and coverage-aware evaluation. **Evidence:** LongFact prompt set; search-assisted SAFE evaluator; factuality metric. **Route:** `adjacent_task_transfer`. **Reading priority:** extended.

**Finding.** LongFact supplies 2,280 prompts across 38 topics. SAFE separates self-contained claims, relevance and search-supportedness. F1@K combines supported-claim precision with a target number of facts, offering a coverage-oriented alternative to precision alone.

**Limit.** F1@K uses a fact-count target, not semantic completeness, and can reward repetition. Search failure is not falsity; decomposition, relevance judgments and source quality remain fallible.

**Candidate rule.** Editorial transfer: resolve pronouns before checking claims, distinguish relevance from support, and retain a separate checklist of required content instead of rewarding fact count alone.

**Test idea.** Record supported, unsupported and irrelevant units; audit missing required information separately from length, and sample automatic verdicts for human review.

**Language coverage:** English prompt set and evaluations inspected.

**Reading depth:** Full-text method, metric, validation and limitations; repository data/license statements inspected.

Inspected locations:

- §2 LongFact
- §3 SAFE and §4 evaluator comparison
- §5 F1@K
- §8 Limitations
- Appendix examples of successful ratings
- Official README: LongFact; License and disclaimer

**Access:** Paper, prompts and evaluator code public; no dataset downloaded or full evaluator executed.

**Observed terms:** Official repository explicitly assigns Apache-2.0 to software and CC BY 4.0 to other materials. Verified in README License and disclaimer; retrieved external webpages retain their own terms.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2403.18802v4); [resource 2](https://github.com/google-deepmind/long-form-factuality); [resource 3](https://github.com/google-deepmind/long-form-factuality/tree/main/longfact).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## FID06

**[Generalization bias in large language model summarization of scientific research](https://doi.org/10.1098/rsos.241776)**

2025 · Peer-reviewed: Royal Society Open Science 12(4), 241776; published 30 April 2025

**Focus:** Preserving scope, qualifiers and evidential strength. **Evidence:** Preregistered empirical comparison of scientific originals and LLM summaries; human coding. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** Across 4,900 summaries, the study found scope-broadening in many tested models despite accuracy prompts. Its rubric tracks shifts from bounded to generic claims, past findings to present assertions, and descriptive results to recommendations—changes that ordinary fact matching can miss.

**Limit.** Results concern selected 2024–2025 models, prompts and largely medical material. Broader wording is not automatically unwarranted; scope can also be narrowed incorrectly. This is not a current-model ranking.

**Candidate rule.** Editorial transfer: preserve population, conditions, time and strength of conclusions; do not turn observations into universal claims or recommendations without additional evidence.

**Test idea.** Compare source and revision for removed quantifiers, changed temporal scope, stronger certainty and newly introduced recommendations; allow justified generalization explicitly.

**Language coverage:** English scientific texts and summaries.

**Reading depth:** Author preprint: operational definitions, limitations and methods read; journal publication verified via PubMed.

Inspected locations:

- Introduction: three generalization categories, PDF pp. 3–4
- §5 Strengths and limitations, PDF pp. 18–19
- §7 Methods, PDF pp. 19–20
- Data availability, PDF p. 21
- PubMed publication metadata

**Access:** Author PDF accessible. Publisher/DOI failed and PMC returned a bot challenge. Public OSF links identified in PDF; access returned 403, so data contents uninspected.

**Observed terms:** Dataset/code license not verified: OSF inaccessible. Publication status verified separately; no blanket permission inferred from open paper access.

**Additional primary resources:** [resource 1](https://pubmed.ncbi.nlm.nih.gov/40309181/); [resource 2](https://arxiv.org/abs/2504.00025); [resource 3](https://arxiv.org/pdf/2504.00025); [resource 4](https://osf.io/q936d/); [resource 5](https://osf.io/25ct6/).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV01

**[CoEdIT: Text Editing by Task-Specific Instruction Tuning](https://aclanthology.org/2023.findings-emnlp.350/)**

2023 · Findings of EMNLP 2023, peer-reviewed

**Focus:** instruction-guided revision. **Evidence:** Model-training study; editing benchmarks and small expert preference evaluations. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** Task-specific editing instruction tuning supports fluency, clarity, coherence and style edits, including composite requests. Expert evaluation checks instruction satisfaction and meaning preservation. The paper's 82k training examples differ from the public release, described by its maintainers as 69k after licensing exclusions.

**Limit.** Mainly English sentence-level, non-meaning-changing editing; small human samples and prompt sensitivity. Fine-tuning results do not establish that adding a prose skill improves a general agent.

**Candidate rule.** Transfer: name the requested edit and protected meaning separately; check each component of composite requests after revision.

**Test idea.** Score instruction satisfaction, factual preservation and unnecessary edits separately; include unchanged, acceptable originals.

**Language coverage:** English.

**Reading depth:** Selected full-text methods, human evaluation, composite-instruction results and limitations; official repository and dataset card.

Inspected locations:

- Sections 3–4: task instructions and experimental setup
- Sections 6.1 and 6.3: 50 single-task inputs and 30 composite instructions; Tables 4 and 7
- Limitations and Ethics Statement
- Dataset card: metadata and Considerations for Using the Data

**Access:** Full text, official code, models and reduced public dataset available; excluded training/validation portions are not redistributed.

**Observed terms:** Dataset card declares Apache-2.0; upstream excluded material has licensing restrictions. Separate code license not verified in the inspected repository root.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2305.09857v2); [resource 2](https://github.com/vipulraheja/coedit); [resource 3](https://huggingface.co/datasets/grammarly/coedit); [resource 4](https://huggingface.co/datasets/grammarly/coedit/blob/main/README.md).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV02

**[EditEval: An Instruction-Based Benchmark for Text Improvements](https://arxiv.org/abs/2209.13331)**

2022 · arXiv preprint; peer-reviewed venue not verified

**Focus:** revision evaluation and instruction robustness. **Evidence:** Benchmark design and comparative model evaluation. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** EditEval separates seven editing tasks and tests multiple natural-language instructions per task. Results vary with prompt wording, while evaluation metrics can disagree. It also includes updating text using external reference material, distinguishing factual updates from surface rewrites.

**Limit.** Older models, predominantly Wikipedia material, uneven task sizes and automatic metrics; one coherence slice has only 35 cases. It does not measure all document-level writing qualities.

**Candidate rule.** Transfer: evaluate clarity, coherence, fluency, paraphrase and factual updates as distinct operations; test equivalent phrasings of the user's request.

**Test idea.** Use three instruction paraphrases per test; report robustness and human judgements alongside task-specific metrics.

**Language coverage:** English.

**Reading depth:** Selected full-text benchmark design, prompting protocol, results and limitations; repository and license.

Inspected locations:

- Section 3 and Table 1: seven edit tasks, ten dataset slices
- Section 6: 3–11 prompt variants per task
- Section 7: prompt robustness and metric disagreement
- Section 8 and Limitations: primarily Wikipedia-derived coverage

**Access:** Paper and evaluation code available; code downloads constituent datasets from their own sources.

**Observed terms:** Repository LICENSE is CC0-1.0. This does not verify or replace the individual licenses of its constituent datasets.

**Additional primary resources:** [resource 1](https://arxiv.org/pdf/2209.13331); [resource 2](https://github.com/facebookresearch/EditEval); [resource 3](https://github.com/facebookresearch/EditEval/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV03

**[Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651)**

2023 · NeurIPS 2023; inspected arXiv v2, venue corroborated by TACL 2024 bibliography

**Focus:** targeted feedback and revision loops. **Evidence:** Inference-time intervention; seven heterogeneous tasks with human, model and task-specific evaluation. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** The feedback-and-revision loop improved reported outcomes on several generation tasks. In ablations across three tasks, specific, actionable feedback outperformed generic or absent feedback. The paper also records fluctuating quality across revisions, so a later draft need not be the best one.

**Limit.** Heterogeneous metrics and proprietary 2023 models; some model judging. Later work challenges initial-prompt fairness. This is neither universal factual verification nor evidence of Chtets effectiveness.

**Candidate rule.** Transfer: tie each revision to a located defect and proposed repair; compare against the previous draft and stop when no justified improvement remains.

**Test idea.** Compare specific-critique revision against a strong first draft and an equal-budget fresh rewrite; count regressions.

**Language coverage:** English; Python in code tasks.

**Reading depth:** Selected full-text method, main results, feedback ablation, limitations and non-monotonic revision analysis; code license.

Inspected locations:

- Section 2: specific, actionable feedback and task-dependent stopping
- Section 3, Table 1: task-specific results including near-zero math gains
- Section 4, Table 2: specific versus generic/no feedback
- Section 6: model dependence
- Appendix H, Table 10: quality can fluctuate across iterations

**Access:** Paper, code, prompts and model outputs available; historical model endpoints may not be reproducible unchanged.

**Observed terms:** Repository LICENSE verified Apache-2.0; individual upstream benchmark licenses not exhaustively verified.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2303.17651v2); [resource 2](https://selfrefine.info/); [resource 3](https://github.com/madaan/self-refine); [resource 4](https://github.com/madaan/self-refine/blob/main/LICENSE).

Checked 2026-09-20. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV04

**[CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fef126561bbf9d4467dbb8d27334b8fe-Abstract-Conference.html)**

2024 · ICLR 2024, peer-reviewed; preprint first posted 2023

**Focus:** external verification before revision. **Evidence:** Tool-assisted correction experiments and ablations on QA, mathematical programs and toxicity. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** CRITIC obtains external feedback before revising outputs. Tool-assisted QA generally exceeds its no-tool variant in the reported settings. Oracle variants correct only known errors and must be distinguished from the deployable procedure. Benefits vary across tasks and baselines.

**Limit.** Primarily factual QA, math programs and toxicity, not prose quality. Tools, prompts and historical models affect results; verification adds latency and does not guarantee accurate external evidence.

**Candidate rule.** Transfer: verify disputed factual changes against sources or calculations before applying them; keep stylistic preference separate from evidential correction.

**Test idea.** Seed supported and unsupported claims; measure corrected errors, newly introduced errors, source support and verification cost.

**Language coverage:** English; Python in mathematical-program tasks.

**Reading depth:** Selected full-text method, experimental distinctions, tool ablations and limitations; repository root license.

Inspected locations:

- Sections 3.2–3.4: tool verification and correction
- Section 4: normal CRITIC versus oracle CRITIC-star
- Section 4.1: free-form QA and no-tool comparison
- Sections 4.2–4.3: task-dependent results
- Appendix A: latency, prompt dependence and transfer limits

**Access:** Full text and parent repository accessible; CRITIC subdirectory web fetch failed during this check; code was not executed.

**Observed terms:** ProphetNet repository root LICENSE verified MIT; CRITIC-specific overrides and external datasets not independently verified.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2305.11738v4); [resource 2](https://github.com/microsoft/ProphetNet/tree/master/CRITIC); [resource 3](https://github.com/microsoft/ProphetNet/blob/master/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV05

**[Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798)**

2024 · ICLR 2024; arXiv v2 dated March 2024, first posted 2023

**Focus:** limits and regression risks of self-correction. **Evidence:** Re-evaluation and counterevidence on reasoning tasks. **Route:** `adjacent_task_transfer`. **Reading priority:** extended.

**Finding.** In tested reasoning settings, intrinsic correction often failed to improve answers and could make them worse. Apparent gains depended on oracle correctness labels, comparison budgets or incomplete initial prompts. The authors explicitly distinguish these findings from preference or style editing.

**Limit.** Reasoning benchmarks and historical model versions; not evidence that prose revision is ineffective, and not a timeless claim about every later model or correction method.

**Candidate rule.** Inference: never treat a self-critique as proof; preserve already-supported claims unless a concrete defect or better evidence justifies changing them.

**Test idea.** Include correct initial drafts; track correct-to-incorrect changes and compare equal-budget baselines without hidden answer labels.

**Language coverage:** English.

**Reading depth:** Selected full-text setup, oracle versus intrinsic comparison, prompt-fairness analysis and domain limitations.

Inspected locations:

- Sections 2–3: intrinsic versus external feedback
- Tables 2–3: oracle and non-oracle outcomes
- Section 4: comparable-call baselines
- Section 5: initial-prompt design
- Section 6: discussion and explicit reasoning-only limitation

**Access:** Full text available in HTML and PDF; no reusable dataset release verified in this check.

**Observed terms:** Code/data license not verified; record is a citation and original annotation, not a redistributed dataset.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2310.01798v2); [resource 2](https://arxiv.org/pdf/2310.01798).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## REV06

**[When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/)**

2024 · Transactions of the ACL 12:1417–1440, peer-reviewed; November 2024

**Focus:** evaluation design for revision systems. **Evidence:** Critical literature synthesis; original taxonomy and evaluation checklist, not a new writing experiment. **Route:** `literature_synthesis`. **Reading priority:** extended.

**Finding.** The survey separates intrinsic correction, correction with external information, and comparisons of final system quality. Its evaluation framework exposes oracle leakage, weak initial prompts and unequal budgets, and recommends assessing the accuracy of feedback itself rather than only the final response.

**Limit.** Synthesis of literature available in 2024; evidence inherits underlying task and model limits. It is not a direct trial of writing quality or current agents.

**Candidate rule.** Transfer: label the source of each correction signal and evaluate diagnosis quality, revised output and computational cost separately.

**Test idea.** Report false-positive critiques, missed defects, accepted harmful edits, human preference and equal-budget baseline results.

**Language coverage:** English article; heterogeneous surveyed tasks, no new multilingual corpus.

**Reading depth:** Selected full-text taxonomy, research questions, synthesis and evaluation checklists.

Inspected locations:

- Sections 2–3: feedback sources and research-question taxonomy
- Table 3: requirements for fair comparisons
- Sections 6–7: strong baselines and feedback quality
- Section 8, Tables 7–8: positive and negative evaluation checklists

**Access:** Open-access full paper; no original writing dataset associated with this survey was verified.

**Observed terms:** Paper explicitly states CC-BY-4.0. No new dataset/code license applicable to this annotation.

**Additional primary resources:** [resource 1](https://aclanthology.org/2024.tacl-1.78.pdf).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI01

**[CoAuthor: Designing a Human-AI Collaborative Writing Dataset for Exploring Language Model Capabilities](https://arxiv.org/abs/2201.06796)**

2022 · CHI 2022, published conference paper

**Focus:** collaborative_writing_and_author_control. **Evidence:** Interaction dataset and observational analyses. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** CoAuthor records 1,445 English writing sessions from 63 writers using GPT-3, including accepted, rejected and revised suggestions. Author contribution and perceived ownership were correlated; productivity and ownership required different measures. The authors explicitly treat these correlations as hypotheses needing intervention studies.

**Limit.** Crowd-worker sessions with older GPT-3 configurations; 62 of 63 writers were native English speakers. Observational correlations do not establish causal benefits or multilingual generalization.

**Candidate rule.** Inference: match assistance to the requested editing scope and preserve opportunities for author choice; assess perceived ownership separately from fluency and output volume.

**Test idea.** Compare light editing and full rewriting on identical briefs; collect author ownership ratings, accepted edits, semantic changes and completion time.

**Language coverage:** English.

**Reading depth:** Selected full-text methods, results and discussion; official resource pages.

Inspected locations:

- 4.2–4.4: interactions, recruitment, dataset overview (PDF pp. 5–7)
- 5.1.1: language capabilities (PDF p. 7)
- 5.2: productivity and ownership (PDF p. 10)
- 6.2: potential use cases (PDF p. 11)
- Interface repository: license and scope

**Access:** Paper, project site and replay interface public; dataset download linked by authors. Full dataset not downloaded in this review.

**Observed terms:** Interface code: MIT verified in official repository. Dataset redistribution license: not verified; code license must not be extended to sessions.

**Additional primary resources:** [resource 1](https://arxiv.org/pdf/2201.06796); [resource 2](https://coauthor.stanford.edu/); [resource 3](https://github.com/minalee-research/coauthor-interface).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI02

**[Olá, Bonjour, Salve! XFORMAL: A Benchmark for Multilingual Formality Style Transfer](https://aclanthology.org/2021.naacl-main.256/)**

2021 · NAACL-HLT 2021, published conference paper

**Focus:** multilingual_register_and_meaning_preservation. **Evidence:** Multilingual benchmark with human rewrite and evaluation protocols. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** XFORMAL evaluates formality transfer in Brazilian Portuguese, French and Italian. Human evaluation separates register, fluency and meaning preservation. Complex methods often perform near simpler baselines, making multilingual transfer a separate empirical question rather than an automatic consequence of English results.

**Limit.** Sentence-level formality in Yahoo Answers does not validate personal voice, long-document coherence, professional correspondence or Russian. Dataset access is conditional.

**Candidate rule.** Inference: define the target register for each language, then check fluency and preserved meaning independently; do not import English stylistic conventions automatically.

**Test idea.** Native French reviewers score requested register, naturalness and unchanged propositions separately on original French briefs.

**Language coverage:** French; Brazilian Portuguese; Italian.

**Reading depth:** Selected full-text evaluation/results and dataset-rights sections; official access instructions.

Inspected locations:

- 5.4: human evaluation (PDF p. 6)
- Table 7 and section 5.5: automatic and human evaluation (PDF pp. 7–8)
- 7.1: dataset rights (PDF p. 9)
- Repository: Obtaining XFORMAL

**Access:** Paper public. Authors require Yahoo L6 access first, then proof and a use description before supplying the complete dataset.

**Observed terms:** Paper section 7.1 reports Yahoo permission for academic use. No unrestricted dataset redistribution license verified; do not bundle corpus with an MIT skill.

**Additional primary resources:** [resource 1](https://aclanthology.org/2021.naacl-main.256.pdf); [resource 2](https://github.com/Elbria/xformal-FoST).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI03

**[Dear Sir or Madam, May I Introduce the GYAFC Dataset: Corpus, Benchmarks and Metrics for Formality Style Transfer](https://aclanthology.org/N18-1012/)**

2018 · NAACL-HLT 2018, published conference paper

**Focus:** register_evaluation. **Evidence:** Parallel formality corpus and human/automatic evaluation study. **Route:** `direct_writing_research`. **Reading priority:** extended.

**Finding.** GYAFC evaluates formality, fluency, meaning preservation and overall preference separately, using five judgments per sentence on sampled English outputs. A formality classifier needed in-domain retraining, illustrating that an automatic style score can depend on the evaluation domain.

**Limit.** English sentence rewrites from two Yahoo Answers domains; formality is one stylistic dimension, not a definition of good writing or author identity.

**Candidate rule.** Inference: treat formality as a requested parameter, not a quality target; reject stylistic improvements that alter substantive meaning.

**Test idea.** Include fluent but fact-changing rewrites and faithful but overly formal rewrites; score semantic fidelity separately from tone.

**Language coverage:** English.

**Reading depth:** Selected full-text evaluation protocol and metric discussion; official dataset access page.

Inspected locations:

- 5.1: human evaluation
- 5.2: automatic metrics
- Repository: corpus access instructions

**Access:** Paper public; official repository asks users to email affiliation and intended use to obtain corpus access. No access requested.

**Observed terms:** Dataset redistribution license not verified. Author-mediated access is not permission for public redistribution.

**Additional primary resources:** [resource 1](https://arxiv.org/html/1803.06535v2); [resource 2](https://aclanthology.org/N18-1012.pdf); [resource 3](https://github.com/raosudha89/GYAFC-corpus).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI04

**[Low-Resource Authorship Style Transfer: Can Non-Famous Authors Be Imitated?](https://arxiv.org/abs/2212.08986)**

2022 · arXiv preprint; first posted 2022, inspected revision v3 dated 2024-11-04; peer-reviewed venue not verified

**Focus:** author_voice_from_examples. **Evidence:** Few-shot authorship-transfer benchmark and prompting method (STYLL). **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** STYLL uses a small set of target-author examples, style descriptors and in-context rewriting. Evaluation distinguishes stylistic movement from semantic preservation. Its examples reveal that imitating citation-heavy style can generate a fabricated hyperlink; human agreement on nuanced author identity is limited.

**Limit.** Short English Reddit posts and older models; imperfect human agreement and hallucinated details limit transfer claims. Multilingual testing is explicitly future work.

**Candidate rule.** Inference: infer voice from supplied samples, preserve style separately from facts, and never fabricate sources or biographical details to imitate an author's habits.

**Test idea.** Use author samples containing citations but an uncited new brief; fail any invented source, quotation, experience or personal fact.

**Language coverage:** English.

**Reading depth:** Selected full-text method, examples, evaluation and limitations.

Inspected locations:

- 3: dataset
- 4.1: STYLL
- Table 1: transfer examples and fabricated hyperlink
- 5: style and semantic metrics
- 6: human evaluation
- 7: future directions

**Access:** Paper public; resource release is stated in article, but dataset/code availability not independently verified here.

**Observed terms:** arXiv perpetual non-exclusive distribution license verified; it is not an unrestricted reuse license. Dataset/code licenses not verified.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2212.08986v3); [resource 2](https://arxiv.org/pdf/2212.08986v3).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI05

**[LaMP: When Large Language Models Meet Personalization](https://aclanthology.org/2024.acl-long.399/)**

2024 · ACL 2024, published conference paper; initial preprint 2023

**Focus:** profile_retrieval_and_personalization. **Evidence:** Seven-task personalization benchmark with retrieval experiments. **Route:** `adjacent_task_transfer`. **Reading priority:** extended.

**Finding.** Retrieving relevant entries from user histories improves personalization metrics across LaMP's classification and generation tasks. Generation mostly concerns short outputs such as titles, email subjects and tweet paraphrases. These results support testing example selection, not claiming that retrieval alone preserves a person's literary voice.

**Limit.** Mainly short outputs and reference-overlap metrics; possible pretraining exposure. The authors identify long-form evaluation, realism and privacy as unresolved limitations.

**Candidate rule.** Inference: select a small, relevant set of authorized author examples for the current genre; validate voice with the author rather than proxy metrics alone.

**Test idea.** Compare no samples, random samples and genre-relevant samples; ask the author to judge voice while independently checking factual preservation.

**Language coverage:** English.

**Reading depth:** Selected full-text tasks, retrieval method, experiment tables and limitations; repository license.

Inspected locations:

- 2: task overview, especially LaMP-6 and LaMP-7
- 3: retrieval augmentation
- 4 and Tables 1–3: results
- Limitations
- Repository: License

**Access:** Paper, benchmark site and code public. Constituent datasets have separate conditions; the email task uses the restricted Avocado collection.

**Observed terms:** Official repository: code and data-creation methods CC BY-NC-SA 4.0; underlying datasets retain their own licenses. Cannot be redistributed wholesale under MIT alone.

**Additional primary resources:** [resource 1](https://arxiv.org/html/2304.11406v3); [resource 2](https://lamp-benchmark.github.io/); [resource 3](https://github.com/lamp-benchmark/lamp).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## VOI06

**[Generative AI enhances individual creativity but reduces the collective diversity of novel content](https://www.science.org/doi/10.1126/sciadv.adn5290)**

2024 · Science Advances 10(28), eadn5290; published article. Full-text reading used the authors' March 2024 preprint, not a confirmed final-version text.

**Focus:** creativity_and_collective_diversity. **Evidence:** Randomized online short-story experiment. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** In a randomized short-story task with 293 writers, access to AI-generated starting ideas improved average reader-rated creativity, particularly for less creative writers, while stories became more similar to one another. Individual quality and diversity across a collection therefore need separate evaluation.

**Limit.** Brief English stories by ordinary participants using AI starting ideas, not professional long-form writing or unrestricted collaboration. Similarity uses embeddings; findings do not establish an inevitable homogenization effect.

**Candidate rule.** Inference: preserve the author's concrete perspective and test alternatives with meaningfully different premises; evaluate diversity separately from polish without assuming this procedure prevents homogenization.

**Test idea.** Blind-rate individual drafts and compare repeated-topic outputs for recurring premises, structure and wording across authors.

**Language coverage:** English.

**Reading depth:** Selected preprint full-text results, similarity analysis, discussion and methods; published metadata and data record.

Inspected locations:

- Results: creative outcomes
- Similarity of stories (preprint PDF pp. 9–10)
- Discussion (pp. 10–12)
- Methods: similarity scores and statistical analysis (p. 15)
- Supplementary Table 17 (p. 32)
- Dryad dataset record

**Access:** Publisher page unavailable in this session; author preprint and Dryad record accessible. Data files not downloaded.

**Observed terms:** Read preprint: CC BY-NC-ND 4.0 verified through arXiv. Final article and Dryad file licenses not verified in this review.

**Additional primary resources:** [resource 1](https://arxiv.org/abs/2312.00506); [resource 2](https://arxiv.org/pdf/2312.00506v3); [resource 3](https://datadryad.org/dataset/doi:10.5061/dryad.qfttdz0pm).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA01

**[WritingBench: A Comprehensive Benchmark for Generative Writing](https://arxiv.org/html/2503.05244v4)**

2025 · arXiv v4, 27 November 2025; conference venue not independently verified because OpenReview returned a browser challenge

**Focus:** Writing-specific evaluation. **Evidence:** Empirical benchmark; human-reviewed task construction and human agreement study. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** The revised benchmark contains 1,000 English/Chinese tasks. Human-reviewed, task-specific criteria outperform static criteria in the authors' 300-query agreement study; the critic reaches 84% agreement. This supports evaluating the actual writing brief, with humans checking the criteria.

**Limit.** Agreement study excludes inputs above 5,000 tokens. Complex length requirements remain difficult; French and Russian transfer is untested. Earlier versions use different counts and evaluators.

**Candidate rule.** Editorial transfer: derive a short rubric from the reader, purpose, supplied material and constraints; verify it before scoring, and check exact counts mechanically.

**Test idea.** Human-check task rubrics; score constraints separately from coherence and voice, with identical generation budgets across conditions.

**Language coverage:** English; Chinese.

**Reading depth:** Targeted full-text methods/results/limitations; version and repository cross-check.

Inspected locations:

- v4 sections 3.1–3.2
- v4 section 4.3 and Table 4
- v4 Appendix A.3
- v4 Appendix D
- repository README update history and LICENSE

**Access:** Full paper and repository readable; OpenReview challenge. Current README lists 1,000 tasks and changing evaluator versions; no dataset downloaded.

**Observed terms:** Repository LICENSE verified: Apache-2.0. Paper: arXiv perpetual non-exclusive license. Separate rights in supplied source materials not verified.

**Additional primary resources:** [resource 1](https://github.com/X-PLUG/WritingBench); [resource 2](https://github.com/X-PLUG/WritingBench/blob/main/LICENSE); [resource 3](https://openreview.net/forum?id=Pkskg9drDQ).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA02

**[LitBench: A Benchmark and Dataset for Reliable Evaluation of Creative Writing](https://arxiv.org/html/2507.00769v1)**

2025 · arXiv preprint v1; peer-reviewed venue not verified

**Focus:** Creative-writing evaluation and human preferences. **Evidence:** Filtered Reddit preference benchmark plus a separate human study. **Route:** `direct_writing_research`. **Reading priority:** extended.

**Finding.** Preference-trained judges outperform tested zero-shot judges on Reddit-derived story comparisons. Adding distilled reasoning lowers accuracy in this setup. A separate study of generated stories finds substantial disagreement with the verifier, preserving an essential role for human readers and authors.

**Limit.** Upvotes proxy popularity, not expert literary judgment. Demographic and genre limits apply. The paper reports 2,480 test pairs; the inspected release exposes 2,381 ID-only pairs.

**Candidate rule.** Editorial transfer: retain the author's intended effect and use human readers for final creative judgments; do not equate a longer critique with a better verdict.

**Test idea.** Blind story comparisons, swapped order, matched length; record author preference separately from general-reader preference.

**Language coverage:** English.

**Reading depth:** Targeted full text, methods/results/limitations/license appendix; live dataset-card inspection.

Inspected locations:

- sections 3.1–3.4
- sections 4–5, including Human Experiments
- section 7
- Appendix B
- Hugging Face test viewer schema and row count

**Access:** Paper and collection readable. Test release contains comment IDs requiring Reddit rehydration, not a ready-to-copy story corpus.

**Observed terms:** Appendix B explicitly retains Reddit authors' copyright and offers no relicensing of test stories. Test dataset license metadata not verified.

**Additional primary resources:** [resource 1](https://huggingface.co/collections/SAA-Lab/litbench); [resource 2](https://huggingface.co/datasets/SAA-Lab/LitBench-Test).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA03

**[SummEval: Re-evaluating Summarization Evaluation](https://aclanthology.org/2021.tacl-1.24/)**

2021 · Transactions of the Association for Computational Linguistics, volume 9; peer-reviewed journal article

**Focus:** Multidimensional human evaluation. **Evidence:** Human annotation study and metric meta-evaluation. **Route:** `direct_writing_research`. **Reading priority:** core.

**Finding.** The study separates coherence, factual consistency, sentence fluency and relevance. Crowd and expert ratings diverge substantially; calibration improves expert agreement. Even reference summaries contain defects. A polished sentence or reference match cannot establish that the whole text is faithful and coherent.

**Limit.** English news summarization and older systems; neither author voice nor all writing genres are measured. Expert adjudication can pull scores toward consensus.

**Candidate rule.** Editorial transfer: review sentence quality, whole-text progression, source fidelity and relevance separately; calibrate reviewers on concrete defects.

**Test idea.** Use paired edits isolating one defect each; require evidence for each dimension before an overall preference.

**Language coverage:** English.

**Reading depth:** Targeted full PDF methods/results; repository and license inspected.

Inspected locations:

- section 4.3, PDF pages 6–7
- section 5.1, PDF page 7
- section 5.2, PDF pages 8–10
- Table 1
- repository Human annotations and Data preparation

**Access:** Full PDF, code and annotation links public. Source news articles are omitted from the release and require separate reconstruction.

**Observed terms:** Repository LICENSE verified: MIT. Source news article rights are separate and not verified; no source articles copied.

**Additional primary resources:** [resource 1](https://aclanthology.org/2021.tacl-1.24.pdf); [resource 2](https://github.com/Yale-LILY/SummEval); [resource 3](https://github.com/Yale-LILY/SummEval/blob/master/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA04

**[G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://aclanthology.org/2023.emnlp-main.153/)**

2023 · EMNLP 2023 main conference; peer-reviewed paper

**Focus:** Rubric-based automatic evaluation. **Evidence:** Metric meta-evaluation and evaluator ablation study. **Route:** `adjacent_task_transfer`. **Reading priority:** extended.

**Finding.** Explicit criteria and evaluation steps improve alignment with human ratings in summarization/dialogue. Reported average summary-level Spearman correlation is 0.514, not near-perfect agreement. The authors warn that evaluator preferences may favor model-generated text and reinforce themselves when used for optimization.

**Limit.** Limited tasks and historical models. Self-preference evidence is preliminary. Model updates and probability-estimation details constrain reproducibility.

**Candidate rule.** Editorial transfer: use a rubric-based judge to surface evidence and defects, then validate a sample with humans before trusting its scores.

**Test idea.** Freeze judge version and rubric; compare against independently rated examples, including fluent text with altered facts.

**Language coverage:** English.

**Reading depth:** Targeted full PDF framework, implementation, result table, bias discussion and limitations.

Inspected locations:

- section 2 and Figure 1
- section 3.1 and Table 1
- section 4 bias/ablation discussion
- Limitations, PDF page 8
- repository LICENSE

**Access:** Full PDF and implementation public; reproducing original evaluation requires model access and sampling budget.

**Observed terms:** Repository LICENSE verified: MIT. Paper/data redistribution terms not separately verified.

**Additional primary resources:** [resource 1](https://aclanthology.org/2023.emnlp-main.153.pdf); [resource 2](https://github.com/nlpyang/geval); [resource 3](https://github.com/nlpyang/geval/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA05

**[Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/html/2306.05685v4)**

2023 · NeurIPS 2023 Datasets and Benchmarks track; proceedings record corroborated

**Focus:** Judge bias and pairwise evaluation design. **Evidence:** Controlled bias probes and comparison with human preferences. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** Judges show position and verbosity biases. Comparing each pair in both orders and requiring consistent wins mitigates position effects. High human agreement depends on treatment of ties and model quality gaps; reported self-favoring tendencies are not conclusive evidence of self-enhancement bias.

**Limit.** Broad assistant evaluation, only ten writing tasks in MT-Bench; old models. Easy-to-separate model pairs are unlike subtle editorial revisions.

**Candidate rule.** Editorial transfer: anonymize drafts, swap their order, permit ties and report inconsistent judgments; have humans resolve close decisions.

**Test idea.** Run A/B and B/A judgments; report wins, losses, ties and order inconsistencies independently.

**Language coverage:** English (MT-Bench); Mixed user languages (Arena).

**Reading depth:** Targeted full-text methods, bias probes, mitigation and agreement results.

Inspected locations:

- sections 2.2–2.3
- sections 3.1–3.4
- section 4.1–4.2 and Tables 5–6
- repository LICENSE

**Access:** Full paper and license readable; GitHub judge subdirectory returned an internal web error during this check.

**Observed terms:** FastChat repository LICENSE verified: Apache-2.0. Conversation dataset-specific terms not verified.

**Additional primary resources:** [resource 1](https://dl.acm.org/doi/10.5555/3666122.3668142); [resource 2](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge); [resource 3](https://github.com/lm-sys/FastChat/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## EVA06

**[Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](https://arxiv.org/html/2404.04475v2)**

2024 · COLM 2024; inspected revised arXiv v2 dated 10 March 2025

**Focus:** Length confounds and evaluation controls. **Evidence:** Regression-based debiasing method and adversarial verbosity experiments. **Route:** `adjacent_task_transfer`. **Reading priority:** core.

**Finding.** Verbosity prompts substantially change raw evaluator win rates. Regression-based length control reduces this sensitivity and improves ranking correlation with Arena. This demonstrates an evaluation confound; it does not establish that shorter writing is inherently better.

**Limit.** Arena is a proxy for preference, not factual truth. Adjustment relies on assumptions; reported correlation improvement has bootstrap p=0.07 versus raw AlpacaEval.

**Candidate rule.** Editorial transfer: compare skill and baseline under the same brief, length allowance and attempt budget; track length alongside quality.

**Test idea.** Record tokens, attempts and latency; include a verbosity stress test and report raw preferences with length distributions.

**Language coverage:** English instruction set.

**Reading depth:** Targeted full-text method/results; v1/v2 comparison and repository limitations.

Inspected locations:

- v2 sections 2–3
- v2 sections 4.1–4.4
- v2 section 4.2 bootstrap significance
- repository When to use and not use AlpacaEval and LICENSE

**Access:** Full text and implementation public. No benchmark run or paid model calls performed.

**Observed terms:** Repository LICENSE verified: Apache-2.0. Paper links a Creative Commons license; exact version not verified. Dataset components may have separate terms.

**Additional primary resources:** [resource 1](https://arxiv.org/abs/2404.04475); [resource 2](https://github.com/tatsu-lab/alpaca_eval); [resource 3](https://github.com/tatsu-lab/alpaca_eval/blob/main/LICENSE).

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.

## COM01

**[The Science of Scientific Writing](https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf)**

1990 · American Scientist, November–December 1990; authorized reprint inspected

**Focus:** Reader expectations and information structure. **Evidence:** Editorial exposition with worked examples; not a controlled intervention study. **Route:** `conceptual_foundation`. **Reading priority:** extended.

**Finding.** Gopen and Swan connect information order, emphasis and reader expectations through worked scientific-prose revisions. Structural editing can expose missing conceptual premises. They explicitly reject rigid application and acknowledge that their revisions may not reflect the original author's intended meaning.

**Limit.** An English scientific-writing exposition, not experimental proof of universal rules. Its proposed additions rely on interpretation; an assistant cannot assume permission to invent the missing content.

**Candidate rule.** Editorial transfer: check continuity and intended emphasis before adding connectives; obtain support for a missing premise rather than inventing a bridge.

**Test idea.** Reorder a dense explanation without changing its claims; identify a missing premise that cannot be repaired from supplied facts.

**Language coverage:** English scientific prose.

**Reading depth:** Selected full-text sections of the authorized reprint.

Inspected locations:

- The Stress Position, PDF pages 5–7
- The Topic Position, PDF pages 8–11
- Perceiving Logical Gaps, PDF pages 11–12
- Writing and the Scientific Process, PDF pages 15–16

**Access:** Complete authorized reprint publicly readable on USENIX; original examples not reproduced in this corpus.

**Observed terms:** Reprint states American Scientist/Sigma Xi copyright and permission for that reprint. No open redistribution license verified; link and original annotations only.

Checked 2026-09-19. The proposed rule is a design hypothesis, not a measured Chtets effect.
