# Hamming Distance  ·  LeetCode #461

**Pattern:** Bit Manipulation
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Differing bit count → XOR then popcount**

---

## Problem

Return the number of positions where the bits of two integers differ.

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
def hamming_distance(x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count
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
