# First Missing Positive  ·  LeetCode #41

**Pattern:** Cyclic Sort
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Stripe

---

## Memory Hook (Recognition Cue)

> **Smallest absent positive in O(N)/O(1) → place each value at index value-1**

---

## Problem

Return the smallest missing positive integer using O(N) time and O(1) space.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Set | O(N) | O(N) | violates space |
| Cyclic sort | O(N) | O(1) | place value v at index v-1 |

---

## Pattern Identification

The answer lies in [1, n+1]. Place each valid value at its home index; the first index whose value is wrong reveals the answer.

---

## Solution (Python)

```python
def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        v = nums[i]
        if 1 <= v <= n and nums[v - 1] != v:
            nums[v - 1], nums[i] = nums[i], nums[v - 1]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- [1,2,3] → 4
- Values out of range ignored
- Empty → 1

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Cyclic Sort](../../../01-patterns/cyclic-sort.md)
- Related questions: `missing-number`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
