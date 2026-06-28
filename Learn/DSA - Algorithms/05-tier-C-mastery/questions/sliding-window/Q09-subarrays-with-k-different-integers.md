# Subarrays with K Different Integers  ·  LeetCode #992

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Exactly K distinct = atMost(K) - atMost(K-1)**

---

## Problem

Count contiguous subarrays with exactly `k` distinct integers.

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

'Exactly K' is hard directly; the classic trick is atMost(K) - atMost(K-1), each an easy sliding window.

---

## Solution (Python)

```python
from collections import defaultdict

def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    def at_most(m):
        count = defaultdict(int)
        left = res = 0
        for right, n in enumerate(nums):
            count[n] += 1
            while len(count) > m:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += right - left + 1            # subarrays ending at right
        return res
    return at_most(k) - at_most(k - 1)
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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `longest-substring-k-distinct`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
