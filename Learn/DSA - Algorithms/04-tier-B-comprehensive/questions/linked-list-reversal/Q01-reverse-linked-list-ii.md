# Reverse Linked List II  ·  LeetCode #92

**Pattern:** Linked List Reversal
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Reverse a sublist [left, right] → dummy + reverse in place**

---

## Problem

Reverse the nodes from position `left` to `right` (1-indexed) and return the head.

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

def reverse_between(head, left: int, right: int):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    for _ in range(right - left):                # repeatedly move cur.next after prev
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next
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

- Pattern sheet: [Linked List Reversal](../../../01-patterns/linked-list-reversal.md)
- Related questions: `reverse-linked-list`, `reverse-nodes-in-k-group`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
