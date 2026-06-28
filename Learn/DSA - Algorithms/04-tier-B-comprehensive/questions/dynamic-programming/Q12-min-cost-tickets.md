# Minimum Cost For Tickets  ·  LeetCode #983

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Min cost over travel days → DP over days with 1/7/30 passes**

---

## Problem

Given travel days and pass costs (1/7/30 day), return the minimum cost.

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
def mincost_tickets(days: list[int], costs: list[int]) -> int:
    travel = set(days)
    last = days[-1]
    dp = [0] * (last + 1)
    for d in range(1, last + 1):
        if d not in travel:
            dp[d] = dp[d - 1]
        else:
            dp[d] = min(
                dp[d - 1] + costs[0],
                dp[max(0, d - 7)] + costs[1],
                dp[max(0, d - 30)] + costs[2],
            )
    return dp[last]
```

**Complexity:** Time O(maxDay), Space O(maxDay).

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
- Related questions: `coin-change`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
