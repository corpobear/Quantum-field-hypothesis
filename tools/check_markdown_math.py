#!/usr/bin/env python3
"""
Check Markdown math blocks across the repository.

This checker accepts both GitHub-supported display-math styles:
  - fenced math blocks: ```math ... ```
  - dollar display blocks: $$ ... $$

It reports:
  - unclosed Markdown code fences
  - unclosed display math blocks using $$ delimiters

Usage:
  python tools/check_markdown_math.py --check
  python tools/check_markdown_math.py --fix

The --fix mode is intentionally conservative. It currently normalizes nothing;
it exists so workflows can call the same interface without rewriting valid math.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".git",
    ".github",
    "node_modules",
    ".venv",
    "venv",
    "__pycache__",
}


@dataclass
class FileReport:
    path: Path
    unclosed_code_fence_line: int | None = None
    unclosed_display_math_line: int | None = None
    changed: bool = False

    @property
    def has_error(self) -> bool:
        return self.unclosed_code_fence_line is not None or self.unclosed_display_math_line is not None


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def is_fence_start(stripped: str) -> bool:
    return stripped.startswith("```") or stripped.startswith("~~~")


def fence_marker(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def check_file(path: Path) -> FileReport:
    lines = path.read_text(encoding="utf-8").splitlines()
    report = FileReport(path=path)

    in_code_fence = False
    code_fence_marker = ""
    code_fence_line: int | None = None

    in_display_math = False
    display_math_line: int | None = None

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        if in_code_fence:
            if stripped == code_fence_marker:
                in_code_fence = False
                code_fence_marker = ""
                code_fence_line = None
            continue

        if is_fence_start(stripped):
            in_code_fence = True
            code_fence_marker = fence_marker(stripped)
            code_fence_line = idx
            continue

        if stripped == "$$":
            if in_display_math:
                in_display_math = False
                display_math_line = None
            else:
                in_display_math = True
                display_math_line = idx
            continue

    if in_code_fence:
        report.unclosed_code_fence_line = code_fence_line
    if in_display_math:
        report.unclosed_display_math_line = display_math_line

    return report


def print_report(reports: list[FileReport], root: Path) -> None:
    errors = [r for r in reports if r.has_error]
    changed = [r for r in reports if r.changed]

    print(f"Scanned Markdown files: {len(reports)}")
    print(f"Files changed: {len(changed)}")
    print(f"Files with unclosed blocks: {len(errors)}")
    print()

    if errors:
        print("Errors:")
        for r in errors:
            rel = r.path.relative_to(root)
            if r.unclosed_code_fence_line is not None:
                print(f"  {rel}: unclosed code fence opened at line {r.unclosed_code_fence_line}")
            if r.unclosed_display_math_line is not None:
                print(f"  {rel}: unclosed display math block opened at line {r.unclosed_display_math_line}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Check Markdown math and fences")
    mode.add_argument("--fix", action="store_true", help="Conservative no-op fix mode; check only")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    root = args.root.resolve()
    reports = [check_file(path) for path in iter_markdown_files(root)]
    print_report(reports, root)

    if any(r.has_error for r in reports):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
