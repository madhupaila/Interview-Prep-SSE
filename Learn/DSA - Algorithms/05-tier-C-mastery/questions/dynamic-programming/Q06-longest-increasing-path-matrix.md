# Longest Increasing Path in a Matrix  ·  LeetCode #329

**Pattern:** Dynamic Programming
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Longest strictly increasing path → DFS + memo on cells**

---

## Problem

Return the length of the longest increasing path in a matrix (4-directional).

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
from functools import cache

def longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    @cache
    def dfs(r, c):
        best = 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best
    return max(dfs(r, c) for r in range(rows) for c in range(cols))
```

**Complexity:** Time O(R·C), Space O(R·C).

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
- Related questions: `longest-increasing-subsequence`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
