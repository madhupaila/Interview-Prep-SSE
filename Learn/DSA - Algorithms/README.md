# DSA Patterns Mastery — Interview Prep Guide

**Target:** 3–5 YOE Engineer → **Senior Software Engineer** — DSA coding rounds at top companies (FAANG, Stripe, Uber, etc.)

A structured, pattern-first DSA system: **24 core patterns** (+ matrix traversal & interview math), memorizable Python templates, a **cue → pattern recognition system**, data-structure deep-dives, **313 company-tagged questions** with end-to-end Python solutions, and a **day-wise mastery schedule** — same learning style as the [HLD](../System%20Design%20-%20High%20Level%20Design/README.md), [LLD](../System%20Design%20-%20Low%20Level%20Design/README.md), [Case Studies](../Case%20Studies/README.md), and [React](../Frontend%20-%20React/README.md) tracks.

> **Philosophy:** You don't memorize 450 solutions. You memorize **~24 patterns** and learn to **recognize which pattern a problem wants** within 60 seconds. Patterns at your fingertips → solve anything.

---

## How to Use This Repo

**Start here for confidence + pattern recognition:**
1. [How to Approach Any Problem (UMPIRE)](00-foundations/01-how-to-approach-any-problem.md) — the universal solving framework
2. [Pattern Recognition Decision Tree](01-patterns/01-pattern-recognition-decision-tree.md) + [Cue Dictionary](01-patterns/02-cue-dictionary.md) — read a problem → name the pattern
3. Print [One-Page Pattern Poster](01-patterns/memory-map-visual-one-page.md) + drill [Flashcards](01-patterns/memory-map-flashcards.md) daily (15 min)
4. [Pattern Master Index](01-patterns/00-pattern-master-index.md) — all 22 patterns at a glance

**Then by phase (see [90-Day Plan](07-study-schedule/master-90-day-plan.md)):**
1. **Days 1–5:** [Foundations](00-foundations/) — complexity, Python idioms, framework
2. **Days 6–40:** [Patterns](01-patterns/) + [Data Structures](02-data-structures/) + [Tier A](03-tier-A-core/) (~150 essential)
3. **Days 41–70:** [Tier B](04-tier-B-comprehensive/) (~150 depth)
4. **Days 71–90:** [Tier C](05-tier-C-mastery/) (~150 hard) + mixed mocks + [company drills](06-company-question-index.md)

**Per question flow:** Read → spot cue → name pattern → recall template → code → state complexity → edge cases.

---

## Repository Structure

| Folder | Contents |
|--------|----------|
| [00-foundations/](00-foundations/) | UMPIRE framework, Big-O, Python-for-interviews idioms, round flow, senior signals |
| [01-patterns/](01-patterns/) | **26 pattern master sheets** + recognition decision tree + cue dictionary + 3 memory maps |
| [02-data-structures/](02-data-structures/) | 10 DS concept docs with full Python implementations |
| [03-tier-A-core/](03-tier-A-core/) | **Essential questions** (Blind 75 + NeetCode 150 style) |
| [04-tier-B-comprehensive/](04-tier-B-comprehensive/) | **Depth questions** |
| [05-tier-C-mastery/](05-tier-C-mastery/) | **Hard / variant questions** |
| [06-company-question-index.md](06-company-question-index.md) | Company × question lookup |
| [07-study-schedule/](07-study-schedule/) | 90-day master plan, 4-week Tier-A sprint, daily-drill protocol |

---

## The 22 Patterns

| # | Pattern | Core cue |
|---|---------|----------|
| 1 | [Two Pointers](01-patterns/two-pointers.md) | Sorted array, pair/triplet, in-place |
| 2 | [Sliding Window](01-patterns/sliding-window.md) | Contiguous subarray/substring + max/min/count |
| 3 | [Fast & Slow Pointers](01-patterns/fast-slow-pointers.md) | Cycle, middle, happy number |
| 4 | [Merge Intervals](01-patterns/merge-intervals.md) | Overlapping intervals |
| 5 | [Cyclic Sort](01-patterns/cyclic-sort.md) | Numbers in range [1..n], find missing/duplicate |
| 6 | [In-place Linked List Reversal](01-patterns/linked-list-reversal.md) | Reverse sublist, no extra space |
| 7 | [Binary Search](01-patterns/binary-search.md) | Sorted, or "minimize/maximize feasible value" |
| 8 | [Top-K Heap](01-patterns/top-k-heap.md) | K largest/smallest/frequent/closest |
| 9 | [K-way Merge](01-patterns/k-way-merge.md) | Merge K sorted lists/arrays |
| 10 | [Monotonic Stack](01-patterns/monotonic-stack.md) | Next greater/smaller element |
| 11 | [Tree BFS](01-patterns/tree-bfs.md) | Level-order, level-by-level |
| 12 | [Tree DFS](01-patterns/tree-dfs.md) | Root-to-leaf paths, recursion |
| 13 | [Graph BFS/DFS](01-patterns/graph-traversal.md) | Connected components, traversal |
| 14 | [Topological Sort](01-patterns/topological-sort.md) | Ordering with dependencies / DAG |
| 15 | [Union-Find](01-patterns/union-find.md) | Connectivity, components, cycle in undirected |
| 16 | [Backtracking](01-patterns/backtracking.md) | Generate all / constraints / "is there a way" |
| 17 | [Subsets & Combinations](01-patterns/subsets-combinations.md) | Power set, permutations, combinations |
| 18 | [Dynamic Programming](01-patterns/dynamic-programming.md) | Overlapping subproblems, optimal substructure |
| 19 | [Greedy](01-patterns/greedy.md) | Local optimum → global, sort then pick |
| 20 | [Bit Manipulation](01-patterns/bit-manipulation.md) | XOR tricks, single number, subsets via bits |
| 21 | [Prefix Sum](01-patterns/prefix-sum.md) | Range sum, subarray sum equals K |
| 22 | [Trie](01-patterns/trie.md) | Prefix search, word dictionary, autocomplete |

Plus [Matrix traversal](01-patterns/matrix-traversal.md) and [Interview Math](01-patterns/math-tricks.md).

---

## Question Count

| Tier | Questions | Location |
|------|-----------|----------|
| Tier A — Core | 117 | [03-tier-A-core/](03-tier-A-core/) |
| Tier B — Comprehensive | 107 | [04-tier-B-comprehensive/](04-tier-B-comprehensive/) |
| Tier C — Mastery | 89 | [05-tier-C-mastery/](05-tier-C-mastery/) |
| **Total** | **313** | |

> Counts grow as more questions are added to `_data/` and the generator re-run. Every question has a full Python solution, pattern tag, complexity, and company tags.

---

## Per-Question Template

Every question file includes:

1. Title, company tags, difficulty, **pattern(s)**, tier
2. **Memory hook** — the recognition cue
3. Problem statement + constraints
4. Clarifying questions
5. **Approaches** — brute force → optimal with complexity each
6. **Pattern identification** — which cue maps here and why
7. **End-to-end Python solution** — clean, idiomatic, runnable
8. Complexity (time/space)
9. Edge cases & pitfalls
10. Follow-ups & variants
11. Related questions + pattern master sheet link

---

## DSA Coding Round Checklist

- [ ] Restate problem + ask about constraints, edge cases, input size
- [ ] State brute force + complexity, then optimize
- [ ] **Name the pattern out loud** before coding
- [ ] Code cleanly; talk through invariants
- [ ] Walk a small example / dry-run
- [ ] State final time/space complexity
- [ ] Mention edge cases handled

---

## Regenerate Content

```bash
cd "DSA - Algorithms"
python _generate_dsa_questions.py
```

---

## Quick Links

- [How to Approach Any Problem](00-foundations/01-how-to-approach-any-problem.md)
- [Pattern Master Index](01-patterns/00-pattern-master-index.md)
- [One-Page Poster](01-patterns/memory-map-visual-one-page.md)
- [Flashcards](01-patterns/memory-map-flashcards.md)
- [90-Day Plan](07-study-schedule/master-90-day-plan.md)
- [Company Index](06-company-question-index.md)
- Sibling tracks: [HLD](../System%20Design%20-%20High%20Level%20Design/README.md) · [LLD](../System%20Design%20-%20Low%20Level%20Design/README.md) · [React](../Frontend%20-%20React/README.md)
