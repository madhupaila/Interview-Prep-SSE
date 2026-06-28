# Sudoku Solver  ·  LeetCode #37

**Pattern:** Backtracking
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Fill a Sudoku → backtrack trying digits with constraint checks**

---

## Problem

Solve a 9×9 Sudoku in place.

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
def solve_sudoku(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r//3)*3 + c//3].add(v)
    def dfs(k):
        if k == len(empties):
            return True
        r, c = empties[k]
        b = (r//3)*3 + c//3
        for d in "123456789":
            if d in rows[r] or d in cols[c] or d in boxes[b]:
                continue
            board[r][c] = d
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if dfs(k + 1):
                return True
            board[r][c] = '.'
            rows[r].discard(d); cols[c].discard(d); boxes[b].discard(d)
        return False
    dfs(0)
```

**Complexity:** Time exponential (bounded), Space O(1).

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
- Related questions: `n-queens`, `valid-sudoku`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
