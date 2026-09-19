"""Regression checks for portable prompts and public archive boundaries."""

from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY / "scripts"))

from package import RUNTIME_REFERENCES, portable_prompt  # noqa: E402
from validate import local_target, LINK_RE, validate  # noqa: E402


class PackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.skill = self.root / "skills/chtets"
        self.write("README.md", "# Fixture\n\n[Compact](docs/portable-prompt.md)\n"
                   "[Extended](docs/portable-prompt-extended.md)\n[Sizes](docs/context-size.json)\n")
        for name in ("LICENSE", "CHANGELOG.md", "CONTRIBUTING.md", ".gitignore"):
            self.write(name, "Fixture public text\n")
        self.write(".github/workflows/check.yml", "name: Fixture\n")
        self.write("skills/chtets/agents/openai.yaml", "interface:\n  display_name: Chtets\n")
        self.write("docs/reference.md", "# Documentation\n")
        self.write("examples/example.md", "# Example\n")
        for name in ("package.py", "validate.py"):
            destination = self.root / "scripts" / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / "scripts" / name, destination)
        for name in RUNTIME_REFERENCES:
            self.write(f"skills/chtets/references/{name}", f"# {name}\n\nRuntime guidance {name}.\n")
        self.write("skills/chtets/references/foundations.md", "# Foundations\n\nOFFLINE_RESEARCH_SENTINEL\n")
        self.write("skills/chtets/SKILL.md", "---\nname: chtets\ndescription: Write accurate prose.\n---\n"
                   "# Chtets\n\nPreserve facts and commitments.\n\n## Read selectively\n\n"
                   "[Composition](references/composition.md)\n[Research](references/foundations.md)\n\n"
                   "## Deliver\n\nDo not claim verification you did not perform.\n")

    def write(self, relative: str, content: str) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")

    def build(self) -> None:
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts/package.py"), "--root", str(self.root)],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_compact_keeps_core_without_local_reference_dependencies(self) -> None:
        prompt = portable_prompt(self.root)
        self.assertIn("Preserve facts and commitments.", prompt)
        self.assertIn("Do not claim verification you did not perform.", prompt)
        self.assertNotIn("references/", prompt)
        self.assertNotIn("OFFLINE_RESEARCH_SENTINEL", prompt)
        self.assertFalse(any(local_target(self.root / "docs/portable-prompt.md", match.group(1))
                             for match in LINK_RE.finditer(prompt)))

    def test_legacy_routing_preserves_task_modes(self) -> None:
        self.write("skills/chtets/SKILL.md", "---\nname: chtets\ndescription: Write accurate prose.\n---\n"
                   "# Chtets\n\n## Match the work to the request\n\n"
                   "**Proofread:** preserve the speaker's words and sequence.\n\n"
                   "Load only the references needed:\n\n| Situation | Reference |\n| --- | --- |\n"
                   "| Flow | [Composition](references/composition.md) |\n\n"
                   "Apply the final checks regardless.\n\n## Deliver\n\nPreserve conditions.\n")
        prompt = portable_prompt(self.root)
        self.assertIn("preserve the speaker's words and sequence", prompt)
        self.assertIn("Apply the final checks regardless.", prompt)
        self.assertIn("Preserve conditions.", prompt)
        self.assertNotIn("references/", prompt)

    def test_extended_resolves_runtime_links_and_excludes_offline_research(self) -> None:
        self.write("skills/chtets/references/review.md", "# Review\n\n"
                   "Use [composition](composition.md) for a broken connection.\n"
                   "```text\n# Preserve this example heading\n```\n")
        prompt = portable_prompt(self.root, extended=True)
        for name in RUNTIME_REFERENCES:
            self.assertIn(f"## Reference: references/{name}", prompt)
        self.assertIn('composition (see "Reference: references/composition.md")', prompt)
        self.assertNotIn("OFFLINE_RESEARCH_SENTINEL", prompt)
        self.assertIn("```text\n# Preserve this example heading\n```", prompt)
        self.assertFalse(any(local_target(self.root / "docs/portable-prompt-extended.md", match.group(1))
                             for match in LINK_RE.finditer(prompt)))

    def test_unhandled_core_dependency_fails_instead_of_losing_instructions(self) -> None:
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nRead [extra](references/review.md).\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unavailable local reference"):
            portable_prompt(self.root)

    def test_archives_separate_research_and_are_reproducible(self) -> None:
        self.write("research/corpus.jsonl", '{"id":"source-1"}\n')
        self.write("research/methodology.md", "# Original research notes\n")
        self.write("evaluations/cases.jsonl", '{"id":"case-1"}\n')
        self.write("research/downloaded.pdf", "Excluded downloaded paper")
        self.write("research/scratch.csv", "Excluded scratch table")
        self.write("scratch/private.json", '{"private":true}\n')
        self.build()
        install = self.root / "dist/chtets-v1.1.0.zip"
        source = self.root / "dist/chtets-source-v1.1.0.zip"
        with zipfile.ZipFile(install) as archive:
            names = set(archive.namelist())
            self.assertIn("chtets/SKILL.md", names)
            self.assertIn("chtets/LICENSE", names)
            self.assertFalse(any("research/" in name or "evaluations/" in name or "docs/" in name for name in names))
        with zipfile.ZipFile(source) as archive:
            names = set(archive.namelist())
            self.assertIn("chtets-source/research/corpus.jsonl", names)
            self.assertIn("chtets-source/evaluations/cases.jsonl", names)
            self.assertIn("chtets-source/docs/portable-prompt-extended.md", names)
            self.assertFalse(any(name.endswith((".pdf", ".csv")) or "/scratch/" in name for name in names))
        before = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in (install, source)}
        # Checkout line endings must not affect release bytes either.
        for path in self.skill.rglob("*.md"):
            path.write_bytes(path.read_bytes().replace(b"\n", b"\r\n"))
        self.build()
        after = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in (install, source)}
        self.assertEqual(before, after)
        self.assertEqual(validate(self.root, require_prompt=True), [])

    def test_skill_link_outside_installation_still_fails(self) -> None:
        self.write("skills/chtets/references/review.md", "# Review\n\n[Local docs](../../../docs/reference.md)\n")
        errors = validate(self.root)
        self.assertTrue(any("skill link is not self-contained" in error for error in errors), errors)

    def test_generated_prompt_local_dependency_is_rejected(self) -> None:
        self.build()
        prompt = self.root / "docs/portable-prompt.md"
        prompt.write_text(prompt.read_text(encoding="utf-8") + "\n[Read more](reference.md)\n", encoding="utf-8")
        self.assertTrue(any("standalone prompt depends on a local file" in error
                            for error in validate(self.root, require_prompt=True)))


if __name__ == "__main__":
    unittest.main()
