# Longest Harmonious Subsequence  ·  LeetCode #594

**Pattern:** Arrays & Hashing
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Max-min diff exactly 1 → count then check n and n+1**

---

## Problem

Return the length of the longest subsequence where max - min == 1.

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

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import Counter

def find_lhs(nums: list[int]) -> int:
    freq = Counter(nums)
    best = 0
    for n in freq:
        if n + 1 in freq:
            best = max(best, freq[n] + freq[n + 1])
    return best
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

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `contains-duplicate`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
