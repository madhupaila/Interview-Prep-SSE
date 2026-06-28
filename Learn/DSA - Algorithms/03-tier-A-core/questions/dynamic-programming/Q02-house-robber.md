# House Robber  ·  LeetCode #198

**Pattern:** Dynamic Programming
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Max non-adjacent sum → dp[i]=max(skip, take+dp[i-2])**

---

## Problem

Maximize the sum of robbed houses without robbing two adjacent houses.

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
def rob(nums: list[int]) -> int:
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur
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
- Related questions: `house-robber-ii`, `climbing-stairs`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
