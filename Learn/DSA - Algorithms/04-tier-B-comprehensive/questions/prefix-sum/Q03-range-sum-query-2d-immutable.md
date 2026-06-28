# Range Sum Query 2D - Immutable  ·  LeetCode #304

**Pattern:** Prefix Sum
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Submatrix sum queries → 2D prefix sums (inclusion-exclusion)**

---

## Problem

Return the sum of a submatrix `(r1,c1)..(r2,c2)` in O(1) after preprocessing.

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

Cue maps to **Prefix Sum** — see [pattern sheet](../../../01-patterns/prefix-sum.md).

---

## Solution (Python)

```python
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        R, C = len(matrix), len(matrix[0])
        self.P = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.P[r+1][c+1] = (matrix[r][c] + self.P[r][c+1]
                                    + self.P[r+1][c] - self.P[r][c])

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        P = self.P
        return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

**Complexity:** Time O(1) query, O(R·C) build, Space O(R·C).

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

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `range-sum-query-immutable`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
