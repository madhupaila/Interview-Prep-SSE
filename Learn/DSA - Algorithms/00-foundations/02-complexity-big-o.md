# Complexity & Big-O — Interview Cheat Sheet

Big-O describes how runtime/space **grows** with input size N. Interviewers expect you to state it for every solution.

---

## Growth Rates (best → worst)

```
O(1) < O(log N) < O(N) < O(N log N) < O(N^2) < O(N^3) < O(2^N) < O(N!)
```

| Big-O | Name | Example |
|-------|------|---------|
| O(1) | Constant | Hashmap lookup, array index |
| O(log N) | Logarithmic | Binary search, balanced BST op |
| O(N) | Linear | Single loop, sliding window |
| O(N log N) | Linearithmic | Sorting, heap of N items |
| O(N^2) | Quadratic | Nested loops, 2D DP |
| O(2^N) | Exponential | Subsets, naive recursion |
| O(N!) | Factorial | Permutations, brute-force TSP |

---

## How to Compute It

1. **Drop constants:** O(2N) → O(N).
2. **Drop lower-order terms:** O(N^2 + N) → O(N^2).
3. **Different inputs, different variables:** two arrays → O(M + N), not O(N).
4. **Nested loops multiply:** loop in loop → O(N·M).
5. **Sequential loops add:** loop then loop → O(N + M).
6. **Recursion:** branches^depth (e.g., 2^N for two recursive calls of depth N), or use the recurrence.

---

## Amortized Complexity

Some operations are occasionally expensive but cheap on average.

- **Dynamic array append (Python `list.append`):** O(1) amortized (occasional resize is O(N) but rare).
- **Hashmap insert:** O(1) amortized.
- **Two-pointer / sliding window:** each element enters and leaves the window once → O(N) total even with a nested-looking `while`.

---

## Space Complexity

Count **extra** space beyond input:

- Recursion stack counts (depth = stack frames). DFS on a tree → O(H) height.
- Hashmap/array you allocate → O(N).
- In-place algorithms → O(1) auxiliary.

---

## Common Data Structure Operations (Python)

| Structure | Access | Search | Insert | Delete | Notes |
|-----------|--------|--------|--------|--------|-------|
| list (array) | O(1) | O(N) | O(N) end-O(1) amortized | O(N) | `append`/`pop()` end O(1) |
| dict / set | — | O(1) avg | O(1) avg | O(1) avg | hash collisions → O(N) worst |
| deque | O(1) ends | O(N) | O(1) ends | O(1) ends | `collections.deque` |
| heapq (binary heap) | O(1) peek | O(N) | O(log N) | O(log N) pop | min-heap only |
| sorted list (bisect) | O(1) | O(log N) | O(N) | O(N) | insert shifts elements |
| BST (balanced) | O(log N) | O(log N) | O(log N) | O(log N) | not built-in in Python |

---

## Sorting Reference

| Algorithm | Time (avg) | Time (worst) | Space | Stable |
|-----------|-----------|--------------|-------|--------|
| Timsort (Python `sorted`) | O(N log N) | O(N log N) | O(N) | Yes |
| Quicksort | O(N log N) | O(N^2) | O(log N) | No |
| Mergesort | O(N log N) | O(N log N) | O(N) | Yes |
| Heapsort | O(N log N) | O(N log N) | O(1) | No |
| Counting/Radix | O(N + K) | O(N + K) | O(N + K) | Yes |

Python's `sorted()` and `list.sort()` use **Timsort** — stable, O(N log N).

---

## Interview Phrases

> "This is O(N log N) dominated by the sort; the scan after is O(N)."

> "Space is O(N) for the hashmap, or O(1) if I'm allowed to mutate the input."

> "The `while` loop looks nested but each element is visited at most twice, so it's amortized O(N)."

---

## Related

- [How to Approach Any Problem](01-how-to-approach-any-problem.md)
- [Python for Interviews](03-python-for-interviews.md)
