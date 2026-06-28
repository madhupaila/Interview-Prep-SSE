# Pattern Master Index

All ~24 interview patterns at a glance. Each row: the **cue** that triggers it, the **idea**, and **complexity**. Memorize the cue column — that is pattern recognition.

> Workflow: read problem → scan this table for a matching cue → open the pattern sheet → recall template → adapt → code.

---

## Arrays / Sequences

| Pattern | Recognition cue | Idea | Typical complexity |
|---------|-----------------|------|--------------------|
| [Two Pointers](two-pointers.md) | Sorted, pair/triplet, in-place | Pointers from ends or same direction | O(N) |
| [Sliding Window](sliding-window.md) | Contiguous subarray/substring + max/min/count | Expand/shrink window | O(N) |
| [Prefix Sum](prefix-sum.md) | Subarray sum=K, range queries, negatives | Cumulative sums + hashmap | O(N) |
| [Cyclic Sort](cyclic-sort.md) | Values in [1..n], missing/duplicate | Place value at its index | O(N) |
| [Merge Intervals](merge-intervals.md) | Overlapping intervals, scheduling | Sort by start, sweep | O(N log N) |
| [Monotonic Stack](monotonic-stack.md) | Next/prev greater/smaller, histogram | Maintain ordered stack | O(N) |
| [Matrix Traversal](matrix-traversal.md) | Spiral/rotate/transpose grid | Index arithmetic, layers | O(R·C) |

## Searching / Selection

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Binary Search](binary-search.md) | Sorted, or minimize-max / maximize-min | Halve search space / answer space | O(log N) / O(N log range) |
| [Top-K Heap](top-k-heap.md) | K largest/smallest/frequent, running median | Size-K heap / two heaps | O(N log K) |
| [K-way Merge](k-way-merge.md) | Merge K sorted inputs | Min-heap of heads | O(N log K) |

## Linked Lists

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Fast & Slow Pointers](fast-slow-pointers.md) | Cycle, middle, happy number | 1x and 2x speed pointers | O(N), O(1) space |
| [LL Reversal](linked-list-reversal.md) | Reverse list/sublist/k-group | Pointer rewiring | O(N), O(1) space |

## Trees & Graphs

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Tree BFS](tree-bfs.md) | Level order, views, min depth | Queue, level by level | O(N) |
| [Tree DFS](tree-dfs.md) | Path sums, diameter, LCA, validate | Recurse + combine children | O(N) |
| [Graph BFS/DFS](graph-traversal.md) | Islands, components, shortest unweighted | Queue/recursion + visited | O(V+E) |
| [Topological Sort](topological-sort.md) | Dependencies/ordering, DAG, cycle | In-degree (Kahn) / DFS post-order | O(V+E) |
| [Union-Find](union-find.md) | Dynamic connectivity, undirected cycle | DSU with compression+rank | O(α(N)) per op |

## Recursion / Enumeration

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Backtracking](backtracking.md) | Generate all / constraint satisfy / small N | Choose-explore-undo | O(2^N), O(N!) |
| [Subsets & Combinations](subsets-combinations.md) | Power set, permutations, combos | Specialized backtracking | O(N·2^N), O(N·N!) |

## Optimization

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Dynamic Programming](dynamic-programming.md) | Count ways / min-max + overlapping subproblems | State + recurrence + memo/table | states × transition |
| [Greedy](greedy.md) | Local optimum → global, sort then pick | Greedy choice + exchange argument | O(N log N) |

## Bit / Math

| Pattern | Recognition cue | Idea | Complexity |
|---------|-----------------|------|------------|
| [Bit Manipulation](bit-manipulation.md) | Single number, set bits, masks | XOR/AND/OR tricks | O(1) / O(2^N) subsets |
| [Trie](trie.md) | Prefix search, dictionary, autocomplete | Char tree | O(L) per word |
| [Interview Math](math-tricks.md) | GCD, primes, fast pow, digits | Number-theory snippets | varies |

---

## Recall Buckets (group for memory)

Group the 24 into **6 zones** for memorization (see [memory-map-master.md](memory-map-master.md)):

1. **Linear scan** — Two Pointers, Sliding Window, Prefix Sum, Cyclic Sort, Monotonic Stack
2. **Sorted/Select** — Binary Search, Top-K Heap, K-way Merge, Merge Intervals
3. **Linked List** — Fast/Slow, Reversal
4. **Tree/Graph** — Tree BFS, Tree DFS, Graph BFS/DFS, Topological Sort, Union-Find
5. **Enumerate** — Backtracking, Subsets/Combinations
6. **Optimize/Bit** — DP, Greedy, Bit Manipulation, Trie, Math, Matrix

---

## Related

- [Pattern Recognition Decision Tree](01-pattern-recognition-decision-tree.md)
- [Cue Dictionary](02-cue-dictionary.md)
- [Flashcards](memory-map-flashcards.md)
- [One-Page Poster](memory-map-visual-one-page.md)
