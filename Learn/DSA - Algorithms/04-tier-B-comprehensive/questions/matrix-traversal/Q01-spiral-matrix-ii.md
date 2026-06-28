# Spiral Matrix II  ·  LeetCode #59

**Pattern:** Matrix Traversal
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Fill 1..n^2 in spiral → same boundary shrink, write values**

---

## Problem

Generate an `n×n` matrix filled with `1..n^2` in spiral order.

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
def generate_matrix(n: int) -> list[list[int]]:
    m = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    val = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            m[top][c] = val; val += 1
        top += 1
        for r in range(top, bottom + 1):
            m[r][right] = val; val += 1
        right -= 1
        for c in range(right, left - 1, -1):
            m[bottom][c] = val; val += 1
        bottom -= 1
        for r in range(bottom, top - 1, -1):
            m[r][left] = val; val += 1
        left += 1
    return m
```

**Complexity:** Time O(N^2), Space O(N^2).

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
