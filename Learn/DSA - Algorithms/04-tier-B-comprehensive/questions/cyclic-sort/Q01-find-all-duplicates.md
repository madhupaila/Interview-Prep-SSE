# Find All Duplicates in an Array  ·  LeetCode #442

**Pattern:** Cyclic Sort
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Values 1..n, each once or twice → sign-mark; second hit = duplicate**

---

## Problem

Return all values appearing twice in `nums` (values in [1, n]).

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
def find_duplicates(nums: list[int]) -> list[int]:
    res = []
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] < 0:
            res.append(abs(n))
        else:
            nums[idx] = -nums[idx]
    return res
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
- Related questions: `find-all-numbers-disappeared`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
