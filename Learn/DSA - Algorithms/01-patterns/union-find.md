# Pattern: Union-Find (Disjoint Set Union)

## Recognition Cues

- "**Connected components**", "are X and Y connected?"
- "Number of provinces / friend circles / islands (dynamic)"
- Detect a **cycle in an undirected graph**
- "Merge accounts", "redundant connection", Kruskal's MST

## Core Idea

Maintain a forest where each set has a representative root. `find(x)` returns the root (with **path compression**); `union(a, b)` links two roots (by **rank/size**). Near-constant per operation.

---

## Template

```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n                 # number of components

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected → cycle
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Dynamic connectivity, incremental unions | Need shortest path → BFS/Dijkstra |
| Count components, cycle in undirected | Directed ordering → topological sort |
| Kruskal's MST | Need the actual path between nodes |

## Complexity

- Per op: **O(α(N))** ≈ O(1) amortized with compression + rank.
- Space: **O(N)**.

## Variants & Pitfalls

- **Number of Provinces**, **Redundant Connection**, **Accounts Merge**, **Number of Islands II** (online), **Kruskal's MST**.
- Pitfall: `union` returning False (already same root) is the cycle signal in undirected graphs.

## Linked Questions

- Tier A: Number of Provinces, Number of Connected Components
- Tier B: Redundant Connection, Accounts Merge, Graph Valid Tree
- Tier C: Number of Islands II, Most Stones Removed, Minimize Malware Spread

## Related

- [Graph BFS/DFS](graph-traversal.md) · [Union-Find DS](../02-data-structures/union-find.md)
