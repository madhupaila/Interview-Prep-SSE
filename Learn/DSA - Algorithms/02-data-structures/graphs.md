# Graphs

Vertices + edges. Master the **representations** and the two core traversals (BFS, DFS); most graph problems build on them.

---

## Representations

```python
from collections import defaultdict

# Adjacency list (most common)
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)          # omit for directed

# Weighted
wgraph = defaultdict(list)
for u, v, w in edges:
    wgraph[u].append((v, w))

# Adjacency matrix (dense / small V)
matrix = [[0] * V for _ in range(V)]
matrix[u][v] = 1
```

| Representation | Space | Edge check | Iterate neighbors |
|----------------|-------|------------|-------------------|
| Adjacency list | O(V+E) | O(deg) | O(deg) |
| Adjacency matrix | O(V^2) | O(1) | O(V) |

---

## Traversals

```python
from collections import deque

def bfs(graph, start):
    seen, q = {start}, deque([start])
    while q:
        node = q.popleft()
        for nbr in graph[node]:
            if nbr not in seen:
                seen.add(nbr)
                q.append(nbr)

def dfs(graph, node, seen):
    seen.add(node)
    for nbr in graph[node]:
        if nbr not in seen:
            dfs(graph, nbr, seen)
```

---

## Algorithm Cheat Sheet

| Problem | Algorithm | Complexity |
|---------|-----------|-----------|
| Traverse / components | BFS / DFS | O(V+E) |
| Shortest path, unweighted | BFS | O(V+E) |
| Shortest path, non-negative weights | Dijkstra | O(E log V) |
| Shortest path, negative weights | Bellman-Ford | O(V·E) |
| All-pairs shortest path | Floyd-Warshall | O(V^3) |
| Ordering with dependencies | Topological Sort | O(V+E) |
| Dynamic connectivity | Union-Find | O(α(N)) |
| Minimum spanning tree | Kruskal / Prim | O(E log V) |

---

## Grid as Graph

A grid cell `(r,c)` connects to its 4 (or 8) neighbors. Most "islands/maze" problems are graph traversals in disguise.

```python
for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...
```

---

## Pitfalls

- Mark visited at **enqueue** time in BFS to avoid duplicates in the queue.
- Directed vs undirected: only add the reverse edge for undirected.
- Deep DFS → recursion limit; consider iterative stack.

---

## Related Patterns

- [Graph BFS/DFS](../01-patterns/graph-traversal.md), [Topological Sort](../01-patterns/topological-sort.md), [Union-Find](../01-patterns/union-find.md)
