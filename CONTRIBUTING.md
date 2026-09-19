# Contributing to Chtets

Improve a decision the agent makes, and show which writing task benefits.

## Propose a focused change

1. Describe the task, audience, source facts, and constraints.
2. Show the failure using synthetic material or text you may share publicly.
3. Explain which instruction is missing, misleading, or too broad.
4. Make the smallest useful change and try a fresh example.

Keep task-specific conventions scoped. A rule for a legal quotation should not flatten a fictional scene; one author's preferred sign-off should not become everyone's default.

## Keep evidence separate from preference

Mark examples as synthetic. Preserve their facts, uncertainty, and commitments during editing. A factual error or a lost requirement cannot be offset by better style.

If reporting an improvement, include the prompts, outputs, model and tool conditions, and how the outputs were assessed. Small demonstrations can show a failure or a useful behavior. They do not establish a general win rate.

## Work on the source files

Edit `skills/chtets/SKILL.md` and its references. `docs/portable-prompt.md` is generated: regenerate it rather than changing it directly.

Run:

```bash
python3 scripts/validate.py
python3 scripts/package.py
```

Review the generated prompt and archives. Add a short entry to `CHANGELOG.md` when the change affects users. Before a release, check the installation steps against the relevant client's official documentation.

## Share only public material

Do not include completed personal profiles, credentials, private correspondence, user histories, or benchmark corpora whose redistribution terms have not been established. Links and original critical analysis are enough to explain the research influence.

Open an issue or pull request in this repository. Submissions are intended to be distributed under the repository's MIT license.
