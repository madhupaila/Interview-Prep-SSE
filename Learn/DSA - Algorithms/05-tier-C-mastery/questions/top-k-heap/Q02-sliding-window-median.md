# Sliding Window Median  ·  LeetCode #480

**Pattern:** Top-K Heap
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Median of each window → two heaps with lazy deletion (or SortedList)**

---

## Problem

Return the median of each window of size `k`.

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
import bisect

def median_sliding_window(nums: list[int], k: int) -> list[float]:
    window = sorted(nums[:k])
    res = []
    def median():
        if k % 2:
            return float(window[k // 2])
        return (window[k // 2 - 1] + window[k // 2]) / 2
    res.append(median())
    for i in range(k, len(nums)):
        window.pop(bisect.bisect_left(window, nums[i - k]))
        bisect.insort(window, nums[i])
        res.append(median())
    return res
```

**Complexity:** Time O(N·K), Space O(K).

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
- Related questions: `find-median-from-data-stream`, `sliding-window-maximum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
