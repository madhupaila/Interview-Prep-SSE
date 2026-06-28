# Pattern: Graph BFS / DFS

## Recognition Cues

- Grid / matrix "islands", "regions", "flood fill"
- "Connected components", "shortest path in unweighted graph" (BFS)
- "Can you reach", "clone graph", "number of ways to traverse"
- Explicit graph (edges) or implicit (grid neighbors, word ladder)

## Core Idea

Visit nodes, marking visited to avoid cycles. **BFS** (queue) finds shortest paths in unweighted graphs and explores level by level. **DFS** (recursion/stack) is natural for connectivity, components, and backtracking-style exploration.

---

## Templates

### Grid DFS (count islands)

```python
def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
            return
        grid[r][c] = '0'                     # mark visited
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r + dr, c + dc)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

### BFS shortest path (unweighted)

```python
from collections import deque

def bfs_shortest(graph, start, target):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        node, dist = q.popleft()
        if node == target:
            return dist
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, dist + 1))
    return -1
```

### Dijkstra (weighted shortest path)

```python
import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist.get(node, float('inf')):
            continue
        for nbr, w in graph[node]:
            nd = d + w
            if nd < dist.get(nbr, float('inf')):
                dist[nbr] = nd
                heapq.heappush(pq, (nd, nbr))
    return dist
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| BFS: unweighted shortest path, level spread | Weighted shortest path → Dijkstra |
| DFS: components, reachability, flood fill | Dependency ordering → topological sort |
| Dijkstra: non-negative weights | Negative weights → Bellman-Ford |

## Complexity

- BFS/DFS: **O(V + E)**. Dijkstra: **O(E log V)**. Space: O(V).

## Variants & Pitfalls

- **Number of Islands**, **Clone Graph**, **Rotting Oranges** (multi-source BFS), **Word Ladder**, **Pacific Atlantic**, **Network Delay Time** (Dijkstra).
- Pitfall: mark visited when **enqueuing** (BFS) to avoid duplicates; raise recursion limit for deep DFS.

## Linked Questions

- Tier A: Number of Islands, Clone Graph, Max Area of Island, Flood Fill
- Tier B: Rotting Oranges, Pacific Atlantic Water Flow, Course Schedule, Word Ladder, Network Delay Time
- Tier C: Word Ladder II, Cheapest Flights Within K Stops, Swim in Rising Water

## Related

- [Topological Sort](topological-sort.md) · [Union-Find](union-find.md) · [Graphs DS](../02-data-structures/graphs.md)
