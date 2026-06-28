# Wiggle Sort II  ·  LeetCode #324

**Pattern:** Two Pointers
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Arrange nums[0]<nums[1]>nums[2]... → sort + interleave halves**

---

## Problem

Reorder so `nums[0] < nums[1] > nums[2] < ...`.

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
def wiggle_sort(nums: list[int]) -> None:
    s = sorted(nums)
    n = len(nums)
    mid = (n + 1) // 2
    small = s[:mid][::-1]                          # smaller half, reversed
    large = s[mid:][::-1]                          # larger half, reversed
    nums[::2] = small
    nums[1::2] = large
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

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `sort-colors`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
