# Move Zeroes  ·  LeetCode #283

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Meta, Amazon, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Partition in place keeping order → write pointer for non-zeros**

---

## Problem

Move all 0s to the end while keeping the relative order of non-zero elements, in place.

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

Cue maps to **Two Pointers** — see [pattern sheet](../../../01-patterns/two-pointers.md).

---

## Solution (Python)

```python
def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
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
- Related questions: `remove-duplicates-sorted`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
