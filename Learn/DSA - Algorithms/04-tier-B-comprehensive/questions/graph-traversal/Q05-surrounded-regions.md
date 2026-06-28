# Surrounded Regions  ·  LeetCode #130

**Pattern:** Graph BFS/DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Capture regions not touching border → DFS from border 'O's first**

---

## Problem

Flip all 'O' regions to 'X' unless connected to the border.

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

Cue maps to **Graph BFS/DFS** — see [pattern sheet](../../../01-patterns/graph-traversal.md).

---

## Solution (Python)

```python
def solve(board: list[list[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'O':
            return
        board[r][c] = '#'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    for r in range(rows):
        dfs(r, 0); dfs(r, cols-1)
    for c in range(cols):
        dfs(0, c); dfs(rows-1, c)
    for r in range(rows):
        for c in range(cols):
            board[r][c] = 'O' if board[r][c] == '#' else 'X'
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

- Pattern sheet: [Graph BFS/DFS](../../../01-patterns/graph-traversal.md)
- Related questions: `number-of-islands`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
