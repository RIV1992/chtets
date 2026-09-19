# Developing a compact writing skill

The current development work starts from commit `78f01bfaaa125fb9cff56640fd20dea6983b93f0`. Its aim is to make a few editorial decisions more explicit while removing unnecessary runtime instructions.

## Separate the questions

Compare A (the previous release) with B (a compact version preserving its editorial rules) before testing new mechanisms. Otherwise a shorter instruction set and a new editing procedure would be confounded. Research additions are separate hypotheses, not benefits inherited from their source papers.

The [34-source register](../research/2026-09-19/README.md) motivates targeted checks of claim scope, dependencies across sentences, purposeful revision, source support and author voice. It stays outside the installed workflow. See [evaluation](evaluation.md) for actual observations and limitations.

Version 1.1.0 retains B. Separate probes of the first three mechanisms showed no incremental benefit on the selected inputs; the extra instructions remain development hypotheses. Evidence-state and author-voice extensions await more discriminating tasks and author review. The absence of a measured benefit does not refute the underlying research or show that a mechanism never helps.

## Instruction ownership

| Owner | Responsibility |
| --- | --- |
| `SKILL.md` | Purpose, edit permission, meaning invariants, progression, appropriate verification, two short checks, delivery and routing |
| `composition.md` | Diagnose missing connections and repair the affected span |
| `evidence.md` | Trace an important claim to evidence and its limits |
| `author-voice.md` | Apply contextual preferences without inventing facts or biography |
| `genres.md` | Resolve a consequential genre-specific choice |
| `review.md` | Diagnose material defects in a requested critique or complex text |
| `foundations.md` | Brief provenance and optional links for maintainers |
| `examples/`, `docs/`, `research/`, `evaluations/` | Teaching, research, implementation and recorded checks; not routine context |

The core must work without optional files. A supplied greeting or sign-off can be applied directly. A named genre does not automatically require its entire guide. A reference develops an applicable rule; it need not restate every core constraint.

## Measure the material actually used

Authoring targets are 650–800 English whitespace words for the core and 750–1,000 for the compact manual prompt. They are engineering targets, not empirical optima. The [generated size report](context-size.json) counts words, Unicode characters and UTF-8 bytes; these are not model tokens or billed use.

Source evidence, history, drafts and tool results also occupy context. Do not truncate material conditions to satisfy an instruction budget. Selective loading avoids irrelevant reads but does not remove previously loaded text from a persistent conversation. Hosts differ in what they inject and expose; report observable behavior and leave unavailable token or latency measurements unknown.

The compact and extended manual prompts are generated from the same source rules. Compact use must not require absent files. Extended use includes operational references deliberately, not the research archive. Keep the installable folder self-contained and retain link-containment validation.

## Decide what to retain

Check critical meaning and instruction failures before stylistic preference. Retain unchanged text when it already meets the request. Recheck a corrected defect on fresh analogous material; never call public development examples an unseen test set.

A small synthetic check can reveal a regression but does not establish general superiority. If a new mechanism shows no discriminating benefit, report it as inconclusive rather than advertising an improvement. Preserve mixed findings, judge disagreement, examples where no change is best and the cost of any additional verification.

Keep personal profiles outside the public package. When updating a personal installation, preserve scoped preferences and check semantic equivalence with the portable instructions rather than replacing the profile with public defaults.
