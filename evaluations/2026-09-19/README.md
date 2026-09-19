# Compact Chtets: development check

Date: 2026-09-19. This is a small model-assisted development comparison, not a controlled efficacy study or a human assessment of literary quality.

## Conditions and separation

- **A:** public skill at commit `78f01bfaaa125fb9cff56640fd20dea6983b93f0`.
- **B:** compact core and references in version 1.1.0, with the existing editorial rules preserved and routing made selective.
- **C1, C2, C3:** B plus one explicit instruction: claim boundaries, dependent spans after editing, or located repair with comparison/rollback. The exact additions are in [mechanism-trials.json](work/mechanism-trials.json). Insert each before `## Read selectively` in B to reconstruct the tested candidate. No candidate was adopted.

A separate fresh agent authored 36 synthetic inputs and separate rubrics without reading the skill, research corpus, earlier examples, or generated responses. There are 12 tasks per language (English, French, Russian), two per language/genre combination. Twelve requests require no change or a local typo correction. The six families are correspondence, expert comment/voice, explanation/shortening, source-based analysis, interface copy, and fiction.

Six fresh writer agents handled A/B × three language batches. Each read only its assigned skill and input file, used references selectively, and returned one answer per task. They did not receive rubrics. All inherited the same host model configuration; exact provider version, sampling settings, reasoning tokens, billed tokens, latency, and equal internal computation were not available. Tool permissions and task material were matched; instruction length and resulting file reads intentionally differed. No browsing or extra drafting agents were allowed.

The requests were batched, not separate API calls: later tasks shared a context with earlier tasks and loaded references. The observations must not be treated as 36 independent replicated model trials. The set is deliberately simple and mostly composed of short, supplied-source tasks; it is not a representative sample of professional writing.

Three fresh model judges received only requests, rubrics, and anonymous X/Y outputs. Pair order was shuffled with a fixed seed (190926); condition labels were withheld until judgments were saved. Judges checked meaning and instructions first, allowed ties, and did not require a reference wording. One judge reviewed each language; there was no human panel, second-order reversal, or inter-rater reliability estimate. The coordinator checked summaries, the non-tie, and manual smoke outputs against the supplied material.

## Observations

| Language | Pairs | Outputs with a judge-reported critical failure: A / B | Preference A / B / tie |
| --- | ---: | ---: | ---: |
| English | 12 | 0 / 0 | 0 / 0 / 12 |
| French | 12 | 0 / 0 | 0 / 1 / 11 |
| Russian | 12 | 0 / 0 | 0 / 0 / 12 |

The narrow-scope responses preserved unchanged text or made the requested typo correction in both conditions. Almost all pairs were tied. This gives no basis for a broad superiority claim. It did not reveal a critical regression from compression on these inputs.

The one preference concerned `fr-creative-01`: A briefly turns a stone to hide a yellow mark, then restores it; B stops the turn and keeps the mark visible. The judge treated this as a minor fidelity issue, although a strict continuous-visibility interpretation could classify A's response as a constraint failure. Raw judgments retain that ambiguity rather than silently changing the totals.

## Individual research probes

The three additions were written before the A/B judgments were reviewed. Fresh writers used C1 on six source/shortening tasks, C2 on six dependent-instruction/interface tasks, and C3 on the twelve narrow-scope tasks plus three voice tasks. These reuse pilot inputs, so they are development probes, not held-out confirmation. C cores were 831–832 words, above the production target; adoption would also require budget-conscious integration.

A separate fresh judge reviewed 27 anonymous B/candidate pairs, shuffled with seed 88267. No critical failures were reported. Outcomes:

| Addition | Pairs | B preferred | Candidate preferred | Ties |
| --- | ---: | ---: | ---: | ---: |
| Claim boundaries (C1) | 6 | 1 | 0 | 5 |
| Dependent span (C2) | 6 | 1 | 0 | 5 |
| Located repair and comparison (C3) | 15 | 0 | 0 | 15 |

The probes did not demonstrate a useful incremental effect. Existing rules already cover much of the intended behavior, and these cases may be too easy to distinguish formulations. All three additions remain documented hypotheses. Evidence-state and author-voice extensions were not introduced: their value requires more discriminating tasks and, for voice, the author's judgment. No combined C or larger confirmatory trial is claimed.

## Context and manual use

| Inventory | A | B |
| --- | ---: | ---: |
| Native core | 1,248 | 792 |
| Core and all six references | 5,960 | 3,048 |
| Default manual prompt | 6,087 | 838 |

All counts use whitespace splitting, including Markdown and frontmatter; they are not tokens. The extended B prompt is 2,947 words. The [generated size report](../../docs/context-size.json) also records characters and UTF-8 bytes.

Writer manifests reported unique skill-file inventories of 4,730 / 4,730 / 3,548 words for A's EN/FR/RU batches and 792 / 1,258 / 792 for B. This is a batch file inventory, not per-task input consumption or verified client telemetry. Source material, prior answers, host instructions, and repeated tool output are excluded. See [batch reads](batch-read-inventory.json).

A fresh writer used only the compact prompt and 15 supplied tasks, with no skill-reference access. Three shortening answers preserved the tested distinctions and conditions at 61 English, 78 French, and 70 Russian words. Twelve arithmetic/extraction/table/typo requests matched their exact expected short answers. See [manual smoke review](manual-smoke-review.json). This supports ordinary use without local references in this host; it is neither an automatic activation test nor an execution in another client.

Native client discovery, long-context interference, repeated-task learning, external fact retrieval, high-stakes texts, and human voice preference remain untested by this run. A small zero-failure set does not establish zero risk or semantic equivalence in general. Use fresh adversarial inputs and author review before making stronger claims.

## Artifacts and reuse

[Inputs](stimuli/inputs.jsonl), [rubrics](stimuli/rubrics.jsonl), outputs, anonymous pairs, judgments, keys, candidate additions, and decoded summaries are included. [Creation notes](stimuli/creation-notes.md) document allocation; [rule ownership](rule-ownership.md) records the compression audit. These are now public development examples and must not be reused as unseen test evidence.

Writer instruction template: complete each request independently; use only the assigned skill and input file; load references selectively; do not browse or use extra agents; return one final answer in the requested language and scope; record files read separately. Manual smoke substitutes the attached compact prompt for the skill folder. Judges see only the request, supplied material, prior rubric and anonymous response pair, check exact constraints before preference, cite defective spans, and allow ties. No private profiles or third-party dataset rows are included.

Run `python3 evaluations/2026-09-19/summarize.py` to recompute the preference and critical-failure counts from the saved anonymous judgments and keys. This checks aggregation, not the truth of the judgments.
