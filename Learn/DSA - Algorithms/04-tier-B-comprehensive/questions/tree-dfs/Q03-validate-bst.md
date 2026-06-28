# Validate Binary Search Tree  ·  LeetCode #98

**Pattern:** Tree DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Is it a BST → pass (low, high) bounds down**

---

## Problem

Return True if the binary tree is a valid BST.

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

Comparing only with the immediate parent is insufficient; thread min/max bounds so every node respects all ancestors.

---

## Solution (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root) -> bool:
    def valid(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float('-inf'), float('inf'))
```

**Complexity:** Time O(N), Space O(H).

---

## Edge Cases & Pitfalls

- Equal values not allowed
- Single node valid

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Tree DFS](../../../01-patterns/tree-dfs.md)
- Related questions: `kth-smallest-in-bst`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
