# Merge k Sorted Lists  ·  LeetCode #23

**Pattern:** K-way Merge
**Tier:** A  ·  **Difficulty:** Hard
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Merge K sorted lists → min-heap of current heads**

---

## Problem

Merge `k` sorted linked lists into one sorted list.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Pairwise merge | O(N log K) | O(1) | divide and conquer |
| Min-heap | O(N log K) | O(K) | heap of heads |

---

## Pattern Identification

Always emit the global minimum among K list heads → a size-K min-heap gives O(log K) per element.

---

## Solution (Python)

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

**Complexity:** Time O(N log K), Space O(K).

---

## Edge Cases & Pitfalls

- Some lists empty
- All empty → None
- Tiebreaker index avoids comparing nodes

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [K-way Merge](../../../01-patterns/k-way-merge.md)
- Related questions: `merge-two-sorted-lists`, `kth-smallest-in-sorted-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)
