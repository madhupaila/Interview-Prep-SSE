# Happy Number  ·  LeetCode #202

**Pattern:** Fast & Slow Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Sequence cycles? → Floyd on digit-square-sum**

---

## Problem

A number is happy if repeatedly summing squares of digits reaches 1. Return True/False.

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

Cue maps to **Fast & Slow Pointers** — see [pattern sheet](../../../01-patterns/fast-slow-pointers.md).

---

## Solution (Python)

```python
def is_happy(n: int) -> bool:
    def nxt(x):
        return sum(int(d) ** 2 for d in str(x))
    slow = n
    fast = nxt(n)
    while fast != 1 and slow != fast:
        slow = nxt(slow)
        fast = nxt(nxt(fast))
    return fast == 1
```

**Complexity:** Time O(log N) per step, Space O(1).

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

- Pattern sheet: [Fast & Slow Pointers](../../../01-patterns/fast-slow-pointers.md)
- Related questions: `linked-list-cycle`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
