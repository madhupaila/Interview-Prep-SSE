# Pattern: Top-K Elements (Heap)

## Recognition Cues

- "**K** largest / smallest / most frequent / closest"
- "Kth largest/smallest"
- A streaming **running median** or top-k over a stream
- Need quick access to the current min or max repeatedly

## Core Idea

Maintain a heap of size **K**. For "K largest" use a **min-heap** of size K (pop the smallest when it grows past K) — the root is the Kth largest. Python's `heapq` is a min-heap; negate for max behavior.

---

## Templates

### K largest with a size-K min-heap

```python
import heapq

def k_largest(nums: list[int], k: int) -> list[int]:
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)      # drop smallest → keep K largest
    return heap                       # heap[0] is the Kth largest
```

### Top-K frequent

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [v for v, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
```

### Two-heap running median

```python
class MedianFinder:
    def __init__(self):
        self.low = []    # max-heap (negated)
        self.high = []   # min-heap

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Need K extremes, not full sort | Need everything sorted → just sort O(N log N) |
| Streaming / online top-k | K ≈ N → sorting is simpler |

## Complexity

- Build/maintain: **O(N log K)**; full heapify O(N). Median ops O(log N).
- Space: **O(K)**.

## Variants & Pitfalls

- **K closest points to origin**, **K closest to a value**, **reorganize string**, **task scheduler**.
- **Quickselect** gives O(N) average for "Kth largest" without a heap.
- Pitfall: for "K largest" use a **min**-heap (counter-intuitive) so you evict the smallest.

## Linked Questions

- Tier A: Kth Largest Element, Top K Frequent Elements, K Closest Points to Origin
- Tier B: Find Median from Data Stream, Task Scheduler, Reorganize String
- Tier C: Sliding Window Median, IPO, Find K Pairs with Smallest Sums

## Related

- [K-way Merge](k-way-merge.md) · [Heaps DS](../02-data-structures/heaps-priority-queue.md)
