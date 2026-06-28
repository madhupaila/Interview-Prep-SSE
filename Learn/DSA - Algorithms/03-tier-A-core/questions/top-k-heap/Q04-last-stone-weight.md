# Last Stone Weight  ·  LeetCode #1046

**Pattern:** Top-K Heap
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Repeatedly smash two largest → max-heap**

---

## Problem

Repeatedly remove the two heaviest stones; return the weight of the last stone (0 if none).

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

def last_stone_weight(stones: list[int]) -> int:
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0
```

**Complexity:** Time O(N log N), Space O(N).

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
