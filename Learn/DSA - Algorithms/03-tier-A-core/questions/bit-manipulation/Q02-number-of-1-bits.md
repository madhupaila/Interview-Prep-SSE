# Number of 1 Bits  ·  LeetCode #191

**Pattern:** Bit Manipulation
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Apple, Microsoft

---

## Memory Hook (Recognition Cue)

> **Count set bits → x & (x-1) clears lowest set bit**

---

## Problem

Return the number of 1 bits (Hamming weight) of an integer.

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
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1                               # drop lowest set bit
        count += 1
    return count
```

**Complexity:** Time O(set bits), Space O(1).

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
- Related questions: `counting-bits`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
