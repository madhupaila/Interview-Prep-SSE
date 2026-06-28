# Merge Two Sorted Lists  ·  LeetCode #21

**Pattern:** K-way Merge
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Microsoft, Apple

---

## Memory Hook (Recognition Cue)

> **Merge two sorted lists → dummy head + compare fronts**

---

## Problem

Merge two sorted linked lists into one sorted list.

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

Cue maps to **K-way Merge** — see [pattern sheet](../../../01-patterns/k-way-merge.md).

---

## Solution (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
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

- Pattern sheet: [K-way Merge](../../../01-patterns/k-way-merge.md)
- Related questions: `merge-k-sorted-lists`, `merge-sorted-array`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
