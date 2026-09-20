# Developing a compact writing skill

Version 1.1.0 established the compact workflow; version 1.1.1 cleans up its documentation and evidence archive. The writing instructions are unchanged. A small comparison found no critical compression regression on the selected tasks. Three extra research instructions showed no discriminating benefit in separate probes and were not adopted. See the [evaluation record](../evaluations/2026-09-19/README.md) for the frozen source versions, outputs, and limitations.

## Separate the questions

Compare a compact version preserving existing rules with its predecessor before testing new mechanisms. Otherwise compression and a new editing procedure would be confounded. The [research-to-practice guide](research.md) connects the most useful source findings to existing decisions; the [34-source corpus](../research/2026-09-19/README.md) preserves the fuller evidence and limits.

Claim boundaries, dependent spans, and purposeful revision remain useful research questions. Evidence-state and author-voice extensions await more discriminating tasks and author review. A small inconclusive probe neither establishes a benefit nor shows that a mechanism never helps.

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

## Maintainer tools

Python is needed only to validate and build repository artifacts. Copying the skill folder or using a prepared prompt requires no Python. The tools use the standard library and need Python 3.10 or later:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/package.py
```

Edit the source skill and references, then review and commit the regenerated `docs/portable-prompt.md`, `docs/portable-prompt-extended.md`, and `docs/context-size.json`. CI checks that all three match the source. On Windows, `python` or `py -3` can replace `python3`.

The builder produces two versioned archives under `dist/` and records their SHA-256 hashes in `dist/SHA256SUMS`:

| Archive | Contents |
| --- | --- |
| `chtets-v1.1.1.zip` | One `chtets/` folder containing the skill, references, agent metadata, and license |
| `chtets-source-v1.1.1.zip` | The public source, documentation, research annotations, evaluation evidence, and maintainer tools |

Build outputs and analysis caches are not source files. Research and evaluation material stay outside the installable archive and both prompts. When reorganizing recorded evidence, preserve original inputs, outputs, judgments, mappings, and source versions; regenerate joins and totals instead of storing parallel copies. See the [evaluation artifact commands](../evaluations/2026-09-19/README.md#artifacts-and-reuse).
