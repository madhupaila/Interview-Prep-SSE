#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject Case Study link blocks into all HLD and LLD question markdown files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEARN = ROOT.parent
HLD_ROOT = LEARN / "System Design - High Level Design"
LLD_ROOT = LEARN / "System Design - Low Level Design"

sys.path.insert(0, str(ROOT))
from _generate_case_studies import (  # noqa: E402
    _extract_meta,
    discover_hld,
    discover_lld,
    out_file,
)
from _case_study_overrides import get_override  # noqa: E402
from _paired_topics_registry import pair_by_hld, pair_by_lld, pair_doc_name  # noqa: E402

MARKER = "## Case Study"


def _rel(from_path: Path, to_path: Path) -> str:
    import os
    return os.path.relpath(to_path, from_path.parent).replace("\\", "/")


def _business_blurb(override: dict, title: str) -> str:
    ctx = override.get("business_context", "")
    if ctx:
        # first paragraph after industry analog line
        lines = [l.strip() for l in ctx.split("\n") if l.strip() and not l.startswith("**Industry")]
        if lines:
            return lines[0][:300]
    analog = override.get("industry_analog", title)
    return f"Real-world context modeled after {analog}. Read the full case study for requirements, constraints, ADRs, and ops."


def _constraints_blurb(override: dict) -> str:
    rows = override.get("constraints")
    if rows:
        return ", ".join(r[0] for r in rows[:4])
    return "budget, timeline, team size, tech stack"


def build_block(item: dict, question_path: Path) -> str:
    out = out_file(item)
    cs_name = out.name
    cs_rel = _rel(question_path, out)
    override = get_override(item["slug"], item["kind"], _extract_meta(question_path.read_text(encoding="utf-8")).get("title", item["slug"]))

    pair_line = ""
    if item["kind"] == "hld":
        pair = pair_by_hld(item["track_key"], item["num"])
    else:
        pair = pair_by_lld(item["track_key"], item["num"])
    if pair:
        pair_path = ROOT / "paired" / pair_doc_name(pair)
        pair_line = f"> **End-to-end pair:** [{pair['title']}]({_rel(question_path, pair_path)})\n"

    impl_line = ""
    if item["kind"] == "lld":
        impl_line = "> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)\n"
    else:
        impl_line = "> **Read order:** Case Study → this question (timed mock)\n"

    blurb = _business_blurb(override, item["slug"])
    constraints = _constraints_blurb(override)

    return f"""{MARKER}

> **Full case study:** [{cs_name}]({cs_rel})
{pair_line}{impl_line}
**Business context:** {blurb}

**Key constraints:** {constraints}

---
"""


def inject(path: Path, item: dict) -> bool:
    text = path.read_text(encoding="utf-8")
    block = build_block(item, path)

    if MARKER in text:
        # replace existing case study section
        new_text = re.sub(
            rf"{re.escape(MARKER)}.*?(?=\n---\n)",
            block.rstrip("\n"),
            text,
            count=1,
            flags=re.S,
        )
    else:
        # insert after difficulty line / first ---
        m = re.search(r"(\*\*Difficulty:\*\*.+?\n\n---\n)", text)
        if m:
            new_text = text[: m.end()] + "\n" + block + text[m.end() :]
        else:
            m2 = re.search(r"(\*\*Difficulty:\*\*.+?\n\n)", text)
            if m2:
                new_text = text[: m2.end()] + block + text[m2.end() :]
            else:
                new_text = block + "\n" + text

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for item in discover_hld():
        if inject(item["question"], item):
            changed += 1
            print(f"Linked HLD {item['question'].name}")
    for item in discover_lld():
        if inject(item["question"], item):
            changed += 1
            print(f"Linked LLD {item['question'].name}")
    print(f"Updated {changed} question files")


if __name__ == "__main__":
    main()
