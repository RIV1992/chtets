# Evaluation

Separate four questions: does the package install, does the agent follow it, does the result preserve meaning, and does a reader prefer the writing?

## Version 1.2.1: maintenance checks

Three fresh agents each handled one new synthetic request using the public candidate: a short conditional message, a completeness audit against a fictional contract and amendment, and a denominator correction across report sections. Requests and acceptance criteria were recorded before execution; writers saw neither criteria nor other outputs. The parent model reviewed the results against the original requests. The [record](../evaluations/maintenance-v1.2.1/results.json) preserves requests, criteria, outputs, runtime hashes, reported reads, and review notes.

The short message retained the conditions in 27 words and reported reading only the core. The local report change propagated 9/20 = 45% through the affected text and reused its table, reporting core and meaning-map reads. The completeness audit found all five requirement categories, retained the amendment and unavailable-appendix limit, and used one table; it reported core, meaning-map, evidence, and review reads. It also identified that the supplied full draft merely referred to the method description and results table rather than containing them.

These are single functional observations, with no baseline or independent human review. They do not establish quality improvements, general reference-loading savings, real standards expertise, or full-report performance. Token use, latency, and hidden host context were not measured. Keep the real report field check separate.

All 17 repository tests passed. Two previously unnoticed faults were recreated in temporary source copies: an incorrect README version now fails validation, and a missing meaning-map output fails evidence-integrity checks. Version checks include supplied release tags and archive labels; remote publication still needs verification. Historical evidence hashes do not constrain later skill instructions.

## Version 1.2.0: optional meaning map

This release adds traceable dependencies across report sections, an explicit change-propagation procedure, and standards-reading guidance on editions, applicability, exceptions, and project evidence. The [release check](../evaluations/meaning-map-v1/README.md) preserves an eight-task comparison with v1.1.1. Read its findings and limitations before interpreting the addition as an improvement.

The larger planned experiment and ablation are deferred in favor of a functional release before field use. No real standards, full-length report, human voice panel, or long-context retrieval test has been evaluated here. Current instruction sizes are in the [generated report](context-size.json); the historical counts below describe their original releases.

## Version 1.1.0: compact workflow

A fresh synthetic set compared the previous public instructions with a compact version: 36 tasks, 12 each in English, French, and Russian. Separate writers did not see the rubrics; separate model judges received anonymous, shuffled pairs. No critical failures were reported for either condition. There were 35 ties and one preference for the compact version, involving a minor continuity issue in a French fictional scene. A stricter reading could classify that original-version issue as a constraint failure.

Three separate research additions were tried on 27 reused pilot inputs. There were 25 ties and two preferences for the compact baseline. None was added to the released core. The experiment did not establish an improvement in writing quality; it supported retaining the smaller instructions without an observed critical regression on this limited set.

The native core is 792 words (previously 1,248), and the default self-contained prompt is 838 words (previously 6,087). Counts are whitespace words, not tokens. A separate compact-prompt run handled three multilingual shortening tasks and 12 minimal requests without local reference access. Seven focused packaging tests check generated prompts, local-link containment, archive boundaries, and reproducibility.

Read the [full protocol, findings, limitations, and saved outputs](../evaluations/2026-09-19/README.md). The runs were language batches in one host, with one sample per condition and model reviewers; exact internal computation and token use were unavailable. Human voice review, a second native client, and long-context interference were not tested. The published inputs are now development material, not an unseen test set.

## A useful comparison for your work

1. Choose fresh tasks representative of your own writing. Keep personal material private.
2. Define the required facts, constraints, and prohibited distortions before drafting.
3. Use the same model, source material, tools, and budget for both conditions. Change only whether the skill is supplied.
4. Preserve both outputs. Hide their origin and vary their order for the reviewer.
5. Assess correctness and task completion first. Then compare coherence, clarity, voice, and economy. Allow ties.
6. Repeat on several topics and have the intended author review voice. Report the task set, conditions, and uncertainty alongside any result.

A false promise, missing condition, invented anecdote, or distorted quotation is a blocking defect. A stylistic preference cannot compensate for it. Conversely, a different valid wording should not fail just because it does not match a single reference sentence.

The [example tasks](../examples/tasks.md) are public development examples. Once used to tune the skill, they should not also serve as unseen test evidence.

## Earlier prototype

Before this public English release, a personalized Russian prototype was tried on six synthetic tasks: a French payment email, an English expert comment, a Russian pilot update, a verbatim memory, a plain-language explanation, and a fictional scene.

Two separate agent runs used the same requests, one with the prototype and one without it. Acceptance criteria were written before generation. A separate model editor received mixed A/B pairs without their origin labels.

| Observation | Ordinary mode | Prototype |
| --- | ---: | ---: |
| Tasks meeting the required constraints | 6 of 6 | 6 of 6 |
| Editorial preferences | 1 | 3 |

Two pairs were ties. This is an illustrative result, not a controlled efficacy study. There was one run per condition; the computational budget was not matched; the prototype condition used additional drafting agents for two tasks. The reviewer was a model, not the author or an independent human panel.

Version 1.0.0 generalized and translated that prototype. The table is not a measured performance result for the public skill. Its role is to document the origin and limits of an earlier check, not to advertise a win rate.

## Version 1.0.0: package and smoke checks

For version 1.0.0, the package validator passed: required files, basic skill metadata, local links, and self-contained references were checked. Both ZIP archives passed integrity checks; rebuilding produced identical bytes. Deliberately broken links, private markers, and references outside the skill folder were rejected by the validator.

A fresh agent read the public English skill and completed three synthetic requests. Review of its outputs found:

| Request | Required behavior | Observed result |
| --- | --- | --- |
| Short release update | Keep an unconfirmed Tuesday review date, a release conditional on passing, a three-business-day delay, and a Monday reviewer request | All preserved within the 60-word limit |
| French payment email | Keep a proposed 480-euro payment toward 900 euros, an unknown date for the remaining payment, and a receipt request; end with `Merci,` | All preserved; the proposed payment was not described as already made |
| Punctuation-only transcript edit | Keep every word, its order, and the repeated phrase | Lexical sequence and repetition preserved |

These are functional checks from one run, reviewed by another model. They do not measure improvement over an unassisted model or establish performance across languages, genres, or agent clients.

The installer paths in [installation.md](installation.md) were checked against client documentation. Native integration has not been executed in every listed client. Successful package validation does not establish literary quality or factual correctness.
