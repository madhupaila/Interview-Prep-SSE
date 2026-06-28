# N-Queens  ·  LeetCode #51

**Pattern:** Backtracking
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Place N non-attacking queens → backtrack with column/diagonal sets**

---

## Problem

Return all distinct solutions placing `n` queens on an `n×n` board.

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

Cue maps to **Backtracking** — see [pattern sheet](../../../01-patterns/backtracking.md).

---

## Solution (Python)

```python
def solve_n_queens(n: int) -> list[list[str]]:
    res = []
    cols, diag, anti = set(), set(), set()
    board = [['.'] * n for _ in range(n)]
    def place(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c)
            board[r][c] = 'Q'
            place(r + 1)
            board[r][c] = '.'
            cols.discard(c); diag.discard(r - c); anti.discard(r + c)
    place(0)
    return res
```

**Complexity:** Time O(N!), Space O(N).

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

- Pattern sheet: [Backtracking](../../../01-patterns/backtracking.md)
- Related questions: `sudoku-solver`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
