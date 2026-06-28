# Kth Largest Element (Quickselect)  ·  LeetCode #215

**Pattern:** Binary Search
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Kth largest in O(N) average → quickselect partition**

---

## Problem

Find the kth largest element using quickselect (average O(N)).

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
import random

def find_kth_largest(nums: list[int], k: int) -> int:
    target = len(nums) - k                         # kth largest = index in sorted order
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        pivot = nums[random.randint(lo, hi)]
        left, mid, right = [], [], []
        for n in nums[lo:hi + 1]:
            (left if n < pivot else right if n > pivot else mid).append(n)
        # rebuild segment
        nums[lo:hi + 1] = left + mid + right
        l_end = lo + len(left)
        r_start = l_end + len(mid)
        if target < l_end:
            hi = l_end - 1
        elif target >= r_start:
            lo = r_start
        else:
            return pivot
    return nums[target]
```

**Complexity:** Time O(N) avg, Space O(N).

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
- Related questions: `kth-largest-element`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
