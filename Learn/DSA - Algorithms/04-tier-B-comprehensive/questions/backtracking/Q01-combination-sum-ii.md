# Combination Sum II  ·  LeetCode #40

**Pattern:** Backtracking
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Combinations to target, each number once, no dup sets → sort + skip duplicates**

---

## Problem

Return unique combinations summing to `target`; each candidate used at most once.

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
def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res = []
    def dfs(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue                          # skip duplicate at this level
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            dfs(i + 1, remaining - candidates[i], path)
            path.pop()
    dfs(0, target, [])
    return res
```

**Complexity:** Time O(2^N), Space O(N).

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
- Related questions: `combination-sum`, `subsets-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
