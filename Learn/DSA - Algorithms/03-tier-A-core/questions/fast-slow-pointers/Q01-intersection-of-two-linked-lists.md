# Intersection of Two Linked Lists  ·  LeetCode #160

**Pattern:** Fast & Slow Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Find merge node → switch heads after reaching end (equalize length)**

---

## Problem

Return the node where two singly linked lists intersect, or None.

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

Cue maps to **Fast & Slow Pointers** — see [pattern sheet](../../../01-patterns/fast-slow-pointers.md).

---

## Solution (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```

**Complexity:** Time O(M+N), Space O(1).

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

- Pattern sheet: [Fast & Slow Pointers](../../../01-patterns/fast-slow-pointers.md)
- Related questions: `linked-list-cycle-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
