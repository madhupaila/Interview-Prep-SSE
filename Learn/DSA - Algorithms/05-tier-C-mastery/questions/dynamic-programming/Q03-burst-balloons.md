# Burst Balloons  ·  LeetCode #312

**Pattern:** Dynamic Programming
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Max coins bursting balloons → interval DP on last-burst**

---

## Problem

Maximize coins from bursting all balloons (coins = left*cur*right at burst time).

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

Think of which balloon is burst LAST in an interval; that fixes its neighbors → interval DP.

---

## Solution (Python)

```python
def max_coins(nums: list[int]) -> int:
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    balloons[left] * balloons[k] * balloons[right]
                    + dp[left][k] + dp[k][right])
    return dp[0][n - 1]
```

**Complexity:** Time O(N^3), Space O(N^2).

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
- Related questions: `matrix-chain`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
