# Pattern: Backtracking

## Recognition Cues

- "**Generate all** solutions / combinations / permutations"
- "Find **a** valid configuration" with constraints (N-Queens, Sudoku)
- Small input (N ≤ ~12–20) hinting at exponential search
- "Is there a path/way" through a decision tree

## Core Idea

Explore a decision tree depth-first: **choose** an option, **recurse**, then **undo** the choice (backtrack). Prune branches that can't lead to a valid solution.

---

## Template

```python
def backtrack(candidates):
    res = []
    path = []
    def dfs(start):
        if is_solution(path):
            res.append(path[:])          # copy!
            return
        for i in range(start, len(candidates)):
            if not is_valid(candidates[i], path):
                continue                 # prune
            path.append(candidates[i])   # choose
            dfs(i + 1)                    # explore (i to allow reuse)
            path.pop()                    # undo
    dfs(0)
    return res
```

### N-Queens style with constraint sets

```python
def solve_n_queens(n: int) -> int:
    cols, diag, anti = set(), set(), set()
    count = 0
    def place(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c)
            place(r + 1)
            cols.remove(c); diag.remove(r - c); anti.remove(r + c)
    place(0)
    return count
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Enumerate all valid configurations | Counting only → often DP is faster |
| Small N, exponential is acceptable | Large N → needs polynomial approach |
| Constraint satisfaction | Optimization with overlapping subproblems → DP |

## Complexity

- Often **O(2^N)**, **O(N!)**, or **O(K^N)** depending on branching. Space: O(depth) recursion + output.

## Variants & Pitfalls

- **Subsets, permutations, combination sum, palindrome partitioning, word search, N-Queens, Sudoku**.
- Pitfall: append a **copy** (`path[:]`) to results; always undo the choice; sort + skip duplicates for unique outputs.

## Linked Questions

- Tier A: Subsets, Combination Sum, Permutations, Letter Combinations of a Phone Number
- Tier B: Subsets II, Combination Sum II, Palindrome Partitioning, Word Search, Generate Parentheses
- Tier C: N-Queens, Sudoku Solver, Word Search II, Restore IP Addresses

## Related

- [Subsets & Combinations](subsets-combinations.md) · [Tree DFS](tree-dfs.md)
