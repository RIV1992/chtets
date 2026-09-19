# Creation notes

All situations, passages, source notes, names, and application states in these files were authored as synthetic fixtures for this dataset. No external browsing, skill files, prior examples, research corpus, or other agents’ outputs were used. No writing/model evaluation was run.

## File counts

- `inputs.jsonl`: 36 writing inputs, with only id, lang, family, request, and material.
- `rubrics.jsonl`: 36 separate rubrics keyed by the same ids.
- `routing-inputs.jsonl`: 12 additional routing inputs.
- `routing-rubrics.jsonl`: 12 separate routing rubrics keyed by the same ids.

## Writing-input allocation

| Language | Correspondence | Expert comment / voice | Explanation / shortening | Sourced analysis | Interface copy | Creative | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| en | 2 | 2 | 2 | 2 | 2 | 2 | 12 |
| fr | 2 | 2 | 2 | 2 | 2 | 2 | 12 |
| ru | 2 | 2 | 2 | 2 | 2 | 2 | 12 |
| Total | 6 | 6 | 6 | 6 | 6 | 6 | 36 |

There are 12 already-good/no-change or narrow-proofread requests: 4 per language. Of these, 6 supply already-correct text and 6 contain a local spelling error. The other 24 writing inputs request substantive composition, rewriting, shortening, analysis, interface text, or fictional continuation.

Narrow-scope ids:

- `en-correspondence-02`
- `en-expert_comment_voice-02`
- `en-sourced_analysis-02`
- `en-interface_copy-02`
- `fr-correspondence-02`
- `fr-expert_comment_voice-02`
- `fr-sourced_analysis-02`
- `fr-interface_copy-02`
- `ru-correspondence-02`
- `ru-expert_comment_voice-02`
- `ru-sourced_analysis-02`
- `ru-interface_copy-02`

## Routing allocation

Each language has one arithmetic, one exact extraction, one supplied-table fact, and one minimal typo request: 4 per language and 12 total.

## Conventions and structural checks

Every writing request that has a word limit explicitly defines words by whitespace separation. Quoted source passages are fully supplied. Output target paragraphs are explicitly labeled where source notes accompany a proofreading request. Creative inputs explicitly permit invention within their stated continuity constraints.

Creation-time checks covered record totals, unique ids, language/family allocation, narrow-scope allocation, field sets, and matching input/rubric ids. These are structural checks only; no efficacy claim is made.
