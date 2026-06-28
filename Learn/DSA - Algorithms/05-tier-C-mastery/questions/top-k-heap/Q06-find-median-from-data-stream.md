# Find Median from Data Stream  ·  LeetCode #295

**Pattern:** Top-K Heap
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Running median → two heaps balanced (low max-heap, high min-heap)**

---

## Problem

Design a structure supporting `addNum` and `findMedian` over a stream.

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

Keep the lower half in a max-heap and upper half in a min-heap, balanced in size; the median is at the heap tops.

---

## Solution (Python)

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []                            # max-heap (negated)
        self.high = []                           # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

**Complexity:** Time O(log N) add, O(1) median, Space O(N).

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
- Related questions: `sliding-window-median`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
