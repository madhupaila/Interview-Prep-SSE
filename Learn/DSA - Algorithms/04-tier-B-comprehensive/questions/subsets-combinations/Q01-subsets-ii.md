# Subsets II  ·  LeetCode #90

**Pattern:** Subsets & Combinations
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Power set with duplicates → sort + skip same value at a level**

---

## Problem

Return all unique subsets when the array may contain duplicates.

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
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res
```

**Complexity:** Time O(N·2^N), Space O(N).

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
- Related questions: `subsets`, `combination-sum-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
