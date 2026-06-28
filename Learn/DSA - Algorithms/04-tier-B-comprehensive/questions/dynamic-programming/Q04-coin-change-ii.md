# Coin Change II  ·  LeetCode #518

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Number of ways to make amount → unbounded knapsack count (coins outer loop)**

---

## Problem

Return the number of combinations that make up `amount`.

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

Coins in the outer loop counts each combination once (order-independent), unlike combination-sum-iv.

---

## Solution (Python)

```python
def change(amount: int, coins: list[int]) -> int:
    dp = [1] + [0] * amount
    for c in coins:                              # coins outer → combinations not permutations
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

**Complexity:** Time O(amount·coins), Space O(amount).

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
- Related questions: `coin-change`, `combination-sum-iv`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
