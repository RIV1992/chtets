# Install Chtets

Chtets is a folder of writing instructions and references. It does not need an API key, a running server, or its own model subscription. You need an agent that can read the files; the agent's own access requirements still apply.

Choose one installation method. The instructions below were checked against official documentation on September 19, 2026. They describe documented integration paths, not completed runtime tests on every product.

## Option 1: use the Skills CLI

From the project where you want to use Chtets, run:

```sh
npx skills add RIV1992/chtets --skill chtets
```

Select your agent and review the destination. The default scope is the current project. Add `--global` for installation across your projects, or `--copy` for independent copies instead of symlinks. To inspect the repository first:

```sh
npx skills add RIV1992/chtets --list
```

These commands use the third-party [Vercel Skills CLI](https://github.com/vercel-labs/skills#install-a-skill). Its current [package metadata](https://github.com/vercel-labs/skills/blob/main/package.json) requires Node.js 22.20.0 or later. Use a supported Node.js version with npm/npx and Git available. The manual method below needs neither Node.js nor the installer.

## Option 2: copy the skill folder

Download the repository through **Code → Download ZIP**, or clone it:

```sh
git clone https://github.com/RIV1992/chtets.git
cd chtets
```

Copy the entire `skills/chtets/` directory into **one** destination from this table. Do not copy only `SKILL.md`: the relative links need the bundled references.

| Agent | One project | All projects for this user | How to invoke |
| --- | --- | --- | --- |
| Codex CLI / IDE extension | `.agents/skills/chtets/` | `~/.agents/skills/chtets/` | `$chtets`, or select through `/skills`. [Official guide](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) |
| Claude Code | `.claude/skills/chtets/` | `~/.claude/skills/chtets/` | `/chtets` followed by your request. [Official guide](https://code.claude.com/docs/en/skills#choose-where-skills-load) |
| Gemini CLI | `.gemini/skills/chtets/` | `~/.gemini/skills/chtets/` | Ask it to use Chtets; check discovery with `/skills list`. [Official guide](https://geminicli.com/docs/cli/skills/) |
| OpenCode | `.opencode/skills/chtets/` | `~/.config/opencode/skills/chtets/` | Ask it to load Chtets through its skill tool. [Official guide](https://opencode.ai/docs/skills/) |
| GitHub Copilot in VS Code | `.github/skills/chtets/` | `~/.copilot/skills/chtets/` | `/chtets` in chat; `/skills` opens configuration. [Official guide](https://code.visualstudio.com/docs/agent-customization/agent-skills) |

The project paths are relative to the destination project, not this distribution repository. `~` means your home directory; in PowerShell use `$HOME`. For a remote container, WSL, or remote agent, install where that agent runs.

Codex searches project skill directories between its working directory and the repository root. Claude Code also supports project and nested scopes; local personal skills do not automatically travel to cloud sessions. See the respective [Codex](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) and [Claude Code](https://code.claude.com/docs/en/skills#use-skills-in-cowork-and-cloud-sessions) discovery rules.

### macOS / Linux example

Run from the downloaded repository root. This example installs Chtets for your local Codex user and stops if a copy already exists:

```sh
chtets_parent="$HOME/.agents/skills"
if [ -e "$chtets_parent/chtets" ] || [ -L "$chtets_parent/chtets" ]; then
  echo "Chtets already exists. Back it up and review the update first."
else
  mkdir -p "$chtets_parent"
  cp -R skills/chtets "$chtets_parent/chtets"
fi
```

For another agent, change only `chtets_parent` to the corresponding parent directory in the table.

### Windows PowerShell example

Run from the downloaded repository root:

```powershell
$chtetsParent = Join-Path $HOME ".agents/skills"
$chtetsTarget = Join-Path $chtetsParent "chtets"
if (Test-Path -LiteralPath $chtetsTarget) {
    throw "Chtets already exists. Back it up and review the update first."
}
New-Item -ItemType Directory -Path $chtetsParent -Force | Out-Null
Copy-Item -LiteralPath ".\skills\chtets" -Destination $chtetsTarget -Recurse
```

This installs for local Codex. Change `$chtetsParent` for another agent. An agent running inside WSL uses the Linux filesystem and Linux installation path.

## Transfer to another device

Copy the full `skills/chtets/` folder from the current repository, or use a versioned skill ZIP from the [releases page](https://github.com/RIV1992/chtets/releases). Check the release version: an older release may precede the current repository instructions.

To build transferable archives from the current checkout, run `python3 scripts/package.py` with Python 3.10 or later. Version 1.1.0 produces `dist/chtets-v1.1.0.zip` with `chtets/SKILL.md`, `chtets/references/`, `chtets/agents/`, and `chtets/LICENSE` under one top-level folder. After extraction, copy `chtets/` to the destination in the table. `dist/chtets-source-v1.1.0.zip` additionally includes documentation, research annotations, and development files. `dist/SHA256SUMS` records both archive hashes.

GitHub's **Download ZIP** contains the whole repository. In that archive, the installable folder is inside `skills/chtets/`; the repository ZIP itself is not a skill-only upload package.

If you installed with symlinks, transfer the actual source folder or reinstall from the repository. A symlink alone will not carry its target to the new device. The Skills CLI also offers [copy installation](https://github.com/vercel-labs/skills#installation-methods).

## Check that it works

Start a fresh agent session after manual installation. Use the invocation shown in the table, then ask:

```text
Use the installed chtets skill. First confirm the SKILL.md path you loaded.
Then shorten this message to at most 45 words, keeping every condition:

We expect the review to finish on Thursday. If the final test passes,
we plan to deploy on Friday. Please confirm by Wednesday whether
your team can join the review. The deployment date is not confirmed.
```

Check the agent's skill selection or file-read activity where the product exposes it. A fluent rewrite by itself does not prove that the skill loaded. The revised message should preserve the test condition, the tentative deployment date, and the Wednesday request.

## Other agents and chat interfaces

For an agent with native Agent Skills support, use its documented skill directory or import flow. A shared file format does not make installation paths, slash commands, or permissions identical across products.

Without native support, attach the self-contained [compact prompt](portable-prompt.md) for ordinary writing. Use the [extended prompt](portable-prompt-extended.md) when you want all five operational guides available without files. Both are generated from the same source; research and evaluation documents are excluded. The extended prompt occupies its full input size even when only one section is relevant.

Ask the agent to apply the attached instructions to your task. This is a prompt-based fallback: automatic discovery and persistence across conversations are not guaranteed. A URL alone is insufficient if the agent cannot retrieve it. A file-reading agent can instead use the complete skill folder and load references selectively.

Local Codex installation does not by itself install the skill into every ChatGPT surface. OpenAI documents [plugin packaging](https://learn.chatgpt.com/docs/build-skills#distribute-skills-with-plugins) for wider distribution.

## Troubleshooting and updates

- **The skill is missing:** check that the installed path ends in `chtets/SKILL.md`, with that exact capitalization. Avoid an extra `chtets/chtets/` level. Check the current project and execution environment.
- **An old copy loads:** check for duplicate names in project and personal locations. Preserve your customizations before replacing a copy; precedence differs by agent.
- **References cannot be read:** copy the full folder with its relative structure. Do not point the agent at files on a different device.
- **Gemini has not discovered the copy:** run `/skills reload`, then `/skills list`. Activation uses a tool and may require your approval. [Gemini guide](https://geminicli.com/docs/cli/skills/)
- **OpenCode hides the skill:** check whether its skill tool or permission for `chtets` is disabled. [OpenCode permissions](https://opencode.ai/docs/skills/#configure-permissions)
- **The agent writes confidently without checking sources:** Chtets provides a method, not browsing access. Provide sources or enable appropriate tools, and ask it to distinguish supplied facts from verified facts.

For updates, save your local changes, obtain a newer repository copy, review the differences, and replace only the installed `chtets/` folder. Keep private author profiles separately so an update cannot overwrite them. Then repeat the loading check above.
