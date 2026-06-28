# Binary Tree Level Order Traversal  ·  LeetCode #102

**Pattern:** Tree BFS
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Group nodes by level → BFS, snapshot queue length per level**

---

## Problem

Return node values level by level (top to bottom).

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

def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out
```

**Complexity:** Time O(N), Space O(W).

---

## Edge Cases & Pitfalls

- Empty tree → []
- Snapshot len(q) before inner loop

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Tree BFS](../../../01-patterns/tree-bfs.md)
- Related questions: `zigzag-level-order`, `right-side-view`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
