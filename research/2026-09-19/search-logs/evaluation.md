# Evaluation strand — search and inspection log

Checked 2026-09-19. Six selected sources; original annotations in `evaluation.json`. This is targeted research, not an exhaustive systematic review. No article text or benchmark examples have been redistributed, no API evaluations run, and no change made to the skill or repository.

## Search path

- Broad discovery: `WritingBench comprehensive benchmark generative writing arxiv`; `SummEval Re-evaluating Summarization Evaluation ACL anthology`; `G-Eval NLG Evaluation using GPT-4 better human alignment ACL`.
- Exact-title follow-up: `"SummEval" "Re-evaluating"`; `"Judging LLM-as-a-Judge" arxiv`; `"Length-Controlled AlpacaEval" arxiv`.
- Scope/venue verification: `"WritingArena" benchmark writing`; `"WritingBench" conference 2025 2026`; `site:neurips.cc "WritingBench"`; `site:openreview.net "WritingBench: A Comprehensive"`.
- Search results were noisy. Direct ACL Anthology, arXiv HTML/PDF, author repositories, and Hugging Face release cards supplied the evidence. Secondary summaries and leaderboards were not evidence for conclusions.

## Inclusion decisions

- EVA01 supplies diverse writing tasks and brief-specific rubrics.
- EVA02 supplies creative-writing-specific judge validation and human preference limits.
- EVA03 separates writing dimensions and exposes annotation/reference defects.
- EVA04 makes rubric-based judging operational, with measured uncertainty.
- EVA05 supplies pairwise order controls, tie handling and bias tests.
- EVA06 demonstrates the length confound and supports fair comparison design.

For Chtets, the proposed same-model, same-attempt-budget test is an editorial/experimental transfer, not a method these papers directly validated for skills. Author acceptance must be recorded separately from external-reader preference; neither should be silently treated as universal writing quality.

## Version and access checks

- **WritingBench:** initially inspected v1, then corrected the source card to v4 after repository history revealed revisions. The v4 URL is the authoritative version used in the card. OpenReview `Pkskg9drDQ` returned a browser verification page; conference venue was therefore not independently confirmed. No circumvention attempted.
- **LitBench:** inspected its full methods and Appendix B, then the live test release. The release is ID-only and its displayed row count differs from the paper. Rehydration was not attempted; no Reddit writing copied. This access issue prevents treating the release as a turnkey text corpus.
- **SummEval/G-Eval:** read the actual ACL PDFs, including methods, result tables, annotation limitations and bias discussions. Their repositories' LICENSE files were opened directly.
- **MT-Bench:** paper HTML and repository LICENSE worked; the judge subdirectory produced an internal web error. No executable reproduction claimed.
- **AlpacaEval-LC:** inspected v1, then v2 after the abstract page identified a revision. The card uses v2; inspected its method, robustness sections and significance qualification. Repository license verified directly.

## Screened out or deferred

- **WritingArena:** the exact name did not yield a verified primary benchmark. A different resource, Arena-Write in [LongWriter-Zero](https://arxiv.org/abs/2506.18841), appeared in search. It is deferred: training for ultra-long generation is less central than the selected writing/evaluation controls. No identity equivalence asserted.
- **Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge**, [arXiv 2406.07791](https://arxiv.org/abs/2406.07791): relevant follow-up surfaced; abstract only, not admitted to the six-source core because it overlaps EVA05.
- **Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation**, [arXiv 2609.02942](https://arxiv.org/abs/2609.02942): new warning surfaced in search; abstract only, queued for full-text review rather than treated as established evidence.
- **MUSE**, [arXiv 2609.15188](https://arxiv.org/abs/2609.15188): very recent story-writing system, abstract only. Potential specialist extension; not used as evidence in this strand.
- **PaperWrite-Bench:** a secondary page described a hypothetical specialization, not a verified independent benchmark. Excluded.
- **EditEval:** assigned to the revision strand, deliberately not duplicated.

## Proposed evaluation design

Use independently held-out briefs across English, French and Russian, spanning short correspondence, explanation, argument, source-based summary and creative writing. Generate baseline and skill variants with the same model/version, source inputs, permitted calls, attempt count and length allowance. Include explicit invariant checks for numbers, conditions, chronology and commitments. Compare anonymized outputs in both orders; allow ties and report order inconsistency. Rate factual fidelity, coherence, relevance, fluency and brief-specific voice separately. Human authors judge intended meaning and voice; readers judge comprehensibility and effect. Record both results, plus tokens, latency and rejected edits. These are proposed controls, not results already obtained.
