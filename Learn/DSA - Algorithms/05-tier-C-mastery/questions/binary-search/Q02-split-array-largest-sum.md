# Split Array Largest Sum  ·  LeetCode #410

**Pattern:** Binary Search
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Minimize the maximum subarray sum over k splits → binary search on the max**

---

## Problem

Split `nums` into `k` non-empty contiguous subarrays minimizing the largest subarray sum.

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

Cue maps to **Binary Search** — see [pattern sheet](../../../01-patterns/binary-search.md).

---

## Solution (Python)

```python
def split_array(nums: list[int], k: int) -> int:
    def splits(cap):
        cnt, cur = 1, 0
        for n in nums:
            if cur + n > cap:
                cnt += 1
                cur = 0
            cur += n
        return cnt
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if splits(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Complexity:** Time O(N log sum), Space O(1).

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

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `capacity-to-ship-packages`, `koko-eating-bananas`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
