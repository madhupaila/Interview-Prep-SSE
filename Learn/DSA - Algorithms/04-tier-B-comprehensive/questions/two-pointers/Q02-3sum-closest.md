# 3Sum Closest  ·  LeetCode #16

**Pattern:** Two Pointers
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Closest triplet sum to target → sort + two pointers tracking best diff**

---

## Problem

Return the sum of three integers closest to `target`.

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

Cue maps to **Two Pointers** — see [pattern sheet](../../../01-patterns/two-pointers.md).

---

## Solution (Python)

```python
def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    best = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(s - target) < abs(best - target):
                best = s
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return s
    return best
```

**Complexity:** Time O(N^2), Space O(1).

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
- Related questions: `3sum`, `4sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
