# Palindromic Substrings  ·  LeetCode #647

**Pattern:** Strings
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Count palindromic substrings → expand around each center**

---

## Problem

Count the number of palindromic substrings in `s`.

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
def count_substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1; r += 1
    return count
```

**Complexity:** Time O(N^2), Space O(1).

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
- Related questions: `longest-palindromic-substring-str`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
