# Pattern: Merge Intervals

## Recognition Cues

- Input is a list of **intervals** `[start, end]`
- "merge overlapping", "insert interval", "free time", "meeting rooms"
- Anything about **overlaps**, **conflicts**, or **scheduling**

## Core Idea

**Sort by start.** Then sweep once: if the current interval overlaps the last kept one (`cur.start <= last.end`), merge by extending `last.end`; otherwise append a new interval.

---

## Template

```python
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:          # overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

### Min meeting rooms (sweep / heap)

```python
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    ends = []                                # min-heap of end times
    for start, end in intervals:
        if ends and ends[0] <= start:
            heapq.heappop(ends)              # reuse a room
        heapq.heappush(ends, end)
    return len(ends)
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Intervals + overlap/merge/insert | Points without ranges |
| Scheduling, calendars, ranges | Graph of dependencies → topological sort |

## Complexity

- Time: **O(N log N)** (the sort). Sweep is O(N).
- Space: **O(N)** output (or O(rooms) for the heap variant).

## Variants & Pitfalls

- **Insert Interval:** add the new one, then merge (or 3-phase: before / overlap / after).
- **Interval intersection:** two-pointer over two sorted lists.
- Pitfall: decide if touching intervals `[1,2],[2,3]` count as overlapping (usually yes for merge).

## Linked Questions

- Tier A: Merge Intervals, Insert Interval, Meeting Rooms
- Tier B: Meeting Rooms II, Interval List Intersections, Non-overlapping Intervals
- Tier C: Employee Free Time, Minimum Number of Arrows to Burst Balloons

## Related

- [Greedy](greedy.md) · [Top-K Heap](top-k-heap.md) · [Sorting cheat](../00-foundations/02-complexity-big-o.md)
