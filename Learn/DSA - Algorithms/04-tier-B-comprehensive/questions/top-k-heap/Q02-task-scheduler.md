# Task Scheduler  ·  LeetCode #621

**Pattern:** Top-K Heap
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Uber

---

## Memory Hook (Recognition Cue)

> **Schedule with cooldown → greedy on most frequent (heap or formula)**

---

## Problem

Given tasks and cooldown `n`, return the least intervals (with idles) to finish all tasks.

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

The most frequent task dictates the skeleton; idle slots fill the gaps unless there are enough other tasks.

---

## Solution (Python)

```python
from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for f in freq.values() if f == max_freq)
    # fill formula: (max_freq-1) blocks of size (n+1), plus tasks at max_freq
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), intervals)
```

**Complexity:** Time O(N), Space O(1).

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
- Related questions: `reorganize-string`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
