# Find Pivot Index  ·  LeetCode #724

**Pattern:** Prefix Sum
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Left sum == right sum → total minus prefix**

---

## Problem

Return the leftmost index where the sum to the left equals the sum to the right.

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

Cue maps to **Prefix Sum** — see [pattern sheet](../../../01-patterns/prefix-sum.md).

---

## Solution (Python)

```python
def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        if left == total - left - n:
            return i
        left += n
    return -1
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

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `range-sum-query-immutable`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
