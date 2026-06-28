# Non-overlapping Intervals  ·  LeetCode #435

**Pattern:** Merge Intervals
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Min removals to remove overlaps → greedy by earliest end**

---

## Problem

Return the minimum number of intervals to remove so the rest don't overlap.

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
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])           # earliest end first
    end = float('-inf')
    keep = 0
    for s, e in intervals:
        if s >= end:
            keep += 1
            end = e
    return len(intervals) - keep
```

**Complexity:** Time O(N log N), Space O(1).

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
- Related questions: `merge-intervals`, `minimum-arrows-balloons`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
