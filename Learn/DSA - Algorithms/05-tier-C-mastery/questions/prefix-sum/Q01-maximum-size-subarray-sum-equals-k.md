# Maximum Size Subarray Sum Equals k  ·  LeetCode #325

**Pattern:** Prefix Sum
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Facebook, Palantir

---

## Memory Hook (Recognition Cue)

> **Longest subarray with sum k (negatives) → first-seen prefix index map**

---

## Problem

Return the maximum length of a subarray summing to `k`.

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
def max_subarray_len(nums: list[int], k: int) -> int:
    first = {0: -1}
    prefix = best = 0
    for i, n in enumerate(nums):
        prefix += n
        if prefix - k in first:
            best = max(best, i - first[prefix - k])
        if prefix not in first:
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
- Related questions: `subarray-sum-equals-k`, `contiguous-array`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
