# Foundations and limitations

Chtets combines three kinds of guidance. Their evidential weight must remain distinct.

| Layer | What it contributes | What it does not establish |
| --- | --- | --- |
| Critical reading of QuestBench | Attention to the exact question, source, version, and evaluation criterion | That these instructions improve literary style |
| Editorial design | Composition, connections, compression, and genre choices | One universally best template |
| Author preferences supplied for a task | Voice and context-specific decisions | Rules for every author or genre |

## Research context

The original skill was informed by a review of Shen et al., [Teaching AI Through Benchmark Construction: QuestBench as a Course-Based Practice for Accountable Knowledge Work, v2](https://arxiv.org/abs/2605.21413v2), and the [QuestBench dataset](https://huggingface.co/datasets/PKUAIWeb/QuestBench/tree/main).

QuestBench concerns accountable knowledge work and evaluation through research questions, reference answers, and scoring criteria. It is not a collection of exemplary prose or a test of literary composition. The editorial rules in Chtets are a separate design contribution, not a writing method validated by that benchmark.

The source review also motivated checking answer keys rather than treating them as infallible. Detailed allegations about a particular record require the original question, a pinned dataset revision, and an appropriate source check. This portable skill does not ship the dataset or use its reference answers as a knowledge base.

## Practical transfer

| Failure to avoid | Chtets decision | How to check |
| --- | --- | --- |
| A plausible answer addresses a different question | Establish purpose and required meanings | Compare the request and result |
| A citation does not support the nearby assertion | Link the claim to a passage and context | Read the supporting source |
| A current term is judged against an old version | Establish the relevant date and edition | Compare like versions |
| An answer key is mistaken | Check the criterion before revising the answer | Compare it with independent support |
| The response has the wrong type or scope | Identify what the question actually asks for | Compare question, answer, and criterion |
| Translations collapse important distinctions | Check the meaning in each language | Preserve the same concepts and limits |
| The final text violates a length or format limit | Check the finished deliverable | Use the requested counting rule or format |
| Accurate facts do not form a connected statement | Give paragraphs functions and check transitions | Read without supplying missing premises |
| Polishing erases the author's position | Use supplied preferences and actual observations | Ask whether the author recognizes the thought |

These are practical design choices, not measured effects attributed to QuestBench. A research task's difficult retrieval path should not become a writing template; a reader often benefits from a simpler route to the point.

## What the public version can claim

This is an English, portable adaptation of an earlier writing skill. Its instructions support English, French, and Russian work, but their quality across languages and agent systems has not been established by a comparative evaluation of this release. The guidance may be useful in other languages; that is not a claim of tested coverage.

There is no proven performance gain for this public version, no guarantee against errors, and no change to the underlying model. Earlier informal exercises do not validate a new translation or release. Follow the evaluation procedure in [review.md](review.md) before making comparative claims, and report its limits.

Source verification depends on access to relevant material and tools. Without them, the agent can check supplied content and internal consistency but must not claim complete external verification. No proprietary service, model, browsing tool, script runtime, or account is required to read and apply the skill itself.
