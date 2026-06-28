# -*- coding: utf-8 -*-
"""Monotonic Stack questions."""

QUESTIONS = [
    {
        "slug": "valid-parentheses", "title": "Valid Parentheses", "pattern": "monotonic-stack", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Easy", "leetcode": 20,
        "cue": "Matching nested brackets → stack of opens",
        "problem": "Return True if the string of brackets `()[]{}` is validly matched and nested.",
        "solution": '''def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Odd length → False", "Empty → True", "Closing first → False"],
        "related": ["min-stack", "generate-parentheses"],
    },
    {
        "slug": "daily-temperatures", "title": "Daily Temperatures", "pattern": "monotonic-stack", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 739,
        "cue": "Days until a warmer temperature → monotonic decreasing stack of indices",
        "problem": "For each day, how many days until a warmer temperature (0 if none).",
        "solution": '''def daily_temperatures(temps: list[int]) -> list[int]:
    res = [0] * len(temps)
    stack = []                                  # indices, decreasing temps
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res''',
        "time": "O(N)", "space": "O(N)",
        "identify": "'Next warmer' is the canonical next-greater-element → decreasing monotonic stack of indices for distances.",
        "related": ["next-greater-element-i", "next-greater-element-ii"],
    },
    {
        "slug": "next-greater-element-i", "title": "Next Greater Element I", "pattern": "monotonic-stack", "tier": "A",
        "companies": "Amazon, Bloomberg", "difficulty": "Easy", "leetcode": 496,
        "cue": "Next greater to the right, mapped across arrays → stack + hashmap",
        "problem": "For each element of `nums1` (a subset of `nums2`), find its next greater element in `nums2`.",
        "solution": '''def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    nxt = {}
    stack = []
    for n in nums2:
        while stack and stack[-1] < n:
            nxt[stack.pop()] = n
        stack.append(n)
    return [nxt.get(n, -1) for n in nums1]''',
        "time": "O(N+M)", "space": "O(N)",
        "related": ["daily-temperatures", "next-greater-element-ii"],
    },
    {
        "slug": "min-stack", "title": "Min Stack", "pattern": "monotonic-stack", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 155,
        "cue": "O(1) getMin alongside push/pop → store running min with each element",
        "problem": "Design a stack supporting push, pop, top, and getMin in O(1).",
        "solution": '''class MinStack:
    def __init__(self):
        self.stack = []                         # (value, min_so_far)

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]''',
        "time": "O(1) per op", "space": "O(N)",
        "related": ["valid-parentheses"],
    },
    {
        "slug": "next-greater-element-ii", "title": "Next Greater Element II (Circular)", "pattern": "monotonic-stack", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 503,
        "cue": "Next greater in a circular array → iterate 2N with modulo",
        "problem": "Return the next greater element for each index in a circular array (-1 if none).",
        "solution": '''def next_greater_elements(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        cur = nums[i % n]
        while stack and nums[stack[-1]] < cur:
            res[stack.pop()] = cur
        if i < n:
            stack.append(i)
    return res''',
        "time": "O(N)", "space": "O(N)",
        "related": ["next-greater-element-i", "daily-temperatures"],
    },
    {
        "slug": "online-stock-span", "title": "Online Stock Span", "pattern": "monotonic-stack", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 901,
        "cue": "Consecutive days price <= today → monotonic stack of (price, span)",
        "problem": "Implement `next(price)` returning the span of days with price ≤ today's, ending today.",
        "solution": '''class StockSpanner:
    def __init__(self):
        self.stack = []                         # (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span''',
        "time": "O(1) amortized", "space": "O(N)",
        "related": ["daily-temperatures"],
    },
    {
        "slug": "remove-k-digits", "title": "Remove K Digits", "pattern": "monotonic-stack", "tier": "B",
        "companies": "Amazon, Google, Uber", "difficulty": "Medium", "leetcode": 402,
        "cue": "Smallest number after removing k digits → monotonic increasing stack",
        "problem": "Remove `k` digits from `num` to form the smallest possible number.",
        "solution": '''def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    stack = stack[:len(stack) - k] if k else stack    # remove remaining from end
    return "".join(stack).lstrip("0") or "0"''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Leading zeros stripped", "Remove all → '0'", "k remaining trimmed from end"],
        "related": ["next-greater-element-ii"],
    },
    {
        "slug": "largest-rectangle-in-histogram", "title": "Largest Rectangle in Histogram", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 84,
        "cue": "Max area under bars → increasing stack; pop resolves width",
        "problem": "Given bar heights, return the area of the largest rectangle in the histogram.",
        "identify": "When a shorter bar arrives, every taller bar on the stack can no longer extend — pop and compute its maximal width.",
        "solution": '''def largest_rectangle_area(heights: list[int]) -> int:
    stack = []                                  # indices, increasing heights
    best = 0
    for i, h in enumerate(heights + [0]):       # sentinel flushes stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best''',
        "time": "O(N)", "space": "O(N)",
        "related": ["maximal-rectangle", "trapping-rain-water-2p"],
    },
    {
        "slug": "maximal-rectangle", "title": "Maximal Rectangle", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 85,
        "cue": "Largest all-1s rectangle in binary matrix → histogram per row + largest rectangle",
        "problem": "Return the area of the largest rectangle of 1s in a binary matrix.",
        "solution": '''def maximal_rectangle(matrix: list[list[str]]) -> int:
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    best = 0

    def largest(hs):
        stack = []
        area = 0
        for i, h in enumerate(hs + [0]):
            while stack and hs[stack[-1]] > h:
                height = hs[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)
        return area

    for row in matrix:
        for c in range(cols):
            heights[c] = heights[c] + 1 if row[c] == '1' else 0
        best = max(best, largest(heights))
    return best''',
        "time": "O(R·C)", "space": "O(C)",
        "related": ["largest-rectangle-in-histogram"],
    },
]
