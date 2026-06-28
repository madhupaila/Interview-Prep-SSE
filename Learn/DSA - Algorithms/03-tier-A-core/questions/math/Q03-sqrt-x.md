# Sqrt(x)  ·  LeetCode #69

**Pattern:** Interview Math
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Integer sqrt → binary search on candidate**

---

## Problem

Return the integer square root of `x` (floor).

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
def my_sqrt(x: int) -> int:
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi
```

**Complexity:** Time O(log X), Space O(1).

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
- Related questions: `pow-x-n`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
