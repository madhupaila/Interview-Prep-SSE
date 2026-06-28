# Search in Rotated Sorted Array  ·  LeetCode #33

**Pattern:** Binary Search
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Rotated sorted + find target → identify the sorted half each step**

---

## Problem

Search `target` in a rotated ascending array of distinct values; return index or -1.

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

Cue maps to **Binary Search** — see [pattern sheet](../../../01-patterns/binary-search.md).

---

## Solution (Python)

```python
def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:               # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                   # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Complexity:** Time O(log N), Space O(1).

---

## Edge Cases & Pitfalls

- No rotation
- Target absent
- Duplicates → O(N) worst (variant II)

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `find-min-rotated-sorted`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
