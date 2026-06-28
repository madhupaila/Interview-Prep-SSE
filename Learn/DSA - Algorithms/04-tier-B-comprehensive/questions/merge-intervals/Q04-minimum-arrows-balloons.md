# Minimum Number of Arrows to Burst Balloons  ·  LeetCode #452

**Pattern:** Merge Intervals
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Min points to stab all intervals → greedy by end**

---

## Problem

Return the minimum number of arrows to burst all balloons (intervals).

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
def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    for s, e in points[1:]:
        if s > end:
            arrows += 1
            end = e
    return arrows
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
- Related questions: `non-overlapping-intervals`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
