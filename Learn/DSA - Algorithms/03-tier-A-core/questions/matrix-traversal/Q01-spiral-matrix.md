# Spiral Matrix  ·  LeetCode #54

**Pattern:** Matrix Traversal
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Google

---

## Memory Hook (Recognition Cue)

> **Read matrix in spiral order → shrink four boundaries**

---

## Problem

Return all elements of the matrix in spiral order.

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
def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
    return res
```

**Complexity:** Time O(R·C), Space O(1).

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
- Related questions: `spiral-matrix-ii`, `rotate-image`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
