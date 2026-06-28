# Pattern: Tree DFS (Recursion)

## Recognition Cues

- "Root-to-leaf **path** sum / count"
- "Diameter", "max path sum", "lowest common ancestor"
- Validate BST, height-balanced, subtree checks
- Anything needing info **bubbled up** from children

## Core Idea

Recurse into children, combine their results at the current node. Decide what each call **returns** (info to parent) vs what it **updates** (a global/closure result). Three orders: pre/in/post.

---

## Templates

### Path sum (top-down)

```python
def has_path_sum(root, target) -> bool:
    if not root:
        return False
    if not root.left and not root.right:      # leaf
        return target == root.val
    rem = target - root.val
    return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)
```

### Bubble-up with a global (diameter / max path sum)

```python
def diameter(root) -> int:
    best = 0
    def depth(node):
        nonlocal best
        if not node:
            return 0
        l, r = depth(node.left), depth(node.right)
        best = max(best, l + r)               # path through this node
        return 1 + max(l, r)                  # height to parent
    depth(root)
    return best
```

### Inorder (BST → sorted)

```python
def inorder(root, out):
    if not root:
        return
    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Path/subtree info, recursion natural | Level grouping → BFS |
| LCA, validate BST, serialize | Very deep tree risks stack overflow (raise recursion limit) |

## Complexity

- Time: **O(N)**. Space: **O(H)** recursion stack (H = height).

## Variants & Pitfalls

- **LCA**, **validate BST** (pass min/max bounds), **path sum II/III**, **serialize/deserialize**, **max path sum** (clamp negatives to 0).
- Pitfall: distinguish the **return value** (to parent) from the **updated global** (answer through a node).

## Linked Questions

- Tier A: Maximum Depth, Same Tree, Invert Tree, Path Sum, Diameter, LCA of BST
- Tier B: Validate BST, Path Sum II, Kth Smallest in BST, Construct from Preorder/Inorder, LCA of Binary Tree
- Tier C: Binary Tree Maximum Path Sum, Serialize/Deserialize, Path Sum III, Count Good Nodes

## Related

- [Tree BFS](tree-bfs.md) · [Backtracking](backtracking.md) · [Trees DS](../02-data-structures/trees-bst.md)
