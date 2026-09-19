# Public development examples for Chtets

This file accompanies `evaluation-seeds.jsonl`: twelve original synthetic cases, four each in English, French and Russian. They are visible development examples, **not a holdout**, and **have not been executed**. They contain no copied research-paper or dataset passages and no real personal data.

## Coverage

| Case | Main failure exposed |
|---|---|
| DEV-EN-01 | A conditional plan becoming a commitment; changing the reference event for a deadline |
| DEV-EN-02 | Fabricating causation or subgroup overlap from two observations |
| DEV-EN-03 | Dropping a closure exception or changing a booking threshold |
| DEV-EN-04 | Unnecessary rewriting during proofreading; a valid unchanged response |
| DEV-FR-01 | Updating an event beyond what the new source supports |
| DEV-FR-02 | Moving actions or objects between entities during pronoun repair |
| DEV-FR-03 | Treating a requested voice change as permission to invent experience |
| DEV-FR-04 | Disconnected sentences, status inflation and invented causal connections |
| DEV-RU-01 | Losing an access condition or inventing a fallback date |
| DEV-RU-02 | Losing exceptions, attribution requirements or counting rules |
| DEV-RU-03 | Accepting an undated update; falsely treating the old version as proven |
| DEV-RU-04 | Improving flow while inventing outcomes or completing unfinished work |

Each `source_ids` entry links to an evidence card in the research corpus. The papers motivate dimensions and controls; they did not supply these texts or validate these cases. The protected meanings and failure conditions are editorial judgments proposed for review.

## How to use

Use the original-language brief and material as the generation input. Reserve the protected meanings, hard failures and soft criteria for evaluation; exposing them to the writer changes the task into a checklist-assisted exercise. Run baseline and skill under equal model, context, length allowance, attempt count and tool budget. DEV-RU-03 explicitly limits the available sources; the other cases also require no external research.

First record semantic failures against the material. A serious meaning error must remain visible even if the prose reads well. Next compare coherence, relevance and voice. Anonymize outputs, judge both orders, allow ties and report order inconsistency. Human reviewers should assess intended meaning and voice, especially where valid alternatives differ. There is no single required wording or reference answer. DEV-EN-04 permits no change; minimal change may also be appropriate elsewhere.

Word limits are task constraints, not a proxy for quality. If counted automatically, document the tokenizer or word-count convention and use the same convention for both conditions. Preserve the original text for reviewer inspection instead of silently truncating outputs.

## Limits

- Twelve deliberately constructed cases cannot estimate reliability, prove skill improvement or represent every genre. Four cases per language do not support language rankings.
- These are independent tasks, not translated or difficulty-matched equivalents. Language differences would be confounded with case differences.
- French and Russian examples have not received independent native-editor review. All cases need reviewer calibration before quantitative use.
- Public development exposure makes them unsuitable as evidence of generalization. Build a separate, unseen set after freezing the proposed skill changes.
- Style and voice judgments are partly subjective. Hard failures concern task scope and meaning; softer preferences must not masquerade as factual defects.
- The cases cover short text and supplied evidence. They do not test long-document coherence, live-source verification, sustained author voice, specialist prose or creative originality.
- Public model judges may have seen similar test patterns. These examples are original, but originality does not guarantee freedom from conceptual contamination.
- No model outputs, win rates, human agreement scores or executed results are included. JSON validation establishes file structure only.
