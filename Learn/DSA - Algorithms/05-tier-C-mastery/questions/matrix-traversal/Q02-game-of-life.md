# Game of Life  ·  LeetCode #289

**Pattern:** Matrix Traversal
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Dropbox

---

## Memory Hook (Recognition Cue)

> **In-place next state → encode old/new in 2 bits**

---

## Problem

Compute the next state of Conway's Game of Life in place.

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

Store next state in a second bit so neighbor counts still see the old state, then shift.

---

## Solution (Python)

```python
def game_of_life(board: list[list[int]]) -> None:
    rows, cols = len(board), len(board[0])
    def live_neighbors(r, c):
        cnt = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] & 1:
                    cnt += 1
        return cnt
    for r in range(rows):
        for c in range(cols):
            n = live_neighbors(r, c)
            if board[r][c] & 1:
                if n in (2, 3):
                    board[r][c] |= 2             # stays alive (bit1 = next)
            elif n == 3:
                board[r][c] |= 2                 # becomes alive
    for r in range(rows):
        for c in range(cols):
            board[r][c] >>= 1
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
- Related questions: `set-matrix-zeroes`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
