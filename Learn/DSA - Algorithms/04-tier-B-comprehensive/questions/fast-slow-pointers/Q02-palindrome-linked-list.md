# Palindrome Linked List  ·  LeetCode #234

**Pattern:** Fast & Slow Pointers
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **List palindrome in O(1) space → find middle, reverse half, compare**

---

## Problem

Return True if the linked list is a palindrome, ideally O(1) space.

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

def is_palindrome(head) -> bool:
    slow = fast = head
    while fast and fast.next:                    # find middle
        slow = slow.next
        fast = fast.next.next
    prev = None                                  # reverse second half
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True
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
