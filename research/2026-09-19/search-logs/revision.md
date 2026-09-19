# Revision strand: search and screening log

Checked: 2026-09-19. Six retained sources: REV01–REV06. Four core, two extended. This is targeted research, not an exhaustive systematic review. All deliverable prose is an original annotation; papers, benchmark records and licensed examples were not copied into the deliverable.

## Search route

- Queries: `CoEdIT text editing instruction tuning paper dataset ACL 2023`; `ITERATER iterative text revision dataset intent paper`; `Self-Refine Iterative Refinement with Self-Feedback CRITIC large language models self correct reasoning yet`.
- Follow-up queries: `"Self-Refine" arxiv 2303.17651`; `"CRITIC" "Large Language Models" paper tool interactive critiquing 2024`; `"Large Language Models Cannot Self-Correct Reasoning Yet" arxiv`; `site:aclanthology.org text revision writing feedback revise benchmark 2025 2024`.
- Recency probe: `"text editing" "2025" "benchmark" "revision"`; `"self-correction" "2025" "writing" "feedback"`. These returned mostly irrelevant results in this session; they do not establish absence of newer work.
- Followed primary links and references from CoEdIT to EditEval and from the TACL survey to original correction studies. Read relevant full-text sections and official repository/dataset metadata.

## Screening decisions

- ITERATER, ASSET and related edit corpora assigned to the coherence strand, to avoid duplicated source records. EditEval retained for its cross-task evaluation protocol and prompt robustness.
- Retained the TACL survey as extended methodological context: it adds explicit distinctions between research questions and diagnoses misleading evaluations. It is labelled synthesis, not direct empirical prose evidence.
- Excluded explanatory blogs, generic prompt advice, commercial summaries and search snippets as evidence.
- MAgICoRe, Socratic Self-Refine, Double-Checker and N-Critics were surfaced. Not retained: predominantly reasoning-specific, redundant with the core correction question, or requiring separate full-text verification. Their omission is not an assessment of quality.
- Did not interpret reasoning gains or failures as measured prose improvements or failures. Candidate rules are explicitly marked as transfer or inference.

## Access and reuse gaps

- CoEdIT official dataset card declares Apache-2.0 and notes the public release is smaller than the paper dataset because of licensing exclusions. Separate repository code license was not visible in the inspected root. No full dataset downloaded.
- EditEval code LICENSE is CC0-1.0; the individual constituent datasets need separate license checks before redistribution or training reuse.
- Self-Refine repository LICENSE is Apache-2.0. OpenReview presented a verification page; no bypass attempted. Venue cross-check came from the TACL article bibliography. Historical API endpoints were not tested.
- CRITIC subdirectory failed to fetch through Web, while the parent repository and MIT license were readable. Specific subdirectory overrides and upstream dataset terms remain unverified.
- Initial guessed HTML version URLs failed for Huang and EditEval; resolved Huang to the authoritative v2 and read EditEval as PDF. The TACL paper was read through ACL's PDF.
- No current-model experiments, paper replications or complete corpus audits were performed in this research strand.

## Synthesis for Chtets

The strongest direct revision inputs are CoEdIT and EditEval: explicitly identify the requested transformation, preserve meaning, and evaluate different edit operations separately. Self-Refine contributes the structure of actionable criticism. CRITIC adds a distinct verification step. Counterevidence and the survey constrain their use: use strong initial drafts, test regressions, do not assume that iteration proves correctness, and distinguish source-grounded changes from stylistic preferences.

These are candidate design decisions for a later Chtets evaluation. They are not evidence that the existing skill already improves writing, and no skill or repository was modified by this strand.
