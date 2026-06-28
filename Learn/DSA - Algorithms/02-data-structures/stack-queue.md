# Stack & Queue

LIFO and FIFO structures. Both O(1) at their working ends.

---

## Stack (LIFO) — use a Python `list`

```python
stack = []
stack.append(x)      # push  O(1)
stack.pop()          # pop   O(1)
stack[-1]            # peek  O(1)
not stack            # empty?
```

**Uses:** matching parentheses, monotonic stack, DFS (iterative), expression evaluation, undo.

```python
def valid_parentheses(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

---

## Queue (FIFO) — use `collections.deque`

```python
from collections import deque
q = deque()
q.append(x)          # enqueue  O(1)
q.popleft()          # dequeue  O(1)
q[0]                 # front
```

> Do **not** use `list.pop(0)` — it's O(N). Use `deque`.

**Uses:** BFS, level-order traversal, sliding-window (monotonic deque), task scheduling.

---

## Monotonic Deque (sliding window max)

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()                 # store indices, values decreasing
    out = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:       # out of window
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

---

## Two stacks → queue / two queues → stack

Common design question. A queue from two stacks: push to `in`, pop by transferring to `out` when empty (amortized O(1)).

---

## Complexity

| Structure | Push | Pop | Peek |
|-----------|------|-----|------|
| Stack (list) | O(1) | O(1) | O(1) |
| Queue (deque) | O(1) | O(1) | O(1) |

---

## Related Patterns

- [Monotonic Stack](../01-patterns/monotonic-stack.md), [Tree BFS](../01-patterns/tree-bfs.md), [Graph BFS/DFS](../01-patterns/graph-traversal.md)
