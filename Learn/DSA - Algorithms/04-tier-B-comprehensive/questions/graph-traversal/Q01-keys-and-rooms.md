# Keys and Rooms  ·  LeetCode #841

**Pattern:** Graph BFS/DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Can visit all rooms → DFS from room 0**

---

## Problem

Return True if all rooms are reachable starting from room 0 (rooms hold keys).

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

Cue maps to **Graph BFS/DFS** — see [pattern sheet](../../../01-patterns/graph-traversal.md).

---

## Solution (Python)

```python
def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    seen = set()
    stack = [0]
    while stack:
        r = stack.pop()
        if r in seen:
            continue
        seen.add(r)
        for key in rooms[r]:
            if key not in seen:
                stack.append(key)
    return len(seen) == len(rooms)
```

**Complexity:** Time O(V+E), Space O(V).

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

- Pattern sheet: [Graph BFS/DFS](../../../01-patterns/graph-traversal.md)
- Related questions: `number-of-islands`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
