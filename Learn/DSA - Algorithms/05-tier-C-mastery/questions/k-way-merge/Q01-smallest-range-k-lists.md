# Smallest Range Covering Elements from K Lists  ·  LeetCode #632

**Pattern:** K-way Merge
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Smallest range touching all K lists → heap of mins, track current max**

---

## Problem

Find the smallest range that includes at least one number from each of the `k` sorted lists.

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

Maintain one pointer per list; the range is [min in heap, running max]. Advancing the min shrinks the range.

---

## Solution (Python)

```python
import heapq

def smallest_range(nums: list[list[int]]) -> list[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(nums)]
    heapq.heapify(heap)
    cur_max = max(lst[0] for lst in nums)
    best = [float('-inf'), float('inf')]
    while heap:
        val, i, j = heapq.heappop(heap)
        if cur_max - val < best[1] - best[0]:
            best = [val, cur_max]
        if j + 1 == len(nums[i]):
            break                                # a list is exhausted
        nxt = nums[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(heap, (nxt, i, j + 1))
    return best
```

**Complexity:** Time O(N log K), Space O(K).

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
- Related questions: `merge-k-sorted-lists`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
