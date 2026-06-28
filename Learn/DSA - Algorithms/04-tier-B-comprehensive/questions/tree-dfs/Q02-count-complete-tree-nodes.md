# Count Complete Tree Nodes  ·  LeetCode #222

**Pattern:** Tree DFS
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Count nodes in complete tree → compare left/right heights**

---

## Problem

Count the nodes of a complete binary tree faster than O(N).

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

Cue maps to **Tree DFS** — see [pattern sheet](../../../01-patterns/tree-dfs.md).

---

## Solution (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root) -> int:
    if not root:
        return 0
    def height(node, left):
        h = 0
        while node:
            node = node.left if left else node.right
            h += 1
        return h
    lh = height(root, True)
    rh = height(root, False)
    if lh == rh:
        return (1 << lh) - 1                       # perfect subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)
```

**Complexity:** Time O(log^2 N), Space O(log N).

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

- Pattern sheet: [Tree DFS](../../../01-patterns/tree-dfs.md)
- Related questions: `max-depth-binary-tree`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
