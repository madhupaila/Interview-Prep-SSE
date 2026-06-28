# Find Minimum in Rotated Sorted Array  ·  LeetCode #153

**Pattern:** Binary Search
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft, Meta

---

## Memory Hook (Recognition Cue)

> **Rotated sorted → compare mid with right to find the pivot**

---

## Problem

Return the minimum of a rotated ascending array with distinct values.

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
def find_min(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1                        # min is to the right
        else:
            hi = mid                            # min is at mid or left
    return nums[lo]
```

**Complexity:** Time O(log N), Space O(1).

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
- Related questions: `search-in-rotated-sorted`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
