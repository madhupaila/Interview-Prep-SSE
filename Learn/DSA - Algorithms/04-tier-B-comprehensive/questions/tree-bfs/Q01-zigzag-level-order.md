# Binary Tree Zigzag Level Order Traversal  ·  LeetCode #103

**Pattern:** Tree BFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Alternate left-right per level → BFS + reverse on odd depth**

---

## Problem

Return level-order traversal alternating direction each level.

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

def zigzag_level_order(root):
    if not root:
        return []
    out, q, left_to_right = [], deque([root]), True
    while q:
        level = deque()
        for _ in range(len(q)):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(list(level))
        left_to_right = not left_to_right
    return out
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
