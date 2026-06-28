# Number Complement  ·  LeetCode #476

**Pattern:** Bit Manipulation
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Cloudera

---

## Memory Hook (Recognition Cue)

> **Flip all meaningful bits → XOR with all-ones mask**

---

## Problem

Return the complement of a positive integer (flip its bits).

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
def find_complement(num: int) -> int:
    mask = (1 << num.bit_length()) - 1
    return num ^ mask
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
- Related questions: `counting-bits`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
