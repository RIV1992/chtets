# Evaluation

Separate four questions: does the package install, does the agent follow it, does the result preserve meaning, and does a reader prefer the writing?

## Earlier prototype

Before this public English release, a personalized Russian prototype was tried on six synthetic tasks: a French payment email, an English expert comment, a Russian pilot update, a verbatim memory, a plain-language explanation, and a fictional scene.

Two separate agent runs used the same requests, one with the prototype and one without it. Acceptance criteria were written before generation. A separate model editor received mixed A/B pairs without their origin labels.

| Observation | Ordinary mode | Prototype |
| --- | ---: | ---: |
| Tasks meeting the required constraints | 6 of 6 | 6 of 6 |
| Editorial preferences | 1 | 3 |

Two pairs were ties. This is an illustrative result, not a controlled efficacy study. There was one run per condition; the computational budget was not matched; the prototype condition used additional drafting agents for two tasks. The reviewer was a model, not the author or an independent human panel.

The English public version generalizes and translates that prototype. The table is not a measured performance result for this release. Its role is to document the origin and limits of an earlier check, not to advertise a win rate.

## Release checks

For version 1.0.0, the package validator passed: required files, basic skill metadata, local links, and self-contained references were checked. Both ZIP archives passed integrity checks; rebuilding produced identical bytes. Deliberately broken links, private markers, and references outside the skill folder were rejected by the validator.

A fresh agent read the public English skill and completed three synthetic requests. Review of its outputs found:

| Request | Required behavior | Observed result |
| --- | --- | --- |
| Short release update | Keep an unconfirmed Tuesday review date, a release conditional on passing, a three-business-day delay, and a Monday reviewer request | All preserved within the 60-word limit |
| French payment email | Keep a proposed 480-euro payment toward 900 euros, an unknown date for the remaining payment, and a receipt request; end with `Merci,` | All preserved; the proposed payment was not described as already made |
| Punctuation-only transcript edit | Keep every word, its order, and the repeated phrase | Lexical sequence and repetition preserved |

These are functional checks from one run, reviewed by another model. They do not measure improvement over an unassisted model or establish performance across languages, genres, or agent clients.

The installer paths in [installation.md](installation.md) were checked against client documentation. Native integration has not been executed in every listed client. Successful package validation does not establish literary quality or factual correctness.

## A useful comparison for your work

1. Choose fresh tasks representative of your own writing. Keep personal material private.
2. Define the required facts, constraints, and prohibited distortions before drafting.
3. Use the same model, source material, tools, and budget for both conditions. Change only whether the skill is supplied.
4. Preserve both outputs. Hide their origin and vary their order for the reviewer.
5. Assess correctness and task completion first. Then compare coherence, clarity, voice, and economy. Allow ties.
6. Repeat on several topics and have the intended author review voice. Report the task set, conditions, and uncertainty alongside any result.

A false promise, missing condition, invented anecdote, or distorted quotation is a blocking defect. A stylistic preference cannot compensate for it. Conversely, a different valid wording should not fail just because it does not match a single reference sentence.

The [example tasks](../examples/tasks.md) are public development examples. Once used to tune the skill, they should not also serve as unseen test evidence.
