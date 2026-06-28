# Best Time to Buy and Sell Stock  ·  LeetCode #121

**Pattern:** Sliding Window
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Max profit one transaction → track min so far (window from min to now)**

---

## Problem

Given daily prices, return the max profit from one buy then one sell (sell after buy).

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

Cue maps to **Sliding Window** — see [pattern sheet](../../../01-patterns/sliding-window.md).

---

## Solution (Python)

```python
def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- Prices decreasing → 0
- Empty → 0

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `best-time-to-buy-sell-stock-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
