# Subtree of Another Tree  ·  LeetCode #572

**Pattern:** Tree DFS
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Is subRoot a subtree → same-tree check at each node**

---

## Problem

Return True if `subRoot` is a subtree of `root`.

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

def is_subtree(root, sub) -> bool:
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)
    if not root:
        return False
    if same(root, sub):
        return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)
```

**Complexity:** Time O(M·N), Space O(H).

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
- Related questions: `same-tree`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
