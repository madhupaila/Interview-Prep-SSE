# Master Memory Map — DSA Patterns

**Print this page.** Groups all 24 patterns into **6 recall zones** with mnemonics so you can reconstruct the whole toolkit from memory.

> Start with [How to Approach Any Problem (UMPIRE)](../00-foundations/01-how-to-approach-any-problem.md). Daily drill: [Flashcards](memory-map-flashcards.md) + [One-Page Poster](memory-map-visual-one-page.md).

---

## The 6 Zones (mnemonic: **L-S-L-T-E-O**)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    SENIOR DSA PATTERN MEMORY MAP                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ SOLVE FLOW (UMPIRE)                                                          │
│   Understand → Match pattern → Plan → Implement → Review → Evaluate         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Z1 LINEAR SCAN                                                              │
│   Two Pointers (sorted pair/in-place) │ Sliding Window (contiguous + min/max)│
│   Prefix Sum (subarray sum=K, negatives) │ Cyclic Sort (values 1..n)         │
│   Monotonic Stack (next greater/smaller)                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Z2 SORTED / SELECT                                                          │
│   Binary Search (sorted OR minimize-max) │ Top-K Heap (k largest/median)     │
│   K-way Merge (merge k sorted) │ Merge Intervals (overlap, sort by start)    │
├──────────────────────────────────────────────────────────────────────────────┤
│ Z3 LINKED LIST                                                              │
│   Fast & Slow (cycle, middle) │ Reversal (k-group, sublist, O(1) space)     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Z4 TREE / GRAPH                                                            │
│   Tree BFS (levels) │ Tree DFS (paths/LCA) │ Graph BFS-DFS (islands)         │
│   Topological Sort (deps/DAG) │ Union-Find (components, undirected cycle)    │
│   Dijkstra (weighted shortest)                                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ Z5 ENUMERATE                                                               │
│   Backtracking (all configs, constraints) │ Subsets/Combinations/Permutations│
├──────────────────────────────────────────────────────────────────────────────┤
│ Z6 OPTIMIZE / BIT / MISC                                                   │
│   DP (state+recurrence+memo) │ Greedy (sort+local pick) │ Bit (XOR/masks)    │
│   Trie (prefix) │ Matrix (spiral/rotate) │ Math (gcd/pow/primes)            │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Zone Router (hear cue → name zone in <5s)

| Hear… | Zone | First pattern to consider |
|-------|------|---------------------------|
| sorted, pair, contiguous, subarray, next-greater | **Z1** | Two Pointers / Sliding Window |
| sorted-search, K-th, merge-k, intervals | **Z2** | Binary Search / Heap |
| linked list, cycle, reverse | **Z3** | Fast-Slow / Reversal |
| tree, graph, islands, prerequisites, components | **Z4** | DFS/BFS / Topo / Union-Find |
| all subsets, permutations, N-Queens | **Z5** | Backtracking |
| ways/min-max + reuse, XOR, prefix-tree | **Z6** | DP / Bit / Trie |

---

## One-line template recall per pattern

| Pattern | Template anchor |
|---------|-----------------|
| Two Pointers | `left, right = 0, n-1; move based on comparison` |
| Sliding Window | `for right: add; while invalid: remove left; update` |
| Prefix Sum | `seen[0]=1; prefix+=n; count+=seen[prefix-k]` |
| Cyclic Sort | `while nums[i]!=nums[nums[i]-1]: swap` |
| Monotonic Stack | `while stack and breaks order: pop+resolve; push` |
| Binary Search | `while lo<=hi: mid; shrink toward target` |
| Top-K Heap | `size-K min-heap; pop when > K` |
| K-way Merge | `heap of (val, list_idx, elem_idx)` |
| Merge Intervals | `sort by start; if start<=last.end: merge` |
| Fast & Slow | `slow=next; fast=next.next; meet⇒cycle` |
| LL Reversal | `prev=None; flip cur.next; advance` |
| Tree BFS | `q=deque; for _ in range(len(q)): process level` |
| Tree DFS | `recurse children; combine; return vs global` |
| Graph DFS | `mark visited; recurse 4 dirs / neighbors` |
| Topo Sort | `indegree; queue 0s; pop+decrement` |
| Union-Find | `find w/ compression; union by rank` |
| Backtracking | `choose → dfs → undo` |
| Subsets | `dfs(start): res.append(path[:]); loop i..n` |
| DP | `define state; recurrence; memo/table` |
| Greedy | `sort; pick local optimum; prove` |
| Bit | `XOR cancels; x&(x-1) clears lowest` |
| Trie | `node.children dict; is_word flag` |

---

## Confidence levels

| Level | You can… |
|-------|----------|
| L1 | Recite the 6 zones + their patterns |
| L2 | Route any problem to a zone in <5s |
| L3 | Recall the template and code it without notes |
| L4 | 45-min mock: identify + optimal solution + complexity |

**Target before interviews:** L3 across Z1–Z4, L2+ on Z5–Z6.

---

## Related

- [Flashcards](memory-map-flashcards.md) · [One-Page Poster](memory-map-visual-one-page.md)
- [Decision Tree](01-pattern-recognition-decision-tree.md) · [Cue Dictionary](02-cue-dictionary.md)
