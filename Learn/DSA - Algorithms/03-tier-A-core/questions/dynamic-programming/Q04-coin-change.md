# Coin Change  ·  LeetCode #322

**Pattern:** Dynamic Programming
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Fewest coins to make amount → unbounded knapsack min**

---

## Problem

Return the fewest coins needed to make `amount`, or -1.

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
def coin_change(coins: list[int], amount: int) -> int:
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
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
- Related questions: `coin-change-ii`, `combination-sum-iv`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
