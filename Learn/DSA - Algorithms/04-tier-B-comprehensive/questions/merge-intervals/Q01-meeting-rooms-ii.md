# Meeting Rooms II  ·  LeetCode #253

**Pattern:** Merge Intervals
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Min rooms for overlapping meetings → min-heap of end times**

---

## Problem

Return the minimum number of conference rooms required.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Heap | O(N log N) | O(N) | reuse room when freed |
| Sweep line | O(N log N) | O(N) | starts/ends events |

---

## Pattern Identification

Sort by start; a min-heap of end times lets us reuse a room whenever the earliest meeting has ended.

---

## Solution (Python)

```python
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    ends = []
    for start, end in intervals:
        if ends and ends[0] <= start:
            heapq.heappop(ends)                  # reuse a freed room
        heapq.heappush(ends, end)
    return len(ends)
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

- Pattern sheet: [Merge Intervals](../../../01-patterns/merge-intervals.md)
- Related questions: `meeting-rooms`, `employee-free-time`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
