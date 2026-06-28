# Insert Interval  ·  LeetCode #57

**Pattern:** Merge Intervals
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Insert into sorted non-overlapping → three phases (before/overlap/after)**

---

## Problem

Insert a new interval into a sorted, non-overlapping list and merge if needed.

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
def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    res = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:    # before
        res.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:   # overlap → merge
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    res.append(new)
    while i < n:                                 # after
        res.append(intervals[i]); i += 1
    return res
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

- Pattern sheet: [Merge Intervals](../../../01-patterns/merge-intervals.md)
- Related questions: `merge-intervals`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
