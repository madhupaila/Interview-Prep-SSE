# Find All Numbers Disappeared in an Array  ·  LeetCode #448

**Pattern:** Cyclic Sort
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Values in 1..n, find all missing → mark indices by sign**

---

## Problem

Given `nums` in [1, n], return all values in [1, n] that do not appear.

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

Range [1..n] lets us use indices as a hash; sign-marking records presence in O(1) space.

---

## Solution (Python)

```python
def find_disappeared_numbers(nums: list[int]) -> list[int]:
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]              # mark seen
    return [i + 1 for i, n in enumerate(nums) if n > 0]
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
- Related questions: `find-all-duplicates`, `missing-number`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
