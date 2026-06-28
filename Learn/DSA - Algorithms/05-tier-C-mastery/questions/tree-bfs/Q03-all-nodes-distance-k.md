# All Nodes Distance K in Binary Tree  ·  LeetCode #863

**Pattern:** Tree BFS
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Distance K from a node → build parent links, BFS outward**

---

## Problem

Return all node values at distance `k` from a target node.

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

Treat the tree as an undirected graph (add parent edges), then BFS k steps from the target.

---

## Solution (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict

def distance_k(root, target, k: int) -> list[int]:
    graph = defaultdict(list)
    def build(node, parent):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        build(node.left, node)
        build(node.right, node)
    build(root, None)
    seen = {target.val}
    q = deque([(target.val, 0)])
    res = []
    while q:
        val, d = q.popleft()
        if d == k:
            res.append(val)
            continue
        for nb in graph[val]:
            if nb not in seen:
                seen.add(nb)
                q.append((nb, d + 1))
    return res
```

**Complexity:** Time O(N), Space O(N).

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

- Pattern sheet: [Tree BFS](../../../01-patterns/tree-bfs.md)
- Related questions: `level-order-traversal`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
