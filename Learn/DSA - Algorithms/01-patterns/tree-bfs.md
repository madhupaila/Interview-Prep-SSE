# Pattern: Tree BFS (Level-Order)

## Recognition Cues

- "**Level order**", "level by level", "left/right view", "zigzag"
- "Minimum depth", "connect nodes at same level"
- Anything processing a tree **breadth-first** / by depth layer

## Core Idea

Use a queue. Process the tree level by level: capture the current queue length as the level size, dequeue exactly that many nodes, and enqueue their children.

---

## Template

```python
from collections import deque

def level_order(root) -> list[list[int]]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):          # snapshot this level's size
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out
```

### Zigzag / right-view tweaks

```python
# Zigzag: reverse `level` on alternate depths
# Right view: take level[-1] each iteration
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Need level grouping / shortest depth | Root-to-leaf path sums → DFS |
| Left/right view, zigzag, connect levels | Whole-subtree recursion → DFS |

## Complexity

- Time: **O(N)** (each node once). Space: **O(W)** max width.

## Variants & Pitfalls

- **Average of levels**, **right side view**, **zigzag traversal**, **minimum depth** (return at first leaf), **populate next-right pointers**.
- Pitfall: snapshot `len(q)` **before** the inner loop, or you'll mix levels.

## Linked Questions

- Tier A: Binary Tree Level Order Traversal, Maximum Depth, Average of Levels
- Tier B: Zigzag Level Order, Right Side View, Minimum Depth, Populating Next Right Pointers
- Tier C: Vertical Order Traversal, All Nodes Distance K

## Related

- [Tree DFS](tree-dfs.md) · [Graph BFS/DFS](graph-traversal.md) · [Trees DS](../02-data-structures/trees-bst.md)
