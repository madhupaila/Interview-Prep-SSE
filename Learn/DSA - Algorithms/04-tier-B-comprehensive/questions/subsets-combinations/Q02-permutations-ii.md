# Permutations II  ·  LeetCode #47

**Pattern:** Subsets & Combinations
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Unique permutations with duplicates → sort + skip used duplicates**

---

## Problem

Return all unique permutations when the array may contain duplicates.

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

Cue maps to **Subsets & Combinations** — see [pattern sheet](../../../01-patterns/subsets-combinations.md).

---

## Solution (Python)

```python
def permute_unique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    used = [False] * len(nums)
    def dfs(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            dfs(path)
            path.pop()
            used[i] = False
    dfs([])
    return res
```

**Complexity:** Time O(N·N!), Space O(N).

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

- Pattern sheet: [Subsets & Combinations](../../../01-patterns/subsets-combinations.md)
- Related questions: `permutations`, `subsets-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
