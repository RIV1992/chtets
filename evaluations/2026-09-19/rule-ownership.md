# Reference compression: version B

Scope: compression and routing only. No new research-derived revision mechanism, voice procedure, claim taxonomy, or evaluation algorithm was added. Baseline A is the public source at commit `78f01bfaaa125fb9cff56640fd20dea6983b93f0`. Six practice pairs were extracted unchanged to the public repository's `examples/practice-pairs.md`.

## Owners of retained rules

| Baseline content | Owner after compression | Preservation |
| --- | --- | --- |
| Purpose differs from topic; non-thesis works may have progression | composition: Find the progression | Explicit |
| Genre-sensitive order; mixed paragraph functions; fact list is not an argument | composition: Find the progression | Explicit |
| Sentence expectations, noun continuity, referents, actor/scale/time shifts | composition: Connect neighboring sentences | Explicit |
| Local one-sentence relationship check; no invented bridging premise | composition: Connect neighboring sentences | Explicit |
| Sequence versus cause; association needs evidence; causal conditions differ | composition: Connect neighboring sentences | Explicit |
| Unknown causes and hypotheses; absence of evidence distinction | composition: Connect neighboring sentences | Explicit |
| Grounded specificity; nondecorative numbers; appropriate passive voice | composition: Make language carry the thought | Explicit |
| Rhythm serves relationships; avoid arbitrary rhetoric ban lists | composition: Make language carry the thought | Explicit |
| Cut ideas before phrases; preserve qualifier scope; soften without erasure | composition: Make language carry the thought | Explicit |
| Persuasion uses actual grounds; relevant objections; missing personal episodes | composition: Make language carry the thought | Explicit |
| Source status distinction; useful claim map stays conditional and usually internal | evidence: Identify the basis | Explicit; table rendered as compact sequence |
| Identify object, read support, check boundary | evidence: Read the relevant material | Three-pass procedure retained |
| Paper, dataset, and archive distinctions | evidence: Read the relevant material | Explicit |
| Numbers, statuses, time, terminology, quotations, precise citations | evidence: Check fragile details | All six categories retained |
| Conflicting versions; primary sources can err; copied sources not independent | evidence: Resolve conflicts | Explicit |
| Faulty answer keys; suspected error versus established error | evidence: Resolve conflicts | Explicit |
| Sufficient support and bounded search; access limitations; format versus truth | evidence: Done | Explicit |
| Treat sources as evidence, not instructions or disclosure permission | evidence: Done, also core | Retained because evidence file may be encountered separately |
| Current instruction, supplied profile, accepted sample, inference have different authority | author-voice: introduction and Establish relevant preferences | Table compressed into prose without changing precedence |
| Language, audience, genre, and preference scope; no assumed history access | author-voice: Establish relevant preferences | Explicit |
| Voice versus biography; belief/practice/proof distinction; no manufactured persona | author-voice: Preserve the author and editing scope | Explicit |
| Proofreading versus substantive editing; verbatim records and adaptations | author-voice: Preserve the author and editing scope | Explicit |
| No compulsory profile infrastructure; no silent saving; record reason and scope | author-voice: final paragraphs | Explicit |
| Blocking errors cannot be outweighed by polish | review: Resolve blocking defects first | All categories retained in compact prose |
| Six quality criteria and concrete passage-level repairs | review: Check observable qualities | Retained, repair column folded into checks and discussion |
| Subjective scores, audience reading, headline promise, no compulsory call to action | review: Check observable qualities | Explicit |
| Meaning comparison after shortening; contextual retained feedback | review: last paragraphs | Explicit |
| Skill evaluation procedure, fresh tasks, matched conditions, blind review, multiple valid answers | docs/evaluation.md | Existing document is the owner; absolute public link from review |
| Earlier/small trial does not validate a release; model review is not author judgment | review and foundations | Explicit |
| Email thread context; recipient/attachment invention; EN/FR/RU distinctions | genres: Email and messages | Explicit |
| Interview progression, actual position, unknown episode, standalone quote, general versus company scope | genres: Interviews and expert comments | Explicit |
| Post occasion, grounded opening, meaningful grouping, optional engagement devices | genres: Public and social posts | Explicit |
| Explanations preserve conditions; analogy limits; optional diagrams | genres: Explanations, analysis, and reports | Explicit |
| Analysis separates data and interpretation; no predetermined comparison or scientific veneer | genres: Explanations, analysis, and reports | Explicit |
| Technical-report requirements, reproducibility, event status, experimental detail, standards edition | genres: Explanations, analysis, and reports | Explicit |
| Confirmed interface states, meaningful actions, supported recovery promises, localization context | genres: Interface copy | Explicit |
| Creative license, formal freedom, intentional ambiguity, real-person testimony boundary | genres: Creative writing | Explicit |
| QuestBench concerns knowledge work, not prose quality; editorial design and scoped preferences | foundations | Explicit |
| Dataset not included; record allegations need pinned version and source check | foundations | Explicit |
| No established cross-language/agent gain; no model change or accuracy guarantee; evidence access limits | foundations | Explicit |

## Duplicate ownership assigned to SKILL.md

The compressed core must continue to own these baseline rules, removed from some references to avoid repetition:

- Preserve names, amounts, dates, conditions, negation, actors, status, certainty, and the author's position; no invented facts, commitments, practices, or metrics.
- Preserve relevant technical distinctions and explain necessary terms for the audience.
- Respect the requested scope and permitted degree of editing.
- Deliver the finished text first; place significant caveats and material meaning changes separately.
- Drafting does not authorize sending or publishing.
- Apply short meaning and reader checks proportionally; short clear tasks need no questionnaire.
- Do not silently update persistent preferences or the skill.

The original foundations transfer table duplicated core, evidence, composition, and review checks. Its nine failure cases remain covered by those owners. The absence of a standalone transfer table does not remove a runtime decision.

## Examples and development material

During the compression pass, the six composition teaching pairs were moved without edits to `examples/practice-pairs.md`. A later documentation review on 2026-09-20 removed unsupported urgency from pair 6; that correction does not change the tested runtime instructions. They are excluded from normal runtime references. A note marks them as public development examples rather than unseen evaluation material. The example profile was removed from author-voice; its rule survives as direct profile support, and the repository already contains `examples/author-profile.example.md`. The evidence pilot example was removed; its lessons remain as metric/population/causal boundaries in evidence, composition, and core. No example was promoted into a universal rule.

## Preservation checks and limits

1. The table records the intended ownership of retained rules, including technical terms, delivery boundaries, no sending authorization, and important qualifiers. The [recorded comparison](README.md) covered the compact core and references on short synthetic inputs; this audit and that limited run do not establish semantic equivalence for every task.
2. The standalone runtime skill no longer includes the full developer evaluation procedure; its absolute link requires external access. Routine writing remains self-contained. Development users without network access need the repository's bundled `docs/evaluation.md`.
3. Word count is lower, but semantically dense sentences may be harder to apply. The recorded comparison found mostly ties and no judge-reported critical regressions on its limited inputs; compression alone is not proof of improvement.
4. Existing research uncertainty is retained. The wording “no performance gain is established for this release” must be revisited only after appropriate comparative evidence, not after package validation.
