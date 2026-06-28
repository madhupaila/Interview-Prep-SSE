# Combination Sum III  ·  LeetCode #216

**Pattern:** Subsets & Combinations
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **k numbers from 1..9 summing to n → bounded backtracking**

---

## Problem

Find all combinations of `k` numbers in 1..9 that sum to `n` (each used once).

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
def combination_sum3(k: int, n: int) -> list[list[int]]:
    res = []
    def dfs(start, k_left, remaining, path):
        if k_left == 0 and remaining == 0:
            res.append(path[:])
            return
        for i in range(start, 10):
            if i > remaining:
                break
            path.append(i)
            dfs(i + 1, k_left - 1, remaining - i, path)
            path.pop()
    dfs(1, k, n, [])
    return res
```

**Complexity:** Time O(C(9,k)), Space O(k).

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
- Related questions: `combination-sum`, `combinations`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
