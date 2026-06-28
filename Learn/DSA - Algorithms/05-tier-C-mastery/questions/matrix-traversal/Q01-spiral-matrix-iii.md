# Find Winner / Tic Tac Toe State  ·  LeetCode #794

**Pattern:** Matrix Traversal
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Validate board state → count + win checks**

---

## Problem

Determine if a given Tic-Tac-Toe board is a valid reachable state.

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
def valid_tic_tac_toe(board: list[str]) -> bool:
    x = sum(row.count('X') for row in board)
    o = sum(row.count('O') for row in board)
    if o > x or x > o + 1:
        return False
    def wins(p):
        lines = list(board) + ["".join(col) for col in zip(*board)]
        lines.append(board[0][0] + board[1][1] + board[2][2])
        lines.append(board[0][2] + board[1][1] + board[2][0])
        return any(line == p * 3 for line in lines)
    if wins('X') and x != o + 1:
        return False
    if wins('O') and x != o:
        return False
    return True
```

**Complexity:** Time O(1), Space O(1).

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
- Related questions: `game-of-life`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
