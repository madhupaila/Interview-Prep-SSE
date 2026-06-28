# Longest Increasing Subsequence  ·  LeetCode #300

**Pattern:** Dynamic Programming
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Longest increasing subsequence → patience sorting with bisect (O(N log N))**

---

## Problem

Return the length of the longest strictly increasing subsequence.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| DP | O(N^2) | O(N) | dp[i]=longest ending at i |
| Patience + bisect | O(N log N) | O(N) | tails array |

---

## Pattern Identification

Cue maps to **Dynamic Programming** — see [pattern sheet](../../../01-patterns/dynamic-programming.md).

---

## Solution (Python)

```python
import bisect

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)
```

**Complexity:** Time O(N log N), Space O(N).

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
- Related questions: `russian-doll-envelopes`, `longest-increasing-path-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
