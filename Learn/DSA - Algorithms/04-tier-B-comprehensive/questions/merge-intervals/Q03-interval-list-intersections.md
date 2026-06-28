# Interval List Intersections  ·  LeetCode #986

**Pattern:** Merge Intervals
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Intersect two sorted interval lists → two pointers**

---

## Problem

Return the intersection of two lists of sorted, disjoint intervals.

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

Cue maps to **Merge Intervals** — see [pattern sheet](../../../01-patterns/merge-intervals.md).

---

## Solution (Python)

```python
def interval_intersection(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            res.append([lo, hi])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return res
```

**Complexity:** Time O(M+N), Space O(M+N).

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

- Pattern sheet: [Merge Intervals](../../../01-patterns/merge-intervals.md)
- Related questions: `merge-intervals`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
