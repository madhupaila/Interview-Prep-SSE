# Path Sum II  ·  LeetCode #113

**Pattern:** Tree DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **All root-to-leaf paths summing to target → backtracking DFS**

---

## Problem

Return all root-to-leaf paths where the sum equals `targetSum`.

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

def path_sum(root, target: int) -> list[list[int]]:
    res = []
    def dfs(node, remaining, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remaining == node.val:
            res.append(path[:])
        else:
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
        path.pop()
    dfs(root, target, [])
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
- Related questions: `path-sum`, `path-sum-iii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
