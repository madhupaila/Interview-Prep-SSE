# Candy  ·  LeetCode #135

**Pattern:** Greedy
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Min candies with rating constraints → two passes (left, right)**

---

## Problem

Each child gets ≥1 candy; higher rating than a neighbor gets more. Minimize total.

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

Satisfy the left-neighbor constraint in a forward pass, then the right-neighbor constraint backward, taking the max.

---

## Solution (Python)

```python
def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)
```

**Complexity:** Time O(N), Space O(N).

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
- Related questions: `partition-labels`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
