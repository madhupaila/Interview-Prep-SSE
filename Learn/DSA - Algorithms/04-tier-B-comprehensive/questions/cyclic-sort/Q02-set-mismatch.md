# Set Mismatch  ·  LeetCode #645

**Pattern:** Cyclic Sort
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Bloomberg

---

## Memory Hook (Recognition Cue)

> **One number duplicated, one missing → cyclic sort then scan**

---

## Problem

Find the duplicated number and the missing number in [1, n].

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

Cue maps to **Cyclic Sort** — see [pattern sheet](../../../01-patterns/cyclic-sort.md).

---

## Solution (Python)

```python
def find_error_nums(nums: list[int]) -> list[int]:
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]            # [duplicate, missing]
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

- Pattern sheet: [Cyclic Sort](../../../01-patterns/cyclic-sort.md)
- Related questions: `missing-number`, `find-all-duplicates`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
