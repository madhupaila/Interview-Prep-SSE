# Rotate Array  ·  LeetCode #189

**Pattern:** Two Pointers
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Rotate right by k in place → reverse whole, reverse parts**

---

## Problem

Rotate the array to the right by `k` steps in place.

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
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1; hi -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
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
- Related questions: `rotate-list`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
