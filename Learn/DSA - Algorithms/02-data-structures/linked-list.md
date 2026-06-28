# Linked List

Nodes linked by pointers. O(1) insert/delete at a known position; O(N) search. Interview favorite for pointer manipulation.

---

## Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

---

## Core Operations

```python
# Traverse
node = head
while node:
    print(node.val)
    node = node.next

# Insert after a node
new = ListNode(5)
new.next = node.next
node.next = new

# Delete next node
if node.next:
    node.next = node.next.next
```

### Dummy head idiom (avoids edge cases when head changes)

```python
def remove_elements(head, val):
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
```

---

## Complexity

| Operation | Singly LL |
|-----------|-----------|
| Access kth | O(N) |
| Insert/delete at known node | O(1) |
| Search | O(N) |
| Prepend | O(1) |

---

## Interview Techniques

- **Dummy head** when the head may change.
- **Two pointers** (fast/slow) for cycle/middle.
- **Reverse** by pointer flipping (O(1) space).
- **Runner** technique for "nth from end" (advance one pointer n steps first).

```python
def nth_from_end(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    while fast:
        fast, slow = fast.next, slow.next
    return slow
```

---

## Pitfalls

- Losing the rest of the list — save `next` before rewiring.
- Null checks: `while fast and fast.next` for two-pointer.
- Forgetting to return `dummy.next`, not `dummy`.

---

## Related Patterns

- [Fast & Slow Pointers](../01-patterns/fast-slow-pointers.md), [LL Reversal](../01-patterns/linked-list-reversal.md), [K-way Merge](../01-patterns/k-way-merge.md)
