# Kth Smallest Element in a Sorted Matrix  ·  LeetCode #378

**Pattern:** K-way Merge
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Kth smallest across sorted rows → heap of row heads (or binary search on value)**

---

## Problem

Find the kth smallest element in an `n×n` matrix with sorted rows and columns.

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

def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[r][0], r, 0) for r in range(min(k, n))]
    heapq.heapify(heap)
    val = 0
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val
```

**Complexity:** Time O(K log N), Space O(N).

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
- Related questions: `merge-k-sorted-lists`, `find-k-pairs-smallest-sums`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
