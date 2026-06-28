# Evaluate Division  ·  LeetCode #399

**Pattern:** Graph BFS/DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **a/b queries from equations → weighted graph DFS product**

---

## Problem

Answer division queries given equations like a/b = 2.0.

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
from collections import defaultdict

def calc_equation(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1 / v
    def dfs(src, dst, seen):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        seen.add(src)
        for nb, w in graph[src].items():
            if nb not in seen:
                res = dfs(nb, dst, seen)
                if res != -1.0:
                    return w * res
        return -1.0
    return [dfs(a, b, set()) for a, b in queries]
```

**Complexity:** Time O(Q·(V+E)), Space O(V+E).

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
- Related questions: `clone-graph`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
