# Missing Number (XOR)  ·  LeetCode #268

**Pattern:** Bit Manipulation
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Missing in 0..n → XOR indices with values**

---

## Problem

Find the missing number in [0, n] using XOR.

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
def missing_number(nums: list[int]) -> int:
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res
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

- Pattern sheet: [Bit Manipulation](../../../01-patterns/bit-manipulation.md)
- Related questions: `single-number`, `missing-number`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
