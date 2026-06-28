# Best Time to Buy and Sell Stock with Cooldown  ·  LeetCode #309

**Pattern:** Dynamic Programming
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Stock trades with cooldown → state machine (hold/sold/rest)**

---

## Problem

Maximize profit with unlimited transactions and a 1-day cooldown after selling.

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

Three states (holding, just sold, resting) with transitions form a clean DP state machine.

---

## Solution (Python)

```python
def max_profit(prices: list[int]) -> int:
    hold = float('-inf')
    sold = 0
    rest = 0
    for p in prices:
        prev_sold = sold
        sold = hold + p                          # sell today
        hold = max(hold, rest - p)               # buy today (rest yesterday)
        rest = max(rest, prev_sold)              # cooldown
    return max(sold, rest)
```

**Complexity:** Time O(N), Space O(1).

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
- Related questions: `maximum-subarray`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
