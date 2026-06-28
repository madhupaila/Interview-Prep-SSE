#!/usr/bin/env python3
"""Repair broken relative markdown links across the Learn folder."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote, unquote

LEARN = Path(__file__).resolve().parent
LINK_RE = re.compile(r"(\]\()([^)#]+)(\))")


def all_markdown_files() -> list[Path]:
    return sorted(LEARN.rglob("*.md"))


def build_file_index() -> dict[str, list[Path]]:
    """Map normalized suffixes to absolute paths for fuzzy target lookup."""
    index: dict[str, list[Path]] = {}
    for path in LEARN.rglob("*"):
        if path.is_file():
            rel = path.relative_to(LEARN).as_posix()
            index.setdefault(rel.lower(), []).append(path)
            index.setdefault(path.name.lower(), []).append(path)
            # also index without leading folders for deep paths
            parts = rel.split("/")
            if len(parts) >= 2:
                suffix = "/".join(parts[-2:]).lower()
                index.setdefault(suffix, []).append(path)
            if len(parts) >= 3:
                suffix3 = "/".join(parts[-3:]).lower()
                index.setdefault(suffix3, []).append(path)
    return index


def resolve_target(raw: str, from_file: Path, index: dict[str, list[Path]]) -> Path | None:
    target = unquote(raw.strip())
    if not target or target.startswith(("http://", "https://", "mailto:", "#", "/")):
        return None

    direct = (from_file.parent / target.split("#")[0]).resolve()
    if direct.exists():
        return direct

    # Java impl folders may link to README.md that was never added — fall back to a demo .java file
    if target.endswith("/README.md") or target.endswith("README.md"):
        folder = (from_file.parent / target.replace("README.md", "").rstrip("/")).resolve()
        if folder.is_dir():
            for pattern in ("*Demo.java", "*.java"):
                matches = sorted(folder.glob(pattern))
                if matches:
                    return matches[0]

    # Directory links (trailing slash) — resolve to README.md or first .java inside
    if target.endswith("/"):
        folder = (from_file.parent / target.rstrip("/")).resolve()
        if folder.is_dir():
            readme = folder / "README.md"
            if readme.exists():
                return readme
            for pattern in ("*Demo.java", "*.java"):
                matches = sorted(folder.glob(pattern))
                if matches:
                    return matches[0]

    norm = target.replace("\\", "/").lstrip("./")
    candidates: list[Path] = []

    for key in (norm.lower(), Path(norm).name.lower()):
        candidates.extend(index.get(key, []))

    parts = norm.split("/")
    for n in (3, 2, 1):
        if len(parts) >= n:
            suffix = "/".join(parts[-n:]).lower()
            candidates.extend(index.get(suffix, []))

    # Prefer paths that end with the same suffix as the link
    norm_lower = norm.lower()
    matched = [c for c in candidates if c.relative_to(LEARN).as_posix().lower().endswith(norm_lower)]
    if len(matched) == 1:
        return matched[0]
    if matched:
        # prefer shortest relative path match
        matched.sort(key=lambda p: len(p.relative_to(LEARN).parts))
        return matched[0]

    if len(candidates) == 1:
        return candidates[0]
    return None


def rel_link(from_file: Path, to_file: Path, fragment: str = "") -> str:
    rel = Path(
        __import__("os").path.relpath(to_file, from_file.parent)
    ).as_posix()
    # encode spaces for markdown compatibility
    rel = "/".join(quote(part, safe="@+") for part in rel.split("/"))
    return f"{rel}{fragment}"


def fix_file(path: Path, index: dict[str, list[Path]]) -> int:
    text = path.read_text(encoding="utf-8")
    changes = 0

    def replacer(match: re.Match[str]) -> str:
        nonlocal changes
        prefix, raw, suffix = match.group(1), match.group(2), match.group(3)
        if raw.strip().startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        fragment = ""
        target_part = raw
        if "#" in raw:
            target_part, fragment = raw.split("#", 1)
            fragment = "#" + fragment

        decoded = unquote(target_part.strip())
        current = (path.parent / decoded).resolve()
        if current.exists():
            return match.group(0)

        resolved = resolve_target(raw, path, index)
        if resolved is None:
            return match.group(0)

        new_link = rel_link(path, resolved, fragment)
        old_link = raw
        if old_link != new_link:
            changes += 1
            return f"{prefix}{new_link}{suffix}"
        return match.group(0)

    new_text = LINK_RE.sub(replacer, text)
    if changes:
        path.write_text(new_text, encoding="utf-8")
    return changes


def fix_case_study_lld_paths() -> int:
    """Case studies copied LLD-relative paths; rewrite to reach LLD from Case Studies tree."""
    cs_root = LEARN / "Case Studies"
    lld = "System Design - Low Level Design"
    hld = "System Design - High Level Design"
    replacements = (
        "09-code-implementations/",
        "01-core-concepts/",
        "02-classic-ood/",
        "03-design-patterns/",
        "04-concurrency-lld/",
        "05-genai-llm-lld/",
    )
    total = 0
    for md in cs_root.rglob("*.md"):
        rel_parts = md.relative_to(cs_root).parts[:-1]
        up = len(rel_parts) + 1  # from file dir to Learn/
        prefix = "../" * up
        text = md.read_text(encoding="utf-8")
        new = text
        for segment in replacements:
            wrong = f"../../{segment}"
            right = f"{prefix}{lld}/{segment}"
            new = new.replace(wrong, right)
            # Some links were partially fixed with wrong depth (../../LLD/... instead of ../../../)
            wrong2 = f"../../{lld}/{segment.rstrip('/')}"
            right2 = f"{prefix}{lld}/{segment.rstrip('/')}"
            new = new.replace(wrong2, right2)
            new = new.replace(wrong, right)
        # paired docs sometimes use one-level-up sibling paths
        for track, segment in ((hld, "02-genai-llm-hld/"), (hld, "03-classic-hld/")):
            wrong = f"../{track}/{segment}"
            right = f"{prefix}{track}/{segment}"
            new = new.replace(wrong, right)
        if new != text:
            md.write_text(new, encoding="utf-8")
            total += 1
    return total


def main() -> None:
    cs_fixed = fix_case_study_lld_paths()
    if cs_fixed:
        print(f"Case Studies path prefix fixes: {cs_fixed} files")
    index = build_file_index()
    total = 0
    files_changed = 0
    for md in all_markdown_files():
        n = fix_file(md, index)
        if n:
            files_changed += 1
            total += n
            print(f"  {n:3d} fixes in {md.relative_to(LEARN)}")
    print(f"\nDone: {total} link fixes across {files_changed} files.")


if __name__ == "__main__":
    main()
