# Koko Eating Bananas  ·  LeetCode #875

**Pattern:** Binary Search
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Minimize an eating speed that fits in h hours → binary search on the answer**

---

## Problem

Find the minimum integer eating speed so all piles are eaten within `h` hours.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Linear scan speed | O(maxPile·N) | O(1) | too slow |
| Binary search on answer | O(N log maxPile) | O(1) | feasible(speed) monotonic |

---

## Pattern Identification

feasible(speed) is monotonic (faster speed never needs more hours) → binary search the smallest feasible speed.

---

## Solution (Python)

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(speed):
        return sum(math.ceil(p / speed) for p in piles)
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Complexity:** Time O(N log maxPile), Space O(1).

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
- Related questions: `capacity-to-ship-packages`, `split-array-largest-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
