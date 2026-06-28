# Permutations  ·  LeetCode #46

**Pattern:** Backtracking
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **All orderings → backtrack with used set**

---

## Problem

Return all permutations of distinct integers.

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

Cue maps to **Backtracking** — see [pattern sheet](../../../01-patterns/backtracking.md).

---

## Solution (Python)

```python
def permute(nums: list[int]) -> list[list[int]]:
    res = []
    used = [False] * len(nums)
    def dfs(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
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

- Pattern sheet: [Backtracking](../../../01-patterns/backtracking.md)
- Related questions: `permutations-ii`, `subsets`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
