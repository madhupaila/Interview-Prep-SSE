# Find the Index of First Occurrence (KMP)  ·  LeetCode #28

**Pattern:** Strings
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Substring search in O(N+M) → KMP failure function**

---

## Problem

Return the index of the first occurrence of `needle` in `haystack`, or -1.

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

Avoid re-scanning by precomputing the longest proper prefix-suffix (LPS) so mismatches jump instead of restart.

---

## Solution (Python)

```python
def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    lps = [0] * len(needle)
    k = 0
    for i in range(1, len(needle)):
        while k and needle[i] != needle[k]:
            k = lps[k - 1]
        if needle[i] == needle[k]:
            k += 1
        lps[i] = k
    k = 0
    for i, ch in enumerate(haystack):
        while k and ch != needle[k]:
            k = lps[k - 1]
        if ch == needle[k]:
            k += 1
        if k == len(needle):
            return i - k + 1
    return -1
```

**Complexity:** Time O(N+M), Space O(M).

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
- Related questions: `repeated-substring-pattern`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
