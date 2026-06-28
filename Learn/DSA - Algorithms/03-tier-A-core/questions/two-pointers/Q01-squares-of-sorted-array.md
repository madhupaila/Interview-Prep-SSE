# Squares of a Sorted Array  ·  LeetCode #977

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Sorted squares → two pointers from both ends (largest first)**

---

## Problem

Return squares of a sorted array, sorted ascending.

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
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    lo, hi = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[lo]) > abs(nums[hi]):
            res[i] = nums[lo] ** 2
            lo += 1
        else:
            res[i] = nums[hi] ** 2
            hi -= 1
    return res
```

**Complexity:** Time O(N), Space O(N).

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
- Related questions: `merge-sorted-array`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
