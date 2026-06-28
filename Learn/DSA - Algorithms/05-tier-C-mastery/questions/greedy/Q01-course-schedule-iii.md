# Course Schedule III  ·  LeetCode #630

**Pattern:** Greedy
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Max courses by deadline → sort by deadline, max-heap of durations**

---

## Problem

Take the maximum number of courses given (duration, lastDay) constraints.

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

Cue maps to **Greedy** — see [pattern sheet](../../../01-patterns/greedy.md).

---

## Solution (Python)

```python
import heapq

def schedule_course(courses: list[list[int]]) -> int:
    courses.sort(key=lambda c: c[1])
    heap = []                                     # max-heap of durations (negated)
    time = 0
    for dur, last in courses:
        heapq.heappush(heap, -dur)
        time += dur
        if time > last:
            time += heapq.heappop(heap)           # drop the longest course
    return len(heap)
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

- Pattern sheet: [Greedy](../../../01-patterns/greedy.md)
- Related questions: `task-scheduler`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
