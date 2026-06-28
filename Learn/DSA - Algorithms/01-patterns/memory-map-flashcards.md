# DSA Pattern Flashcards (Cue → Pattern → Template)

**How to use:** Cover the right two columns. Read the cue. Say the **pattern** + **template anchor** in <5 seconds. Check. Mark misses for tomorrow. Target **55/60** before interviewing.

---

## Z1 — Linear Scan

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 1 | Sorted array, find pair summing to target | Two Pointers | `left/right`, move by comparison |
| 2 | Remove duplicates in place from sorted | Two Pointers | read/write pointers |
| 3 | Longest substring without repeating | Sliding Window | expand right, shrink left on dup |
| 4 | Max sum subarray of size k | Sliding Window (fixed) | add right, subtract `i-k` |
| 5 | At most K distinct chars | Sliding Window | shrink while `len(count) > k` |
| 6 | Subarray sum equals K (negatives) | Prefix Sum + Hashmap | `count += seen[prefix-k]` |
| 7 | Range sum queries, immutable | Prefix Sum | `prefix[j+1]-prefix[i]` |
| 8 | Array values 1..n, find missing | Cyclic Sort | swap to index `v-1` |
| 9 | First missing positive | Cyclic Sort | place valid, scan |
| 10 | Next greater element / temperatures | Monotonic Stack | pop while breaks order |
| 11 | Largest rectangle in histogram | Monotonic Stack | increasing stack + sentinel |
| 12 | Valid parentheses | Stack | push open, match close |

## Z2 — Sorted / Select

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 13 | Search in sorted array | Binary Search | `lo<=hi`, shrink half |
| 14 | Search in rotated sorted | Binary Search | find sorted half |
| 15 | Min capacity / Koko bananas / ship in D days | Binary Search on Answer | `feasible(mid)` monotonic |
| 16 | Kth largest element | Heap (size-K) | min-heap, pop > K |
| 17 | Top K frequent | Heap + Counter | `nlargest(k, freq)` |
| 18 | Median from data stream | Two Heaps | low max-heap, high min-heap |
| 19 | Merge K sorted lists | K-way Merge | heap of heads |
| 20 | Merge overlapping intervals | Merge Intervals | sort by start, extend end |
| 21 | Minimum meeting rooms | Intervals + Heap | min-heap of end times |

## Z3 — Linked List

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 22 | Detect cycle in linked list | Fast & Slow | meet ⇒ cycle |
| 23 | Find middle of list | Fast & Slow | fast 2x |
| 24 | Happy number | Fast & Slow | cycle on digit-sq-sum |
| 25 | Reverse linked list | LL Reversal | flip `cur.next` |
| 26 | Reverse in k-groups | LL Reversal | reverse k, recurse |
| 27 | Reorder list | Fast/Slow + Reverse + Merge | middle → reverse → zip |

## Z4 — Tree / Graph

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 28 | Level order / zigzag / right view | Tree BFS | `for _ in range(len(q))` |
| 29 | Min depth of tree | Tree BFS | return at first leaf |
| 30 | Path sum / root-to-leaf | Tree DFS | subtract along path |
| 31 | Diameter / max path sum | Tree DFS | bubble up height + global |
| 32 | Validate BST | Tree DFS | pass min/max bounds |
| 33 | LCA | Tree DFS | return found subtrees |
| 34 | Number of islands | Graph DFS | flood fill, mark visited |
| 35 | Shortest path unweighted | BFS | queue + dist |
| 36 | Rotting oranges | Multi-source BFS | enqueue all sources |
| 37 | Network delay / weighted shortest | Dijkstra | heap `(dist, node)` |
| 38 | Course schedule / build order | Topological Sort | in-degree queue |
| 39 | Connected components / provinces | Union-Find | find + union |
| 40 | Redundant connection | Union-Find | union returns False ⇒ cycle |

## Z5 — Enumerate

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 41 | All subsets / power set | Subsets | `dfs(start)`, append copy |
| 42 | All permutations | Backtracking | `used[]` set |
| 43 | Combination sum | Backtracking | reuse → `dfs(i)`, else `dfs(i+1)` |
| 44 | Generate parentheses | Backtracking | track open/close counts |
| 45 | N-Queens / Sudoku | Backtracking | constraint sets, undo |
| 46 | Word search on board | Backtracking | DFS + visited mark |
| 47 | Palindrome partitioning | Backtracking | cut + recurse |

## Z6 — Optimize / Bit / Misc

| # | Cue | Pattern | Template anchor |
|---|-----|---------|-----------------|
| 48 | Climbing stairs / house robber | 1D DP | `prev, cur = cur, max(...)` |
| 49 | Coin change / knapsack | DP knapsack | reverse inner loop (0/1) |
| 50 | Longest common subsequence | 2D DP | grid `dp[i][j]` |
| 51 | Edit distance | 2D DP | insert/delete/replace |
| 52 | Longest increasing subsequence | DP / patience | `bisect` on tails |
| 53 | Word break | DP | `dp[i]` reachable |
| 54 | Jump game | Greedy | track furthest reach |
| 55 | Partition labels / gas station | Greedy | last index / running sum |
| 56 | Single number | Bit XOR | XOR all |
| 57 | Counting bits / power of two | Bit | `x & (x-1)` |
| 58 | Prefix search / autocomplete | Trie | children dict + is_word |
| 59 | Spiral / rotate image | Matrix | transpose + reverse |
| 60 | Pow(x, n) / sqrt | Math | binary exponentiation |

---

## Drill scorecard

| Date | Score /60 | Misses (note pattern numbers) |
|------|-----------|-------------------------------|
| | | |

**Daily routine:** 5 min flashcards → 5 min write one template from memory → 5 min identify-only on 3 random problem titles. (See [daily-drill-protocol.md](../07-study-schedule/daily-drill-protocol.md).)

---

## Related

- [Master Memory Map](memory-map-master.md) · [One-Page Poster](memory-map-visual-one-page.md)
- [Decision Tree](01-pattern-recognition-decision-tree.md) · [Cue Dictionary](02-cue-dictionary.md)
