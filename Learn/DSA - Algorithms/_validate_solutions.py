#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate that every question's solution string is syntactically valid Python.

Usage: python _validate_solutions.py
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "_data"


def main() -> None:
    total = 0
    errors = 0
    slugs: dict[tuple[str, str], str] = {}
    for path in sorted(DATA_DIR.glob("_data_*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for q in getattr(mod, "QUESTIONS", []):
            total += 1
            key = (q.get("tier"), q.get("slug"))
            if key in slugs:
                print(f"DUPLICATE slug+tier {key} in {path.name} and {slugs[key]}")
                errors += 1
            slugs[key] = path.name
            try:
                compile(q["solution"], f"{q.get('slug', '?')}.py", "exec")
            except SyntaxError as e:
                errors += 1
                print(f"SYNTAX ERROR in {path.name} :: {q.get('slug')} -> {e}")
    print(f"Checked {total} solutions, {errors} error(s).")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
