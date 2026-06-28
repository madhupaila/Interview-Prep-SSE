# Find K Pairs with Smallest Sums  ·  LeetCode #373

**Pattern:** K-way Merge
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Smallest k pair sums from two sorted arrays → heap seeded with first column**

---

## Problem

Return the `k` pairs `(u,v)` from two sorted arrays with the smallest sums.

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

Cue maps to **K-way Merge** — see [pattern sheet](../../../01-patterns/k-way-merge.md).

---

## Solution (Python)

```python
import heapq

def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    if not nums1 or not nums2:
        return []
    heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
    heapq.heapify(heap)
    res = []
    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return res
```

**Complexity:** Time O(K log K), Space O(K).

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

- Pattern sheet: [K-way Merge](../../../01-patterns/k-way-merge.md)
- Related questions: `kth-smallest-in-sorted-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
