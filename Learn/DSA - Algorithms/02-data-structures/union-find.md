# Union-Find (Disjoint Set Union)

Tracks a partition of elements into disjoint sets with near-O(1) `find` and `union`. The go-to for dynamic connectivity.

---

## Implementation (path compression + union by rank)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n                 # number of disjoint sets

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:  # path compression
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False               # already connected
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

---

## Complexity

| Operation | Cost |
|-----------|------|
| find / union | O(α(N)) ≈ O(1) amortized |
| Space | O(N) |

(α is the inverse Ackermann function — effectively constant.)

---

## When to Use

| Use | Signal |
|-----|--------|
| Count connected components | "how many groups" |
| Detect cycle in **undirected** graph | union returns False |
| Dynamic merging (online) | edges added over time |
| Kruskal's MST | sort edges, union if not connected |
| Group equivalences | accounts merge, equations |

---

## String / arbitrary keys

Map keys to integer ids (or use a dict-based parent):

```python
parent = {}
def find(x):
    parent.setdefault(x, x)
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
```

---

## Pitfalls

- Without compression + rank, it degrades to O(N) chains.
- Union-Find gives connectivity, **not** the path between nodes — use BFS for paths.

---

## Related Patterns

- [Union-Find pattern](../01-patterns/union-find.md), [Graph BFS/DFS](../01-patterns/graph-traversal.md)
