# Populating Next Right Pointers in Each Node  ·  LeetCode #116

**Pattern:** Tree BFS
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Connect level neighbors → use established next pointers, O(1) space**

---

## Problem

Connect each node's `next` to its right neighbor on the same level (perfect binary tree).

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

Cue maps to **Tree BFS** — see [pattern sheet](../../../01-patterns/tree-bfs.md).

---

## Solution (Python)

```python
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    leftmost = root
    while leftmost and leftmost.left:
        node = leftmost
        while node:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next
        leftmost = leftmost.left
    return root
```

**Complexity:** Time O(N), Space O(1).

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

- Pattern sheet: [Tree BFS](../../../01-patterns/tree-bfs.md)
- Related questions: `level-order-traversal`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
