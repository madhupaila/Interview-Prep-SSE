# -*- coding: utf-8 -*-
"""Subsets & Combinations questions."""

QUESTIONS = [
    {
        "slug": "subsets", "title": "Subsets", "pattern": "subsets-combinations", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 78,
        "cue": "Power set → backtrack appending every prefix",
        "problem": "Return all subsets of an array of distinct integers.",
        "solution": '''def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res''',
        "time": "O(N·2^N)", "space": "O(N)",
        "related": ["subsets-ii", "combinations"],
    },
    {
        "slug": "combinations", "title": "Combinations", "pattern": "subsets-combinations", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 77,
        "cue": "All k-size selections → backtrack with start index",
        "problem": "Return all combinations of `k` numbers from `1..n`.",
        "solution": '''def combine(n: int, k: int) -> list[list[int]]:
    res = []
    def dfs(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            dfs(i + 1, path)
            path.pop()
    dfs(1, [])
    return res''',
        "time": "O(k·C(n,k))", "space": "O(k)",
        "related": ["subsets", "combination-sum"],
    },
    {
        "slug": "subsets-ii", "title": "Subsets II", "pattern": "subsets-combinations", "tier": "B",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 90,
        "cue": "Power set with duplicates → sort + skip same value at a level",
        "problem": "Return all unique subsets when the array may contain duplicates.",
        "solution": '''def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res''',
        "time": "O(N·2^N)", "space": "O(N)",
        "related": ["subsets", "combination-sum-ii"],
    },
    {
        "slug": "permutations-ii", "title": "Permutations II", "pattern": "subsets-combinations", "tier": "B",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 47,
        "cue": "Unique permutations with duplicates → sort + skip used duplicates",
        "problem": "Return all unique permutations when the array may contain duplicates.",
        "solution": '''def permute_unique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    used = [False] * len(nums)
    def dfs(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(nums[i])
            dfs(path)
            path.pop()
            used[i] = False
    dfs([])
    return res''',
        "time": "O(N·N!)", "space": "O(N)",
        "related": ["permutations", "subsets-ii"],
    },
    {
        "slug": "combination-sum-iii", "title": "Combination Sum III", "pattern": "subsets-combinations", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 216,
        "cue": "k numbers from 1..9 summing to n → bounded backtracking",
        "problem": "Find all combinations of `k` numbers in 1..9 that sum to `n` (each used once).",
        "solution": '''def combination_sum3(k: int, n: int) -> list[list[int]]:
    res = []
    def dfs(start, k_left, remaining, path):
        if k_left == 0 and remaining == 0:
            res.append(path[:])
            return
        for i in range(start, 10):
            if i > remaining:
                break
            path.append(i)
            dfs(i + 1, k_left - 1, remaining - i, path)
            path.pop()
    dfs(1, k, n, [])
    return res''',
        "time": "O(C(9,k))", "space": "O(k)",
        "related": ["combination-sum", "combinations"],
    },
    {
        "slug": "letter-case-permutation", "title": "Letter Case Permutation", "pattern": "subsets-combinations", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 784,
        "cue": "Toggle case of each letter → branch on letters",
        "problem": "Return all strings from toggling the case of each letter in `s` (digits fixed).",
        "solution": '''def letter_case_permutation(s: str) -> list[str]:
    res = []
    def dfs(i, path):
        if i == len(s):
            res.append("".join(path))
            return
        ch = s[i]
        if ch.isalpha():
            path.append(ch.lower()); dfs(i + 1, path); path.pop()
            path.append(ch.upper()); dfs(i + 1, path); path.pop()
        else:
            path.append(ch); dfs(i + 1, path); path.pop()
    dfs(0, [])
    return res''',
        "time": "O(2^L·L)", "space": "O(L)",
        "related": ["subsets"],
    },
]
