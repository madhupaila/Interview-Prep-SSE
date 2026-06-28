# Target Sum  ·  LeetCode #494

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Assign +/- to reach target → subset-sum counting**

---

## Problem

Count ways to assign +/- to each number so the sum equals `target`.

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
from collections import defaultdict

def find_target_sum_ways(nums: list[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    for n in nums:
        nxt = defaultdict(int)
        for s, cnt in dp.items():
            nxt[s + n] += cnt
            nxt[s - n] += cnt
        dp = nxt
    return dp[target]
```

**Complexity:** Time O(N·S), Space O(S).

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
- Related questions: `partition-equal-subset-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
