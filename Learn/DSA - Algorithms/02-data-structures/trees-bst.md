# Trees & Binary Search Trees

Hierarchical structure. Binary tree: ≤2 children. BST: left < node < right, enabling O(log N) ops when balanced.

---

## Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

## Traversals

```python
# DFS (recursive)
def inorder(root):                 # BST → sorted order
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def preorder(root):                # root first (serialize)
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):               # children first (delete, bubble-up)
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

# BFS (level order)
from collections import deque
def level_order(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
    return out
```

---

## BST Operations

```python
def search_bst(root, target):
    while root:
        if root.val == target: return root
        root = root.left if target < root.val else root.right
    return None

def insert_bst(root, val):
    if not root: return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

| Operation | Balanced BST | Skewed BST |
|-----------|--------------|------------|
| Search/Insert/Delete | O(log N) | O(N) |
| Inorder (sorted) | O(N) | O(N) |

---

## Key Facts for Interviews

- **Inorder of BST = sorted** → validates BST, finds kth smallest.
- **Height** drives recursion depth (space O(H)).
- **Balanced** trees: AVL, Red-Black (Python has none built-in; `sortedcontainers.SortedList` fills the gap).
- Validate BST by passing **(low, high)** bounds, not just comparing parent.

```python
def is_valid_bst(root, low=float('-inf'), high=float('inf')):
    if not root: return True
    if not (low < root.val < high): return False
    return (is_valid_bst(root.left, low, root.val) and
            is_valid_bst(root.right, root.val, high))
```

---

## Pitfalls

- Deep recursion on skewed trees → `sys.setrecursionlimit`.
- Validating BST with only immediate-child comparison is wrong — use bounds.

---

## Related Patterns

- [Tree DFS](../01-patterns/tree-dfs.md), [Tree BFS](../01-patterns/tree-bfs.md), [Backtracking](../01-patterns/backtracking.md)
