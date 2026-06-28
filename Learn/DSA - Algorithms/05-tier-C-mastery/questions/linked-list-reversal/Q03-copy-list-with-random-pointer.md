# Copy List with Random Pointer  ·  LeetCode #138

**Pattern:** Linked List Reversal
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Deep copy with random links → hashmap old→new (or interleave)**

---

## Problem

Deep copy a linked list where each node has an extra random pointer.

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

Cue maps to **Linked List Reversal** — see [pattern sheet](../../../01-patterns/linked-list-reversal.md).

---

## Solution (Python)

```python
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    clones = {}
    cur = head
    while cur:
        clones[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        clones[cur].next = clones.get(cur.next)
        clones[cur].random = clones.get(cur.random)
        cur = cur.next
    return clones[head]
```

**Complexity:** Time O(N), Space O(N).

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

- Pattern sheet: [Linked List Reversal](../../../01-patterns/linked-list-reversal.md)
- Related questions: `clone-graph`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
