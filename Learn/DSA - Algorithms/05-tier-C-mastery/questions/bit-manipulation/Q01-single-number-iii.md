# Single Number III  ·  LeetCode #260

**Pattern:** Bit Manipulation
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Two uniques among pairs → XOR all, split by a differing bit**

---

## Problem

Exactly two elements appear once (rest twice). Return both.

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

XOR of all leaves a^b; a set bit in it differs between the two — partition numbers by that bit and XOR each group.

---

## Solution (Python)

```python
def single_number(nums: list[int]) -> list[int]:
    xor = 0
    for n in nums:
        xor ^= n
    diff = xor & (-xor)                          # lowest set bit where they differ
    a = b = 0
    for n in nums:
        if n & diff:
            a ^= n
        else:
            b ^= n
    return [a, b]
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
- Related questions: `single-number`, `single-number-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
