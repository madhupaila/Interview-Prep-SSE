# Merge Two Sorted Lists (Recursive)  ·  LeetCode #21

**Pattern:** Linked List Reversal
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Recursive list build → pick smaller head, recurse**

---

## Problem

Merge two sorted linked lists recursively.

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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val <= l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    l2.next = merge_two_lists(l1, l2.next)
    return l2
```

**Complexity:** Time O(M+N), Space O(M+N) stack.

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
- Related questions: `merge-two-sorted-lists`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
