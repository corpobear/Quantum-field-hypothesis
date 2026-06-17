#!/usr/bin/env python3
"""
Check and optionally fix Markdown math blocks across the repository.

Problems this catches:
  - unclosed Markdown code fences
  - unclosed display math blocks using $$ delimiters
  - fenced ```math blocks that may display as annotation/code instead of rendered math

Fix behavior:
  - converts fenced ```math blocks into GitHub-friendly $$ display math blocks
  - reports genuinely unclosed blocks without trying to guess the repair

Usage:
  python tools/check_markdown_math.py --check
  python tools/check_markdown_math.py --fix
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
    converted_math_fences: int = 0
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


def is_math_fence_start(stripped: str) -> bool:
    return stripped.startswith("```math") or stripped.startswith("~~~math")


def check_or_fix_file(path: Path, fix: bool) -> FileReport:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    out: list[str] = []

    report = FileReport(path=path)

    in_code_fence = False
    code_fence_marker = ""
    code_fence_line: int | None = None
    in_math_fence_to_convert = False

    in_display_math = False
    display_math_line: int | None = None

    for idx, line in enumerate(lines, start=1):
        newline = "\n" if line.endswith("\n") else ""
        body = line[:-1] if newline else line
        stripped = body.strip()

        if in_math_fence_to_convert:
            if stripped == code_fence_marker:
                out.append("$$" + newline)
                in_math_fence_to_convert = False
                in_code_fence = False
                code_fence_marker = ""
                code_fence_line = None
            else:
                out.append(line)
            continue

        if in_code_fence:
            out.append(line)
            if stripped == code_fence_marker:
                in_code_fence = False
                code_fence_marker = ""
                code_fence_line = None
            continue

        if is_math_fence_start(stripped):
            report.converted_math_fences += 1
            if fix:
                out.append("$$" + newline)
                in_math_fence_to_convert = True
                in_code_fence = True
                code_fence_marker = fence_marker(stripped)
                code_fence_line = idx
            else:
                out.append(line)
                in_code_fence = True
                code_fence_marker = fence_marker(stripped)
                code_fence_line = idx
            continue

        if is_fence_start(stripped):
            out.append(line)
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
            out.append(line)
            continue

        out.append(line)

    if in_code_fence:
        report.unclosed_code_fence_line = code_fence_line
    if in_display_math:
        report.unclosed_display_math_line = display_math_line

    new_text = "".join(out)
    if fix and new_text != original:
        path.write_text(new_text, encoding="utf-8")
        report.changed = True

    return report


def print_report(reports: list[FileReport], root: Path) -> None:
    converted = [r for r in reports if r.converted_math_fences]
    changed = [r for r in reports if r.changed]
    errors = [r for r in reports if r.has_error]

    print(f"Scanned Markdown files: {len(reports)}")
    print(f"Files with fenced math blocks: {len(converted)}")
    print(f"Files changed: {len(changed)}")
    print(f"Files with unclosed blocks: {len(errors)}")
    print()

    if converted:
        print("Fenced math blocks detected/converted:")
        for r in converted:
            rel = r.path.relative_to(root)
            print(f"  {rel}: {r.converted_math_fences}")
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
    mode.add_argument("--check", action="store_true", help="Check only; do not modify files")
    mode.add_argument("--fix", action="store_true", help="Convert fenced math blocks to $$ display math")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    args = parser.parse_args()

    root = args.root.resolve()
    reports = [check_or_fix_file(path, fix=args.fix) for path in iter_markdown_files(root)]
    print_report(reports, root)

    has_errors = any(r.has_error for r in reports)
    has_fenced_math = any(r.converted_math_fences for r in reports)

    if args.check and (has_errors or has_fenced_math):
        return 1

    # In fix mode, return success after safe conversions are written. Any
    # remaining unclosed block is still reported and should be caught by a
    # follow-up --check run.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
