# Maximum XOR of Two Numbers in an Array  ·  LeetCode #421

**Pattern:** Bit Manipulation
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Max pairwise XOR → build prefix greedily bit by bit**

---

## Problem

Return the maximum XOR of any two numbers in the array.

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
def find_maximum_xor(nums: list[int]) -> int:
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {n & mask for n in nums}
        candidate = max_xor | (1 << i)
        if any(candidate ^ p in prefixes for p in prefixes):
            max_xor = candidate
    return max_xor
```

**Complexity:** Time O(32·N), Space O(N).

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
- Related questions: `single-number-iii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
