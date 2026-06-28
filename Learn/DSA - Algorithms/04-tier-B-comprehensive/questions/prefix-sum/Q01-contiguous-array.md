# Contiguous Array  ·  LeetCode #525

**Pattern:** Prefix Sum
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Longest subarray equal #0s and #1s → map 0→-1, first index of each prefix**

---

## Problem

Return the max length of a contiguous subarray with equal numbers of 0 and 1.

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

Map 0→-1 so 'equal counts' becomes 'subarray sum 0'; track the first index of each prefix to maximize length.

---

## Solution (Python)

```python
def find_max_length(nums: list[int]) -> int:
    first = {0: -1}
    prefix = best = 0
    for i, n in enumerate(nums):
        prefix += 1 if n == 1 else -1
        if prefix in first:
            best = max(best, i - first[prefix])
        else:
            first[prefix] = i
    return best
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

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `subarray-sum-equals-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
