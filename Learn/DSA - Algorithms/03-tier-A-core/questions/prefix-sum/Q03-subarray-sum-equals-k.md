# Subarray Sum Equals K  ·  LeetCode #560

**Pattern:** Prefix Sum
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Count subarrays summing to K (negatives!) → prefix sum + hashmap of counts**

---

## Problem

Return the number of contiguous subarrays whose sum equals `k`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Brute force | O(N^2) | O(1) | all subarrays |
| Prefix + hashmap | O(N) | O(N) | count[prefix-k] |

---

## Pattern Identification

Negatives rule out sliding window. prefix[j]-prefix[i]=k ⇒ for each j add the count of prefix value (prefix-k) seen so far.

---

## Solution (Python)

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    prefix = count = 0
    for n in nums:
        prefix += n
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Negative numbers
- k = 0
- Seed seen[0]=1 for prefixes from index 0

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Prefix Sum](../../../01-patterns/prefix-sum.md)
- Related questions: `contiguous-array`, `subarray-sums-divisible-by-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
