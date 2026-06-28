# Top K Frequent Words  ·  LeetCode #692

**Pattern:** Top-K Heap
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Bloomberg

---

## Memory Hook (Recognition Cue)

> **K frequent words, ties alphabetical → heap with custom order**

---

## Problem

Return the `k` most frequent words, ties broken lexicographically.

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
from collections import Counter
import heapq

def top_k_frequent(words: list[str], k: int) -> list[str]:
    freq = Counter(words)
    # heap by (-count, word) so most frequent + lexicographically smallest first
    heap = [(-c, w) for w, c in freq.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
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
- Related questions: `top-k-frequent-elements`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
