# Diagonal Traverse  ·  LeetCode #498

**Pattern:** Matrix Traversal
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Zigzag diagonals → group by r+c, reverse alternate diagonals**

---

## Problem

Return matrix elements in diagonal (zigzag) order.

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
def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    if not mat:
        return []
    rows, cols = len(mat), len(mat[0])
    diagonals = {}
    for r in range(rows):
        for c in range(cols):
            diagonals.setdefault(r + c, []).append(mat[r][c])
    res = []
    for d in range(rows + cols - 1):
        if d % 2 == 0:
            res.extend(reversed(diagonals[d]))
        else:
            res.extend(diagonals[d])
    return res
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

- Pattern sheet: [Matrix Traversal](../../../01-patterns/matrix-traversal.md)
- Related questions: `spiral-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
