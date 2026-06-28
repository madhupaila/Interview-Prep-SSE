# Sliding Window Maximum  ·  LeetCode #239

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Max of each fixed window → monotonic decreasing deque of indices**

---

## Problem

Return the maximum of each contiguous window of size `k`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Heap | O(N log N) | O(N) | lazy delete |
| Monotonic deque | O(N) | O(k) | front is window max |

---

## Pattern Identification

We need the running max as the window slides — a monotonic deque keeps candidates in decreasing order so the front is always the max.

---

## Solution (Python)

```python
from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()                                # indices, values decreasing
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
```

**Complexity:** Time O(N), Space O(k).

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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `sliding-window-median`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
