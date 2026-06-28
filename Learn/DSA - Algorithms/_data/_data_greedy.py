# -*- coding: utf-8 -*-
"""Greedy questions."""

QUESTIONS = [
    {
        "slug": "jump-game", "title": "Jump Game", "pattern": "greedy", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 55,
        "cue": "Can reach the end → track furthest reachable index",
        "problem": "Each value is the max jump length. Return True if you can reach the last index.",
        "solution": '''def can_jump(nums: list[int]) -> bool:
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["jump-game-ii"],
    },
    {
        "slug": "best-time-to-buy-sell-stock-ii", "title": "Best Time to Buy and Sell Stock II", "pattern": "greedy", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 122,
        "cue": "Unlimited transactions → sum every positive delta",
        "problem": "Maximize profit with as many transactions as you like (sell before re-buy).",
        "solution": '''def max_profit(prices: list[int]) -> int:
    return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))''',
        "time": "O(N)", "space": "O(1)",
        "related": ["best-time-to-buy-sell-stock"],
    },
    {
        "slug": "gas-station", "title": "Gas Station", "pattern": "greedy", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 134,
        "cue": "Circular tour feasibility → if total >= 0, start after last deficit",
        "problem": "Return the starting gas station index to complete the circuit, or -1.",
        "solution": '''def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start''',
        "time": "O(N)", "space": "O(1)",
        "identify": "If total gas ≥ total cost a solution exists; the start is just after the point where the running tank dips lowest.",
        "related": ["jump-game"],
    },
    {
        "slug": "maximum-subarray-greedy", "title": "Maximum Subarray (Greedy view)", "pattern": "greedy", "tier": "A",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 53,
        "cue": "Drop prefix when running sum goes negative",
        "problem": "Find the maximum contiguous subarray sum (greedy framing of Kadane).",
        "solution": '''def max_sub_array(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        if cur < 0:
            cur = 0                              # greedily drop negative prefix
        cur += n
        best = max(best, cur)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "related": ["maximum-subarray"],
    },
    {
        "slug": "jump-game-ii", "title": "Jump Game II", "pattern": "greedy", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 45,
        "cue": "Min jumps to end → BFS-like greedy on current reach window",
        "problem": "Return the minimum number of jumps to reach the last index (always reachable).",
        "solution": '''def jump(nums: list[int]) -> int:
    jumps = 0
    cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps''',
        "time": "O(N)", "space": "O(1)",
        "related": ["jump-game"],
    },
    {
        "slug": "partition-labels", "title": "Partition Labels", "pattern": "greedy", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 763,
        "cue": "Split so each letter in one part → extend end to last index of each char",
        "problem": "Partition the string so each letter appears in at most one part; return part sizes.",
        "solution": '''def partition_labels(s: str) -> list[int]:
    last = {ch: i for i, ch in enumerate(s)}
    res = []
    start = end = 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["merge-intervals"],
    },
    {
        "slug": "two-city-scheduling", "title": "Two City Scheduling", "pattern": "greedy", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1029,
        "cue": "Send half to each city minimizing cost → sort by cost difference",
        "problem": "Send `n` people to city A and `n` to city B minimizing total cost.",
        "solution": '''def two_city_sched_cost(costs: list[list[int]]) -> int:
    costs.sort(key=lambda c: c[0] - c[1])        # prefer A when A is relatively cheaper
    n = len(costs) // 2
    return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["partition-labels"],
    },
    {
        "slug": "candy", "title": "Candy", "pattern": "greedy", "tier": "C",
        "companies": "Amazon, Google, Uber", "difficulty": "Hard", "leetcode": 135,
        "cue": "Min candies with rating constraints → two passes (left, right)",
        "problem": "Each child gets ≥1 candy; higher rating than a neighbor gets more. Minimize total.",
        "solution": '''def candy(ratings: list[int]) -> int:
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)''',
        "time": "O(N)", "space": "O(N)",
        "identify": "Satisfy the left-neighbor constraint in a forward pass, then the right-neighbor constraint backward, taking the max.",
        "related": ["partition-labels"],
    },
    {
        "slug": "task-scheduler-greedy", "title": "Reorganize String / Scheduling (Greedy)", "pattern": "greedy", "tier": "C",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 767,
        "cue": "Arrange so no two adjacent equal → place most frequent first with a gap",
        "problem": "Rearrange characters so no two identical are adjacent (greedy on frequency).",
        "solution": '''from collections import Counter

def reorganize_string(s: str) -> str:
    freq = Counter(s)
    n = len(s)
    if max(freq.values()) > (n + 1) // 2:
        return ""
    res = [''] * n
    i = 0
    for ch, _ in freq.most_common():
        for _ in range(freq[ch]):
            res[i] = ch
            i += 2
            if i >= n:
                i = 1                            # fill odd slots next
    return "".join(res)''',
        "time": "O(N)", "space": "O(N)",
        "related": ["reorganize-string"],
    },
]
