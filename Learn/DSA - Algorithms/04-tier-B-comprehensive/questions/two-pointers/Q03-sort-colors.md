# Sort Colors (Dutch Flag)  ·  LeetCode #75

**Pattern:** Two Pointers
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Microsoft, Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Three-way partition (0/1/2) in one pass → low/mid/high pointers**

---

## Problem

Sort an array of 0s, 1s, 2s in place in one pass.

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
def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1                          # don't advance mid (swapped-in unknown)
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- All same color
- Do not advance mid after swapping from high

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `move-zeroes`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
