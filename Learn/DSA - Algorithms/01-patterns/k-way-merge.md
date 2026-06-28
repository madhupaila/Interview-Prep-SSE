# Pattern: K-way Merge

## Recognition Cues

- "Merge **K sorted** lists / arrays"
- "Smallest range covering elements from K lists"
- "Kth smallest in a sorted matrix"
- Combine multiple sorted streams into one sorted output

## Core Idea

Push the **head of each list** into a min-heap. Repeatedly pop the smallest and push the next element from the same list. The heap always holds at most K candidates.

---

## Template

```python
import heapq

def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))   # (value, list_idx, elem_idx)
    out = []
    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
```

### Merge K sorted linked lists

```python
import heapq

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

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Multiple already-sorted inputs | A single array → just sort |
| Need globally sorted merge / kth across lists | Inputs unsorted |

## Complexity

- Time: **O(N log K)** where N = total elements, K = number of lists.
- Space: **O(K)** heap.

## Variants & Pitfalls

- **Kth smallest in sorted matrix** (each row is a sorted list).
- **Smallest range covering K lists** (track current max while popping min).
- Pitfall: include a tiebreaker (list index) in the heap tuple so it never compares nodes directly.

## Linked Questions

- Tier A: Merge Two Sorted Lists, Merge K Sorted Lists
- Tier B: Kth Smallest Element in a Sorted Matrix, Find K Pairs with Smallest Sums
- Tier C: Smallest Range Covering Elements from K Lists, Merge K Sorted Arrays

## Related

- [Top-K Heap](top-k-heap.md) · [Heaps DS](../02-data-structures/heaps-priority-queue.md)
