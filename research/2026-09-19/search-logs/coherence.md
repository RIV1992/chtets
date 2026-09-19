# Coherence, revision and simplification search log

Checked 2026-09-19. This is a targeted literature search, not a systematic review or exhaustive citation census. Selection sought actionable complements to factual question-answering: rhetorical relationships, entity continuity, revision intent, document context, and meaning-sensitive evaluation.

## Searches and retrieval

Web search queries included:

- `site.aclanthology.org discourse coherence entity grid Barzilay Lapata 2008`
- `site.aclanthology.org revision intent sentence revision dataset writing`
- `site.aclanthology.org simplification meaning preservation ASSET dataset 2020`
- `"Itera" "revision" dataset` with ACL domain filter
- `"SWiPE" "simplification"` with ACL domain filter
- `"SALSA" simplification` with ACL domain filter
- `"Rhetorical Structure Theory" Mann Thompson 1988 pdf` with SFU domain filter
- `IteraTeR A Dataset for Iterative Text Revision`
- `SWiPE A Dataset for Document-Level Simplification of Wikipedia Pages`
- `SALSA A Benchmark for Semantic Analysis of Simplification Actions`
- `"IteraTeR" "Iterative" "Text" "Revision" "2022"`
- `SALSA sentence simplification Heineman 2023 2024`

Several searches returned unrelated or overly broad hits, even with precise terms. Those hits were discarded. Discovery was completed through original ACL/arXiv pages and the papers' original repositories and bibliographies. Author-maintained RST pages linked the original 1988 scan. Metadata and venue checks used the ACL Anthology and original arXiv records, not third-party summaries.

## Selection and boundaries

Selected six sources, COH01–COH06. All six were read beyond their abstracts; exact sections are recorded in the JSON. The 1988 RST scan was image-only: original §§1–2.2 were visually read after rendering PDF scan pages 1–3. The author-maintained introduction and relation definitions were also read. Other PDFs were parsed to text; SWiPE also had readable HTML.

The 2005 entity-grid conference paper was excluded as redundant with the expanded 2008 journal article. The 2017 neural coherence and 2013 graph-based papers surfaced but were not promoted: model architecture changes are less directly useful to a portable editorial skill than the basic representation and its limitations. The 2022 R3 and DElIteraTeR follow-ups were discovered through the original repository; they remain optional follow-up reading rather than fully evaluated sources. Newsela was not selected as an easily distributable corpus: access restrictions were reported by the primary simplification papers, and this branch did not obtain access or verify current contractual terms. Generic exam-revision results, financial asset results, commentary, and surveys were excluded.

This branch did not run models, reproduce experiments, or inspect every row of any dataset. Proposed skill rules are explicitly editorial transfers. Empirical benchmark results do not establish that adding those rules improves Chtets, and predominantly English evidence does not validate Russian or French performance.

## Resource and license checks

- ASSET: original LICENSE read; CC BY-NC 4.0. Original repository is archived but readable. Its references permit deleting low-priority information and must not be treated as exact meaning-preservation gold standards.
- IteraTeR: original repository LICENSE and author's Hugging Face document-dataset card both declare Apache-2.0. Dataset card and sample schema inspected. GitHub website retrieval intermittently failed; public raw URLs were accessible via HTTP. Rights in underlying source texts were not separately cleared.
- SWiPE: original LICENSE.txt declares Apache-2.0; original GitHub API listing confirms data files exist. Repository is archived. Source Wikipedia rights were not separately cleared. No bulk download or row-level audit was performed.
- SALSA: original LICENSE declares Apache-2.0. README links to `data/`, but the directory is absent in the current root listing and the public GitHub contents endpoint for `/data` returned HTTP 404. Code and interface configuration remain accessible. README describes 12K annotations while the paper reports 19K annotations on 840 simplifications; no attempt was made to reconcile absent downloadable data or treat these as interchangeable counts.
- RST: original scan shows publisher copyright; author-maintained site says all rights reserved. No open redistribution license was verified.
- Entity-grid: ACL landing-page policy identifies pre-2016 materials as CC BY-NC-SA 3.0; experimental-data/code terms were not verified.

No third-party paper, dataset, or substantial excerpt is intended for the public deliverable. Temporary PDFs, extracted text and rendered scan pages are under `work/coherence-private/` for inspection only and must be excluded from all published or downloadable corpus packages. The deliverable is the original annotations and source links in `coherence.json`.
