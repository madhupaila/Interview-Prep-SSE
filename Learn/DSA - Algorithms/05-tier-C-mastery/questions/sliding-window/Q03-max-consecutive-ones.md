# Maximum Consecutive Ones  ·  LeetCode #485

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Longest run of 1s → running count reset on 0**

---

## Problem

Return the maximum number of consecutive 1s in a binary array.

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

Cue maps to **Sliding Window** — see [pattern sheet](../../../01-patterns/sliding-window.md).

---

## Solution (Python)

```python
def find_max_consecutive_ones(nums: list[int]) -> int:
    best = cur = 0
    for n in nums:
        cur = cur + 1 if n == 1 else 0
        best = max(best, cur)
    return best
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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `max-consecutive-ones-iii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
