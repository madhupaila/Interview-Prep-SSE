# Min Cost to Connect All Points  ·  LeetCode #1584

**Pattern:** Union-Find
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **MST over points → Kruskal with Union-Find (or Prim)**

---

## Problem

Connect all points with minimum total Manhattan-distance cost (MST).

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

Connect all with min cost = Minimum Spanning Tree; Kruskal sorts edges and unions disjoint components.

---

## Solution (Python)

```python
def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
            edges.append((d, i, j))
    edges.sort()
    total = used = 0
    for d, i, j in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
            total += d
            used += 1
            if used == n - 1:
                break
    return total
```

**Complexity:** Time O(N^2 log N), Space O(N^2).

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

- Pattern sheet: [Union-Find](../../../01-patterns/union-find.md)
- Related questions: `number-of-provinces`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
