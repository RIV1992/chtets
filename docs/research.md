# Research behind the writing decisions

Chtets draws on research about evidence, coherence, revision, and register. The seven connections below explain decisions already present in the skill. They are editorial transfers from specific studies or frameworks, not experimentally established effects of the Chtets prompt. All examples are original and synthetic.

For the complete reading record, see the [34-source corpus](../research/2026-09-19/README.md). The [QuestBench audit](../research/2026-09-19/questbench-audit.md) preserves the initial benchmark review, record-level observations, and pinned dataset revision.

## 1. Put information in an order the reader can follow

Gopen and Swan explain continuity and emphasis through worked scientific-prose examples. Their article is editorial exposition; it does not establish a universal sentence pattern. Chtets uses this perspective to check referents, paragraph purpose, and missing premises in [composition](../skills/chtets/references/composition.md). [Primary reprint, pp. 7–12](https://www.usenix.org/sites/default/files/gopen_and_swan_science_of_scientific_writing.pdf) · corpus COM01.

“A worker inspects it hourly. The retry queue holds failed uploads” becomes “The retry queue holds failed uploads. A worker inspects it every hour.” Reordering supplies the referent without inventing a fact. If a connection requires an unknown premise, wording alone cannot establish it.

## 2. Recheck the passage around an edit

In SWiPE's annotated Wikipedia sample, 43% of edits crossed sentence boundaries. That percentage belongs to the sample, not to all writing. The observation helps explain why Chtets' existing composition checks extend to affected connections. [Primary paper, §4.4](https://arxiv.org/html/2305.19204v1) · corpus COH05.

After deleting the sentence that introduces a trial schedule, do not leave “This schedule applies until Friday” without an identifiable schedule. Keep the introduction or name the schedule using supplied facts. The same check matters after moving, splitting, or merging sentences.

## 3. Preserve the limits of a finding

A study of 4,900 summaries found scope broadening in outputs from many tested models, including under accuracy prompts. Its evidence concerns selected models and predominantly medical research; it does not establish the behavior of every model or genre. Chtets preserves population, conditions, time, and certainty through its meaning and [evidence checks](../skills/chtets/references/evidence.md). [Author manuscript](https://arxiv.org/pdf/2504.00025) · [publication](https://doi.org/10.1098/rsos.241776) · corpus FID06.

“During the six-week pilot, 18 of 24 participants reported shorter waits” cannot become “The service reduces waiting times.” The shorter sentence loses the sample, duration, self-report, and limits on a causal conclusion.

## 4. Check support and required coverage separately

FActScore evaluates support for individual factual units and distinguishes precision from recall. ALCE evaluates answer correctness and citation quality separately. Neither makes every cited source true. Chtets combines claim-level evidence checks with a separate check that the request has been answered. [FActScore, §3.1](https://aclanthology.org/2023.emnlp-main.741.pdf) · [ALCE, §§2–3](https://aclanthology.org/2023.emnlp-main.398.pdf) · corpus FID01/FID02.

A passage saying a trial began in May does not support “The trial began in May and cut costs by 20%.” Removing the percentage repairs attribution; if the brief asks for the outcome, that information remains missing. See the [supplied-source practice task](../examples/tasks.md#7-check-a-claim-against-its-source).

## 5. Give another revision a specific purpose

Self-Refine's feedback ablations across three tasks favored specific, actionable feedback over generic or absent feedback. The paper also shows a case where successive revisions lose quality. Historical, heterogeneous task results do not establish that repeated prose self-review improves accuracy. Chtets' [review procedure](../skills/chtets/references/review.md) therefore targets material defects and stops when they are resolved. [Primary paper, §4/Table 2 and Appendix H/Table 10](https://arxiv.org/html/2303.17651v2) · corpus REV03.

“The request is buried behind three background sentences; move the existing request to the opening and retain its deadline” gives a checkable editing purpose. “Improve the tone” leaves both the defect and the success criterion unclear.

## 6. Change register without changing a commitment

XFORMAL evaluates formality transfer in Brazilian Portuguese, French, and Italian, with separate judgments of register, fluency, and meaning. Sentence-level rewrites do not establish personal voice, professional correspondence quality, or Russian performance. Chtets treats [author voice](../skills/chtets/references/author-voice.md) and preserved meaning as separate checks. [Primary paper, §§5.3–5.5](https://aclanthology.org/2021.naacl-main.256.pdf) · corpus VOI02.

“On prévoit de vous répondre vendredi” can become “Nous prévoyons de vous répondre vendredi.” Substituting “Nous nous engageons” adds a commitment. A more formal expression must retain the original degree of certainty.

## 7. Name the defect before giving a verdict

SummEval assesses coherence, consistency, fluency, and relevance separately. Its news-summary framework does not measure every genre or an author's voice. Chtets uses distinct meaning and reader checks so that polished wording cannot conceal a changed fact. [Primary paper, §§4.3–5.1](https://aclanthology.org/2021.tacl-1.24.pdf) · corpus EVA03.

Given “confirmation is still pending,” the fluent sentence “Your reservation is confirmed” fails the meaning check. A useful review identifies the altered status and restores it instead of offering only a quality score.

## What has actually been tested in Chtets

A small [development comparison](../evaluations/2026-09-19/README.md) supported retaining the compact instructions without an observed critical regression on those inputs. Separate additions emphasizing claim boundaries, dependent spans, and located repairs showed no discriminating benefit and were not adopted. The results neither validate these transfers generally nor refute the source research.

Research annotations, teaching examples, and evaluation records stay outside normal writing context. Keep useful decisions in the skill; consult the corpus when investigating a failure or developing a change. Resource terms, source overlap, multilingual gaps, and reading scope remain in the [methodology](../research/2026-09-19/methodology.md) and [resource register](../research/2026-09-19/resource-register.md).
