# -*- coding: utf-8 -*-
"""Backtracking questions."""

QUESTIONS = [
    {
        "slug": "combination-sum", "title": "Combination Sum", "pattern": "backtracking", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 39,
        "cue": "All combinations summing to target (reuse allowed) → backttrack with start index",
        "problem": "Return all unique combinations of `candidates` summing to `target`; numbers may be reused.",
        "solution": '''def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    def dfs(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i, remaining - candidates[i], path)   # i (not i+1) → reuse
            path.pop()
    dfs(0, target, [])
    return res''',
        "time": "O(2^T)", "space": "O(T)",
        "related": ["combination-sum-ii", "subsets"],
    },
    {
        "slug": "permutations", "title": "Permutations", "pattern": "backtracking", "tier": "A",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 46,
        "cue": "All orderings → backtrack with used set",
        "problem": "Return all permutations of distinct integers.",
        "solution": '''def permute(nums: list[int]) -> list[list[int]]:
    res = []
    used = [False] * len(nums)
    def dfs(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
            dfs(path)
            path.pop()
            used[i] = False
    dfs([])
    return res''',
        "time": "O(N·N!)", "space": "O(N)",
        "related": ["permutations-ii", "subsets"],
    },
    {
        "slug": "letter-combinations-phone", "title": "Letter Combinations of a Phone Number", "pattern": "backtracking", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 17,
        "cue": "Cartesian product of digit letters → backtrack per digit",
        "problem": "Return all letter combinations a phone number could represent.",
        "solution": '''def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl',
               '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res = []
    def dfs(i, path):
        if i == len(digits):
            res.append("".join(path))
            return
        for ch in mapping[digits[i]]:
            path.append(ch)
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res''',
        "time": "O(4^N·N)", "space": "O(N)",
        "related": ["generate-parentheses"],
    },
    {
        "slug": "generate-parentheses", "title": "Generate Parentheses", "pattern": "backtracking", "tier": "A",
        "companies": "Amazon, Meta, Google, Uber", "difficulty": "Medium", "leetcode": 22,
        "cue": "Valid bracket combos → track open/close counts as constraints",
        "problem": "Generate all combinations of `n` well-formed parentheses.",
        "solution": '''def generate_parenthesis(n: int) -> list[str]:
    res = []
    def dfs(path, open_count, close_count):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append('(')
            dfs(path, open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(path, open_count, close_count + 1)
            path.pop()
    dfs([], 0, 0)
    return res''',
        "time": "O(4^N / sqrt(N))", "space": "O(N)",
        "related": ["letter-combinations-phone"],
    },
    {
        "slug": "combination-sum-ii", "title": "Combination Sum II", "pattern": "backtracking", "tier": "B",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 40,
        "cue": "Combinations to target, each number once, no dup sets → sort + skip duplicates",
        "problem": "Return unique combinations summing to `target`; each candidate used at most once.",
        "solution": '''def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res = []
    def dfs(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue                          # skip duplicate at this level
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            dfs(i + 1, remaining - candidates[i], path)
            path.pop()
    dfs(0, target, [])
    return res''',
        "time": "O(2^N)", "space": "O(N)",
        "related": ["combination-sum", "subsets-ii"],
    },
    {
        "slug": "word-search", "title": "Word Search", "pattern": "backtracking", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 79,
        "cue": "Path spelling a word on a grid → DFS + visited mark, backtrack",
        "problem": "Return True if `word` exists in the grid via 4-directional adjacent cells (no reuse).",
        "solution": '''def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
            return False
        board[r][c] = '#'                         # mark visited
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1)
                 or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = word[i]                     # restore
        return found
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False''',
        "time": "O(R·C·4^L)", "space": "O(L)",
        "related": ["word-search-ii"],
    },
    {
        "slug": "palindrome-partitioning", "title": "Palindrome Partitioning", "pattern": "backtracking", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 131,
        "cue": "All partitions into palindromes → backtrack on cut positions",
        "problem": "Return all ways to partition `s` so every substring is a palindrome.",
        "solution": '''def partition(s: str) -> list[list[str]]:
    res = []
    def is_pal(sub):
        return sub == sub[::-1]
    def dfs(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if is_pal(piece):
                path.append(piece)
                dfs(end, path)
                path.pop()
    dfs(0, [])
    return res''',
        "time": "O(N·2^N)", "space": "O(N)",
        "related": ["palindrome-partitioning-ii"],
    },
    {
        "slug": "n-queens", "title": "N-Queens", "pattern": "backtracking", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 51,
        "cue": "Place N non-attacking queens → backtrack with column/diagonal sets",
        "problem": "Return all distinct solutions placing `n` queens on an `n×n` board.",
        "solution": '''def solve_n_queens(n: int) -> list[list[str]]:
    res = []
    cols, diag, anti = set(), set(), set()
    board = [['.'] * n for _ in range(n)]
    def place(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag or (r + c) in anti:
                continue
            cols.add(c); diag.add(r - c); anti.add(r + c)
            board[r][c] = 'Q'
            place(r + 1)
            board[r][c] = '.'
            cols.discard(c); diag.discard(r - c); anti.discard(r + c)
    place(0)
    return res''',
        "time": "O(N!)", "space": "O(N)",
        "related": ["sudoku-solver"],
    },
    {
        "slug": "sudoku-solver", "title": "Sudoku Solver", "pattern": "backtracking", "tier": "C",
        "companies": "Amazon, Google, Uber", "difficulty": "Hard", "leetcode": 37,
        "cue": "Fill a Sudoku → backtrack trying digits with constraint checks",
        "problem": "Solve a 9×9 Sudoku in place.",
        "solution": '''def solve_sudoku(board: list[list[str]]) -> None:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                empties.append((r, c))
            else:
                rows[r].add(v); cols[c].add(v); boxes[(r//3)*3 + c//3].add(v)
    def dfs(k):
        if k == len(empties):
            return True
        r, c = empties[k]
        b = (r//3)*3 + c//3
        for d in "123456789":
            if d in rows[r] or d in cols[c] or d in boxes[b]:
                continue
            board[r][c] = d
            rows[r].add(d); cols[c].add(d); boxes[b].add(d)
            if dfs(k + 1):
                return True
            board[r][c] = '.'
            rows[r].discard(d); cols[c].discard(d); boxes[b].discard(d)
        return False
    dfs(0)''',
        "time": "exponential (bounded)", "space": "O(1)",
        "related": ["n-queens", "valid-sudoku"],
    },
]
