# Subarray Sums Divisible by K  ·  LeetCode #974

**Pattern:** Prefix Sum
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Count subarrays with sum % k == 0 → bucket prefix remainders**

---

## Problem

Count contiguous subarrays whose sum is divisible by `k`.

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

Cue maps to **Prefix Sum** — see [pattern sheet](../../../01-patterns/prefix-sum.md).

---

## Solution (Python)

```python
from collections import defaultdict

def subarrays_div_by_k(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    prefix = res = 0
    for n in nums:
        prefix = (prefix + n) % k
        res += count[prefix]
        count[prefix] += 1
    return res
```

**Complexity:** Time O(N), Space O(k).

---

## Edge Cases & Pitfalls

- Negative numbers (Python % is non-negative)
- Equal remainders form valid subarrays

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `subarray-sum-equals-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
