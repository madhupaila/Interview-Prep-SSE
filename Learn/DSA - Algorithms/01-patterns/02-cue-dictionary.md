# Cue Dictionary — Problem Keywords → Pattern

The fastest lookup: find the **phrase** the problem uses, get the **pattern**. Skim this until the mappings are automatic.

---

## Keyword → Pattern

| Phrase / keyword in the problem | Pattern to reach for |
|---------------------------------|----------------------|
| "sorted array" + "pair / two sum / triplet" | Two Pointers |
| "reverse" + "in place" / "two ends" | Two Pointers |
| "longest / shortest substring" | Sliding Window |
| "maximum sum subarray of size k" | Sliding Window (fixed) |
| "at most K distinct" | Sliding Window (variable) |
| "anagram / permutation in string" | Sliding Window + Counter |
| "subarray sum equals K" | Prefix Sum + Hashmap |
| "range sum" / "sum between i and j" | Prefix Sum |
| "product of array except self" | Prefix/Suffix products |
| "numbers in range 1..n" / "missing / duplicate" | Cyclic Sort |
| "first missing positive" | Cyclic Sort |
| "next greater / next warmer / stock span" | Monotonic Stack |
| "largest rectangle / trapping rain water" | Monotonic Stack |
| "valid parentheses / balanced" | Stack |
| "search in sorted / rotated sorted" | Binary Search |
| "minimize the maximum / maximize the minimum" | Binary Search on Answer |
| "Kth smallest / largest in sorted matrix" | Binary Search / Heap |
| "K most frequent / K closest / Kth largest" | Heap (Top-K) |
| "median of a stream" | Two Heaps |
| "merge K sorted lists/arrays" | K-way Merge |
| "intervals overlap / merge / insert" | Merge Intervals |
| "meeting rooms / min rooms" | Merge Intervals + Heap |
| "linked list has a cycle / find middle" | Fast & Slow Pointers |
| "happy number" | Fast & Slow Pointers |
| "reverse linked list / k-group / swap pairs" | LL Reversal |
| "level order / level by level / zigzag / right view" | Tree BFS |
| "root to leaf / path sum / diameter / LCA" | Tree DFS |
| "validate BST / kth smallest in BST" | Tree DFS (inorder) |
| "number of islands / regions / flood fill" | Graph DFS/BFS |
| "shortest path (unweighted) / min steps" | BFS |
| "shortest path with weights" | Dijkstra |
| "course schedule / build order / prerequisites" | Topological Sort |
| "connected components / friend circles / provinces" | Union-Find |
| "redundant connection / cycle in undirected" | Union-Find |
| "accounts merge" | Union-Find |
| "generate all subsets / power set" | Subsets (backtracking) |
| "all permutations / combinations" | Backtracking |
| "combination sum / partition / N-Queens / Sudoku" | Backtracking |
| "word search on board" | Backtracking (+ Trie for many words) |
| "number of ways / min cost / can you reach" + reuse | Dynamic Programming |
| "longest increasing subsequence" | DP (or patience sort) |
| "edit distance / LCS / distinct subsequences" | 2D DP (strings) |
| "coin change / knapsack / partition equal subset" | DP (knapsack) |
| "house robber / climbing stairs / decode ways" | 1D DP |
| "jump game / gas station / partition labels" | Greedy |
| "single number / appears once" | Bit Manipulation (XOR) |
| "count bits / power of two" | Bit Manipulation |
| "prefix search / autocomplete / word dictionary" | Trie |
| "spiral / rotate image / set zeroes" | Matrix Traversal |
| "gcd / primes / pow(x,n) / sqrt" | Interview Math |

---

## Constraint → Approach (size cue)

| Constraint | Hint |
|------------|------|
| N ≤ 12 | Backtracking / permutations (O(N!)) |
| N ≤ 20 | Subsets / bitmask DP (O(2^N)) |
| N ≤ 500 | O(N^3) DP acceptable |
| N ≤ 5,000 | O(N^2) DP/loops |
| N ≤ 10^5–10^6 | O(N log N) / O(N): sort, heap, two pointers, sliding window, hashing |
| Answer "mod 1e9+7" | Counting DP / combinatorics |
| "in place", "O(1) space" | Two pointers, cyclic sort, bit tricks |

---

## Anti-cues (don't be fooled)

- "Subarray sum" **with negatives** → NOT sliding window → Prefix Sum + Hashmap.
- "Greedy looks right" → verify with a counterexample; many need DP.
- "Sorted output of permutations" → sort input + skip duplicates in backtracking.
- "K ≈ N" for top-K → just sort, skip the heap.

---

## Related

- [Pattern Recognition Decision Tree](01-pattern-recognition-decision-tree.md)
- [Pattern Master Index](00-pattern-master-index.md)
- [Flashcards](memory-map-flashcards.md)
