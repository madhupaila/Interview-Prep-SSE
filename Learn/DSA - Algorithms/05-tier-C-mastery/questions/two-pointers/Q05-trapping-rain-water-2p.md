# Trapping Rain Water (Two Pointers)  ·  LeetCode #42

**Pattern:** Two Pointers
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Goldman Sachs

---

## Memory Hook (Recognition Cue)

> **Water above bars → two pointers tracking left/right max**

---

## Problem

Compute total trapped rainwater given elevation heights.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| DP arrays | O(N) | O(N) | prefix max L/R |
| Two pointers | O(N) | O(1) | move side with smaller max |

---

## Pattern Identification

Water at a position depends on min(maxLeft, maxRight). Two pointers let the smaller side commit safely.

---

## Solution (Python)

```python
def trap(height: list[int]) -> int:
    if not height:
        return 0
    lo, hi = 0, len(height) - 1
    left_max, right_max = height[lo], height[hi]
    water = 0
    while lo < hi:
        if left_max < right_max:
            lo += 1
            left_max = max(left_max, height[lo])
            water += left_max - height[lo]
        else:
            hi -= 1
            right_max = max(right_max, height[hi])
            water += right_max - height[hi]
    return water
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
- Related questions: `container-with-most-water`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
