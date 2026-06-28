# Maximum Subarray (Kadane)  ·  LeetCode #53

**Pattern:** Dynamic Programming
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Max contiguous sum → extend or restart running sum**

---

## Problem

Find the contiguous subarray with the largest sum and return that sum.

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

At each index, the best subarray ending here either extends the previous or starts fresh — Kadane's DP.

---

## Solution (Python)

```python
def max_sub_array(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
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

- Pattern sheet: [Dynamic Programming](../../../01-patterns/dynamic-programming.md)
- Related questions: `maximum-product-subarray`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
