# First Bad Version  ·  LeetCode #278

**Pattern:** Binary Search
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **First True in monotone predicate → binary search boundary**

---

## Problem

Find the first bad version given an `isBadVersion(v)` API.

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

Cue maps to **Binary Search** — see [pattern sheet](../../../01-patterns/binary-search.md).

---

## Solution (Python)

```python
def is_bad_version(v: int) -> bool:
    ...                                            # provided API stub

def first_bad_version(n: int) -> int:
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad_version(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Complexity:** Time O(log N), Space O(1).

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

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `search-insert-position`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
