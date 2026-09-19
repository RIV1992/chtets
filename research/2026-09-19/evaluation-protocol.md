# Evaluating a proposed Chtets change

Status: proposed protocol, not an executed experiment. The accompanying 12 examples are original, public development material. They are neither a validated benchmark nor an unseen test set.

## Ask a narrow question

Name the change and its predicted effect before generating outputs. For example: “Does the scope-preservation check reduce unsupported generalization without increasing unnecessary qualifications?” Avoid testing ten new rules at once and attributing the outcome to any one rule.

Use two comparisons for different purposes:

- **Revision test:** existing Chtets versus Chtets with one proposed change.
- **Overall usefulness test:** a well-specified ordinary prompt versus the frozen Chtets version.

A deliberately weak baseline would not answer either question fairly. The choice of controls is informed by REV06 and EVA05–EVA06; its application here is our experimental design.

## Prepare fresh material

Have a person who did not tune the change prepare or reserve new briefs. Include realistic correspondence, explanations, summaries, arguments and creative tasks where appropriate. Stratify English, French and Russian results instead of pooling them into a claim of multilingual coverage. A translation of one example is not three independent situations.

Specify in advance:

1. The reader, purpose, genre, language, permitted editing scope and length rule.
2. The source facts, any supplied author examples and the material allowed for research.
3. Required meanings and disqualifying errors.
4. A few soft criteria relevant to that brief.
5. Valid alternatives, including a justified unchanged draft.

Do not show hidden checking notes or preferred outputs to the generating agents. Do not put the evaluation cases into the runtime skill. If cases have influenced a revision, move them into the development set and obtain new held-out cases.

## Keep generation comparable

Use the same model and version, decoding settings where controllable, source inputs, tools, output limit, total call/token budget and number of allowed attempts. Record the exact prompts and actual resource use. If extra verification is the intervention, report its extra cost explicitly; distinguish a cost-matched comparison from a maximum-quality comparison.

For externally sourced tasks, freeze the retrieved evidence supplied to both conditions where feasible. If live retrieval itself is being tested, document dates and access differences. Keep original outputs even when they contain obvious mistakes. Do not quietly repair one condition before review.

## Review hard errors before preferences

| Check | Examples | How to record |
| --- | --- | --- |
| Instruction compliance | Wrong language, forbidden rewrite, missing requested action | Pass/fail for each explicit condition |
| Meaning preservation | Changed amount, population, certainty, chronology, exception or actor | Specific source/output spans and error type |
| Evidence | Unsupported addition, irrelevant citation, unresolved conflict presented as settled | Claim, supporting passage, decision and remaining uncertainty |
| Coverage | Necessary caveat or argument deleted | Missing required meaning, not simply word count |
| Coherence | Broken reference, unexplained term, false transition | Location and consequence for comprehension |
| Voice and reader fit | Unrequested register, genericization, lost stance | Author judgment plus reader judgment kept separate |
| Economy | Repetition or overload without added function | Concrete passage; neither shorter nor longer wins automatically |

Hard-error freedom is necessary for acceptance, but it does not make all compliant outputs equally useful. Assess soft qualities only in their own dimensions. Do not let a high fluency score compensate for an invented commitment. Source fidelity is not independent verification of the source's truth.

## Blind the comparison

Remove condition labels and randomize presentation order. For automated pairwise judging, judge both orders, permit ties and flag inconsistent decisions. Use the same rubric and source material. Have a competent human inspect disagreements and a sample of apparent wins; author voice requires the author's or an explicitly qualified proxy's judgment.

An automatic judge can locate candidate defects. It must not be the sole evidence that a skill improves text. Do not disclose the expected answer to one condition or use an oracle error label unavailable in ordinary work.

## Report what happened

Save task and run IDs, corpus/skill/model versions, prompts, source snapshot, outputs, permitted and actual budget, word count under a named counting convention, reviewer instructions, judgments and adjudications.

Report task counts and denominators, violations by type, paired wins/ties/losses, order-inconsistent judgments, harmful changes, author acceptance and resource use. Break down by language and operation. Where uncertainty is estimated, state the method and assumptions; repeated outputs from one brief are not automatically independent observations.

Choose sample size and decision rules before observing results. A small pilot diagnoses failure modes; it cannot establish universal quality. Preserve mixed findings and publish representative failures as well as successes when sharing results. No comparison has been run as part of this corpus-building task.
