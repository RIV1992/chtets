#!/usr/bin/env python3
"""Check a portable Chtets source tree using only Python's standard library."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL_REL = Path("skills/chtets")
REQUIRED_FILES = (
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
    "skills/chtets/SKILL.md", "skills/chtets/agents/openai.yaml",
    "scripts/validate.py", "scripts/package.py", ".github/workflows/check.yml",
    ".gitignore",
)
SOURCE_TOP_LEVEL = (
    "README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", ".gitignore",
    "NOTICE", "CITATION.cff", "SECURITY.md", "CODE_OF_CONDUCT.md",
)
SOURCE_DIRECTORIES = ("skills", "docs", "examples", "scripts", ".github/workflows")
PUBLIC_EXTENSIONS = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".cff"}
LINK_RE = re.compile(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^)\n]+)\s*\)")
DEFINITION_RE = re.compile(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", re.MULTILINE)
PRIVATE_PATTERNS = (
    (r"sandbox:/", "local sandbox link"),
    (r"/(?:workspace|Users)/", "private absolute path"),
    (r"/root/\.codex/", "private installation path"),
    (r"libfile_[0-9a-f]+", "private file identifier"),
    (r"skill-[0-9a-f]{24,}", "private skill identifier"),
    (r"<OWNER>|YOUR_GITHUB_USERNAME", "unresolved repository owner"),
    (r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", "private key"),
    (r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}", "access token"),
)


def source_files(root: Path) -> list[Path]:
    """Return the explicit public source set, never build output or Git data."""
    files = {root / name for name in SOURCE_TOP_LEVEL if (root / name).is_file()}
    for directory in SOURCE_DIRECTORIES:
        base = root / directory
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            relative_parts = path.relative_to(base).parts
            if any(part.startswith(".") or part == "__pycache__" for part in relative_parts):
                continue
            if path.is_file() and path.suffix in PUBLIC_EXTENSIONS:
                files.add(path)
    return sorted(files, key=lambda p: p.relative_to(root).as_posix())


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Read the simple scalar YAML fields used by the skill; no YAML dependency."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md has unclosed YAML frontmatter") from exc
    fields: dict[str, str] = {}
    index = 1
    while index < end:
        line = lines[index]
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            if key in fields:
                raise ValueError(f"duplicate frontmatter field: {key}")
            if value in {">", "|", ">-", "|-", ">+", "|+"}:
                parts = []
                index += 1
                while index < end and (not lines[index].strip() or lines[index].startswith((" ", "\t"))):
                    parts.append(lines[index].strip())
                    index += 1
                value = " ".join(parts)
                index -= 1
            elif len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
                value = value[1:-1]
            fields[key] = value.strip()
        index += 1
    return fields, "\n".join(lines[end + 1:]).lstrip("\n") + "\n"


def without_fenced_code(text: str) -> str:
    lines = []
    fence_char = ""
    fence_length = 0
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if not fence_char:
                fence_char, fence_length = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = ""
            lines.append("")
        else:
            lines.append("" if fence_char else line)
    return "\n".join(lines)


def link_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<"):
        return value[1:value.find(">")]
    return re.split(r"\s+[\"']", value, maxsplit=1)[0].strip()


def local_target(source: Path, raw: str) -> Path | None:
    target = link_target(raw)
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    return (source.parent / unquote(parsed.path)).resolve()


def validate(root: Path, require_prompt: bool = False) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")
    for directory in ("docs", "examples", "skills/chtets/references"):
        if not any((root / directory).glob("*.md")):
            errors.append(f"{directory}/ must contain at least one Markdown file")
    if require_prompt and not (root / "docs/portable-prompt.md").is_file():
        errors.append("missing generated docs/portable-prompt.md")

    skill = root / SKILL_REL
    entrypoint = skill / "SKILL.md"
    if entrypoint.is_file():
        try:
            fields, body = parse_frontmatter(entrypoint.read_text(encoding="utf-8"))
            if fields.get("name") != "chtets":
                errors.append("SKILL.md frontmatter name must be chtets")
            if not fields.get("description", "").strip():
                errors.append("SKILL.md needs a nonempty description")
            if not re.search(r"[A-Za-z]{3,}", fields.get("description", "")):
                errors.append("SKILL.md needs an English description")
            if not body.strip():
                errors.append("SKILL.md has no instructions")
        except (ValueError, UnicodeError) as exc:
            errors.append(str(exc))

    files = source_files(root)
    for path in files:
        relative = path.relative_to(root).as_posix()
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"source files must not be symlinks or escape the repository: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"public source must be UTF-8 text: {relative}")
            continue
        if path.suffix in {".md", ".yaml", ".yml"} or path.name == "LICENSE":
            for pattern, description in PRIVATE_PATTERNS:
                if re.search(pattern, text, flags=re.IGNORECASE):
                    errors.append(f"{relative}: {description}")
        if path.suffix == ".md":
            visible = without_fenced_code(text)
            targets = [match.group(1) for match in LINK_RE.finditer(visible)]
            targets.extend(match.group(1) for match in DEFINITION_RE.finditer(visible))
            if path.is_relative_to(skill):
                targets.extend(re.findall(r"`((?:\.?\.?/)*references/[^`\n]+\.md)`", visible))
            for raw in targets:
                target = local_target(path, raw)
                if target is None:
                    continue
                if not target.is_relative_to(root):
                    errors.append(f"{relative}: link escapes repository: {link_target(raw)}")
                elif path.is_relative_to(skill) and not target.is_relative_to(skill):
                    errors.append(f"{relative}: skill link is not self-contained: {link_target(raw)}")
                elif not target.exists():
                    # The generated prompt is intentionally optional before the first build.
                    if target != root / "docs/portable-prompt.md" or require_prompt:
                        errors.append(f"{relative}: broken local link: {link_target(raw)}")
        if path.suffix == ".py":
            try:
                tree = ast.parse(text, filename=relative)
            except SyntaxError as exc:
                errors.append(f"{relative}: {exc}")
                continue
            for node in ast.walk(tree):
                modules = []
                if isinstance(node, ast.Import):
                    modules = [alias.name.split(".")[0] for alias in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    modules = [node.module.split(".")[0]]
                for module in modules:
                    if module not in sys.stdlib_module_names and module != "validate":
                        errors.append(f"{relative}: non-stdlib import: {module}")
    if skill.exists():
        for path in skill.rglob("*"):
            if path.is_symlink():
                errors.append(f"skill must not contain symlinks: {path.relative_to(root)}")
            elif path.is_file() and path.suffix not in {".md", ".yaml", ".yml", ".json", ".txt"}:
                errors.append(f"unexpected runtime or binary file in static skill: {path.relative_to(root)}")
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--require-prompt", action="store_true", help="also require the generated portable prompt")
    args = parser.parse_args()
    errors = validate(args.root, require_prompt=args.require_prompt)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    references = list((args.root / SKILL_REL / "references").rglob("*.md"))
    print(f"Validated {len(source_files(args.root))} public source files and {len(references)} skill references.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
