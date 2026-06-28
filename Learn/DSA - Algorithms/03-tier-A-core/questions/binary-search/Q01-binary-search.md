# Binary Search  ·  LeetCode #704

**Pattern:** Binary Search
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Sorted + find target → classic halving**

---

## Problem

Return the index of `target` in a sorted array, or -1.

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
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
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
- Related questions: `search-insert-position`, `find-first-last-position`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
