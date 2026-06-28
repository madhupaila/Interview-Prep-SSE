# Minimum Height Trees  ·  LeetCode #310

**Pattern:** Topological Sort
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Roots giving min height → trim leaves layer by layer**

---

## Problem

Return all roots that produce a minimum height tree.

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

The centroids of the tree minimize height; peel leaves until ≤2 nodes remain.

---

## Solution (Python)

```python
from collections import defaultdict, deque

def find_min_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    if n == 1:
        return [0]
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    leaves = deque(node for node in range(n) if len(graph[node]) == 1)
    remaining = n
    while remaining > 2:
        size = len(leaves)
        remaining -= size
        for _ in range(size):
            leaf = leaves.popleft()
            nb = graph[leaf].pop()
            graph[nb].discard(leaf)
            if len(graph[nb]) == 1:
                leaves.append(nb)
    return list(leaves)
```

**Complexity:** Time O(V), Space O(V).

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

- Pattern sheet: [Topological Sort](../../../01-patterns/topological-sort.md)
- Related questions: `course-schedule`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
