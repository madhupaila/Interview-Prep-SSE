# Reorganize String  ·  LeetCode #767

**Pattern:** Top-K Heap
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **No two adjacent equal → always place the most frequent available**

---

## Problem

Rearrange characters so no two adjacent are equal, or return '' if impossible.

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

def reorganize_string(s: str) -> str:
    freq = Counter(s)
    if max(freq.values()) > (len(s) + 1) // 2:
        return ""
    heap = [(-c, ch) for ch, c in freq.items()]
    heapq.heapify(heap)
    res = []
    prev = None
    while heap:
        cnt, ch = heapq.heappop(heap)
        res.append(ch)
        if prev and prev[0] < 0:
            heapq.heappush(heap, prev)
        prev = (cnt + 1, ch)                      # used one
    return "".join(res)
```

**Complexity:** Time O(N log A), Space O(A).

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
- Related questions: `task-scheduler`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
