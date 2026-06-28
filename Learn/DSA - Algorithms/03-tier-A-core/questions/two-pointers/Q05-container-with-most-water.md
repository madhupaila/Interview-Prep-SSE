# Container With Most Water  ·  LeetCode #11

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Max area between two lines → ends inward, move the shorter**

---

## Problem

Given heights, find two lines forming a container holding the most water.

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

Width shrinks each step, so we only gain by increasing the limiting (shorter) height — move that pointer.

---

## Solution (Python)

```python
def max_area(height: list[int]) -> int:
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1                          # moving the shorter may help
        else:
            hi -= 1
    return best
```

**Complexity:** Time O(N), Space O(1).

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

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `trapping-rain-water`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
