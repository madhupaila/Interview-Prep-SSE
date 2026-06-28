# Pattern: Matrix / Grid Traversal

## Recognition Cues

- 2D grid input with **spiral / diagonal / rotate / transpose**
- "Set matrix zeroes", "rotate image", "spiral order"
- In-place grid transformations
- (Grid graph search lives in [Graph BFS/DFS](graph-traversal.md))

## Core Idea

Master index arithmetic and boundary control. Common operations: transpose (`m[i][j] ↔ m[j][i]`), reverse rows for rotation, layer-by-layer boundary walking for spiral.

---

## Templates

### Rotate image 90° in place

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):                         # transpose
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:                         # reverse each row
        row.reverse()
```

### Spiral order

```python
def spiral_order(matrix):
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

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Geometric grid transforms | Pathfinding/connectivity → BFS/DFS |
| In-place rotate/transpose/spiral | Sparse structure → other representations |

## Complexity

- Time: **O(R·C)** (visit each cell once). Space: **O(1)** in-place or O(R·C) output.

## Variants & Pitfalls

- **Rotate Image**, **Spiral Matrix I/II**, **Set Matrix Zeroes** (use first row/col as markers for O(1) space), **Transpose**, **Diagonal Traverse**, **Game of Life**.
- Pitfall: re-check `top <= bottom` / `left <= right` before the third/fourth spiral edges to avoid double counting.

## Linked Questions

- Tier A: Spiral Matrix, Rotate Image, Set Matrix Zeroes
- Tier B: Spiral Matrix II, Diagonal Traverse, Game of Life
- Tier C: Spiral Matrix III, Rotate by layers variants

## Related

- [Graph BFS/DFS](graph-traversal.md) · [Arrays & Hashing](../02-data-structures/arrays-hashing.md)
