# -*- coding: utf-8 -*-
"""Top-K Heap questions."""

QUESTIONS = [
    {
        "slug": "kth-largest-element", "title": "Kth Largest Element in an Array", "pattern": "top-k-heap", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 215,
        "cue": "Kth largest → size-K min-heap (root is the answer)",
        "problem": "Return the kth largest element in an unsorted array.",
        "approaches": [("Sort", "O(N log N)", "O(1)", "simple"), ("Size-K heap", "O(N log K)", "O(K)", "evict smallest"), ("Quickselect", "O(N) avg", "O(1)", "partition")],
        "solution": '''import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]''',
        "time": "O(N log K)", "space": "O(K)",
        "related": ["top-k-frequent-elements", "k-closest-points"],
    },
    {
        "slug": "top-k-frequent-elements", "title": "Top K Frequent Elements", "pattern": "top-k-heap", "tier": "A",
        "companies": "Amazon, Meta, Google, Uber", "difficulty": "Medium", "leetcode": 347,
        "cue": "K most frequent → Counter + heap (or bucket sort O(N))",
        "problem": "Return the `k` most frequent elements.",
        "approaches": [("Heap", "O(N log K)", "O(N)", "nlargest on freq"), ("Bucket sort", "O(N)", "O(N)", "index by frequency")],
        "solution": '''from collections import Counter
import heapq

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    return [v for v, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]''',
        "time": "O(N log K)", "space": "O(N)",
        "related": ["kth-largest-element", "top-k-frequent-words"],
    },
    {
        "slug": "k-closest-points", "title": "K Closest Points to Origin", "pattern": "top-k-heap", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 973,
        "cue": "K closest → size-K max-heap by distance (negate)",
        "problem": "Return the `k` closest points to the origin.",
        "solution": '''import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []                                    # max-heap of (-dist, point)
    for x, y in points:
        d = x * x + y * y
        heapq.heappush(heap, (-d, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [p for _, p in heap]''',
        "time": "O(N log K)", "space": "O(K)",
        "related": ["kth-largest-element"],
    },
    {
        "slug": "last-stone-weight", "title": "Last Stone Weight", "pattern": "top-k-heap", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 1046,
        "cue": "Repeatedly smash two largest → max-heap",
        "problem": "Repeatedly remove the two heaviest stones; return the weight of the last stone (0 if none).",
        "solution": '''import heapq

def last_stone_weight(stones: list[int]) -> int:
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["kth-largest-element"],
    },
    {
        "slug": "task-scheduler", "title": "Task Scheduler", "pattern": "top-k-heap", "tier": "B",
        "companies": "Amazon, Meta, Uber", "difficulty": "Medium", "leetcode": 621,
        "cue": "Schedule with cooldown → greedy on most frequent (heap or formula)",
        "problem": "Given tasks and cooldown `n`, return the least intervals (with idles) to finish all tasks.",
        "solution": '''from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    freq = Counter(tasks)
    max_freq = max(freq.values())
    max_count = sum(1 for f in freq.values() if f == max_freq)
    # fill formula: (max_freq-1) blocks of size (n+1), plus tasks at max_freq
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(len(tasks), intervals)''',
        "time": "O(N)", "space": "O(1)",
        "identify": "The most frequent task dictates the skeleton; idle slots fill the gaps unless there are enough other tasks.",
        "related": ["reorganize-string"],
    },
    {
        "slug": "reorganize-string", "title": "Reorganize String", "pattern": "top-k-heap", "tier": "B",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 767,
        "cue": "No two adjacent equal → always place the most frequent available",
        "problem": "Rearrange characters so no two adjacent are equal, or return '' if impossible.",
        "solution": '''from collections import Counter
import heapq

def reorganize_string(s: str) -> str:
    freq = Counter(s)
    if max(freq.values()) > (len(s) + 1) // 2:
        return ""
    heap = [(-c, ch) for ch, c in freq.items()]
    heapq.heapify(heap)
    res = []
    prev = None
    while heap:
        cnt, ch = heapq.heappop(heap)
        res.append(ch)
        if prev and prev[0] < 0:
            heapq.heappush(heap, prev)
        prev = (cnt + 1, ch)                      # used one
    return "".join(res)''',
        "time": "O(N log A)", "space": "O(A)",
        "related": ["task-scheduler"],
    },
    {
        "slug": "k-closest-to-x", "title": "Find K Closest Elements", "pattern": "top-k-heap", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 658,
        "cue": "K closest to x in sorted array → binary search the window start",
        "problem": "Return the `k` closest integers to `x` (sorted) from a sorted array.",
        "solution": '''def find_closest_elements(arr: list[int], k: int, x: int) -> list[int]:
    lo, hi = 0, len(arr) - k
    while lo < hi:
        mid = (lo + hi) // 2
        if x - arr[mid] > arr[mid + k] - x:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo + k]''',
        "time": "O(log(N-K) + K)", "space": "O(1)",
        "related": ["k-closest-points"],
    },
    {
        "slug": "find-median-from-data-stream", "title": "Find Median from Data Stream", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 295,
        "cue": "Running median → two heaps balanced (low max-heap, high min-heap)",
        "problem": "Design a structure supporting `addNum` and `findMedian` over a stream.",
        "identify": "Keep the lower half in a max-heap and upper half in a min-heap, balanced in size; the median is at the heap tops.",
        "solution": '''import heapq

class MedianFinder:
    def __init__(self):
        self.low = []                            # max-heap (negated)
        self.high = []                           # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2''',
        "time": "O(log N) add, O(1) median", "space": "O(N)",
        "related": ["sliding-window-median"],
    },
    {
        "slug": "ipo", "title": "IPO (Maximize Capital)", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 502,
        "cue": "Pick k projects maximizing capital → sort by cost, max-heap of affordable profits",
        "problem": "Choose at most `k` projects (each needs capital, yields profit) to maximize final capital.",
        "solution": '''import heapq

def find_maximized_capital(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    projects = sorted(zip(capital, profits))     # by capital ascending
    available = []                               # max-heap of profits
    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(available, -projects[i][1])
            i += 1
        if not available:
            break
        w -= heapq.heappop(available)            # add best affordable profit
    return w''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["find-median-from-data-stream"],
    },
]
