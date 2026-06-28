# Pow(x, n)  ·  LeetCode #50

**Pattern:** Interview Math
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Fast exponentiation → square and halve the exponent**

---

## Problem

Implement `x` raised to the power `n` in O(log n).

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

Cue maps to **Interview Math** — see [pattern sheet](../../../01-patterns/math-tricks.md).

---

## Solution (Python)

```python
def my_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```

**Complexity:** Time O(log N), Space O(1).

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

- Pattern sheet: [Interview Math](../../../01-patterns/math-tricks.md)
- Related questions: `sqrt-x`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
