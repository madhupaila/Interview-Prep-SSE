# Pattern Recognition Decision Tree

The skill that wins interviews: **read a problem → identify the pattern in under 60 seconds.** Walk this tree top-down.

---

## Master Decision Tree

```mermaid
flowchart TD
  Start[Read problem + note constraints] --> Q1{Data structure?}

  Q1 -->|Array / String| Arr{What is asked?}
  Q1 -->|Linked List| LL{Cycle or reverse?}
  Q1 -->|Tree| Tree{Level or path?}
  Q1 -->|Graph / Grid| Graph{What relation?}
  Q1 -->|Intervals| MI[Merge Intervals]
  Q1 -->|Need all configs| BT[Backtracking / Subsets]

  Arr -->|Contiguous subarray + max/min/count| SW[Sliding Window]
  Arr -->|Sorted + pair/triplet| TP[Two Pointers]
  Arr -->|Subarray sum=K / range sum| PS[Prefix Sum]
  Arr -->|Values in 1..n / missing| CS[Cyclic Sort]
  Arr -->|Next greater/smaller| MS[Monotonic Stack]
  Arr -->|Sorted lookup / min-max feasible| BS[Binary Search]
  Arr -->|K largest/smallest/frequent| HK[Top-K Heap]
  Arr -->|Count ways / min-max + overlap| DP[Dynamic Programming]
  Arr -->|Local pick proven optimal| GR[Greedy]

  LL -->|Cycle / middle| FS[Fast and Slow]
  LL -->|Reverse sublist/k-group| LR[LL Reversal]

  Tree -->|Level by level / views| TB[Tree BFS]
  Tree -->|Path / subtree / LCA| TD[Tree DFS]

  Graph -->|Shortest unweighted| GB[BFS]
  Graph -->|Weighted shortest| DJ[Dijkstra]
  Graph -->|Components / connectivity| UF[Union-Find]
  Graph -->|Ordering with deps| TS[Topological Sort]
  Graph -->|Islands / reachability| GD[DFS / BFS]
```

---

## Quick Routing Rules (memorize these 12)

| If the problem says… | Pattern |
|----------------------|---------|
| "contiguous subarray/substring" + longest/shortest/max | **Sliding Window** |
| "sorted array" + "two numbers / pair / triplet" | **Two Pointers** |
| "subarray sum equals K" (with negatives) | **Prefix Sum + Hashmap** |
| "numbers from 1 to n" + missing/duplicate | **Cyclic Sort** |
| "next greater / warmer / span / histogram" | **Monotonic Stack** |
| "sorted" + search OR "minimize the max / Kth" | **Binary Search** |
| "K largest / smallest / most frequent / median" | **Heap** |
| "merge K sorted" | **K-way Merge** |
| "intervals" + overlap/merge/rooms | **Merge Intervals** |
| "all subsets / permutations / combinations / N-Queens" | **Backtracking** |
| "min/max cost, number of ways" + reuse | **DP** |
| "prerequisites / build order / cycle in directed" | **Topological Sort** |

---

## Tie-Breakers (when two patterns fit)

| Conflict | Decide by |
|----------|-----------|
| Sliding Window vs Prefix Sum | Negatives present → Prefix Sum; all-positive contiguous → Sliding Window |
| Two Pointers vs Hashmap | Sorted/in-place → Two Pointers; unsorted O(N) lookup → Hashmap |
| DP vs Greedy | Can you prove greedy? If counterexample exists → DP |
| DP vs Backtracking | Need count/optimum → DP; need the actual configurations → Backtracking |
| Union-Find vs DFS | Many dynamic unions/queries → Union-Find; one-shot components → DFS |
| BFS vs Dijkstra | Unweighted → BFS; weighted (non-negative) → Dijkstra |

---

## 60-Second Recognition Drill

1. What is the **input type**? (array, list, tree, graph, intervals)
2. What is the **goal verb**? (find, count, generate, order, optimize)
3. Any **magic words**? (sorted, contiguous, K, prefix, prerequisite, all)
4. What does **N** allow? (see complexity table in [foundations](../00-foundations/01-how-to-approach-any-problem.md))
5. State: "This looks like **<pattern>** because **<cue>**."

---

## Related

- [Cue Dictionary](02-cue-dictionary.md) — exhaustive keyword → pattern table
- [Pattern Master Index](00-pattern-master-index.md)
- [Flashcards](memory-map-flashcards.md)
