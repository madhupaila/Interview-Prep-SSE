# Range Sum Query - Immutable  ·  LeetCode #303

**Pattern:** Prefix Sum
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Facebook

---

## Memory Hook (Recognition Cue)

> **Many range-sum queries, no updates → precompute prefix sums**

---

## Problem

Implement `sumRange(i, j)` over an immutable array with O(1) per query.

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
class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]
```

**Complexity:** Time O(1) query, O(N) build, Space O(N).

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
- Related questions: `range-sum-query-2d-immutable`, `subarray-sum-equals-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
