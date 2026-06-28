# Count Subarrays With Score Less Than K  ·  LeetCode #2302

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Count windows with sum*len < k → sliding window counting**

---

## Problem

Count subarrays where (sum × length) < k.

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
def count_subarrays(nums: list[int], k: int) -> int:
    left = total = res = 0
    for right, n in enumerate(nums):
        total += n
        while total * (right - left + 1) >= k:
            total -= nums[left]
            left += 1
        res += right - left + 1
    return res
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
- Related questions: `minimum-size-subarray-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
