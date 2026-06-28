# K Closest Points to Origin  ·  LeetCode #973

**Pattern:** Top-K Heap
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **K closest → size-K max-heap by distance (negate)**

---

## Problem

Return the `k` closest points to the origin.

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

Cue maps to **Top-K Heap** — see [pattern sheet](../../../01-patterns/top-k-heap.md).

---

## Solution (Python)

```python
import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []                                    # max-heap of (-dist, point)
    for x, y in points:
        d = x * x + y * y
        heapq.heappush(heap, (-d, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [p for _, p in heap]
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

- Pattern sheet: [Top-K Heap](../../../01-patterns/top-k-heap.md)
- Related questions: `kth-largest-element`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
