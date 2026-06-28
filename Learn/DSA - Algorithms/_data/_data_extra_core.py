# -*- coding: utf-8 -*-
"""Extra Tier A/B fill-in questions across patterns."""

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
    # ---- Arrays & Hashing ----
    {
        "slug": "contains-duplicate-ii", "title": "Contains Duplicate II", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 219,
        "cue": "Duplicate within distance k → last-seen index map",
        "problem": "Return True if there are duplicates within index distance `k`.",
        "solution": '''def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    last = {}
    for i, n in enumerate(nums):
        if n in last and i - last[n] <= k:
            return True
        last[n] = i
    return False''',
        "time": "O(N)", "space": "O(N)",
        "related": ["contains-duplicate"],
    },
    {
        "slug": "intersection-two-arrays", "title": "Intersection of Two Arrays", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 349,
        "cue": "Common unique elements → set intersection",
        "problem": "Return the unique intersection of two arrays.",
        "solution": '''def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))''',
        "time": "O(M+N)", "space": "O(M+N)",
        "related": ["intersection-two-arrays-ii"],
    },
    {
        "slug": "ransom-note", "title": "Ransom Note", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 383,
        "cue": "Can build note from magazine letters → frequency subset",
        "problem": "Return True if `ransomNote` can be built from `magazine` letters.",
        "solution": '''from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    return not (Counter(ransom_note) - Counter(magazine))''',
        "time": "O(N)", "space": "O(1)",
        "related": ["valid-anagram"],
    },
    {
        "slug": "isomorphic-strings", "title": "Isomorphic Strings", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, LinkedIn", "difficulty": "Easy", "leetcode": 205,
        "cue": "Consistent char mapping both ways → two dicts",
        "problem": "Return True if `s` and `t` are isomorphic (consistent character mapping).",
        "solution": '''def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_to_t, t_to_s = {}, {}
    for a, b in zip(s, t):
        if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
            return False
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["word-pattern"],
    },
    {
        "slug": "word-pattern", "title": "Word Pattern", "pattern": "arrays-hashing", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 290,
        "cue": "Bijection pattern↔words → two-way map",
        "problem": "Return True if `s` follows the same pattern as `pattern`.",
        "solution": '''def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    p_to_w, w_to_p = {}, {}
    for p, w in zip(pattern, words):
        if p_to_w.setdefault(p, w) != w or w_to_p.setdefault(w, p) != p:
            return False
    return True''',
        "time": "O(N)", "space": "O(N)",
        "related": ["isomorphic-strings"],
    },
    {
        "slug": "longest-harmonious-subsequence", "title": "Longest Harmonious Subsequence", "pattern": "arrays-hashing", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 594,
        "cue": "Max-min diff exactly 1 → count then check n and n+1",
        "problem": "Return the length of the longest subsequence where max - min == 1.",
        "solution": '''from collections import Counter

def find_lhs(nums: list[int]) -> int:
    freq = Counter(nums)
    best = 0
    for n in freq:
        if n + 1 in freq:
            best = max(best, freq[n] + freq[n + 1])
    return best''',
        "time": "O(N)", "space": "O(N)",
        "related": ["contains-duplicate"],
    },
    # ---- Two Pointers ----
    {
        "slug": "squares-of-sorted-array", "title": "Squares of a Sorted Array", "pattern": "two-pointers", "tier": "A",
        "companies": "Amazon, Meta", "difficulty": "Easy", "leetcode": 977,
        "cue": "Sorted squares → two pointers from both ends (largest first)",
        "problem": "Return squares of a sorted array, sorted ascending.",
        "solution": '''def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    lo, hi = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[lo]) > abs(nums[hi]):
            res[i] = nums[lo] ** 2
            lo += 1
        else:
            res[i] = nums[hi] ** 2
            hi -= 1
    return res''',
        "time": "O(N)", "space": "O(N)",
        "related": ["merge-sorted-array"],
    },
    {
        "slug": "backspace-string-compare", "title": "Backspace String Compare", "pattern": "two-pointers", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 844,
        "cue": "Compare after backspaces → scan from the end skipping deletes",
        "problem": "Return True if two strings are equal after processing backspace `#` characters.",
        "solution": '''def backspace_compare(s: str, t: str) -> bool:
    def nxt(string, i):
        skip = 0
        while i >= 0:
            if string[i] == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                break
            i -= 1
        return i
    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = nxt(s, i)
        j = nxt(t, j)
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        if (i >= 0) != (j >= 0):
            return False
        i -= 1; j -= 1
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["valid-palindrome"],
    },
    # ---- Linked List ----
    {
        "slug": "intersection-of-two-linked-lists", "title": "Intersection of Two Linked Lists", "pattern": "fast-slow-pointers", "tier": "A",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Easy", "leetcode": 160,
        "cue": "Find merge node → switch heads after reaching end (equalize length)",
        "problem": "Return the node where two singly linked lists intersect, or None.",
        "solution": _LISTNODE + '''
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a''',
        "time": "O(M+N)", "space": "O(1)",
        "related": ["linked-list-cycle-ii"],
    },
    # ---- Tree DFS ----
    {
        "slug": "symmetric-tree", "title": "Symmetric Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Microsoft, LinkedIn", "difficulty": "Easy", "leetcode": 101,
        "cue": "Mirror symmetry → compare left subtree with mirrored right",
        "problem": "Return True if a binary tree is a mirror of itself.",
        "solution": _TREENODE + '''
def is_symmetric(root) -> bool:
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return mirror(a.left, b.right) and mirror(a.right, b.left)
    return mirror(root, root) if root else True''',
        "time": "O(N)", "space": "O(H)",
        "related": ["same-tree", "invert-binary-tree"],
    },
    {
        "slug": "binary-tree-paths", "title": "Binary Tree Paths", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Google, Apple", "difficulty": "Easy", "leetcode": 257,
        "cue": "All root-to-leaf paths → DFS building path strings",
        "problem": "Return all root-to-leaf paths as strings.",
        "solution": _TREENODE + '''
def binary_tree_paths(root) -> list[str]:
    res = []
    def dfs(node, path):
        if not node:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            res.append("->".join(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])
    return res''',
        "time": "O(N)", "space": "O(H)",
        "related": ["path-sum-ii"],
    },
    {
        "slug": "sum-root-to-leaf-numbers", "title": "Sum Root to Leaf Numbers", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 129,
        "cue": "Sum of path-formed numbers → carry running number down",
        "problem": "Each root-to-leaf path forms a number; return the total sum.",
        "solution": _TREENODE + '''
def sum_numbers(root) -> int:
    def dfs(node, cur):
        if not node:
            return 0
        cur = cur * 10 + node.val
        if not node.left and not node.right:
            return cur
        return dfs(node.left, cur) + dfs(node.right, cur)
    return dfs(root, 0)''',
        "time": "O(N)", "space": "O(H)",
        "related": ["path-sum"],
    },
    {
        "slug": "count-complete-tree-nodes", "title": "Count Complete Tree Nodes", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 222,
        "cue": "Count nodes in complete tree → compare left/right heights",
        "problem": "Count the nodes of a complete binary tree faster than O(N).",
        "solution": _TREENODE + '''
def count_nodes(root) -> int:
    if not root:
        return 0
    def height(node, left):
        h = 0
        while node:
            node = node.left if left else node.right
            h += 1
        return h
    lh = height(root, True)
    rh = height(root, False)
    if lh == rh:
        return (1 << lh) - 1                       # perfect subtree
    return 1 + count_nodes(root.left) + count_nodes(root.right)''',
        "time": "O(log^2 N)", "space": "O(log N)",
        "related": ["max-depth-binary-tree"],
    },
    # ---- Graph ----
    {
        "slug": "find-the-town-judge", "title": "Find the Town Judge", "pattern": "graph-traversal", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 997,
        "cue": "Node trusted by all, trusts none → in/out degree counts",
        "problem": "Find the town judge: trusted by everyone else and trusts no one.",
        "solution": '''def find_judge(n: int, trust: list[list[int]]) -> int:
    score = [0] * (n + 1)
    for a, b in trust:
        score[a] -= 1
        score[b] += 1
    for i in range(1, n + 1):
        if score[i] == n - 1:
            return i
    return -1''',
        "time": "O(E)", "space": "O(N)",
        "related": ["find-celebrity"],
    },
    {
        "slug": "keys-and-rooms", "title": "Keys and Rooms", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 841,
        "cue": "Can visit all rooms → DFS from room 0",
        "problem": "Return True if all rooms are reachable starting from room 0 (rooms hold keys).",
        "solution": '''def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
    seen = set()
    stack = [0]
    while stack:
        r = stack.pop()
        if r in seen:
            continue
        seen.add(r)
        for key in rooms[r]:
            if key not in seen:
                stack.append(key)
    return len(seen) == len(rooms)''',
        "time": "O(V+E)", "space": "O(V)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "evaluate-division", "title": "Evaluate Division", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 399,
        "cue": "a/b queries from equations → weighted graph DFS product",
        "problem": "Answer division queries given equations like a/b = 2.0.",
        "solution": '''from collections import defaultdict

def calc_equation(equations, values, queries):
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1 / v
    def dfs(src, dst, seen):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        seen.add(src)
        for nb, w in graph[src].items():
            if nb not in seen:
                res = dfs(nb, dst, seen)
                if res != -1.0:
                    return w * res
        return -1.0
    return [dfs(a, b, set()) for a, b in queries]''',
        "time": "O(Q·(V+E))", "space": "O(V+E)",
        "related": ["clone-graph"],
    },
    # ---- DP ----
    {
        "slug": "min-cost-tickets", "title": "Minimum Cost For Tickets", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 983,
        "cue": "Min cost over travel days → DP over days with 1/7/30 passes",
        "problem": "Given travel days and pass costs (1/7/30 day), return the minimum cost.",
        "solution": '''def mincost_tickets(days: list[int], costs: list[int]) -> int:
    travel = set(days)
    last = days[-1]
    dp = [0] * (last + 1)
    for d in range(1, last + 1):
        if d not in travel:
            dp[d] = dp[d - 1]
        else:
            dp[d] = min(
                dp[d - 1] + costs[0],
                dp[max(0, d - 7)] + costs[1],
                dp[max(0, d - 30)] + costs[2],
            )
    return dp[last]''',
        "time": "O(maxDay)", "space": "O(maxDay)",
        "related": ["coin-change"],
    },
    {
        "slug": "delete-and-earn", "title": "Delete and Earn", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 740,
        "cue": "Earn points deleting + adjacents removed → house-robber on value buckets",
        "problem": "Maximize points where taking value v deletes all v-1 and v+1.",
        "solution": '''from collections import Counter

def delete_and_earn(nums: list[int]) -> int:
    points = Counter(nums)
    max_v = max(nums)
    prev = cur = 0
    for v in range(1, max_v + 1):
        take = prev + v * points.get(v, 0)
        prev, cur = cur, max(cur, take)
    return cur''',
        "time": "O(N + maxV)", "space": "O(maxV)",
        "related": ["house-robber"],
    },
    {
        "slug": "minimum-falling-path-sum", "title": "Minimum Falling Path Sum", "pattern": "dynamic-programming", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 931,
        "cue": "Min path top→bottom (3 directions) → row DP",
        "problem": "Return the minimum sum of any falling path through the matrix.",
        "solution": '''def min_falling_path_sum(matrix: list[list[int]]) -> int:
    n = len(matrix)
    dp = matrix[0][:]
    for r in range(1, n):
        new = [0] * n
        for c in range(n):
            best = dp[c]
            if c > 0:
                best = min(best, dp[c - 1])
            if c < n - 1:
                best = min(best, dp[c + 1])
            new[c] = matrix[r][c] + best
        dp = new
    return min(dp)''',
        "time": "O(N^2)", "space": "O(N)",
        "related": ["min-path-sum"],
    },
    # ---- Greedy ----
    {
        "slug": "lemonade-change", "title": "Lemonade Change", "pattern": "greedy", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 860,
        "cue": "Give change greedily → prefer using larger bills first",
        "problem": "Return True if you can give correct change to every customer (bills 5/10/20).",
        "solution": '''def lemonade_change(bills: list[int]) -> bool:
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if not five:
                return False
            five -= 1; ten += 1
        else:
            if ten and five:
                ten -= 1; five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["gas-station"],
    },
    {
        "slug": "maximum-units-on-truck", "title": "Maximum Units on a Truck", "pattern": "greedy", "tier": "A",
        "companies": "Amazon", "difficulty": "Easy", "leetcode": 1710,
        "cue": "Maximize units under box limit → sort by units desc",
        "problem": "Load at most `truckSize` boxes maximizing total units.",
        "solution": '''def maximum_units(box_types: list[list[int]], truck_size: int) -> int:
    box_types.sort(key=lambda b: b[1], reverse=True)
    total = 0
    for count, units in box_types:
        take = min(count, truck_size)
        total += take * units
        truck_size -= take
        if truck_size == 0:
            break
    return total''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["two-city-scheduling"],
    },
    # ---- Binary Search ----
    {
        "slug": "first-bad-version", "title": "First Bad Version", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Easy", "leetcode": 278,
        "cue": "First True in monotone predicate → binary search boundary",
        "problem": "Find the first bad version given an `isBadVersion(v)` API.",
        "solution": '''def is_bad_version(v: int) -> bool:
    ...                                            # provided API stub

def first_bad_version(n: int) -> int:
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        if is_bad_version(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["search-insert-position"],
    },
    {
        "slug": "valid-perfect-square", "title": "Valid Perfect Square", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 367,
        "cue": "Is perfect square → binary search candidate",
        "problem": "Return True if `num` is a perfect square (no sqrt builtin).",
        "solution": '''def is_perfect_square(num: int) -> bool:
    lo, hi = 1, num
    while lo <= hi:
        mid = (lo + hi) // 2
        sq = mid * mid
        if sq == num:
            return True
        if sq < num:
            lo = mid + 1
        else:
            hi = mid - 1
    return False''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["sqrt-x"],
    },
    # ---- Heap ----
    {
        "slug": "kth-largest-in-stream-2", "title": "Find K Pairs / Connect Sticks", "pattern": "top-k-heap", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1167,
        "cue": "Min cost to connect sticks → always merge two smallest (heap)",
        "problem": "Connect sticks paying the sum each merge; minimize total cost.",
        "solution": '''import heapq

def connect_sticks(sticks: list[int]) -> int:
    heapq.heapify(sticks)
    total = 0
    while len(sticks) > 1:
        a = heapq.heappop(sticks)
        b = heapq.heappop(sticks)
        cost = a + b
        total += cost
        heapq.heappush(sticks, cost)
    return total''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["last-stone-weight"],
    },
    # ---- Stack ----
    {
        "slug": "implement-queue-using-stacks", "title": "Implement Queue using Stacks", "pattern": "monotonic-stack", "tier": "A",
        "companies": "Amazon, Microsoft, Bloomberg", "difficulty": "Easy", "leetcode": 232,
        "cue": "FIFO from two LIFO stacks → transfer when out empty (amortized O(1))",
        "problem": "Implement a queue using two stacks.",
        "solution": '''class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._shift()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._shift()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack''',
        "time": "O(1) amortized", "space": "O(N)",
        "related": ["min-stack"],
    },
    # ---- Strings ----
    {
        "slug": "first-unique-char-str", "title": "First Unique Character in a String", "pattern": "strings", "tier": "A",
        "companies": "Amazon, Bloomberg", "difficulty": "Easy", "leetcode": 387,
        "cue": "First non-repeating → frequency then scan",
        "problem": "Return the index of the first non-repeating character, or -1.",
        "solution": '''from collections import Counter

def first_uniq_char(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1''',
        "time": "O(N)", "space": "O(1)",
        "related": ["valid-anagram-str"],
    },
    {
        "slug": "count-and-say", "title": "Count and Say", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 38,
        "cue": "Run-length encode previous term → group consecutive",
        "problem": "Return the nth term of the count-and-say sequence.",
        "solution": '''def count_and_say(n: int) -> str:
    s = "1"
    for _ in range(n - 1):
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            res.append(str(j - i) + s[i])
            i = j
        s = "".join(res)
    return s''',
        "time": "O(N·len)", "space": "O(len)",
        "related": ["string-compression"],
    },
    {
        "slug": "string-compression", "title": "String Compression", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 443,
        "cue": "In-place run-length compress → read/write pointers",
        "problem": "Compress a char array in place using counts; return new length.",
        "solution": '''def compress(chars: list[str]) -> int:
    write = 0
    read = 0
    n = len(chars)
    while read < n:
        ch = chars[read]
        count = 0
        while read < n and chars[read] == ch:
            read += 1
            count += 1
        chars[write] = ch
        write += 1
        if count > 1:
            for d in str(count):
                chars[write] = d
                write += 1
    return write''',
        "time": "O(N)", "space": "O(1)",
        "related": ["count-and-say"],
    },
    # ---- Bit ----
    {
        "slug": "hamming-distance", "title": "Hamming Distance", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 461,
        "cue": "Differing bit count → XOR then popcount",
        "problem": "Return the number of positions where the bits of two integers differ.",
        "solution": '''def hamming_distance(x: int, y: int) -> int:
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count''',
        "time": "O(1)", "space": "O(1)",
        "related": ["number-of-1-bits"],
    },
    {
        "slug": "complement-of-base-10", "title": "Number Complement", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Cloudera", "difficulty": "Easy", "leetcode": 476,
        "cue": "Flip all meaningful bits → XOR with all-ones mask",
        "problem": "Return the complement of a positive integer (flip its bits).",
        "solution": '''def find_complement(num: int) -> int:
    mask = (1 << num.bit_length()) - 1
    return num ^ mask''',
        "time": "O(1)", "space": "O(1)",
        "related": ["counting-bits"],
    },
    # ---- Cyclic / Math ----
    {
        "slug": "single-element-sorted-array", "title": "Single Element in a Sorted Array", "pattern": "binary-search", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 540,
        "cue": "One non-duplicate in sorted pairs → binary search on parity",
        "problem": "Find the element appearing once in a sorted array where others appear twice.",
        "solution": '''def single_non_duplicate(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid % 2 == 1:
            mid -= 1                               # align to even index
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid
    return nums[lo]''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["single-number"],
    },
]
