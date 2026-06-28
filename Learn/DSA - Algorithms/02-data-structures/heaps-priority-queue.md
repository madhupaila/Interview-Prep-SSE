# Heaps & Priority Queue

A binary heap gives O(log N) insert/extract of the min (or max). Python's `heapq` is a **min-heap** over a list.

---

## heapq Basics

```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
heapq.heappop(h)          # 1 (smallest)  O(log N)
h[0]                      # peek min       O(1)
heapq.heapify(arr)        # build heap     O(N)
heapq.heappushpop(h, x)   # push then pop  O(log N)
heapq.heapreplace(h, x)   # pop then push
heapq.nlargest(k, arr)    # O(N log k)
heapq.nsmallest(k, arr)
```

### Max-heap: negate values

```python
heapq.heappush(h, -val)
largest = -heapq.heappop(h)
```

### Heap of tuples (priority, item)

```python
heapq.heappush(h, (dist, node))    # sorts by dist, then node
```

---

## Patterns Built on Heaps

| Goal | Technique |
|------|-----------|
| K largest | size-K min-heap |
| K smallest | size-K max-heap (negate) |
| Streaming median | two heaps (low max, high min) |
| Merge K sorted | heap of list heads |
| Dijkstra | heap of (dist, node) |
| Task scheduling | heap by priority/time |

```python
# Kth largest (size-K min-heap)
def kth_largest(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for n in nums[k:]:
        if n > h[0]:
            heapq.heapreplace(h, n)
    return h[0]
```

---

## Complexity

| Operation | Cost |
|-----------|------|
| push / pop | O(log N) |
| peek | O(1) |
| heapify | O(N) |
| nlargest/nsmallest(k) | O(N log k) |

---

## Pitfalls

- `heapq` is min-only; negate for max behavior.
- Tuples with non-comparable second elements crash on ties — add a unique tiebreaker (e.g., an incrementing counter or index).
- `heapify` is O(N), cheaper than N pushes.

---

## Related Patterns

- [Top-K Heap](../01-patterns/top-k-heap.md), [K-way Merge](../01-patterns/k-way-merge.md), [Graph BFS/DFS (Dijkstra)](../01-patterns/graph-traversal.md)
