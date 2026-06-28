# -*- coding: utf-8 -*-
"""Sliding Window questions."""

QUESTIONS = [
    {
        "slug": "best-time-to-buy-sell-stock", "title": "Best Time to Buy and Sell Stock", "pattern": "sliding-window", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Easy", "leetcode": 121,
        "cue": "Max profit one transaction → track min so far (window from min to now)",
        "problem": "Given daily prices, return the max profit from one buy then one sell (sell after buy).",
        "solution": '''def max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    best = 0
    for p in prices:
        min_price = min(min_price, p)
        best = max(best, p - min_price)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Prices decreasing → 0", "Empty → 0"],
        "related": ["best-time-to-buy-sell-stock-ii"],
    },
    {
        "slug": "longest-substring-without-repeating", "title": "Longest Substring Without Repeating Characters", "pattern": "sliding-window", "tier": "A",
        "companies": "Amazon, Meta, Bloomberg, Adobe", "difficulty": "Medium", "leetcode": 3,
        "cue": "Longest substring with a constraint → variable window + last-seen map",
        "problem": "Return the length of the longest substring without repeating characters.",
        "approaches": [("Brute force", "O(N^2)", "O(N)", "check all substrings"), ("Sliding window", "O(N)", "O(min(N,charset))", "jump left past last dup")],
        "identify": "Contiguous substring + 'longest valid' is the textbook variable sliding-window; a map of last index lets left jump in O(1).",
        "solution": '''def length_of_longest_substring(s: str) -> int:
    last = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(min(N, charset))",
        "edges": ["Empty → 0", "All same char → 1", "All unique → len(s)"],
        "related": ["longest-repeating-character-replacement", "minimum-window-substring"],
    },
    {
        "slug": "longest-repeating-character-replacement", "title": "Longest Repeating Character Replacement", "pattern": "sliding-window", "tier": "A",
        "companies": "Google, Amazon, Meta", "difficulty": "Medium", "leetcode": 424,
        "cue": "Window valid if (size - maxFreq) <= k → expand/shrink",
        "problem": "You may replace at most `k` characters. Return the length of the longest substring of one repeating letter achievable.",
        "solution": '''from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    count = defaultdict(int)
    left = best = max_freq = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        max_freq = max(max_freq, count[ch])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "identify": "A window is valid when the characters we must replace (window size minus the most frequent char) is ≤ k.",
        "related": ["longest-substring-without-repeating"],
    },
    {
        "slug": "permutation-in-string", "title": "Permutation in String", "pattern": "sliding-window", "tier": "A",
        "companies": "Microsoft, Amazon, Meta", "difficulty": "Medium", "leetcode": 567,
        "cue": "Fixed-size window matching a frequency profile",
        "problem": "Return True if `s2` contains a permutation of `s1` as a substring.",
        "solution": '''from collections import Counter

def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    need = Counter(s1)
    window = Counter(s2[:len(s1)])
    if window == need:
        return True
    for i in range(len(s1), len(s2)):
        window[s2[i]] += 1
        left = s2[i - len(s1)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            return True
    return False''',
        "time": "O(N)", "space": "O(1)",
        "related": ["find-all-anagrams-in-a-string"],
    },
    {
        "slug": "max-average-subarray", "title": "Maximum Average Subarray I", "pattern": "sliding-window", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 643,
        "cue": "Fixed window of size k → slide the sum",
        "problem": "Find the contiguous subarray of length `k` with the maximum average.",
        "solution": '''def find_max_average(nums: list[int], k: int) -> float:
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best / k''',
        "time": "O(N)", "space": "O(1)",
        "related": ["max-consecutive-ones-iii"],
    },
    {
        "slug": "find-all-anagrams-in-a-string", "title": "Find All Anagrams in a String", "pattern": "sliding-window", "tier": "B",
        "companies": "Amazon, Meta, Uber", "difficulty": "Medium", "leetcode": 438,
        "cue": "All start indices of an anagram → fixed window frequency match",
        "problem": "Return all start indices of `p`'s anagrams in `s`.",
        "solution": '''from collections import Counter

def find_anagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []
    need = Counter(p)
    window = Counter(s[:len(p)])
    res = [0] if window == need else []
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left = s[i - len(p)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == need:
            res.append(i - len(p) + 1)
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["permutation-in-string"],
    },
    {
        "slug": "minimum-window-substring", "title": "Minimum Window Substring", "pattern": "sliding-window", "tier": "B",
        "companies": "Meta, Amazon, Google, Uber", "difficulty": "Hard", "leetcode": 76,
        "cue": "Smallest window covering all required chars → expand then shrink while valid",
        "problem": "Return the minimum window in `s` containing all characters of `t` (with multiplicity).",
        "approaches": [("Sliding window", "O(N)", "O(charset)", "have/need counter, shrink while valid")],
        "identify": "Minimum-length valid window: grow right until valid, then shrink left while still valid, recording the best.",
        "solution": '''from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (float('inf'), 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:                    # window valid → shrink
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float('inf') else s[best[1]: best[2] + 1]''',
        "time": "O(N)", "space": "O(charset)",
        "edges": ["t longer than s → ''", "No valid window → ''", "Duplicates in t"],
        "related": ["longest-substring-without-repeating", "minimum-size-subarray-sum"],
    },
    {
        "slug": "minimum-size-subarray-sum", "title": "Minimum Size Subarray Sum", "pattern": "sliding-window", "tier": "B",
        "companies": "Amazon, Google, Facebook", "difficulty": "Medium", "leetcode": 209,
        "cue": "Shortest subarray with sum >= target (positives) → shrink while valid",
        "problem": "Return the minimal length of a contiguous subarray whose sum ≥ `target`, or 0.",
        "solution": '''def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    best = float('inf')
    for right, n in enumerate(nums):
        total += n
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float('inf') else best''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["No valid subarray → 0", "Works only for non-negative values"],
        "related": ["minimum-window-substring"],
    },
    {
        "slug": "max-consecutive-ones-iii", "title": "Max Consecutive Ones III", "pattern": "sliding-window", "tier": "B",
        "companies": "Amazon, Google, Facebook", "difficulty": "Medium", "leetcode": 1004,
        "cue": "Longest window with at most k zeros → shrink when zeros > k",
        "problem": "Return the longest subarray of 1s if you can flip at most `k` zeros.",
        "solution": '''def longest_ones(nums: list[int], k: int) -> int:
    left = zeros = best = 0
    for right, n in enumerate(nums):
        if n == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "related": ["longest-repeating-character-replacement"],
    },
    {
        "slug": "fruit-into-baskets", "title": "Fruit Into Baskets", "pattern": "sliding-window", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 904,
        "cue": "Longest subarray with at most 2 distinct → variable window + counter",
        "problem": "Pick the longest subarray containing at most two distinct values.",
        "solution": '''from collections import defaultdict

def total_fruit(fruits: list[int]) -> int:
    count = defaultdict(int)
    left = best = 0
    for right, f in enumerate(fruits):
        count[f] += 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "related": ["longest-substring-without-repeating"],
    },
    {
        "slug": "sliding-window-maximum", "title": "Sliding Window Maximum", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 239,
        "cue": "Max of each fixed window → monotonic decreasing deque of indices",
        "problem": "Return the maximum of each contiguous window of size `k`.",
        "approaches": [("Heap", "O(N log N)", "O(N)", "lazy delete"), ("Monotonic deque", "O(N)", "O(k)", "front is window max")],
        "solution": '''from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = deque()                                # indices, values decreasing
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res''',
        "time": "O(N)", "space": "O(k)",
        "identify": "We need the running max as the window slides — a monotonic deque keeps candidates in decreasing order so the front is always the max.",
        "related": ["sliding-window-median"],
    },
    {
        "slug": "longest-substring-k-distinct", "title": "Longest Substring with At Most K Distinct Characters", "pattern": "sliding-window", "tier": "C",
        "companies": "Google, Amazon, Facebook", "difficulty": "Medium", "leetcode": 340,
        "cue": "At most K distinct → variable window + frequency map sized K",
        "problem": "Return the length of the longest substring with at most `k` distinct characters.",
        "solution": '''from collections import defaultdict

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    count = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(k)",
        "related": ["fruit-into-baskets", "longest-substring-without-repeating"],
    },
    {
        "slug": "subarrays-with-k-different-integers", "title": "Subarrays with K Different Integers", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 992,
        "cue": "Exactly K distinct = atMost(K) - atMost(K-1)",
        "problem": "Count contiguous subarrays with exactly `k` distinct integers.",
        "solution": '''from collections import defaultdict

def subarrays_with_k_distinct(nums: list[int], k: int) -> int:
    def at_most(m):
        count = defaultdict(int)
        left = res = 0
        for right, n in enumerate(nums):
            count[n] += 1
            while len(count) > m:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += right - left + 1            # subarrays ending at right
        return res
    return at_most(k) - at_most(k - 1)''',
        "time": "O(N)", "space": "O(N)",
        "identify": "'Exactly K' is hard directly; the classic trick is atMost(K) - atMost(K-1), each an easy sliding window.",
        "related": ["longest-substring-k-distinct"],
    },
]
