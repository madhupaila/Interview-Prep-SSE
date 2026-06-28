# Count Number of Nice Subarrays  ·  LeetCode #1248

**Pattern:** Prefix Sum
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Exactly k odd numbers → prefix count of odds + hashmap**

---

## Problem

Count subarrays with exactly `k` odd numbers.

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

Replace 'sum' with 'count of odds'; it's Subarray Sum Equals K on parity.

---

## Solution (Python)

```python
from collections import defaultdict

def number_of_subarrays(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    odds = res = 0
    for n in nums:
        odds += n & 1
        res += count[odds - k]
        count[odds] += 1
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

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `subarray-sum-equals-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
