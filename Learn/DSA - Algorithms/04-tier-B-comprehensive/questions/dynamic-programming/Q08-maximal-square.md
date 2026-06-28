# Maximal Square  ·  LeetCode #221

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Largest all-1 square → dp=min(top,left,diag)+1**

---

## Problem

Return the area of the largest square of 1s in a binary matrix.

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

Cue maps to **Dynamic Programming** — see [pattern sheet](../../../01-patterns/dynamic-programming.md).

---

## Solution (Python)

```python
def maximal_square(matrix: list[list[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * (cols + 1)
    best = 0
    for r in range(rows):
        prev = 0                                 # dp[r-1][c-1]
        for c in range(1, cols + 1):
            temp = dp[c]
            if matrix[r][c-1] == '1':
                dp[c] = min(dp[c], dp[c-1], prev) + 1
                best = max(best, dp[c])
            else:
                dp[c] = 0
            prev = temp
    return best * best
```

**Complexity:** Time O(M·N), Space O(N).

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

- Pattern sheet: [Dynamic Programming](../../../01-patterns/dynamic-programming.md)
- Related questions: `maximal-rectangle`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
