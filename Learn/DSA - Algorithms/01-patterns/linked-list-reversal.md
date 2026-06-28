# Pattern: In-place Linked List Reversal

## Recognition Cues

- "Reverse a linked list" (whole, sub-list, or in **groups of k**)
- Rearrange nodes **without extra space** (O(1))
- Reorder / rotate a linked list

## Core Idea

Walk the list maintaining `prev`, `cur`, and `next` pointers, flipping each `cur.next` to point backward. No new nodes are created — just pointer rewiring.

---

## Templates

### Reverse entire list

```python
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next        # save
        cur.next = prev       # flip
        prev = cur            # advance
        cur = nxt
    return prev               # new head
```

### Reverse a sub-list [m, n] / groups of k

```python
def reverse_k_group(head, k):
    # check there are k nodes
    node, count = head, 0
    while node and count < k:
        node, count = node.next, count + 1
    if count < k:
        return head
    # reverse first k
    prev, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    head.next = reverse_k_group(cur, k)   # head is now tail of this group
    return prev
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Pointer rewiring, O(1) space | Random access needed → convert to array |
| Reverse / reorder / rotate lists | Doubly-linked with prev already available (simpler) |

## Complexity

- Time: **O(N)**. Space: **O(1)** (iterative) or O(N/k) recursion stack for k-group.

## Variants & Pitfalls

- **Reverse Nodes in k-Group**, **Reverse between positions m..n**, **Rotate List**, **Reorder List** (find middle → reverse second half → merge).
- Pitfall: always save `next` before flipping; use a **dummy head** when the head itself may change.

## Linked Questions

- Tier A: Reverse Linked List, Reorder List
- Tier B: Reverse Linked List II, Swap Nodes in Pairs, Rotate List
- Tier C: Reverse Nodes in k-Group

## Related

- [Fast & Slow Pointers](fast-slow-pointers.md) · [Linked List DS](../02-data-structures/linked-list.md)
