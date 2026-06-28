# -*- coding: utf-8 -*-
"""Tree BFS questions."""

_TREENODE = '''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

QUESTIONS = [
    {
        "slug": "level-order-traversal", "title": "Binary Tree Level Order Traversal", "pattern": "tree-bfs", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, LinkedIn", "difficulty": "Medium", "leetcode": 102,
        "cue": "Group nodes by level → BFS, snapshot queue length per level",
        "problem": "Return node values level by level (top to bottom).",
        "solution": _TREENODE + '''
from collections import deque

def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out''',
        "time": "O(N)", "space": "O(W)",
        "edges": ["Empty tree → []", "Snapshot len(q) before inner loop"],
        "related": ["zigzag-level-order", "right-side-view"],
    },
    {
        "slug": "max-depth-binary-tree", "title": "Maximum Depth of Binary Tree", "pattern": "tree-bfs", "tier": "A",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Easy", "leetcode": 104,
        "cue": "Tree height → BFS count levels (or DFS)",
        "problem": "Return the maximum depth of a binary tree.",
        "solution": _TREENODE + '''
def max_depth(root) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))''',
        "time": "O(N)", "space": "O(H)",
        "related": ["minimum-depth-binary-tree", "level-order-traversal"],
    },
    {
        "slug": "average-of-levels", "title": "Average of Levels in Binary Tree", "pattern": "tree-bfs", "tier": "A",
        "companies": "Amazon, Facebook", "difficulty": "Easy", "leetcode": 637,
        "cue": "Per-level aggregate → BFS sum each level",
        "problem": "Return the average value of nodes on each level.",
        "solution": _TREENODE + '''
from collections import deque

def average_of_levels(root) -> list[float]:
    res, q = [], deque([root])
    while q:
        total = 0
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            total += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(total / n)
    return res''',
        "time": "O(N)", "space": "O(W)",
        "related": ["level-order-traversal"],
    },
    {
        "slug": "zigzag-level-order", "title": "Binary Tree Zigzag Level Order Traversal", "pattern": "tree-bfs", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 103,
        "cue": "Alternate left-right per level → BFS + reverse on odd depth",
        "problem": "Return level-order traversal alternating direction each level.",
        "solution": _TREENODE + '''
from collections import deque

def zigzag_level_order(root):
    if not root:
        return []
    out, q, left_to_right = [], deque([root]), True
    while q:
        level = deque()
        for _ in range(len(q)):
            node = q.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(list(level))
        left_to_right = not left_to_right
    return out''',
        "time": "O(N)", "space": "O(W)",
        "related": ["level-order-traversal"],
    },
    {
        "slug": "right-side-view", "title": "Binary Tree Right Side View", "pattern": "tree-bfs", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 199,
        "cue": "Last node of each level → BFS, take level[-1]",
        "problem": "Return the values visible from the right side, top to bottom.",
        "solution": _TREENODE + '''
from collections import deque

def right_side_view(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if i == n - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res''',
        "time": "O(N)", "space": "O(W)",
        "related": ["level-order-traversal"],
    },
    {
        "slug": "minimum-depth-binary-tree", "title": "Minimum Depth of Binary Tree", "pattern": "tree-bfs", "tier": "B",
        "companies": "Amazon, Facebook", "difficulty": "Easy", "leetcode": 111,
        "cue": "Shortest root-to-leaf → BFS returns at first leaf",
        "problem": "Return the minimum depth (nodes on shortest root-to-leaf path).",
        "solution": _TREENODE + '''
from collections import deque

def min_depth(root) -> int:
    if not root:
        return 0
    q = deque([(root, 1)])
    while q:
        node, d = q.popleft()
        if not node.left and not node.right:
            return d
        if node.left:
            q.append((node.left, d + 1))
        if node.right:
            q.append((node.right, d + 1))
    return 0''',
        "time": "O(N)", "space": "O(W)",
        "related": ["max-depth-binary-tree"],
    },
    {
        "slug": "populating-next-right-pointers", "title": "Populating Next Right Pointers in Each Node", "pattern": "tree-bfs", "tier": "C",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 116,
        "cue": "Connect level neighbors → use established next pointers, O(1) space",
        "problem": "Connect each node's `next` to its right neighbor on the same level (perfect binary tree).",
        "solution": '''class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    leftmost = root
    while leftmost and leftmost.left:
        node = leftmost
        while node:
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            node = node.next
        leftmost = leftmost.left
    return root''',
        "time": "O(N)", "space": "O(1)",
        "related": ["level-order-traversal"],
    },
    {
        "slug": "all-nodes-distance-k", "title": "All Nodes Distance K in Binary Tree", "pattern": "tree-bfs", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 863,
        "cue": "Distance K from a node → build parent links, BFS outward",
        "problem": "Return all node values at distance `k` from a target node.",
        "solution": _TREENODE + '''
from collections import deque, defaultdict

def distance_k(root, target, k: int) -> list[int]:
    graph = defaultdict(list)
    def build(node, parent):
        if not node:
            return
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        build(node.left, node)
        build(node.right, node)
    build(root, None)
    seen = {target.val}
    q = deque([(target.val, 0)])
    res = []
    while q:
        val, d = q.popleft()
        if d == k:
            res.append(val)
            continue
        for nb in graph[val]:
            if nb not in seen:
                seen.add(nb)
                q.append((nb, d + 1))
    return res''',
        "time": "O(N)", "space": "O(N)",
        "identify": "Treat the tree as an undirected graph (add parent edges), then BFS k steps from the target.",
        "related": ["level-order-traversal"],
    },
]
