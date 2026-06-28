# Subsets (Bitmask)  ·  LeetCode #78

**Pattern:** Bit Manipulation
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **All subsets via integers → iterate 0..2^n-1**

---

## Problem

Generate all subsets using bitmask enumeration.

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

Cue maps to **Bit Manipulation** — see [pattern sheet](../../../01-patterns/bit-manipulation.md).

---

## Solution (Python)

```python
def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = []
    for mask in range(1 << n):
        res.append([nums[i] for i in range(n) if mask & (1 << i)])
    return res
```

**Complexity:** Time O(N·2^N), Space O(1) extra.

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

- Pattern sheet: [Bit Manipulation](../../../01-patterns/bit-manipulation.md)
- Related questions: `subsets`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
