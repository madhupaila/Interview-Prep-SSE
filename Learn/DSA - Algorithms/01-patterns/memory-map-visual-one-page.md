# DSA Patterns — One Page Poster

**Print this. Tape it near your desk. Recite once each morning.**

---

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                  DSA INTERVIEW — ONE PAGE PATTERN MAP                         ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  SOLVE FLOW (UMPIRE): Understand → Match → Plan → Implement → Review → Eval    ║
║  SIZE CUE: N!≤12  2^N≤20  N^3≤500  N^2≤5k  NlogN/N≤1e6                          ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z1 LINEAR SCAN                                                               ║
║   sorted+pair............Two Pointers     contiguous+min/max...Sliding Window  ║
║   subarray sum=K.........Prefix Sum       values 1..n..........Cyclic Sort     ║
║   next greater/smaller...Monotonic Stack                                       ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z2 SORTED / SELECT                                                          ║
║   sorted search / min-max....Binary Search    K largest/median....Heap         ║
║   merge K sorted.............K-way Merge       overlap ranges......Merge Interval║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z3 LINKED LIST                                                              ║
║   cycle / middle.....Fast & Slow      reverse / k-group.....LL Reversal        ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z4 TREE / GRAPH                                                            ║
║   levels.........Tree BFS       paths/LCA.......Tree DFS                        ║
║   islands........Graph DFS/BFS  weighted SP.....Dijkstra                        ║
║   prerequisites..Topo Sort      components......Union-Find                      ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z5 ENUMERATE                                                              ║
║   all configs / constraints....Backtracking   subsets/perms....Subsets         ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  Z6 OPTIMIZE / BIT / MISC                                                  ║
║   ways/min-max+reuse...DP    sort+local pick...Greedy   XOR/masks...Bit         ║
║   prefix tree.........Trie   spiral/rotate.....Matrix   gcd/pow.....Math        ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  TIE-BREAKERS                                                              ║
║   neg numbers? Prefix Sum not Sliding Window                                   ║
║   greedy unprovable? use DP                                                    ║
║   need configs? Backtracking; need count/opt? DP                               ║
║   unweighted? BFS; weighted? Dijkstra                                          ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  ALWAYS SAY: brute force + Big-O → name pattern → code → dry-run → complexity  ║
╚════════════════════════════════════════════════════════════════════════════════╝
```

---

## 10-second router

| Hear… | Pattern family |
|-------|----------------|
| sorted / pair / contiguous / next-greater | **Z1** scan |
| sorted-search / Kth / merge-k / intervals | **Z2** select |
| linked list / cycle / reverse | **Z3** list |
| tree / graph / islands / prereq / components | **Z4** tree-graph |
| all subsets / permutations / N-Queens | **Z5** enumerate |
| ways / min-max + reuse / XOR / prefix-tree | **Z6** optimize |

---

## 7-day pattern sprint

| Day | Memorize zone | Drill |
|-----|---------------|-------|
| 1 | Z1 Linear Scan | Flashcards 1–12 + write 3 templates |
| 2 | Z2 Sorted/Select | Flashcards 13–21 |
| 3 | Z3 + Z4a (lists, tree) | Flashcards 22–33 |
| 4 | Z4b (graph) | Flashcards 34–40 |
| 5 | Z5 Enumerate | Flashcards 41–47 |
| 6 | Z6 Optimize/Bit | Flashcards 48–60 |
| 7 | Full poster blank | Reproduce from memory + 1 mock |

---

## Related

- [Master Memory Map](memory-map-master.md) · [Flashcards](memory-map-flashcards.md)
- [Decision Tree](01-pattern-recognition-decision-tree.md) · [Cue Dictionary](02-cue-dictionary.md)
