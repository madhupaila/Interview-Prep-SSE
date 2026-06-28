# Delete and Earn  ·  LeetCode #740

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Earn points deleting + adjacents removed → house-robber on value buckets**

---

## Problem

Maximize points where taking value v deletes all v-1 and v+1.

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
from collections import Counter

def delete_and_earn(nums: list[int]) -> int:
    points = Counter(nums)
    max_v = max(nums)
    prev = cur = 0
    for v in range(1, max_v + 1):
        take = prev + v * points.get(v, 0)
        prev, cur = cur, max(cur, take)
    return cur
```

**Complexity:** Time O(N + maxV), Space O(maxV).

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
- Related questions: `house-robber`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
