# Find First and Last Position of Element  ·  LeetCode #34

**Pattern:** Binary Search
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Range of a value in sorted → two boundary searches**

---

## Problem

Return the first and last index of `target` in a sorted array, or [-1, -1].

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
def search_range(nums: list[int], target: int) -> list[int]:
    def bound(is_left):
        lo, hi, res = 0, len(nums) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                res = mid
                if is_left:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return res
    return [bound(True), bound(False)]
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
- Related questions: `binary-search`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
