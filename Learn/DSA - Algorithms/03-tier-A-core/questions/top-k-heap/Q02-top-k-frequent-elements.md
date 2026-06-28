# Top K Frequent Elements  ·  LeetCode #347

**Pattern:** Top-K Heap
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Uber

---

## Memory Hook (Recognition Cue)

> **K most frequent → Counter + heap (or bucket sort O(N))**

---

## Problem

Return the `k` most frequent elements.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Heap | O(N log K) | O(N) | nlargest on freq |
| Bucket sort | O(N) | O(N) | index by frequency |

---

## Pattern Identification

Cue maps to **Top-K Heap** — see [pattern sheet](../../../01-patterns/top-k-heap.md).

---

## Solution (Python)

```python
from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    return [v for v, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
```

**Complexity:** Time O(N log K), Space O(N).

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
- Related questions: `kth-largest-element`, `top-k-frequent-words`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
