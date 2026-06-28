# -*- coding: utf-8 -*-
"""Extra Tier C (mastery) questions across patterns."""

_LISTNODE = '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
_TREENODE = '''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

QUESTIONS = [
    {
        "slug": "minimum-window-subsequence", "title": "Minimum Window Subsequence", "pattern": "sliding-window", "tier": "C",
        "companies": "Google, Amazon", "difficulty": "Hard", "leetcode": 727,
        "cue": "Smallest window of s containing t as subsequence → forward match then shrink backward",
        "problem": "Return the minimum window of `s` that contains `t` as a subsequence.",
        "solution": '''def min_window(s: str, t: str) -> str:
    best = ""
    i = 0
    while i < len(s):
        j = 0
        if s[i] == t[0]:
            start = i
            while i < len(s):
                if s[i] == t[j]:
                    j += 1
                    if j == len(t):
                        break
                i += 1
            if j == len(t):
                end = i
                while j > 0:                      # shrink backward
                    if s[i] == t[j - 1]:
                        j -= 1
                    i -= 1
                i += 1
                if not best or end - i + 1 < len(best):
                    best = s[i:end + 1]
        i += 1
    return best''',
        "time": "O(N·M)", "space": "O(1)",
        "related": ["minimum-window-substring"],
    },
    {
        "slug": "longest-substring-at-most-two-distinct", "title": "Longest Substring with At Most Two Distinct Characters", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 159,
        "cue": "At most 2 distinct → sliding window with counter",
        "problem": "Return the length of the longest substring with at most two distinct characters.",
        "solution": '''from collections import defaultdict

def length_of_longest_substring_two_distinct(s: str) -> int:
    count = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "related": ["longest-substring-k-distinct"],
    },
    {
        "slug": "max-consecutive-ones", "title": "Maximum Consecutive Ones", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 485,
        "cue": "Longest run of 1s → running count reset on 0",
        "problem": "Return the maximum number of consecutive 1s in a binary array.",
        "solution": '''def find_max_consecutive_ones(nums: list[int]) -> int:
    best = cur = 0
    for n in nums:
        cur = cur + 1 if n == 1 else 0
        best = max(best, cur)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "related": ["max-consecutive-ones-iii"],
    },
    {
        "slug": "search-2d-matrix-ii", "title": "Search a 2D Matrix II", "pattern": "binary-search", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 240,
        "cue": "Row+col sorted matrix → start top-right, eliminate row/col",
        "problem": "Search a value in a matrix sorted ascending across rows and down columns.",
        "solution": '''def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    r, c = 0, len(matrix[0]) - 1
    while r < len(matrix) and c >= 0:
        if matrix[r][c] == target:
            return True
        if matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False''',
        "time": "O(M+N)", "space": "O(1)",
        "related": ["search-2d-matrix"],
    },
    {
        "slug": "find-peak-element", "title": "Find Peak Element", "pattern": "binary-search", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 162,
        "cue": "Any peak → binary search toward the rising side",
        "problem": "Return the index of any peak element (greater than its neighbors).",
        "solution": '''def find_peak_element(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["find-min-rotated-sorted"],
    },
    {
        "slug": "kth-largest-stream", "title": "Kth Largest Element in a Stream", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 703,
        "cue": "Streaming kth largest → maintain size-K min-heap",
        "problem": "Design a class that returns the kth largest element after each `add`.",
        "solution": '''import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]''',
        "time": "O(log K) per add", "space": "O(K)",
        "related": ["kth-largest-element"],
    },
    {
        "slug": "sliding-window-median", "title": "Sliding Window Median", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 480,
        "cue": "Median of each window → two heaps with lazy deletion (or SortedList)",
        "problem": "Return the median of each window of size `k`.",
        "solution": '''import bisect

def median_sliding_window(nums: list[int], k: int) -> list[float]:
    window = sorted(nums[:k])
    res = []
    def median():
        if k % 2:
            return float(window[k // 2])
        return (window[k // 2 - 1] + window[k // 2]) / 2
    res.append(median())
    for i in range(k, len(nums)):
        window.pop(bisect.bisect_left(window, nums[i - k]))
        bisect.insort(window, nums[i])
        res.append(median())
    return res''',
        "time": "O(N·K)", "space": "O(K)",
        "related": ["find-median-from-data-stream", "sliding-window-maximum"],
    },
    {
        "slug": "lru-cache", "title": "LRU Cache", "pattern": "linked-list-reversal", "tier": "C",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Medium", "leetcode": 146,
        "cue": "O(1) get/put with eviction → hashmap + doubly linked list (OrderedDict)",
        "problem": "Design an LRU cache with O(1) `get` and `put`.",
        "solution": '''from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)''',
        "time": "O(1) per op", "space": "O(capacity)",
        "identify": "Need ordering by recency + O(1) lookup → hashmap to nodes of a doubly linked list (OrderedDict encapsulates both).",
        "related": ["lfu-cache"],
    },
    {
        "slug": "flatten-multilevel-doubly-linked-list", "title": "Flatten a Multilevel Doubly Linked List", "pattern": "linked-list-reversal", "tier": "C",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 430,
        "cue": "Flatten child branches inline → DFS with stack",
        "problem": "Flatten a multilevel doubly linked list so all nodes appear in a single level.",
        "solution": '''class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return None
    stack = []
    cur = head
    prev = None
    while cur or stack:
        if not cur:
            cur = stack.pop()
        if prev:
            prev.next = cur
            cur.prev = prev
        if cur.child:
            if cur.next:
                stack.append(cur.next)
            cur.next = cur.child
            cur.child.prev = cur
            cur.child = None
        prev = cur
        cur = cur.next
    return head''',
        "time": "O(N)", "space": "O(N)",
        "related": ["reorder-list"],
    },
    {
        "slug": "copy-list-with-random-pointer", "title": "Copy List with Random Pointer", "pattern": "linked-list-reversal", "tier": "C",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 138,
        "cue": "Deep copy with random links → hashmap old→new (or interleave)",
        "problem": "Deep copy a linked list where each node has an extra random pointer.",
        "solution": '''class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None
    clones = {}
    cur = head
    while cur:
        clones[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        clones[cur].next = clones.get(cur.next)
        clones[cur].random = clones.get(cur.random)
        cur = cur.next
    return clones[head]''',
        "time": "O(N)", "space": "O(N)",
        "related": ["clone-graph"],
    },
    {
        "slug": "vertical-order-traversal", "title": "Binary Tree Vertical Order Traversal", "pattern": "tree-bfs", "tier": "C",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 314,
        "cue": "Group by column → BFS tracking column index",
        "problem": "Return node values grouped by column, left to right.",
        "solution": _TREENODE + '''
from collections import defaultdict, deque

def vertical_order(root):
    if not root:
        return []
    cols = defaultdict(list)
    q = deque([(root, 0)])
    min_c = max_c = 0
    while q:
        node, c = q.popleft()
        cols[c].append(node.val)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    return [cols[c] for c in range(min_c, max_c + 1)]''',
        "time": "O(N)", "space": "O(N)",
        "related": ["level-order-traversal"],
    },
    {
        "slug": "count-good-subarrays", "title": "Count Subarrays With Score Less Than K", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 2302,
        "cue": "Count windows with sum*len < k → sliding window counting",
        "problem": "Count subarrays where (sum × length) < k.",
        "solution": '''def count_subarrays(nums: list[int], k: int) -> int:
    left = total = res = 0
    for right, n in enumerate(nums):
        total += n
        while total * (right - left + 1) >= k:
            total -= nums[left]
            left += 1
        res += right - left + 1
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["minimum-size-subarray-sum"],
    },
    {
        "slug": "trapping-rain-water-ii", "title": "Trapping Rain Water II", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 407,
        "cue": "2D water trapping → min-heap from borders inward",
        "problem": "Compute trapped water volume in a 2D elevation map.",
        "solution": '''import heapq

def trap_rain_water(height_map: list[list[int]]) -> int:
    if not height_map or not height_map[0]:
        return 0
    m, n = len(height_map), len(height_map[0])
    visited = [[False] * n for _ in range(m)]
    heap = []
    for i in range(m):
        for j in range(n):
            if i in (0, m - 1) or j in (0, n - 1):
                heapq.heappush(heap, (height_map[i][j], i, j))
                visited[i][j] = True
    water = 0
    while heap:
        h, r, c = heapq.heappop(heap)
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                water += max(0, h - height_map[nr][nc])
                heapq.heappush(heap, (max(h, height_map[nr][nc]), nr, nc))
    return water''',
        "time": "O(M·N log(M·N))", "space": "O(M·N)",
        "identify": "Water level is bounded by the lowest surrounding wall — process cells outward from the border using a min-heap.",
        "related": ["trapping-rain-water-2p"],
    },
    {
        "slug": "course-schedule-iii", "title": "Course Schedule III", "pattern": "greedy", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 630,
        "cue": "Max courses by deadline → sort by deadline, max-heap of durations",
        "problem": "Take the maximum number of courses given (duration, lastDay) constraints.",
        "solution": '''import heapq

def schedule_course(courses: list[list[int]]) -> int:
    courses.sort(key=lambda c: c[1])
    heap = []                                     # max-heap of durations (negated)
    time = 0
    for dur, last in courses:
        heapq.heappush(heap, -dur)
        time += dur
        if time > last:
            time += heapq.heappop(heap)           # drop the longest course
    return len(heap)''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["task-scheduler"],
    },
    {
        "slug": "longest-consecutive-sequence-uf", "title": "Longest Consecutive Sequence (Union-Find)", "pattern": "union-find", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 128,
        "cue": "Longest run via connectivity → union n with n+1",
        "problem": "Find the longest consecutive run length using Union-Find.",
        "solution": '''def longest_consecutive(nums: list[int]) -> int:
    parent = {n: n for n in nums}
    size = {n: 1 for n in nums}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            size[rb] += size[ra]
    for n in nums:
        if n + 1 in parent:
            union(n, n + 1)
    return max(size[find(n)] for n in nums) if nums else 0''',
        "time": "O(N α)", "space": "O(N)",
        "related": ["longest-consecutive-sequence"],
    },
    {
        "slug": "subtree-with-max-average", "title": "Subarray Product Less Than K", "pattern": "sliding-window", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 713,
        "cue": "Count subarrays with product < k → sliding window of product",
        "problem": "Count contiguous subarrays whose product is strictly less than `k`.",
        "solution": '''def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0
    prod = 1
    left = res = 0
    for right, n in enumerate(nums):
        prod *= n
        while prod >= k:
            prod //= nums[left]
            left += 1
        res += right - left + 1
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["minimum-size-subarray-sum"],
    },
    {
        "slug": "maximum-product-subarray", "title": "Maximum Product Subarray", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 152,
        "cue": "Max product (negatives flip) → track running max and min",
        "problem": "Return the maximum product of a contiguous subarray.",
        "solution": '''def max_product(nums: list[int]) -> int:
    best = cur_max = cur_min = nums[0]
    for n in nums[1:]:
        candidates = (n, cur_max * n, cur_min * n)
        cur_max = max(candidates)
        cur_min = min(candidates)
        best = max(best, cur_max)
    return best''',
        "time": "O(N)", "space": "O(1)",
        "identify": "A negative number swaps max and min, so track both running extremes.",
        "related": ["maximum-subarray"],
    },
    {
        "slug": "unique-binary-search-trees", "title": "Unique Binary Search Trees", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 96,
        "cue": "Count BST shapes → Catalan number DP",
        "problem": "Count structurally unique BSTs storing values `1..n`.",
        "solution": '''def num_trees(n: int) -> int:
    dp = [1] * (n + 1)
    for nodes in range(2, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            total += dp[root - 1] * dp[nodes - root]
        dp[nodes] = total
    return dp[n]''',
        "time": "O(N^2)", "space": "O(N)",
        "related": ["unique-binary-search-trees-ii"],
    },
    {
        "slug": "palindrome-partitioning-ii", "title": "Palindrome Partitioning II", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 132,
        "cue": "Min cuts for palindrome partition → DP + palindrome table",
        "problem": "Return the minimum cuts so every substring of the partition is a palindrome.",
        "solution": '''def min_cut(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    cuts = [0] * n
    for i in range(n):
        min_cut = i                               # worst case: cut before each char
        for j in range(i + 1):
            if s[j] == s[i] and (i - j < 2 or is_pal[j + 1][i - 1]):
                is_pal[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, cuts[j - 1] + 1)
        cuts[i] = min_cut
    return cuts[-1]''',
        "time": "O(N^2)", "space": "O(N^2)",
        "related": ["palindrome-partitioning"],
    },
    {
        "slug": "decode-string", "title": "Decode String", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 394,
        "cue": "Nested k[encoded] → stack of (count, prefix)",
        "problem": "Decode strings like `3[a2[c]]` → `accaccacc`.",
        "solution": '''def decode_string(s: str) -> str:
    stack = []
    cur = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == ']':
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur''',
        "time": "O(N)", "space": "O(N)",
        "related": ["basic-calculator-ii"],
    },
    {
        "slug": "asteroid-collision", "title": "Asteroid Collision", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 735,
        "cue": "Simulate collisions → stack, resolve right-moving vs left-moving",
        "problem": "Return the state of asteroids after all collisions (sign = direction).",
        "solution": '''def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        alive = True
        while alive and a < 0 and stack and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop()
                alive = False
            else:
                alive = False
        if alive:
            stack.append(a)
    return stack''',
        "time": "O(N)", "space": "O(N)",
        "related": ["daily-temperatures"],
    },
    {
        "slug": "find-all-anagrams-extra", "title": "Permutation in String (Window)", "pattern": "sliding-window", "tier": "C",
        "companies": "Microsoft, Amazon", "difficulty": "Medium", "leetcode": 567,
        "cue": "Fixed window frequency match → match-count optimization",
        "problem": "Return True if s2 contains a permutation of s1 (window match-count variant).",
        "solution": '''def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1
    for i, ch in enumerate(s2):
        window[ord(ch) - 97] += 1
        if i >= len(s1):
            window[ord(s2[i - len(s1)]) - 97] -= 1
        if window == need:
            return True
    return False''',
        "time": "O(N)", "space": "O(1)",
        "related": ["permutation-in-string"],
    },
    {
        "slug": "shortest-path-binary-matrix", "title": "Shortest Path in Binary Matrix", "pattern": "graph-traversal", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1091,
        "cue": "Shortest 8-directional path → BFS",
        "problem": "Return the length of the shortest clear path (8-directional) from top-left to bottom-right.",
        "solution": '''from collections import deque

def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while q:
        r, c, d = q.popleft()
        if r == n - 1 and c == n - 1:
            return d
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc, d + 1))
    return -1''',
        "time": "O(N^2)", "space": "O(N^2)",
        "related": ["number-of-islands", "rotting-oranges"],
    },
    {
        "slug": "min-cost-connect-points", "title": "Min Cost to Connect All Points", "pattern": "union-find", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1584,
        "cue": "MST over points → Kruskal with Union-Find (or Prim)",
        "problem": "Connect all points with minimum total Manhattan-distance cost (MST).",
        "solution": '''def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
            edges.append((d, i, j))
    edges.sort()
    total = used = 0
    for d, i, j in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj
            total += d
            used += 1
            if used == n - 1:
                break
    return total''',
        "time": "O(N^2 log N)", "space": "O(N^2)",
        "identify": "Connect all with min cost = Minimum Spanning Tree; Kruskal sorts edges and unions disjoint components.",
        "related": ["number-of-provinces"],
    },
    {
        "slug": "kth-smallest-bst-iterator", "title": "Binary Search Tree Iterator", "pattern": "tree-dfs", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 173,
        "cue": "Inorder iterator with O(H) space → controlled stack",
        "problem": "Implement a BST iterator with `next()` and `hasNext()` in average O(1), O(H) space.",
        "solution": _TREENODE + '''
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return bool(self.stack)''',
        "time": "O(1) amortized next", "space": "O(H)",
        "related": ["kth-smallest-in-bst"],
    },
    {
        "slug": "subsets-bitmask", "title": "Subsets (Bitmask)", "pattern": "bit-manipulation", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 78,
        "cue": "All subsets via integers → iterate 0..2^n-1",
        "problem": "Generate all subsets using bitmask enumeration.",
        "solution": '''def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    res = []
    for mask in range(1 << n):
        res.append([nums[i] for i in range(n) if mask & (1 << i)])
    return res''',
        "time": "O(N·2^N)", "space": "O(1) extra",
        "related": ["subsets"],
    },
    {
        "slug": "design-twitter", "title": "Design Twitter", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Meta, Twitter", "difficulty": "Medium", "leetcode": 355,
        "cue": "Merge recent tweets of followees → heap merge of timelines",
        "problem": "Design Twitter: post tweets, follow/unfollow, and fetch 10 most recent feed tweets.",
        "solution": '''from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)           # user -> [(time, tweetId)]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            for t in self.tweets[u][-10:]:
                heap.append(t)
        return [tid for _, tid in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)''',
        "time": "O(N log N) feed", "space": "O(N)",
        "related": ["merge-k-sorted-lists"],
    },
    {
        "slug": "longest-repeating-substring", "title": "Repeated DNA Sequences", "pattern": "strings", "tier": "C",
        "companies": "Amazon, LinkedIn", "difficulty": "Medium", "leetcode": 187,
        "cue": "Find length-10 substrings appearing >1 → rolling hashset of windows",
        "problem": "Return all 10-letter sequences occurring more than once in a DNA string.",
        "solution": '''def find_repeated_dna_sequences(s: str) -> list[str]:
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        chunk = s[i:i + 10]
        if chunk in seen:
            repeated.add(chunk)
        seen.add(chunk)
    return list(repeated)''',
        "time": "O(N)", "space": "O(N)",
        "related": ["implement-strstr-kmp"],
    },
    {
        "slug": "kth-largest-quickselect", "title": "Kth Largest Element (Quickselect)", "pattern": "binary-search", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 215,
        "cue": "Kth largest in O(N) average → quickselect partition",
        "problem": "Find the kth largest element using quickselect (average O(N)).",
        "solution": '''import random

def find_kth_largest(nums: list[int], k: int) -> int:
    target = len(nums) - k                         # kth largest = index in sorted order
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        pivot = nums[random.randint(lo, hi)]
        left, mid, right = [], [], []
        for n in nums[lo:hi + 1]:
            (left if n < pivot else right if n > pivot else mid).append(n)
        # rebuild segment
        nums[lo:hi + 1] = left + mid + right
        l_end = lo + len(left)
        r_start = l_end + len(mid)
        if target < l_end:
            hi = l_end - 1
        elif target >= r_start:
            lo = r_start
        else:
            return pivot
    return nums[target]''',
        "time": "O(N) avg", "space": "O(N)",
        "related": ["kth-largest-element"],
    },
    {
        "slug": "spiral-matrix-iii", "title": "Find Winner / Tic Tac Toe State", "pattern": "matrix-traversal", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 794,
        "cue": "Validate board state → count + win checks",
        "problem": "Determine if a given Tic-Tac-Toe board is a valid reachable state.",
        "solution": '''def valid_tic_tac_toe(board: list[str]) -> bool:
    x = sum(row.count('X') for row in board)
    o = sum(row.count('O') for row in board)
    if o > x or x > o + 1:
        return False
    def wins(p):
        lines = list(board) + ["".join(col) for col in zip(*board)]
        lines.append(board[0][0] + board[1][1] + board[2][2])
        lines.append(board[0][2] + board[1][1] + board[2][0])
        return any(line == p * 3 for line in lines)
    if wins('X') and x != o + 1:
        return False
    if wins('O') and x != o:
        return False
    return True''',
        "time": "O(1)", "space": "O(1)",
        "related": ["game-of-life"],
    },
    {
        "slug": "min-remove-valid-parentheses", "title": "Minimum Remove to Make Valid Parentheses", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Meta, Amazon", "difficulty": "Medium", "leetcode": 1249,
        "cue": "Remove minimal invalid parens → stack of indices",
        "problem": "Remove the minimum number of parentheses to make the string valid.",
        "solution": '''def min_remove_to_make_valid(s: str) -> str:
    s = list(s)
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    for i in stack:
        s[i] = ''
    return "".join(s)''',
        "time": "O(N)", "space": "O(N)",
        "related": ["valid-parentheses"],
    },
    {
        "slug": "longest-valid-parentheses", "title": "Longest Valid Parentheses", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 32,
        "cue": "Longest balanced substring → stack of indices or DP",
        "problem": "Return the length of the longest valid (well-formed) parentheses substring.",
        "solution": '''def longest_valid_parentheses(s: str) -> int:
    stack = [-1]
    best = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)                   # new base index
            else:
                best = max(best, i - stack[-1])
    return best''',
        "time": "O(N)", "space": "O(N)",
        "related": ["valid-parentheses"],
    },
    {
        "slug": "wiggle-sort-ii", "title": "Wiggle Sort II", "pattern": "two-pointers", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 324,
        "cue": "Arrange nums[0]<nums[1]>nums[2]... → sort + interleave halves",
        "problem": "Reorder so `nums[0] < nums[1] > nums[2] < ...`.",
        "solution": '''def wiggle_sort(nums: list[int]) -> None:
    s = sorted(nums)
    n = len(nums)
    mid = (n + 1) // 2
    small = s[:mid][::-1]                          # smaller half, reversed
    large = s[mid:][::-1]                          # larger half, reversed
    nums[::2] = small
    nums[1::2] = large''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["sort-colors"],
    },
    {
        "slug": "find-celebrity", "title": "Find the Celebrity", "pattern": "two-pointers", "tier": "C",
        "companies": "Amazon, Meta, LinkedIn", "difficulty": "Medium", "leetcode": 277,
        "cue": "Find node known by all but knows none → eliminate candidates linearly",
        "problem": "Find the celebrity (known by everyone, knows no one) using the `knows(a,b)` API.",
        "solution": '''def knows(a: int, b: int) -> bool:
    ...                                            # provided API stub

def find_celebrity(n: int) -> int:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i                          # candidate can't be celebrity
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate''',
        "time": "O(N)", "space": "O(1)",
        "identify": "One pass narrows to a single candidate (if A knows B, A is out); a second pass verifies it.",
        "related": ["majority-element"],
    },
    {
        "slug": "insert-delete-getrandom", "title": "Insert Delete GetRandom O(1)", "pattern": "arrays-hashing", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 380,
        "cue": "O(1) insert/delete/random → array + value→index map, swap-with-last",
        "problem": "Design a set supporting insert, remove, and getRandom all in average O(1).",
        "solution": '''import random

class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = self.idx[val]
        last = self.arr[-1]
        self.arr[i] = last
        self.idx[last] = i
        self.arr.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)''',
        "time": "O(1) avg", "space": "O(N)",
        "identify": "Random access needs an array; O(1) delete needs swapping the target with the last element and updating the index map.",
        "related": ["insert-delete-getrandom-duplicates"],
    },
    {
        "slug": "evaluate-rpn", "title": "Evaluate Reverse Polish Notation", "pattern": "monotonic-stack", "tier": "C",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Medium", "leetcode": 150,
        "cue": "Evaluate postfix → stack of operands",
        "problem": "Evaluate an arithmetic expression in Reverse Polish Notation.",
        "solution": '''def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {'+', '-', '*', '/'}
    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))           # truncate toward zero
        else:
            stack.append(int(t))
    return stack[0]''',
        "time": "O(N)", "space": "O(N)",
        "related": ["basic-calculator-ii"],
    },
    {
        "slug": "top-k-frequent-words", "title": "Top K Frequent Words", "pattern": "top-k-heap", "tier": "C",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 692,
        "cue": "K frequent words, ties alphabetical → heap with custom order",
        "problem": "Return the `k` most frequent words, ties broken lexicographically.",
        "solution": '''from collections import Counter
import heapq

def top_k_frequent(words: list[str], k: int) -> list[str]:
    freq = Counter(words)
    # heap by (-count, word) so most frequent + lexicographically smallest first
    heap = [(-c, w) for w, c in freq.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["top-k-frequent-elements"],
    },
    {
        "slug": "rotate-array", "title": "Rotate Array", "pattern": "two-pointers", "tier": "C",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 189,
        "cue": "Rotate right by k in place → reverse whole, reverse parts",
        "problem": "Rotate the array to the right by `k` steps in place.",
        "solution": '''def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1; hi -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)''',
        "time": "O(N)", "space": "O(1)",
        "related": ["rotate-list"],
    },
    {
        "slug": "longest-increasing-subsequence-count", "title": "Number of Longest Increasing Subsequence", "pattern": "dynamic-programming", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 673,
        "cue": "Count of LIS → dp length + dp count arrays",
        "problem": "Return the number of longest strictly increasing subsequences.",
        "solution": '''def find_number_of_lis(nums: list[int]) -> int:
    n = len(nums)
    length = [1] * n
    count = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]
    longest = max(length)
    return sum(c for l, c in zip(length, count) if l == longest)''',
        "time": "O(N^2)", "space": "O(N)",
        "related": ["longest-increasing-subsequence"],
    },
]
