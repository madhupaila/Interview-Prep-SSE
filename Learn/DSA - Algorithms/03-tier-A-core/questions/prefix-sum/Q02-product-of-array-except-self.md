# Product of Array Except Self  ·  LeetCode #238

**Pattern:** Prefix Sum
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Apple

---

## Memory Hook (Recognition Cue)

> **Each index = product of others → prefix product × suffix product**

---

## Problem

Return an array where `out[i]` is the product of all elements except `nums[i]`, without division, O(N).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Division | O(N) | O(1) | fails on zeros / disallowed |
| Prefix × suffix | O(N) | O(1) extra | two passes |

---

## Pattern Identification

Cue maps to **Prefix Sum** — see [pattern sheet](../../../01-patterns/prefix-sum.md).

---

## Solution (Python)

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res
```

**Complexity:** Time O(N), Space O(1) extra.

---

## Edge Cases & Pitfalls

- Contains zero(s)
- Single element

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `range-sum-query-immutable`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
