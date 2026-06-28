# -*- coding: utf-8 -*-
"""Dynamic Programming questions."""

QUESTIONS = [
    {
        "slug": "climbing-stairs", "title": "Climbing Stairs", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Google, Adobe", "difficulty": "Easy", "leetcode": 70,
        "cue": "Ways to reach step n (1 or 2 at a time) → Fibonacci recurrence",
        "problem": "Count distinct ways to climb to the top taking 1 or 2 steps.",
        "solution": '''def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a''',
        "time": "O(N)", "space": "O(1)",
        "related": ["min-cost-climbing-stairs", "house-robber"],
    },
    {
        "slug": "house-robber", "title": "House Robber", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Google, Microsoft", "difficulty": "Medium", "leetcode": 198,
        "cue": "Max non-adjacent sum → dp[i]=max(skip, take+dp[i-2])",
        "problem": "Maximize the sum of robbed houses without robbing two adjacent houses.",
        "solution": '''def rob(nums: list[int]) -> int:
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur''',
        "time": "O(N)", "space": "O(1)",
        "related": ["house-robber-ii", "climbing-stairs"],
    },
    {
        "slug": "maximum-subarray", "title": "Maximum Subarray (Kadane)", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, LinkedIn", "difficulty": "Medium", "leetcode": 53,
        "cue": "Max contiguous sum → extend or restart running sum",
        "problem": "Find the contiguous subarray with the largest sum and return that sum.",
        "solution": '''def max_sub_array(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "identify": "At each index, the best subarray ending here either extends the previous or starts fresh — Kadane's DP.",
        "related": ["maximum-product-subarray"],
    },
    {
        "slug": "coin-change", "title": "Coin Change", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 322,
        "cue": "Fewest coins to make amount → unbounded knapsack min",
        "problem": "Return the fewest coins needed to make `amount`, or -1.",
        "solution": '''def coin_change(coins: list[int], amount: int) -> int:
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1''',
        "time": "O(amount·coins)", "space": "O(amount)",
        "related": ["coin-change-ii", "combination-sum-iv"],
    },
    {
        "slug": "longest-increasing-subsequence", "title": "Longest Increasing Subsequence", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Medium", "leetcode": 300,
        "cue": "Longest increasing subsequence → patience sorting with bisect (O(N log N))",
        "problem": "Return the length of the longest strictly increasing subsequence.",
        "approaches": [("DP", "O(N^2)", "O(N)", "dp[i]=longest ending at i"), ("Patience + bisect", "O(N log N)", "O(N)", "tails array")],
        "solution": '''import bisect

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["russian-doll-envelopes", "longest-increasing-path-matrix"],
    },
    {
        "slug": "unique-paths", "title": "Unique Paths", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 62,
        "cue": "Count grid paths (right/down) → dp[c]+=dp[c-1]",
        "problem": "Count paths from top-left to bottom-right moving only right or down.",
        "solution": '''def unique_paths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[-1]''',
        "time": "O(M·N)", "space": "O(N)",
        "related": ["unique-paths-ii", "min-path-sum"],
    },
    {
        "slug": "word-break", "title": "Word Break", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Meta, Google, Uber", "difficulty": "Medium", "leetcode": 139,
        "cue": "Can split into dictionary words → dp[i] reachable",
        "problem": "Return True if `s` can be segmented into space-separated dictionary words.",
        "solution": '''def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]''',
        "time": "O(N^2)", "space": "O(N)",
        "related": ["word-break-ii"],
    },
    {
        "slug": "min-cost-climbing-stairs", "title": "Min Cost Climbing Stairs", "pattern": "dynamic-programming", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 746,
        "cue": "Min cost to top → dp[i]=cost[i]+min(dp[i-1],dp[i-2])",
        "problem": "Reach the top paying costs; you can start at index 0 or 1. Return min cost.",
        "solution": '''def min_cost_climbing_stairs(cost: list[int]) -> int:
    a = b = 0
    for i in range(2, len(cost) + 1):
        a, b = b, min(b + cost[i - 1], a + cost[i - 2])
    return b''',
        "time": "O(N)", "space": "O(1)",
        "related": ["climbing-stairs"],
    },
    {
        "slug": "house-robber-ii", "title": "House Robber II", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 213,
        "cue": "Houses in a circle → max of (rob 0..n-2) and (rob 1..n-1)",
        "problem": "Like House Robber, but houses are arranged in a circle.",
        "solution": '''def rob(nums: list[int]) -> int:
    def rob_line(arr):
        prev = cur = 0
        for n in arr:
            prev, cur = cur, max(cur, prev + n)
        return cur
    if len(nums) == 1:
        return nums[0]
    return max(rob_line(nums[:-1]), rob_line(nums[1:]))''',
        "time": "O(N)", "space": "O(1)",
        "related": ["house-robber"],
    },
    {
        "slug": "decode-ways", "title": "Decode Ways", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 91,
        "cue": "Ways to decode digits to letters → dp on 1- and 2-digit splits",
        "problem": "Count ways to decode a digit string where A=1..Z=26.",
        "solution": '''def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    prev2, prev1 = 1, 1
    for i in range(1, len(s)):
        cur = 0
        if s[i] != '0':
            cur += prev1
        if 10 <= int(s[i-1:i+1]) <= 26:
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Leading zero → 0", "'06' invalid two-digit"],
        "related": ["climbing-stairs"],
    },
    {
        "slug": "longest-common-subsequence", "title": "Longest Common Subsequence", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google, Microsoft", "difficulty": "Medium", "leetcode": 1143,
        "cue": "LCS of two strings → 2D dp grid",
        "problem": "Return the length of the longest common subsequence of two strings.",
        "solution": '''def longest_common_subsequence(a: str, b: str) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]''',
        "time": "O(M·N)", "space": "O(M·N)",
        "related": ["edit-distance", "distinct-subsequences"],
    },
    {
        "slug": "coin-change-ii", "title": "Coin Change II", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 518,
        "cue": "Number of ways to make amount → unbounded knapsack count (coins outer loop)",
        "problem": "Return the number of combinations that make up `amount`.",
        "solution": '''def change(amount: int, coins: list[int]) -> int:
    dp = [1] + [0] * amount
    for c in coins:                              # coins outer → combinations not permutations
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]''',
        "time": "O(amount·coins)", "space": "O(amount)",
        "identify": "Coins in the outer loop counts each combination once (order-independent), unlike combination-sum-iv.",
        "related": ["coin-change", "combination-sum-iv"],
    },
    {
        "slug": "partition-equal-subset-sum", "title": "Partition Equal Subset Sum", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 416,
        "cue": "Split into two equal-sum halves → 0/1 knapsack on sum/2 (boolean)",
        "problem": "Return True if the array can be partitioned into two subsets of equal sum.",
        "solution": '''def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for n in nums:
        for s in range(target, n - 1, -1):       # reverse → each item once
            dp[s] = dp[s] or dp[s - n]
    return dp[target]''',
        "time": "O(N·sum)", "space": "O(sum)",
        "related": ["target-sum", "coin-change"],
    },
    {
        "slug": "min-path-sum", "title": "Minimum Path Sum", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 64,
        "cue": "Min cost path in grid → dp[c]=grid+min(up,left)",
        "problem": "Find a path from top-left to bottom-right minimizing the sum of values.",
        "solution": '''def min_path_sum(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [float('inf')] * cols
    dp[0] = 0
    for r in range(rows):
        dp[0] += grid[r][0]
        for c in range(1, cols):
            dp[c] = grid[r][c] + min(dp[c], dp[c - 1])
    return dp[-1]''',
        "time": "O(M·N)", "space": "O(N)",
        "related": ["unique-paths"],
    },
    {
        "slug": "longest-palindromic-substring", "title": "Longest Palindromic Substring", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 5,
        "cue": "Longest palindrome substring → expand around each center",
        "problem": "Return the longest palindromic substring of `s`.",
        "solution": '''def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return l + 1, r - 1
    for i in range(len(s)):
        l1, r1 = expand(i, i)
        l2, r2 = expand(i, i + 1)
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]''',
        "time": "O(N^2)", "space": "O(1)",
        "related": ["palindromic-substrings"],
    },
    {
        "slug": "maximal-square", "title": "Maximal Square", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 221,
        "cue": "Largest all-1 square → dp=min(top,left,diag)+1",
        "problem": "Return the area of the largest square of 1s in a binary matrix.",
        "solution": '''def maximal_square(matrix: list[list[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * (cols + 1)
    best = 0
    for r in range(rows):
        prev = 0                                 # dp[r-1][c-1]
        for c in range(1, cols + 1):
            temp = dp[c]
            if matrix[r][c-1] == '1':
                dp[c] = min(dp[c], dp[c-1], prev) + 1
                best = max(best, dp[c])
            else:
                dp[c] = 0
            prev = temp
    return best * best''',
        "time": "O(M·N)", "space": "O(N)",
        "related": ["maximal-rectangle"],
    },
    {
        "slug": "target-sum", "title": "Target Sum", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 494,
        "cue": "Assign +/- to reach target → subset-sum counting",
        "problem": "Count ways to assign +/- to each number so the sum equals `target`.",
        "solution": '''from collections import defaultdict

def find_target_sum_ways(nums: list[int], target: int) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    for n in nums:
        nxt = defaultdict(int)
        for s, cnt in dp.items():
            nxt[s + n] += cnt
            nxt[s - n] += cnt
        dp = nxt
    return dp[target]''',
        "time": "O(N·S)", "space": "O(S)",
        "related": ["partition-equal-subset-sum"],
    },
    {
        "slug": "unique-paths-ii", "title": "Unique Paths II", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Bloomberg", "difficulty": "Medium", "leetcode": 63,
        "cue": "Grid paths with obstacles → dp, zero out blocked cells",
        "problem": "Count top-left to bottom-right paths avoiding obstacle cells (value 1).",
        "solution": '''def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    cols = len(grid[0])
    dp = [0] * cols
    dp[0] = 1
    for row in grid:
        for c in range(cols):
            if row[c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]''',
        "time": "O(M·N)", "space": "O(N)",
        "related": ["unique-paths"],
    },
    {
        "slug": "combination-sum-iv", "title": "Combination Sum IV", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 377,
        "cue": "Count ordered ways to reach target → amount outer loop (permutations)",
        "problem": "Count the number of ordered combinations summing to `target`.",
        "solution": '''def combination_sum4(nums: list[int], target: int) -> int:
    dp = [1] + [0] * target
    for a in range(1, target + 1):               # amount outer → counts orderings
        for n in nums:
            if n <= a:
                dp[a] += dp[a - n]
    return dp[target]''',
        "time": "O(target·N)", "space": "O(target)",
        "identify": "Amount outer / numbers inner counts permutations — contrast with coin-change-ii (combinations).",
        "related": ["coin-change-ii"],
    },
    {
        "slug": "edit-distance", "title": "Edit Distance", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Hard", "leetcode": 72,
        "cue": "Min edits to transform → 2D dp insert/delete/replace",
        "problem": "Return the minimum number of insert/delete/replace operations to turn `a` into `b`.",
        "solution": '''def min_distance(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]''',
        "time": "O(M·N)", "space": "O(M·N)",
        "related": ["longest-common-subsequence", "distinct-subsequences"],
    },
    {
        "slug": "best-time-buy-sell-cooldown", "title": "Best Time to Buy and Sell Stock with Cooldown", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 309,
        "cue": "Stock trades with cooldown → state machine (hold/sold/rest)",
        "problem": "Maximize profit with unlimited transactions and a 1-day cooldown after selling.",
        "solution": '''def max_profit(prices: list[int]) -> int:
    hold = float('-inf')
    sold = 0
    rest = 0
    for p in prices:
        prev_sold = sold
        sold = hold + p                          # sell today
        hold = max(hold, rest - p)               # buy today (rest yesterday)
        rest = max(rest, prev_sold)              # cooldown
    return max(sold, rest)''',
        "time": "O(N)", "space": "O(1)",
        "identify": "Three states (holding, just sold, resting) with transitions form a clean DP state machine.",
        "related": ["maximum-subarray"],
    },
    {
        "slug": "burst-balloons", "title": "Burst Balloons", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 312,
        "cue": "Max coins bursting balloons → interval DP on last-burst",
        "problem": "Maximize coins from bursting all balloons (coins = left*cur*right at burst time).",
        "identify": "Think of which balloon is burst LAST in an interval; that fixes its neighbors → interval DP.",
        "solution": '''def max_coins(nums: list[int]) -> int:
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                dp[left][right] = max(
                    dp[left][right],
                    balloons[left] * balloons[k] * balloons[right]
                    + dp[left][k] + dp[k][right])
    return dp[0][n - 1]''',
        "time": "O(N^3)", "space": "O(N^2)",
        "related": ["matrix-chain"],
    },
    {
        "slug": "regular-expression-matching", "title": "Regular Expression Matching", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Hard", "leetcode": 10,
        "cue": "Match with . and * → 2D dp on prefixes",
        "problem": "Implement regex matching with `.` (any char) and `*` (zero+ of previous).",
        "solution": '''def is_match(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-2]            # zero occurrences
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[m][n]''',
        "time": "O(M·N)", "space": "O(M·N)",
        "related": ["edit-distance"],
    },
    {
        "slug": "distinct-subsequences", "title": "Distinct Subsequences", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 115,
        "cue": "Count subsequences of s equal to t → 2D dp",
        "problem": "Count the distinct subsequences of `s` that equal `t`.",
        "solution": '''def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n, 0, -1):                # reverse to reuse previous row
            if s[i-1] == t[j-1]:
                dp[j] += dp[j-1]
    return dp[n]''',
        "time": "O(M·N)", "space": "O(N)",
        "related": ["longest-common-subsequence"],
    },
    {
        "slug": "longest-increasing-path-matrix", "title": "Longest Increasing Path in a Matrix", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 329,
        "cue": "Longest strictly increasing path → DFS + memo on cells",
        "problem": "Return the length of the longest increasing path in a matrix (4-directional).",
        "solution": '''from functools import cache

def longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    @cache
    def dfs(r, c):
        best = 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best
    return max(dfs(r, c) for r in range(rows) for c in range(cols))''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["longest-increasing-subsequence"],
    },
    {
        "slug": "word-break-ii", "title": "Word Break II", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 140,
        "cue": "All sentence segmentations → memoized backtracking",
        "problem": "Return all sentences formed by adding spaces so each word is in the dictionary.",
        "solution": '''from functools import cache

def word_break(s: str, word_dict: list[str]) -> list[str]:
    words = set(word_dict)
    @cache
    def dfs(start):
        if start == len(s):
            return [""]
        res = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for rest in dfs(end):
                    res.append(word + ("" if rest == "" else " " + rest))
        return res
    return dfs(0)''',
        "time": "O(2^N)", "space": "O(2^N)",
        "related": ["word-break"],
    },
]
