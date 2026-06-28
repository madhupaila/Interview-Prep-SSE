# Missing Number  ·  LeetCode #268

**Pattern:** Cyclic Sort
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Microsoft, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Numbers 0..n with one missing → sum formula or XOR or cyclic placement**

---

## Problem

Given `n` distinct numbers in range [0, n], return the missing one.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sum formula | O(N) | O(1) | n(n+1)/2 - sum |
| XOR | O(N) | O(1) | xor indices and values |

---

## Pattern Identification

Cue maps to **Cyclic Sort** — see [pattern sheet](../../../01-patterns/cyclic-sort.md).

---

## Solution (Python)

```python
def missing_number(nums: list[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
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

- Pattern sheet: [Cyclic Sort](../../../01-patterns/cyclic-sort.md)
- Related questions: `find-all-numbers-disappeared`, `first-missing-positive`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
