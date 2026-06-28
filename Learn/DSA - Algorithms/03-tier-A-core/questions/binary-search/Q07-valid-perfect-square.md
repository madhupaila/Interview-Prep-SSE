# Valid Perfect Square  ·  LeetCode #367

**Pattern:** Binary Search
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Is perfect square → binary search candidate**

---

## Problem

Return True if `num` is a perfect square (no sqrt builtin).

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

Cue maps to **Binary Search** — see [pattern sheet](../../../01-patterns/binary-search.md).

---

## Solution (Python)

```python
def is_perfect_square(num: int) -> bool:
    lo, hi = 1, num
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == num:
            return True
        if sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
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

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `sqrt-x`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
