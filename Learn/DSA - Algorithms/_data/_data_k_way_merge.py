# -*- coding: utf-8 -*-
"""K-way Merge questions."""

QUESTIONS = [
    {
        "slug": "merge-two-sorted-lists", "title": "Merge Two Sorted Lists", "pattern": "k-way-merge", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, Apple", "difficulty": "Easy", "leetcode": 21,
        "cue": "Merge two sorted lists → dummy head + compare fronts",
        "problem": "Merge two sorted linked lists into one sorted list.",
        "solution": '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next''',
        "time": "O(M+N)", "space": "O(1)",
        "related": ["merge-k-sorted-lists", "merge-sorted-array"],
    },
    {
        "slug": "merge-k-sorted-lists", "title": "Merge k Sorted Lists", "pattern": "k-way-merge", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Hard", "leetcode": 23,
        "cue": "Merge K sorted lists → min-heap of current heads",
        "problem": "Merge `k` sorted linked lists into one sorted list.",
        "approaches": [("Pairwise merge", "O(N log K)", "O(1)", "divide and conquer"), ("Min-heap", "O(N log K)", "O(K)", "heap of heads")],
        "identify": "Always emit the global minimum among K list heads → a size-K min-heap gives O(log K) per element.",
        "solution": '''import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next''',
        "time": "O(N log K)", "space": "O(K)",
        "edges": ["Some lists empty", "All empty → None", "Tiebreaker index avoids comparing nodes"],
        "related": ["merge-two-sorted-lists", "kth-smallest-in-sorted-matrix"],
    },
    {
        "slug": "kth-smallest-in-sorted-matrix", "title": "Kth Smallest Element in a Sorted Matrix", "pattern": "k-way-merge", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 378,
        "cue": "Kth smallest across sorted rows → heap of row heads (or binary search on value)",
        "problem": "Find the kth smallest element in an `n×n` matrix with sorted rows and columns.",
        "solution": '''import heapq

def kth_smallest(matrix: list[list[int]], k: int) -> int:
    n = len(matrix)
    heap = [(matrix[r][0], r, 0) for r in range(min(k, n))]
    heapq.heapify(heap)
    val = 0
    for _ in range(k):
        val, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
    return val''',
        "time": "O(K log N)", "space": "O(N)",
        "related": ["merge-k-sorted-lists", "find-k-pairs-smallest-sums"],
    },
    {
        "slug": "find-k-pairs-smallest-sums", "title": "Find K Pairs with Smallest Sums", "pattern": "k-way-merge", "tier": "B",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Medium", "leetcode": 373,
        "cue": "Smallest k pair sums from two sorted arrays → heap seeded with first column",
        "problem": "Return the `k` pairs `(u,v)` from two sorted arrays with the smallest sums.",
        "solution": '''import heapq

def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    if not nums1 or not nums2:
        return []
    heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
    heapq.heapify(heap)
    res = []
    while heap and len(res) < k:
        _, i, j = heapq.heappop(heap)
        res.append([nums1[i], nums2[j]])
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return res''',
        "time": "O(K log K)", "space": "O(K)",
        "related": ["kth-smallest-in-sorted-matrix"],
    },
    {
        "slug": "smallest-range-k-lists", "title": "Smallest Range Covering Elements from K Lists", "pattern": "k-way-merge", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 632,
        "cue": "Smallest range touching all K lists → heap of mins, track current max",
        "problem": "Find the smallest range that includes at least one number from each of the `k` sorted lists.",
        "solution": '''import heapq

def smallest_range(nums: list[list[int]]) -> list[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(nums)]
    heapq.heapify(heap)
    cur_max = max(lst[0] for lst in nums)
    best = [float('-inf'), float('inf')]
    while heap:
        val, i, j = heapq.heappop(heap)
        if cur_max - val < best[1] - best[0]:
            best = [val, cur_max]
        if j + 1 == len(nums[i]):
            break                                # a list is exhausted
        nxt = nums[i][j + 1]
        cur_max = max(cur_max, nxt)
        heapq.heappush(heap, (nxt, i, j + 1))
    return best''',
        "time": "O(N log K)", "space": "O(K)",
        "identify": "Maintain one pointer per list; the range is [min in heap, running max]. Advancing the min shrinks the range.",
        "related": ["merge-k-sorted-lists"],
    },
]
