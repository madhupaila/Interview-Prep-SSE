# Binary Tree Paths  ·  LeetCode #257

**Pattern:** Tree DFS
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Apple

---

## Memory Hook (Recognition Cue)

> **All root-to-leaf paths → DFS building path strings**

---

## Problem

Return all root-to-leaf paths as strings.

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

def binary_tree_paths(root) -> list[str]:
    res = []
    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            res.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return res
```

**Complexity:** Time O(N), Space O(H).

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
- Related questions: `path-sum-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
