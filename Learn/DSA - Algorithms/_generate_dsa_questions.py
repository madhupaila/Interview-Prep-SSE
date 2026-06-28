#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate DSA question markdown files from per-pattern data modules.

Usage:
    python _generate_dsa_questions.py            # generate all questions + indexes
    python _generate_dsa_questions.py --index    # regenerate indexes only

Data modules live in _data/_data_<pattern>.py and each exposes a list QUESTIONS
of dicts. See _data/_schema.py for the dict schema and defaults.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "_data"

TIER_DIRS = {
    "A": "03-tier-A-core",
    "B": "04-tier-B-comprehensive",
    "C": "05-tier-C-mastery",
}
TIER_LABEL = {
    "A": "Tier A — Core",
    "B": "Tier B — Comprehensive",
    "C": "Tier C — Mastery",
}

# pattern slug -> (display name, pattern sheet path relative to TRACK ROOT)
PATTERNS = {
    "arrays-hashing": ("Arrays & Hashing", "01-patterns/00-pattern-master-index.md"),
    "two-pointers": ("Two Pointers", "01-patterns/two-pointers.md"),
    "sliding-window": ("Sliding Window", "01-patterns/sliding-window.md"),
    "prefix-sum": ("Prefix Sum", "01-patterns/prefix-sum.md"),
    "cyclic-sort": ("Cyclic Sort", "01-patterns/cyclic-sort.md"),
    "monotonic-stack": ("Monotonic Stack", "01-patterns/monotonic-stack.md"),
    "binary-search": ("Binary Search", "01-patterns/binary-search.md"),
    "top-k-heap": ("Top-K Heap", "01-patterns/top-k-heap.md"),
    "k-way-merge": ("K-way Merge", "01-patterns/k-way-merge.md"),
    "merge-intervals": ("Merge Intervals", "01-patterns/merge-intervals.md"),
    "fast-slow-pointers": ("Fast & Slow Pointers", "01-patterns/fast-slow-pointers.md"),
    "linked-list-reversal": ("Linked List Reversal", "01-patterns/linked-list-reversal.md"),
    "tree-bfs": ("Tree BFS", "01-patterns/tree-bfs.md"),
    "tree-dfs": ("Tree DFS", "01-patterns/tree-dfs.md"),
    "graph-traversal": ("Graph BFS/DFS", "01-patterns/graph-traversal.md"),
    "topological-sort": ("Topological Sort", "01-patterns/topological-sort.md"),
    "union-find": ("Union-Find", "01-patterns/union-find.md"),
    "backtracking": ("Backtracking", "01-patterns/backtracking.md"),
    "subsets-combinations": ("Subsets & Combinations", "01-patterns/subsets-combinations.md"),
    "dynamic-programming": ("Dynamic Programming", "01-patterns/dynamic-programming.md"),
    "greedy": ("Greedy", "01-patterns/greedy.md"),
    "bit-manipulation": ("Bit Manipulation", "01-patterns/bit-manipulation.md"),
    "trie": ("Trie", "01-patterns/trie.md"),
    "matrix-traversal": ("Matrix Traversal", "01-patterns/matrix-traversal.md"),
    "math": ("Interview Math", "01-patterns/math-tricks.md"),
    "strings": ("Strings", "02-data-structures/strings.md"),
}

# Question files live at <root>/<tier>/questions/<pattern>/Qxx.md → 3 levels deep.
ROOT_PREFIX = "../../../"

REQUIRED = ("slug", "title", "pattern", "tier", "companies", "difficulty",
            "cue", "problem", "solution")


def load_questions() -> list[dict]:
    questions: list[dict] = []
    if not DATA_DIR.exists():
        return questions
    for path in sorted(DATA_DIR.glob("_data_*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for q in getattr(mod, "QUESTIONS", []):
            missing = [k for k in REQUIRED if k not in q]
            if missing:
                raise ValueError(f"{path.name}: {q.get('slug', '?')} missing {missing}")
            questions.append(q)
    return questions


def _approaches_table(approaches) -> str:
    if not approaches:
        return "_See solution below._"
    lines = ["| Approach | Time | Space | Note |", "|----------|------|-------|------|"]
    for a in approaches:
        # a = (name, time, space, note) or (name, time, note)
        if len(a) == 4:
            name, t, s, note = a
        else:
            name, t, note = a
            s = "—"
        lines.append(f"| {name} | {t} | {s} | {note} |")
    return "\n".join(lines)


def _bullets(items) -> str:
    if not items:
        return "_None._"
    return "\n".join(f"- {x}" for x in items)


def _numbered(items) -> str:
    if not items:
        return "_None._"
    return "\n".join(f"{i+1}. {x}" for i, x in enumerate(items))


def render(q: dict, seq: int) -> str:
    pattern = q["pattern"]
    pat_name, pat_sheet_rel = PATTERNS.get(pattern, (pattern.title(), "01-patterns/00-pattern-master-index.md"))
    pat_sheet = ROOT_PREFIX + pat_sheet_rel
    lc = f"  ·  LeetCode #{q['leetcode']}" if q.get("leetcode") else ""
    related = q.get("related", [])
    related_md = ", ".join(f"`{r}`" for r in related) if related else "_See pattern sheet._"

    return f"""# {q['title']}{lc}

**Pattern:** {pat_name}
**Tier:** {q['tier']}  ·  **Difficulty:** {q['difficulty']}
**Companies:** {q['companies']}

---

## Memory Hook (Recognition Cue)

> **{q['cue']}**

---

## Problem

{q['problem']}

---

## Clarifying Questions

{_bullets(q.get('clarify', ['Input size / value ranges?', 'Sorted? duplicates? negatives? empty?', 'Return value vs in-place?']))}

---

## Approaches

{_approaches_table(q.get('approaches'))}

---

## Pattern Identification

{q.get('identify', f'Cue maps to **{pat_name}** — see [pattern sheet]({pat_sheet}).')}

---

## Solution (Python)

```python
{q['solution'].strip()}
```

**Complexity:** Time {q.get('time', 'O(N)')}, Space {q.get('space', 'O(1)')}.

---

## Edge Cases & Pitfalls

{_bullets(q.get('edges', ['Empty input', 'Single element', 'All duplicates / negatives']))}

---

## Follow-Ups

{_numbered(q.get('followups', ['Can you reduce space?', 'How does this scale / handle streaming input?']))}

---

## Related

- Pattern sheet: [{pat_name}]({pat_sheet})
- Related questions: {related_md}
- [Pattern Master Index]({ROOT_PREFIX}01-patterns/00-pattern-master-index.md) · [Decision Tree]({ROOT_PREFIX}01-patterns/01-pattern-recognition-decision-tree.md)
"""


def out_path(q: dict, seq: int) -> Path:
    tier_dir = TIER_DIRS[q["tier"]]
    return ROOT / tier_dir / "questions" / q["pattern"] / f"Q{seq:02d}-{q['slug']}.md"


def clean_question_dirs() -> int:
    """Remove previously generated Qxx-*.md files to avoid orphans on rename/recount."""
    removed = 0
    for tier_dir in TIER_DIRS.values():
        qroot = ROOT / tier_dir / "questions"
        if qroot.exists():
            for f in qroot.rglob("Q*.md"):
                f.unlink()
                removed += 1
    return removed


def write_questions(questions: list[dict]) -> list[tuple[Path, dict]]:
    # sequence per (tier, pattern)
    seq_counter: dict[tuple[str, str], int] = defaultdict(int)
    written = []
    for q in questions:
        key = (q["tier"], q["pattern"])
        seq_counter[key] += 1
        seq = seq_counter[key]
        path = out_path(q, seq)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render(q, seq), encoding="utf-8")
        written.append((path, q))
    return written


def write_tier_readmes(questions: list[dict]) -> None:
    for tier, tier_dir in TIER_DIRS.items():
        tqs = [q for q in questions if q["tier"] == tier]
        by_pat: dict[str, list[dict]] = defaultdict(list)
        for q in tqs:
            by_pat[q["pattern"]].append(q)
        lines = [
            f"# {TIER_LABEL[tier]} ({len(tqs)} questions)",
            "",
            f"Questions organized by pattern. Study a pattern's [master sheet](../01-patterns/00-pattern-master-index.md) first, then solve.",
            "",
            "| Pattern | Count | Questions |",
            "|---------|-------|-----------|",
        ]
        seq_counter: dict[tuple[str, str], int] = defaultdict(int)
        # recompute seq to build links consistent with write_questions order
        order_seq: dict[int, int] = {}
        for q in questions:
            if q["tier"] != tier:
                # still need global seq alignment per (tier,pattern); skip others
                pass
        # simpler: recompute per pattern in file order
        pat_seq: dict[str, int] = defaultdict(int)
        links_by_pat: dict[str, list[str]] = defaultdict(list)
        for q in questions:
            if q["tier"] != tier:
                continue
            pat_seq[q["pattern"]] += 1
            s = pat_seq[q["pattern"]]
            links_by_pat[q["pattern"]].append(
                f"[{q['title']}](questions/{q['pattern']}/Q{s:02d}-{q['slug']}.md)"
            )
        for pat in PATTERNS:
            if pat in links_by_pat:
                name = PATTERNS[pat][0]
                qs = links_by_pat[pat]
                lines.append(f"| {name} | {len(qs)} | {' · '.join(qs)} |")
        (ROOT / tier_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_company_index(questions: list[dict]) -> None:
    by_company: dict[str, list[dict]] = defaultdict(list)
    for q in questions:
        for c in [x.strip() for x in q["companies"].split(",")]:
            if c:
                by_company[c].append(q)
    pat_seq: dict[tuple[str, str], int] = defaultdict(int)
    seq_lookup: dict[int, int] = {}
    for i, q in enumerate(questions):
        pat_seq[(q["tier"], q["pattern"])] += 1
        seq_lookup[i] = pat_seq[(q["tier"], q["pattern"])]

    def link(q, idx):
        s = seq_lookup[idx]
        return f"[{q['title']}]({TIER_DIRS[q['tier']]}/questions/{q['pattern']}/Q{s:02d}-{q['slug']}.md)"

    idx_of = {id(q): i for i, q in enumerate(questions)}
    lines = [
        "# Company × Question Index",
        "",
        "Questions tagged by company. Use before a specific company's loop.",
        "",
    ]
    for company in sorted(by_company, key=lambda c: (-len(by_company[c]), c)):
        qs = by_company[company]
        if len(qs) < 2:
            continue
        lines.append(f"## {company} ({len(qs)})")
        lines.append("")
        lines.append("| Question | Pattern | Tier | Difficulty |")
        lines.append("|----------|---------|------|------------|")
        for q in qs:
            i = idx_of[id(q)]
            pat_name = PATTERNS.get(q["pattern"], (q["pattern"],))[0]
            lines.append(f"| {link(q, i)} | {pat_name} | {q['tier']} | {q['difficulty']} |")
        lines.append("")
    (ROOT / "06-company-question-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_summary(questions: list[dict]) -> None:
    by_tier = defaultdict(int)
    by_pat = defaultdict(int)
    for q in questions:
        by_tier[q["tier"]] += 1
        by_pat[q["pattern"]] += 1
    print(f"Total questions: {len(questions)}")
    for t in ("A", "B", "C"):
        print(f"  Tier {t}: {by_tier[t]}")
    print("By pattern:")
    for pat in PATTERNS:
        if by_pat[pat]:
            print(f"  {pat}: {by_pat[pat]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", action="store_true", help="Regenerate indexes only")
    args = ap.parse_args()

    questions = load_questions()
    if not questions:
        print("No questions found in _data/. Add _data_<pattern>.py modules.")
        return

    if not args.index:
        removed = clean_question_dirs()
        if removed:
            print(f"Cleaned {removed} stale question files.")
        write_questions(questions)
        print(f"Wrote {len(questions)} question files.")

    write_tier_readmes(questions)
    write_company_index(questions)
    print_summary(questions)


if __name__ == "__main__":
    main()
