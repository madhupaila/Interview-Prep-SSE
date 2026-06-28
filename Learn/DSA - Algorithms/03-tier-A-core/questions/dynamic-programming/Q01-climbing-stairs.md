# Climbing Stairs  ·  LeetCode #70

**Pattern:** Dynamic Programming
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Adobe

---

## Memory Hook (Recognition Cue)

> **Ways to reach step n (1 or 2 at a time) → Fibonacci recurrence**

---

## Problem

Count distinct ways to climb to the top taking 1 or 2 steps.

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
def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a
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
- Related questions: `min-cost-climbing-stairs`, `house-robber`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
