# Path Sum III  ·  LeetCode #437

**Pattern:** Tree DFS
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Count downward paths summing to target → prefix-sum hashmap on the path**

---

## Problem

Count paths (any node to any descendant) summing to `targetSum`.

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

Combine Tree DFS with the Subarray-Sum-Equals-K prefix-sum trick along the current root-to-node path.

---

## Solution (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

def path_sum_iii(root, target: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    def dfs(node, prefix):
        if not node:
            return 0
        prefix += node.val
        res = count[prefix - target]
        count[prefix] += 1
        res += dfs(node.left, prefix) + dfs(node.right, prefix)
        count[prefix] -= 1                       # backtrack
        return res
    return dfs(root, 0)
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
- Related questions: `path-sum-ii`, `subarray-sum-equals-k`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
