# Reorder List  ·  LeetCode #143

**Pattern:** Fast & Slow Pointers
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **L0→Ln→L1→Ln-1... → find middle, reverse second half, merge**

---

## Problem

Reorder list to L0→Ln→L1→Ln-1→… in place.

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

def reorder_list(head) -> None:
    if not head or not head.next:
        return
    slow = fast = head                           # find middle
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next                           # reverse second half
    slow.next = None
    prev = None
    while second:
        second.next, prev, second = prev, second, second.next
    first, second = head, prev                   # merge alternately
    while second:
        first.next, first = second, first.next
        second.next, second = first, second.next
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
- Related questions: `middle-of-linked-list`, `reverse-linked-list`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
