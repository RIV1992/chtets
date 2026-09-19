#!/usr/bin/env python3
"""Build deterministic archives and compact/extended chat prompts (Python 3.10+)."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

from validate import (
    DEFINITION_RE, LINK_RE, ROOT, SKILL_REL, local_target, parse_frontmatter, source_files, validate,
)

DEFAULT_VERSION = "1.1.0"
ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
RUNTIME_REFERENCES = (
    "author-voice.md", "composition.md", "evidence.md", "genres.md", "review.md",
)
ROUTING_HEADING = "## Read selectively"
COMPACT_FALLBACK = (
    "Use the instructions in this document directly. For an ordinary writing task, "
    "no reference files are needed. Apply simple explicit preferences directly. "
    "For a difficult passage, identify the specific "
    "problem and apply the relevant checks below; do not expand every short request "
    "into a full audit. If evidence or tools are unavailable, preserve uncertainty "
    "and state any material limitation. Never imply that you read or verified "
    "material you could not access."
)


def replace_routing(body: str, replacement: str) -> str:
    """Replace only reference routing, never neighboring substantive instructions.

    The canonical core isolates routing under ``## Read selectively``. Legacy
    v1.0 combines task modes and routing, so remove only its marked table rather
    than dropping the entire heading and its editing permissions.
    """
    pattern = rf"^{re.escape(ROUTING_HEADING)}\s*\n.*?(?=^## |\Z)"
    if re.search(pattern, body, flags=re.MULTILINE | re.DOTALL):
        return re.sub(pattern, replacement + "\n\n", body, count=1, flags=re.MULTILINE | re.DOTALL)
    marker = "Load only the references needed:"
    legacy = rf"^{re.escape(marker)}\n(?:\s*\n|\|[^\n]*\n)+"
    if re.search(legacy, body, flags=re.MULTILINE):
        return re.sub(legacy, replacement + "\n\n", body, count=1, flags=re.MULTILINE)
    # A self-contained core without a routing section is valid. Any leftover
    # local reference still fails during export instead of disappearing silently.
    return body


def nest_headings(text: str) -> str:
    """Nest source headings without changing fenced examples."""
    lines = []
    fence_char = ""
    fence_length = 0
    for line in text.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            marker = fence.group(1)
            if not fence_char:
                fence_char, fence_length = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = ""
        if not fence_char and not fence:
            line = re.sub(r"^(#{1,5}) ", r"#\1 ", line)
        lines.append(line)
    return "\n".join(lines).strip()


def write_zip(destination: Path, entries: dict[str, bytes]) -> None:
    """Stored entries avoid compressor-version differences across Python runtimes."""
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def normalized_bytes(path: Path) -> bytes:
    # Git checkouts can use CRLF on Windows. Archive bytes remain identical.
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def portable_prompt(root: Path, *, extended: bool = False) -> str:
    skill = root / SKILL_REL
    entrypoint = skill / "SKILL.md"
    fields, body = parse_frontmatter(entrypoint.read_text(encoding="utf-8"))
    references = [skill / "references" / name for name in RUNTIME_REFERENCES] if extended else []
    if extended:
        missing = [path.name for path in references if not path.is_file()]
        if missing:
            raise ValueError("missing runtime references: " + ", ".join(missing))
    section_names = {entrypoint.resolve(): "Core instructions"}
    section_names.update({path.resolve(): f"Reference: {path.relative_to(skill).as_posix()}" for path in references})

    def flatten(path: Path, text: str) -> str:
        # The surrounding section supplies the title; retain all actual rules.
        text = re.sub(r"\A# [^\n]+\n+", "", text, count=1)

        def replace_link(match: re.Match[str]) -> str:
            target = local_target(path, match.group(1))
            if target is None:
                return match.group(0)
            if target not in section_names:
                raise ValueError(f"standalone prompt has an unavailable local reference in {path.name}: {match.group(1)}")
            label = re.match(r"!?\[([^\]]*)\]", match.group(0)).group(1)
            return f'{label} (see "{section_names[target]}")'

        text = LINK_RE.sub(replace_link, text)
        # Reference-style Markdown cannot silently preserve a disk dependency.
        for match in DEFINITION_RE.finditer(text):
            if local_target(path, match.group(1)) is not None:
                raise ValueError(f"use an inline link for exportable references in {path.name}: {match.group(1)}")
        # References named in code spans remain usable when no files exist.
        def replace_reference(match: re.Match[str]) -> str:
            target = (path.parent / match.group(1)).resolve()
            if target in section_names:
                return f'"{section_names[target]}"'
            raise ValueError(f"standalone prompt has an unavailable local reference in {path.name}: {match.group(1)}")

        text = re.sub(r"`((?:\.?\.?/)*references/[^`\n]+\.md)`", replace_reference, text)
        return nest_headings(text)

    if extended:
        routing = (
            "Use only the relevant included reference section for a specific difficulty. "
            "The core instructions are sufficient for ordinary writing; apply simple explicit preferences directly. "
            "All operational references are already included in this document; "
            "selecting a section does not reduce its pasted input size."
        )
    else:
        routing = COMPACT_FALLBACK
    body = replace_routing(body, routing)
    parts = [
        "# Chtets portable prompt" + (" — extended" if extended else " — compact"),
        "> Generated by `python scripts/package.py`. Edit the source skill and references, then rebuild.",
        "Paste or attach this document in a chat app and ask the agent to use Chtets for your writing task. "
        "This is a manual prompt, not native automatic skill installation. "
        "The app's instruction hierarchy, context limits and available tools still apply.",
        "This document is self-contained: no local reference files or skill-discovery tools are needed. "
        + ("It contains the core and operational references, excluding research and evaluation documentation. "
           "When an instruction names a reference, use its included section."
           if extended else "It contains the core writing instructions for ordinary use."),
        f"Purpose: {fields['description']}",
        "## Core instructions",
        flatten(entrypoint, body),
    ]
    for path in references:
        parts.extend(["---", f"## {section_names[path.resolve()]}", flatten(path, path.read_text(encoding="utf-8"))])
    return "\n\n".join(parts) + "\n"


def context_size_report(root: Path, compact: str, extended: str) -> dict[str, object]:
    """Report file inventory sizes, not token counts or per-request telemetry."""
    skill = root / SKILL_REL
    paths = [skill / "SKILL.md", *sorted((skill / "references").rglob("*.md"))]
    counts = {
        path.relative_to(root).as_posix(): len(path.read_text(encoding="utf-8").split())
        for path in paths
    }
    counts.update({
        "docs/portable-prompt.md": len(compact.split()),
        "docs/portable-prompt-extended.md": len(extended.split()),
    })
    texts = {path.relative_to(root).as_posix(): path.read_text(encoding="utf-8") for path in paths}
    texts.update({"docs/portable-prompt.md": compact, "docs/portable-prompt-extended.md": extended})
    return {
        "measurement": "English whitespace words: len(text.split()); includes Markdown and frontmatter",
        "limitations": "File sizes are not model tokens or observed task context. Native reference loading varies by task. Pasting the extended prompt supplies all its text.",
        "words_by_file": counts,
        "characters_by_file": {name: len(text) for name, text in texts.items()},
        "utf8_bytes_by_file": {name: len(text.encode("utf-8")) for name, text in texts.items()},
        "native_core_words": counts["skills/chtets/SKILL.md"],
        "runtime_reference_words": sum(counts[f"skills/chtets/references/{name}"] for name in RUNTIME_REFERENCES),
        "all_skill_markdown_words": sum(counts[path.relative_to(root).as_posix()] for path in paths),
        "compact_prompt_words": len(compact.split()),
        "extended_prompt_words": len(extended.split()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--version", default=DEFAULT_VERSION, help="release version, without a v prefix")
    args = parser.parse_args()
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", args.version):
        parser.error("--version must be a semantic version such as 1.0.0")
    root = args.root.resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    try:
        compact = portable_prompt(root)
        extended = portable_prompt(root, extended=True)
        report = context_size_report(root, compact, extended)
    except (ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for name, content in (
        ("docs/portable-prompt.md", compact),
        ("docs/portable-prompt-extended.md", extended),
        ("docs/context-size.json", json.dumps(report, indent=2, ensure_ascii=False) + "\n"),
    ):
        (root / name).write_text(content, encoding="utf-8", newline="\n")
    errors = validate(root, require_prompt=True)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    output = root / "dist"
    output.mkdir(exist_ok=True)
    skill = root / SKILL_REL
    skill_entries = {
        "chtets/" + path.relative_to(skill).as_posix(): normalized_bytes(path)
        for path in source_files(root) if path.is_relative_to(skill)
    }
    skill_entries["chtets/LICENSE"] = normalized_bytes(root / "LICENSE")
    source_entries = {
        "chtets-source/" + path.relative_to(root).as_posix(): normalized_bytes(path)
        for path in source_files(root)
    }
    archives = [
        (output / f"chtets-v{args.version}.zip", skill_entries),
        (output / f"chtets-source-v{args.version}.zip", source_entries),
    ]
    checksums = []
    for destination, entries in archives:
        write_zip(destination, entries)
        digest = hashlib.sha256(destination.read_bytes()).hexdigest()
        checksums.append(f"{digest}  {destination.name}")
        print(f"Built {destination.relative_to(root)} ({len(entries)} files)")
    (output / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8", newline="\n")
    print("Generated compact/extended prompts, docs/context-size.json and dist/SHA256SUMS")
    print(f"Whitespace words (not tokens): core {report['native_core_words']}; "
          f"runtime references {report['runtime_reference_words']}; "
          f"compact {report['compact_prompt_words']}; extended {report['extended_prompt_words']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
