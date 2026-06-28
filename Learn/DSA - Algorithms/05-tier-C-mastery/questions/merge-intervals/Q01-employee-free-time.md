# Employee Free Time  ·  LeetCode #759

**Pattern:** Merge Intervals
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Common free gaps across schedules → flatten, sort, find gaps**

---

## Problem

Given each employee's sorted busy intervals, return the common free time intervals.

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
def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    intervals = sorted([iv for emp in schedule for iv in emp], key=lambda x: x[0])
    res = []
    end = intervals[0][1]
    for s, e in intervals[1:]:
        if s > end:
            res.append([end, s])                 # gap = free time
        end = max(end, e)
    return res
```

**Complexity:** Time O(N log N), Space O(N).

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
- Related questions: `merge-intervals`, `meeting-rooms-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
