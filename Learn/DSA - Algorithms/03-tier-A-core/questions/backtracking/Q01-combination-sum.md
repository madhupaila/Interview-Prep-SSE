# Combination Sum  ·  LeetCode #39

**Pattern:** Backtracking
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **All combinations summing to target (reuse allowed) → backttrack with start index**

---

## Problem

Return all unique combinations of `candidates` summing to `target`; numbers may be reused.

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
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    def dfs(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remaining - candidates[i], path)   # i (not i+1) → reuse
            path.pop()
    dfs(0, target, [])
    return res
```

**Complexity:** Time O(2^T), Space O(T).

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
- Related questions: `combination-sum-ii`, `subsets`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
