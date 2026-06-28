# Daily Temperatures  ·  LeetCode #739

**Pattern:** Monotonic Stack
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Days until a warmer temperature → monotonic decreasing stack of indices**

---

## Problem

For each day, how many days until a warmer temperature (0 if none).

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

'Next warmer' is the canonical next-greater-element → decreasing monotonic stack of indices for distances.

---

## Solution (Python)

```python
def daily_temperatures(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack = []                                  # indices, decreasing temps
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res
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

- Pattern sheet: [Monotonic Stack](../../../01-patterns/monotonic-stack.md)
- Related questions: `next-greater-element-i`, `next-greater-element-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
