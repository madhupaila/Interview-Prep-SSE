# Invert Binary Tree  ·  LeetCode #226

**Pattern:** Tree DFS
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Mirror a tree → swap children recursively**

---

## Problem

Invert (mirror) a binary tree.

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

def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
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
- Related questions: `same-tree`, `symmetric-tree`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
