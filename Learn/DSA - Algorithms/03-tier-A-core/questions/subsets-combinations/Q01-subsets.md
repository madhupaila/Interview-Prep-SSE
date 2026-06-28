# Subsets  ·  LeetCode #78

**Pattern:** Subsets & Combinations
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Power set → backtrack appending every prefix**

---

## Problem

Return all subsets of an array of distinct integers.

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
def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
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
- Related questions: `subsets-ii`, `combinations`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
