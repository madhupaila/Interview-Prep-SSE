# Average of Levels in Binary Tree  ·  LeetCode #637

**Pattern:** Tree BFS
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Facebook

---

## Memory Hook (Recognition Cue)

> **Per-level aggregate → BFS sum each level**

---

## Problem

Return the average value of nodes on each level.

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

Cue maps to **Tree BFS** — see [pattern sheet](../../../01-patterns/tree-bfs.md).

---

## Solution (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def average_of_levels(root) -> list[float]:
    res, q = [], deque([root])
    while q:
        total = 0
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            total += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(total / n)
    return res
```

**Complexity:** Time O(N), Space O(W).

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
