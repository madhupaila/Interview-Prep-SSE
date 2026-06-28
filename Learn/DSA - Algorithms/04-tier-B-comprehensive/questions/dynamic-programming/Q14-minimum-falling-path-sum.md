# Minimum Falling Path Sum  ·  LeetCode #931

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Min path top→bottom (3 directions) → row DP**

---

## Problem

Return the minimum sum of any falling path through the matrix.

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

Cue maps to **Dynamic Programming** — see [pattern sheet](../../../01-patterns/dynamic-programming.md).

---

## Solution (Python)

```python
def min_falling_path_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    dp = matrix[0][:]
    for r in range(1, n):
        new = [0] * n
        for c in range(n):
            best = dp[c]
            if c > 0:
                best = min(best, dp[c - 1])
            if c < n - 1:
                best = min(best, dp[c + 1])
            new[c] = matrix[r][c] + best
        dp = new
    return min(dp)
```

**Complexity:** Time O(N^2), Space O(N).

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

- Pattern sheet: [Dynamic Programming](../../../01-patterns/dynamic-programming.md)
- Related questions: `min-path-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
