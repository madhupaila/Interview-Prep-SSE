# Best Time to Buy and Sell Stock II  ·  LeetCode #122

**Pattern:** Greedy
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Unlimited transactions → sum every positive delta**

---

## Problem

Maximize profit with as many transactions as you like (sell before re-buy).

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

Cue maps to **Greedy** — see [pattern sheet](../../../01-patterns/greedy.md).

---

## Solution (Python)

```python
def max_profit(prices: list[int]) -> int:
    return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
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

- Pattern sheet: [Greedy](../../../01-patterns/greedy.md)
- Related questions: `best-time-to-buy-sell-stock`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
