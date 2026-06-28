# Unique Binary Search Trees  ·  LeetCode #96

**Pattern:** Dynamic Programming
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Count BST shapes → Catalan number DP**

---

## Problem

Count structurally unique BSTs storing values `1..n`.

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
def num_trees(n: int) -> int:
    dp = [1] * (n + 1)
    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            total += dp[root - 1] * dp[nodes - root]
        dp[nodes] = total
    return dp[n]
```

**Complexity:** Time O(N^2), Space O(N).

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
- Related questions: `unique-binary-search-trees-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
