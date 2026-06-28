# Merge Intervals  ·  LeetCode #56

**Pattern:** Merge Intervals
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Combine overlapping ranges → sort by start, sweep**

---

## Problem

Merge all overlapping intervals.

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
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

**Complexity:** Time O(N log N), Space O(N).

---

## Edge Cases & Pitfalls

- Single interval
- Touching intervals [1,2],[2,3] merge
- Already sorted

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Merge Intervals](../../../01-patterns/merge-intervals.md)
- Related questions: `insert-interval`, `non-overlapping-intervals`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
