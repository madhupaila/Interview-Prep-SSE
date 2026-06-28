# Add Two Numbers  ·  LeetCode #2

**Pattern:** Linked List Reversal
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft, Adobe

---

## Memory Hook (Recognition Cue)

> **Add digit lists with carry → build new list**

---

## Problem

Add two numbers represented as reversed-digit linked lists; return the sum list.

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

def add_two_numbers(l1, l2):
    dummy = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1:
            s += l1.val; l1 = l1.next
        if l2:
            s += l2.val; l2 = l2.next
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next
```

**Complexity:** Time O(max(M,N)), Space O(max(M,N)).

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
- Related questions: `add-two-numbers-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
