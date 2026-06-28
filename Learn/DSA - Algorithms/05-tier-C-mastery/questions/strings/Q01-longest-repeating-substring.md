# Repeated DNA Sequences  ·  LeetCode #187

**Pattern:** Strings
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Find length-10 substrings appearing >1 → rolling hashset of windows**

---

## Problem

Return all 10-letter sequences occurring more than once in a DNA string.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

_See solution below._

---

## Pattern Identification

Cue maps to **Strings** — see [pattern sheet](../../../02-data-structures/strings.md).

---

## Solution (Python)

```python
def find_repeated_dna_sequences(s: str) -> list[str]:
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        chunk = s[i:i + 10]
        if chunk in seen:
            repeated.add(chunk)
        seen.add(chunk)
    return list(repeated)
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Empty input
- Single element
- All duplicates / negatives

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Strings](../../../02-data-structures/strings.md)
- Related questions: `implement-strstr-kmp`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
