# Number of Islands II  ·  LeetCode #305

**Pattern:** Union-Find
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Islands count after each addLand (online) → Union-Find dynamic**

---

## Problem

After each land addition, return the current number of islands.

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

Each new land starts as its own island; merging with existing neighbors decrements the count.

---

## Solution (Python)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

def num_islands2(m: int, n: int, positions: list[list[int]]) -> list[int]:
    dsu = DSU(m * n)
    land = set()
    res = []
    count = 0
    for r, c in positions:
        idx = r * n + c
        if idx in land:
            res.append(count)
            continue
        land.add(idx)
        count += 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            nidx = nr * n + nc
            if 0 <= nr < m and 0 <= nc < n and nidx in land:
                if dsu.union(idx, nidx):
                    count -= 1
        res.append(count)
    return res
```

**Complexity:** Time O(K α), Space O(M·N).

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
- Related questions: `number-of-islands`, `redundant-connection`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
