# Rotate Image  ·  LeetCode #48

**Pattern:** Matrix Traversal
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Apple

---

## Memory Hook (Recognition Cue)

> **Rotate 90 in place → transpose then reverse rows**

---

## Problem

Rotate an `n×n` matrix 90° clockwise in place.

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

Cue maps to **Matrix Traversal** — see [pattern sheet](../../../01-patterns/matrix-traversal.md).

---

## Solution (Python)

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

**Complexity:** Time O(N^2), Space O(1).

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

- Pattern sheet: [Matrix Traversal](../../../01-patterns/matrix-traversal.md)
- Related questions: `spiral-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
