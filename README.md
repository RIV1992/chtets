# Chtets — Clear writing, faithful meaning

Chtets is a portable writing and editing skill for AI agents. Its workflow helps the agent clarify the purpose, connect ideas, cut unnecessary words, and preserve the author's meaning, voice, and commitments.

**Install:** `npx skills add RIV1992/chtets --skill chtets` · [Installation guide](docs/installation.md) · [Examples](examples/tasks.md) · [MIT license](LICENSE)

Use it for emails, articles, expert comments, explanations, interface copy, and creative prose. The instructions are in English; the workflow also includes guidance for writing in French and Russian.

## A small edit can change a promise

**Source facts:** the team expects approval by Thursday; approval is still pending; launch depends on approval.

| Draft | Edited with those facts preserved |
| --- | --- |
| “We will launch on Thursday.” | “We expect approval by Thursday and plan to launch once it comes through.” |

The correction preserves the dependency and the uncertainty.

## Make the connection clear

**Source facts:** test invitations are landing in spam; launch requires reliable delivery.

| Draft | Edited to make the reasoning explicit |
| --- | --- |
| “Our test emails are landing in spam. We should delay the launch.” | “Our test emails are landing in spam, so invitees may miss them. We should delay the launch until delivery is reliable.” |

The edit explains why the delivery problem matters to the launch. It keeps a possible consequence as a risk rather than reporting it as an event that has already happened. Both examples are illustrative edits based on the stated facts.

## Quick start

With Node.js and npm available, run:

```bash
npx skills add RIV1992/chtets --skill chtets
```

Choose your agent and installation scope when prompted. Then give the agent a task and the source material:

```text
Use Chtets to edit the draft below for a prospective customer.
Keep the facts, conditions, and level of certainty. Make the argument flow
from one sentence to the next. Return the finished text first.

[Your draft]
```

The skill itself is Markdown and has no runtime dependencies. The command above uses the separate [Skills CLI](https://github.com/vercel-labs/skills). You can also [copy the skill folder manually](docs/installation.md#option-2-copy-the-skill-folder) or download a [release archive](https://github.com/RIV1992/chtets/releases).

## What it helps with

| Your task | What the agent should check |
| --- | --- |
| Write from notes | Reader, purpose, central thought, and necessary context |
| Repair a disjointed draft | The relationship between neighboring sentences and paragraphs |
| Shorten a text | Repetition and detours, while retaining conditions and qualifications |
| Make a claim persuasive | Its evidence, concrete meaning, and limits |
| Write in someone's voice | Confirmed preferences and actual experience supplied by that person |
| Translate or adapt | Intent, register, terminology, and strength of commitments |
| Proofread a transcript | The permitted level of change; preserve verbatim speech when requested |
| Write a scene | Viewpoint, movement, rhythm, and meaningful detail |

Chtets separates two editorial passes: **meaning and evidence**, then **reader and language**. A fluent sentence still needs a sound claim; an accurate collection of facts still needs a clear line of thought.

See [example requests and source material](examples/tasks.md) for drafting, shortening, verification, transcript editing, and creative writing.

## Bring your own voice

Give the agent your style guide, a few writing samples, and any preferences that matter to the task.

Copy [the author-profile example](examples/author-profile.example.md), keep the completed profile private, and explicitly ask your agent to use it. Profiles are optional; there is no automatic profile loader. See [customization](docs/customization.md) for scoped preferences and safe updates.

## Agent support and portability

The package follows the `SKILL.md` folder structure used by Agent Skills clients. Our [installation guide](docs/installation.md) covers Codex, Claude Code, Gemini CLI, OpenCode, and GitHub Copilot in VS Code using their documented discovery paths.

These are documentation-checked installation routes, not a claim that every client/version has passed an end-to-end test. Invocation, file access, and web research depend on the host agent.

For chat apps without native skills, attach or paste the [compact prompt](docs/portable-prompt.md) with your task. It contains the core workflow in one self-contained file. The [extended prompt](docs/portable-prompt-extended.md) also includes the five operational guides. Pasting it supplies all of that text, even if the agent only uses one section. Neither prompt installs an automatically discovered skill.

The native core is **792 words**; the compact prompt is **838 words**, down from the previous 6,087-word all-in-one prompt. These are whitespace word counts, not model tokens. References load only when a task needs them. See the [size report](docs/context-size.json) for reproducible counts.

## What's inside

| Path | Purpose |
| --- | --- |
| [`skills/chtets/SKILL.md`](skills/chtets/SKILL.md) | Core workflow and reference routing |
| [`skills/chtets/references/`](skills/chtets/references/) | Composition, genres, evidence, author voice, review, and foundations |
| [`docs/installation.md`](docs/installation.md) | Installer, manual copy, supported paths, and troubleshooting |
| [`docs/customization.md`](docs/customization.md) | Optional personal style and project conventions |
| [`docs/research.md`](docs/research.md) | Research influence and limits of the evidence |
| [`docs/evaluation.md`](docs/evaluation.md) | What has been checked and how to evaluate a change |
| [`research/2026-09-19/`](research/2026-09-19/) | 34 annotated sources, limitations, search logs, and development scenarios |
| [`docs/development.md`](docs/development.md) | Rule ownership, context budgets, and criteria for new instructions |
| [`examples/tasks.md`](examples/tasks.md) | Ready-to-use requests with synthetic source material |
| [`scripts/`](scripts/) | Dependency-free validation and reproducible packaging |

Keep the entire `skills/chtets` folder when installing: the main file links to its references. Ordinary use requires no server, API key, network call, or executable script from this repository. An agent may still use its own tools when your task calls for research.

## Evidence and limits

The [research notes](docs/research.md) explain how QuestBench informed the evidence checks and how research on coherence, factual fidelity, revision, voice, and evaluation informs further development. Findings, proposed transfers, and tests are recorded separately. The research corpus stays outside the installed writing workflow. The [evaluation notes](docs/evaluation.md) document what has been tested and its limits; they do not establish a general improvement in writing quality.

Chtets can guide an agent's decisions. It cannot guarantee factual correctness, access unavailable sources, or reproduce an author's voice without adequate material.

## Contribute

A useful contribution starts with a writing task where the current guidance fails. Include synthetic or shareable source material, the observed problem, and the smallest rule change that addresses it. [Contribution guide](CONTRIBUTING.md).

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/package.py
```

Packaging produces compact and extended prompts, a size report, a portable skill ZIP, a full source ZIP, and SHA-256 checksums. On Windows, `python` or `py -3` can replace `python3`.

## License

[MIT](LICENSE). Copyright © 2026 RIV1992. External papers, datasets, and client documentation remain subject to their respective terms.
