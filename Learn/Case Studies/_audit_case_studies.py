#!/usr/bin/env python3
"""Audit case studies against plan quality bar."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from _paired_topics_registry import PAIRED_TOPICS  # noqa: E402

REQUIRED_PARTS = [
    "Part 1", "Part 2", "Part 3", "Part 4", "Part 5", "Part 6",
    "Part 7", "Part 9", "Part 10", "Part 11", "Part 12",
]
GOLD = [
    "paired/CS-PAIR-01-enterprise-rag.md",
    "hld/classic/CS-HLD-C01-url-shortener.md",
    "lld/classic-ood/CS-LLD-O01-parking-lot.md",
]
SCRIPTS = [
    "_generate_case_studies.py",
    "_case_study_overrides.py",
    "_paired_topics_registry.py",
    "_link_case_studies.py",
]


def main() -> None:
    cs_files = sorted(ROOT.rglob("CS-*.md"))
    paired = sorted((ROOT / "paired").glob("CS-PAIR-*.md"))
    issues: list[str] = []
    stats = {
        "individual": len(cs_files) - len(paired),
        "paired": len(paired),
        "total_cs": len(cs_files),
        "lines_min": 10**9,
        "lines_max": 0,
        "lines_sum": 0,
        "missing_parts_files": 0,
        "lt3_adrs": 0,
        "no_constraints_table": 0,
        "no_slo": 0,
        "hld_no_lld_boundary": 0,
        "lld_no_hld_boundary": 0,
        "generic_analog": 0,
        "below_800_lines": 0,
    }

    for f in cs_files:
        text = f.read_text(encoding="utf-8")
        lines = text.count("\n") + 1
        stats["lines_sum"] += lines
        stats["lines_min"] = min(stats["lines_min"], lines)
        stats["lines_max"] = max(stats["lines_max"], lines)
        if lines < 800:
            stats["below_800_lines"] += 1

        missing = [p for p in REQUIRED_PARTS if p not in text]
        if missing:
            stats["missing_parts_files"] += 1
            if len(issues) < 20:
                issues.append(f"{f.name}: missing {missing}")

        adr_count = len(re.findall(r"ADR-\d+", text))
        if adr_count < 3:
            stats["lt3_adrs"] += 1

        if "| Constraint | Detail |" not in text:
            stats["no_constraints_table"] += 1

        if "SLI" not in text and "SLO" not in text:
            stats["no_slo"] += 1

        rel = f.as_posix()
        if "/hld/" in rel and "LLD Boundary" not in text:
            stats["hld_no_lld_boundary"] += 1
        if "/lld/" in rel and "HLD Boundary" not in text and "Scale Projection" not in text:
            stats["lld_no_hld_boundary"] += 1

        if "Leading products in the" in text:
            stats["generic_analog"] += 1

    stats["lines_avg"] = round(stats["lines_sum"] / max(len(cs_files), 1), 1)

    # Question file links
    hld_q = list((ROOT.parent / "System Design - High Level Design").rglob("questions/Q*.md"))
    lld_q = list((ROOT.parent / "System Design - Low Level Design").rglob("questions/Q*.md"))
    hld_linked = sum(1 for f in hld_q if "## Case Study" in f.read_text(encoding="utf-8"))
    lld_linked = sum(1 for f in lld_q if "## Case Study" in f.read_text(encoding="utf-8"))

    idx = (ROOT / "index.md").read_text(encoding="utf-8")
    idx_rows = len(re.findall(r"^\| CS-", idx, re.M))

    print("=== CASE STUDIES AUDIT ===\n")
    print("FILE COUNTS (expected: 219 individual + 20 paired = 239 CS files)")
    print(f"  Individual case studies: {stats['individual']} (expect 219)")
    print(f"  Paired case studies:     {stats['paired']} (expect 20)")
    print(f"  Total CS-*.md:           {stats['total_cs']}")
    print(f"  Index rows:              {idx_rows} (expect ~239)")
    print(f"  Paired registry:         {len(PAIRED_TOPICS)} (expect 20)")
    print()
    print("QUESTION LINKS (expect 105 HLD + 114 LLD = 219)")
    print(f"  HLD questions linked:    {hld_linked}/105")
    print(f"  LLD questions linked:    {lld_linked}/114")
    print()
    print("FRAMEWORK & SCRIPTS")
    print(f"  00-framework files:      {len(list((ROOT/'00-framework').glob('*.md')))} (expect 3)")
    print(f"  README.md:               {(ROOT/'README.md').exists()}")
    print(f"  Gold standards:          {sum(1 for g in GOLD if (ROOT/g).exists())}/3")
    print(f"  Generator scripts:       {sum(1 for s in SCRIPTS if (ROOT/s).exists())}/4")
    print()
    print("LINE DEPTH (plan target: 800-1200 lines)")
    print(f"  Average lines:           {stats['lines_avg']}")
    print(f"  Min / Max:               {stats['lines_min']} / {stats['lines_max']}")
    print(f"  Files below 800 lines:     {stats['below_800_lines']}/{stats['total_cs']}")
    print()
    print("QUALITY BAR CHECKS")
    print(f"  Files missing parts:     {stats['missing_parts_files']}")
    print(f"  Files with <3 ADRs:      {stats['lt3_adrs']}")
    print(f"  No constraints table:    {stats['no_constraints_table']}")
    print(f"  No SLI/SLO:              {stats['no_slo']}")
    print(f"  HLD missing LLD boundary:{stats['hld_no_lld_boundary']}")
    print(f"  LLD missing HLD boundary:{stats['lld_no_hld_boundary']}")
    print(f"  Generic industry analog: {stats['generic_analog']}")
    if issues:
        print("\nSAMPLE ISSUES:")
        for i in issues[:10]:
            print(f"  - {i}")


if __name__ == "__main__":
    main()
