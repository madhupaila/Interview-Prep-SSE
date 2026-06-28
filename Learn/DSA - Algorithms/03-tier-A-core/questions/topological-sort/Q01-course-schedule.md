# Course Schedule  ·  LeetCode #207

**Pattern:** Topological Sort
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Can finish all with prerequisites → detect cycle via Kahn's**

---

## Problem

Return True if you can finish all courses given prerequisite pairs.

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

Cue maps to **Topological Sort** — see [pattern sheet](../../../01-patterns/topological-sort.md).

---

## Solution (Python)

```python
from collections import deque, defaultdict

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    indeg = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indeg[course] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    seen = 0
    while q:
        node = q.popleft()
        seen += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return seen == num_courses
```

**Complexity:** Time O(V+E), Space O(V+E).

---

## Edge Cases & Pitfalls

- Cycle → False
- No prereqs → True

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Topological Sort](../../../01-patterns/topological-sort.md)
- Related questions: `course-schedule-ii`, `alien-dictionary`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
