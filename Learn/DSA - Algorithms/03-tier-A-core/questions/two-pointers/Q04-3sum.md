# 3Sum  ·  LeetCode #15

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Meta, Amazon, Microsoft, Adobe

---

## Memory Hook (Recognition Cue)

> **Triplets summing to 0 → sort + fix one + two-pointer the rest**

---

## Problem

Return all unique triplets `[a,b,c]` with `a+b+c == 0`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Brute force | O(N^3) | O(1) | all triplets |
| Sort + two pointers | O(N^2) | O(1) | fix i, scan pair; skip dups |

---

## Pattern Identification

Pair-sum-to-target with two pointers, wrapped in a loop fixing the first element. Sorting enables both the two-pointer scan and duplicate skipping.

---

## Solution (Python)

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                          # skip duplicate anchors
        if nums[i] > 0:
            break                             # no positive triple sums to 0
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1; hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res
```

**Complexity:** Time O(N^2), Space O(1).

---

## Edge Cases & Pitfalls

- Fewer than 3 elements
- All zeros → one triplet
- Duplicates must be skipped

---

## Follow-Ups

1. 3Sum Closest
2. 4Sum
3. 3Sum Smaller (count)

---

## Related

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `3sum-closest`, `4sum`, `two-sum-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
