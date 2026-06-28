# Reverse Nodes in k-Group  ·  LeetCode #25

**Pattern:** Linked List Reversal
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Meta, Microsoft, Google

---

## Memory Hook (Recognition Cue)

> **Reverse every k nodes → count k, reverse block, recurse/link**

---

## Problem

Reverse the list nodes `k` at a time; leftover tail (< k) stays as is.

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

Confirm k nodes exist, reverse exactly k by pointer flipping, then connect the reversed block's tail to the recursively-processed remainder.

---

## Solution (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k: int):
    node = head
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head                              # fewer than k → leave as is
    prev, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    head.next = reverse_k_group(cur, k)          # head is now tail of group
    return prev
```

**Complexity:** Time O(N), Space O(N/k) recursion.

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
- Related questions: `reverse-linked-list-ii`, `swap-nodes-in-pairs`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
