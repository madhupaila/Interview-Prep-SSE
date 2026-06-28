# Two Sum II (Sorted Input)  ·  LeetCode #167

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Sorted + pair sum → move pointer by comparison (O(1) space)**

---

## Problem

Given a 1-indexed sorted array, return indices of two numbers adding to `target`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Hashmap | O(N) | O(N) | ignores sortedness |
| Two pointers | O(N) | O(1) | exploit sorted order |

---

## Pattern Identification

Cue maps to **Two Pointers** — see [pattern sheet](../../../01-patterns/two-pointers.md).

---

## Solution (Python)

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []
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

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `two-sum`, `3sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
