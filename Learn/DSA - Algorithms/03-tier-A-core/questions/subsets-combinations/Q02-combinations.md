# Combinations  ·  LeetCode #77

**Pattern:** Subsets & Combinations
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **All k-size selections → backtrack with start index**

---

## Problem

Return all combinations of `k` numbers from `1..n`.

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
def combine(n: int, k: int) -> list[list[int]]:
    res = []
    def dfs(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            dfs(i + 1, path)
            path.pop()
    dfs(1, [])
    return res
```

**Complexity:** Time O(k·C(n,k)), Space O(k).

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
- Related questions: `subsets`, `combination-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
