# Minimum Depth of Binary Tree  ·  LeetCode #111

**Pattern:** Tree BFS
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Facebook

---

## Memory Hook (Recognition Cue)

> **Shortest root-to-leaf → BFS returns at first leaf**

---

## Problem

Return the minimum depth (nodes on shortest root-to-leaf path).

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

def min_depth(root) -> int:
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if not node.left and not node.right:
            return d
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right, d + 1))
    return 0
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
- Related questions: `max-depth-binary-tree`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
