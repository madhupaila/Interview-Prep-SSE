# Valid Sudoku  ·  LeetCode #36

**Pattern:** Arrays & Hashing
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Apple, Uber

---

## Memory Hook (Recognition Cue)

> **Check rows/cols/boxes for dupes → 3 sets keyed by index**

---

## Problem

Determine if a 9×9 Sudoku board is valid (filled cells only; no need to be solvable).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Three sets | O(1) | O(1) | 81 cells fixed; track seen per row/col/box |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import defaultdict

def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            b = (r // 3, c // 3)
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                return False
            rows[r].add(v); cols[c].add(v); boxes[b].add(v)
    return True
```

**Complexity:** Time O(1), Space O(1).

---

## Edge Cases & Pitfalls

- Empty cells '.' skipped
- 9x9 fixed size

---

## Follow-Ups

1. Solve the Sudoku (backtracking)
2. Generalize to N²×N²

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `sudoku-solver`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
