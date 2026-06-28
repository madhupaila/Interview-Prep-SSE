# Pattern: Fast & Slow Pointers (Floyd's Cycle Detection)

## Recognition Cues

- **Linked list** cycle detection / find cycle start
- Find the **middle** of a linked list in one pass
- "Happy number", or any **functional graph** (each node has one next)
- Detect a cycle in a sequence defined by `next = f(cur)`

## Core Idea

Move `slow` one step and `fast` two steps. If there's a cycle they meet; if `fast` hits the end, no cycle. Distance math lets you also find the cycle's start and the midpoint.

---

## Templates

### Detect cycle + find start

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None                 # no cycle
    slow = head
    while slow is not fast:          # both move 1 step → meet at start
        slow = slow.next
        fast = fast.next
    return slow
```

### Find middle

```python
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow                      # second middle for even length
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Linked list cycle / midpoint | Array random access available → indices |
| O(1) space required | You can use a visited set (simpler, O(N) space) |
| Functional iteration `x = f(x)` | Multiple "next" edges → real graph traversal |

## Complexity

- Time: **O(N)**. Space: **O(1)**.

## Variants & Pitfalls

- **Happy Number:** apply digit-square-sum as `f`; cycle ⇒ not happy.
- **Palindrome linked list:** find middle, reverse second half, compare.
- Pitfall: check `fast and fast.next` to avoid `None.next` errors.

## Linked Questions

- Tier A: Linked List Cycle, Middle of Linked List, Happy Number
- Tier B: Linked List Cycle II (start), Palindrome Linked List, Reorder List
- Tier C: Find the Duplicate Number (cycle in array), Circular Array Loop

## Related

- [In-place Linked List Reversal](linked-list-reversal.md) · [Cyclic Sort](cyclic-sort.md)
