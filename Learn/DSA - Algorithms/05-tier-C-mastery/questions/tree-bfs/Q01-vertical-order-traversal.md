# Binary Tree Vertical Order Traversal  ·  LeetCode #314

**Pattern:** Tree BFS
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Group by column → BFS tracking column index**

---

## Problem

Return node values grouped by column, left to right.

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

from collections import defaultdict, deque

def vertical_order(root):
    if not root:
        return []
    cols = defaultdict(list)
    q = deque([(root, 0)])
    min_c = max_c = 0
    while q:
        node, c = q.popleft()
        cols[c].append(node.val)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    return [cols[c] for c in range(min_c, max_c + 1)]
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
