# Linked List Cycle  ·  LeetCode #141

**Pattern:** Fast & Slow Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Detect a cycle → slow 1x, fast 2x; they meet iff cycle**

---

## Problem

Return True if the linked list has a cycle.

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

def has_cycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
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

- Pattern sheet: [Fast & Slow Pointers](../../../01-patterns/fast-slow-pointers.md)
- Related questions: `linked-list-cycle-ii`, `middle-of-linked-list`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
