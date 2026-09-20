# Chtets — Clear writing, faithful meaning

Chtets is a portable writing and editing skill for AI agents. It guides the agent to preserve the author's meaning and voice, make the reasoning clear, and trace important claims to their sources. When a fact or requirement changes, it helps identify which passages, tables, and conclusions need another look.

Use it for everyday correspondence, articles, technical reports, translation, and creative prose. The instructions are written in English and include guidance for English, French, and Russian.

**Current version: [1.2.0](https://github.com/RIV1992/chtets/releases/tag/v1.2.0)** · [Install](docs/installation.md) · [Use in a chat](docs/portable-prompt.md) · [Examples](examples/tasks.md)

## Start with your text

With Node.js and npm available, install through the [Skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add RIV1992/chtets --skill chtets
```

Choose your agent and installation scope, then provide the task and source material:

```text
Use Chtets to edit the draft below for its intended reader.
Preserve the facts, conditions, uncertainty, and author position.
Make the reasoning easy to follow. Return the finished text first.

[Draft and supporting material]
```

You can also [copy the skill folder](docs/installation.md#option-2-copy-the-skill-folder) or download the [installable archive](https://github.com/RIV1992/chtets/releases/download/v1.2.0/chtets-v1.2.0.zip). Keep the whole folder so its references remain available.

**Chtets is Markdown guidance. Using it requires no Python, server, or executable code from this repository.** Its host agent supplies the model and any tools needed for your task.

## What changes in the writing process

| Task | What Chtets asks the agent to do |
| --- | --- |
| Draft from notes | Find the point, organize the material, and supply the context a reader needs |
| Edit or shorten | Improve flow and economy while preserving facts, conditions, and commitments |
| Write from sources | Match material claims to supporting passages, editions, units, and limits |
| Revise a complex report | Follow changed premises through dependent sections, tables, and summaries |
| Adapt an author's voice | Use supplied samples and scoped preferences without inventing experience |
| Translate | Preserve intent, register, uncertainty, and the strength of a request or promise |
| Proofread a record | Respect the permitted corrections and preserve verbatim wording when required |
| Write creatively | Support viewpoint, rhythm, and deliberate ambiguity |

The final review separates **meaning and evidence** from **reader and language**. A fluent sentence can still change a promise; a list of correct facts can still leave a gap in the argument.

## From a sentence to a whole report

These examples use synthetic facts.

| Source material | Faithful result |
| --- | --- |
| Approval is expected by Thursday; launch depends on it | “We expect approval by Thursday and plan to launch once it comes through.” |
| A correction changes a pilot from 18 reports among 24 participants to 18 among 36 | Update 75% to 50%, “a majority” to “half,” and any dependent headline, table, or conclusion. Keep the self-report and pilot limitations. |

For interdependent work, the optional [meaning map](docs/meaning-map.md) records claims, grounds, conditions, and affected passages. In a report built from standards, it keeps the exact requirement and its applicability separate from evidence that the project satisfies it. An edition change or exception can alter the conclusion; a planned test does not establish compliance.

The map is a working interpretation that must be checked against the material. Routine messages use the core directly. See the [worked example](examples/meaning-map.md) and [editing practice pairs](examples/practice-pairs.md).

## Use it across agents and chats

The package follows the `SKILL.md` folder structure. The [installation guide](docs/installation.md) covers documented paths for Codex, Claude Code, Gemini CLI, OpenCode, and GitHub Copilot. Those routes have not all been tested end to end; discovery and tool access depend on the host.

For a chat without native skill support, attach the self-contained [compact prompt](docs/portable-prompt.md). The [extended prompt](docs/portable-prompt-extended.md) includes all six operational guides. These are manual prompts; attaching one does not install a persistent skill.

The core contains **798 whitespace words**, and the compact prompt **842**. Optional references are read for specific difficulties. The extended prompt contains **3,555 words**, all supplied when pasted. These are file word counts, not model tokens or measured per-task context. [Size report](docs/context-size.json).

To personalize it, provide a style guide or writing samples. Keep completed profiles private and apply preferences within their scope. [Author-profile example](examples/author-profile.example.md) · [Customization](docs/customization.md).

## Evidence and limits

The [evaluation record](docs/evaluation.md) preserves tasks, outputs, judgments, and limitations. The v1.2.0 check compared eight synthetic requests with v1.1.1: the model reviewer reported no critical failures in either version, seven ties, and one slight preference for the new version. This does not establish a general improvement or performance on full-length reports with real standards.

Chtets guides the agent's work. Accuracy still depends on source access, interpretation, and review. It cannot supply missing evidence or guarantee an author's voice. The [research guide](docs/research.md) explains which findings inform the instructions; research and evaluation archives remain outside the installed skill.

## Repository guide

| Location | Purpose |
| --- | --- |
| [skills/chtets](skills/chtets/) | Installable core, operational references, and agent metadata |
| [docs](docs/) and [examples](examples/) | Installation, manual prompts, explanations, and sample requests |
| [research](research/2026-09-19/) and [evaluations](evaluations/) | Research provenance and preserved evaluation evidence |
| [scripts](scripts/) and [tests](tests/) | Python tools for maintainers: validation, packaging, and regression checks |

To contribute, bring a concrete writing failure and the smallest useful correction. [Contribution guide](CONTRIBUTING.md) · [Development and releases](docs/development.md) · [Changelog](CHANGELOG.md).

[MIT license](LICENSE). Copyright © 2026 RIV1992. External sources retain their own terms.
