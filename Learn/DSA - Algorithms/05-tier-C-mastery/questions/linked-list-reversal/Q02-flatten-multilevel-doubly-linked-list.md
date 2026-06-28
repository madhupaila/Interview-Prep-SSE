# Flatten a Multilevel Doubly Linked List  ·  LeetCode #430

**Pattern:** Linked List Reversal
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Flatten child branches inline → DFS with stack**

---

## Problem

Flatten a multilevel doubly linked list so all nodes appear in a single level.

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
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None
    stack = []
    cur = head
    prev = None
    while cur or stack:
        if not cur:
            cur = stack.pop()
        if prev:
            prev.next = cur
            cur.prev = prev
        if cur.child:
            if cur.next:
                stack.append(cur.next)
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
        prev = cur
        cur = cur.next
    return head
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
- Related questions: `reorder-list`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
