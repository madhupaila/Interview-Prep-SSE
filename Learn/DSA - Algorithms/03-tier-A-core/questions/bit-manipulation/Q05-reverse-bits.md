# Reverse Bits  ·  LeetCode #190

**Pattern:** Bit Manipulation
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Apple

---

## Memory Hook (Recognition Cue)

> **Reverse 32-bit integer → shift result, pull lowest bit**

---

## Problem

Reverse the bits of a 32-bit unsigned integer.

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
def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res
```

**Complexity:** Time O(1), Space O(1).

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
- Related questions: `number-of-1-bits`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
