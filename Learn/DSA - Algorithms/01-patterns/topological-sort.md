# Pattern: Topological Sort

## Recognition Cues

- "**Order** tasks/courses with **prerequisites/dependencies**"
- "Is there a valid ordering?" / "detect a cycle in a **directed** graph"
- Build order, compile order, course schedule
- DAG (directed acyclic graph) implied

## Core Idea

**Kahn's algorithm (BFS):** compute in-degrees; start from nodes with in-degree 0; repeatedly remove a node and decrement neighbors' in-degrees. If you can't process all nodes, there's a cycle.

---

## Template (Kahn's BFS)

```python
from collections import deque, defaultdict

def topo_sort(num_nodes: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    indeg = [0] * num_nodes
    for u, v in edges:                 # edge u -> v (u before v)
        graph[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(num_nodes) if indeg[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == num_nodes else []   # [] = cycle
```

### DFS variant (post-order + cycle check)

```python
def topo_dfs(num_nodes, graph):
    state = [0] * num_nodes            # 0=unseen,1=visiting,2=done
    order = []
    def dfs(u):
        if state[u] == 1:
            return False               # back-edge → cycle
        if state[u] == 2:
            return True
        state[u] = 1
        for v in graph[u]:
            if not dfs(v):
                return False
        state[u] = 2
        order.append(u)
        return True
    for u in range(num_nodes):
        if not dfs(u):
            return []
    return order[::-1]
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Directed dependencies, ordering | Undirected connectivity → Union-Find/DFS |
| Cycle detection in DAG context | Weighted shortest path → Dijkstra |

## Complexity

- Time: **O(V + E)**. Space: **O(V + E)**.

## Variants & Pitfalls

- **Course Schedule I/II**, **Alien Dictionary**, **Minimum Height Trees** (trim leaves), **Parallel Courses**.
- Pitfall: "no valid order" means a cycle — return `[]` and check `len(order) == num_nodes`.

## Linked Questions

- Tier A: Course Schedule, Course Schedule II
- Tier B: Alien Dictionary, Minimum Height Trees, Sequence Reconstruction
- Tier C: Parallel Courses III, Sort Items by Groups Respecting Dependencies

## Related

- [Graph BFS/DFS](graph-traversal.md) · [Union-Find](union-find.md)
