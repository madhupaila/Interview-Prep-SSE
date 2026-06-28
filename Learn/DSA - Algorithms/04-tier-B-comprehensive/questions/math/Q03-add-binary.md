# Add Binary  ·  LeetCode #67

**Pattern:** Interview Math
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Add binary strings → carry from the end**

---

## Problem

Add two binary strings and return the sum as a binary string.

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
def add_binary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i]); i -= 1
        if j >= 0:
            total += int(b[j]); j -= 1
        carry, digit = divmod(total, 2)
        res.append(str(digit))
    return "".join(reversed(res))
```

**Complexity:** Time O(max(M,N)), Space O(max(M,N)).

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
- Related questions: `plus-one`, `add-two-numbers`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
