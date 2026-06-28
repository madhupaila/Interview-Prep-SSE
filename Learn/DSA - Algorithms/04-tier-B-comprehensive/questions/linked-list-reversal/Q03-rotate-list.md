# Rotate List  ·  LeetCode #61

**Pattern:** Linked List Reversal
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Rotate right by k → close into ring, cut at new tail**

---

## Problem

Rotate the list to the right by `k` places.

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

def rotate_right(head, k: int):
    if not head or not head.next or k == 0:
        return head
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head                             # make ring
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head
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
- Related questions: `reverse-linked-list`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
