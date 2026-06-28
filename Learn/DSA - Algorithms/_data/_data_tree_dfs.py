# -*- coding: utf-8 -*-
"""Tree DFS questions."""

_TREENODE = '''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

QUESTIONS = [
    {
        "slug": "invert-binary-tree", "title": "Invert Binary Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Easy", "leetcode": 226,
        "cue": "Mirror a tree → swap children recursively",
        "problem": "Invert (mirror) a binary tree.",
        "solution": _TREENODE + '''
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root''',
        "time": "O(N)", "space": "O(H)",
        "related": ["same-tree", "symmetric-tree"],
    },
    {
        "slug": "same-tree", "title": "Same Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 100,
        "cue": "Structural + value equality → parallel DFS",
        "problem": "Return True if two binary trees are identical.",
        "solution": _TREENODE + '''
def is_same_tree(p, q) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)''',
        "time": "O(N)", "space": "O(H)",
        "related": ["subtree-of-another-tree", "symmetric-tree"],
    },
    {
        "slug": "diameter-of-binary-tree", "title": "Diameter of Binary Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Easy", "leetcode": 543,
        "cue": "Longest path between any two nodes → bubble up height + global max",
        "problem": "Return the length (in edges) of the longest path between any two nodes.",
        "solution": _TREENODE + '''
def diameter_of_binary_tree(root) -> int:
    best = 0
    def depth(node):
        nonlocal best
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)
    depth(root)
    return best''',
        "time": "O(N)", "space": "O(H)",
        "identify": "Path through a node = leftHeight + rightHeight; track global max while returning height to parent.",
        "related": ["binary-tree-maximum-path-sum", "max-depth-binary-tree"],
    },
    {
        "slug": "balanced-binary-tree", "title": "Balanced Binary Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 110,
        "cue": "Height-balanced check → return height, propagate imbalance",
        "problem": "Return True if the tree is height-balanced (subtree heights differ by ≤ 1).",
        "solution": _TREENODE + '''
def is_balanced(root) -> bool:
    def height(node):
        if not node:
            return 0
        l = height(node.left)
        if l == -1:
            return -1
        r = height(node.right)
        if r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    return height(root) != -1''',
        "time": "O(N)", "space": "O(H)",
        "related": ["max-depth-binary-tree"],
    },
    {
        "slug": "path-sum", "title": "Path Sum", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 112,
        "cue": "Root-to-leaf equals target → subtract along path",
        "problem": "Return True if some root-to-leaf path sums to `targetSum`.",
        "solution": _TREENODE + '''
def has_path_sum(root, target: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return target == root.val
    rem = target - root.val
    return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)''',
        "time": "O(N)", "space": "O(H)",
        "related": ["path-sum-ii", "path-sum-iii"],
    },
    {
        "slug": "lowest-common-ancestor-bst", "title": "Lowest Common Ancestor of a BST", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 235,
        "cue": "LCA in BST → walk down using value comparison",
        "problem": "Return the lowest common ancestor of two nodes in a BST.",
        "solution": _TREENODE + '''
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None''',
        "time": "O(H)", "space": "O(1)",
        "related": ["lowest-common-ancestor-binary-tree"],
    },
    {
        "slug": "subtree-of-another-tree", "title": "Subtree of Another Tree", "pattern": "tree-dfs", "tier": "A",
        "companies": "Amazon, Meta", "difficulty": "Easy", "leetcode": 572,
        "cue": "Is subRoot a subtree → same-tree check at each node",
        "problem": "Return True if `subRoot` is a subtree of `root`.",
        "solution": _TREENODE + '''
def is_subtree(root, sub) -> bool:
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)
    if not root:
        return False
    if same(root, sub):
        return True
    return is_subtree(root.left, sub) or is_subtree(root.right, sub)''',
        "time": "O(M·N)", "space": "O(H)",
        "related": ["same-tree"],
    },
    {
        "slug": "validate-bst", "title": "Validate Binary Search Tree", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta, Microsoft, Bloomberg", "difficulty": "Medium", "leetcode": 98,
        "cue": "Is it a BST → pass (low, high) bounds down",
        "problem": "Return True if the binary tree is a valid BST.",
        "identify": "Comparing only with the immediate parent is insufficient; thread min/max bounds so every node respects all ancestors.",
        "solution": _TREENODE + '''
def is_valid_bst(root) -> bool:
    def valid(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return valid(node.left, low, node.val) and valid(node.right, node.val, high)
    return valid(root, float('-inf'), float('inf'))''',
        "time": "O(N)", "space": "O(H)",
        "edges": ["Equal values not allowed", "Single node valid"],
        "related": ["kth-smallest-in-bst"],
    },
    {
        "slug": "kth-smallest-in-bst", "title": "Kth Smallest Element in a BST", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 230,
        "cue": "Kth smallest in BST → inorder yields sorted, stop at k",
        "problem": "Return the kth smallest value in a BST.",
        "solution": _TREENODE + '''
def kth_smallest(root, k: int) -> int:
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    return -1''',
        "time": "O(H + k)", "space": "O(H)",
        "related": ["validate-bst"],
    },
    {
        "slug": "lowest-common-ancestor-binary-tree", "title": "Lowest Common Ancestor of a Binary Tree", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta, Microsoft, Google", "difficulty": "Medium", "leetcode": 236,
        "cue": "LCA (no BST) → return node if found in subtree; split point is LCA",
        "problem": "Return the LCA of two nodes in a binary tree.",
        "solution": _TREENODE + '''
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root                              # p and q in different subtrees
    return left or right''',
        "time": "O(N)", "space": "O(H)",
        "related": ["lowest-common-ancestor-bst"],
    },
    {
        "slug": "path-sum-ii", "title": "Path Sum II", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 113,
        "cue": "All root-to-leaf paths summing to target → backtracking DFS",
        "problem": "Return all root-to-leaf paths where the sum equals `targetSum`.",
        "solution": _TREENODE + '''
def path_sum(root, target: int) -> list[list[int]]:
    res = []
    def dfs(node, remaining, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and remaining == node.val:
            res.append(path[:])
        else:
            dfs(node.left, remaining - node.val, path)
            dfs(node.right, remaining - node.val, path)
        path.pop()
    dfs(root, target, [])
    return res''',
        "time": "O(N)", "space": "O(H)",
        "related": ["path-sum", "path-sum-iii"],
    },
    {
        "slug": "construct-tree-preorder-inorder", "title": "Construct Binary Tree from Preorder and Inorder", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 105,
        "cue": "Rebuild tree → preorder gives root, inorder splits subtrees",
        "problem": "Build the binary tree from its preorder and inorder traversals.",
        "solution": _TREENODE + '''
def build_tree(preorder: list[int], inorder: list[int]):
    idx = {v: i for i, v in enumerate(inorder)}
    self_pre = iter(preorder)
    def build(lo, hi):
        if lo > hi:
            return None
        val = next(self_pre)
        node = TreeNode(val)
        mid = idx[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node
    return build(0, len(inorder) - 1)''',
        "time": "O(N)", "space": "O(N)",
        "related": ["construct-tree-inorder-postorder"],
    },
    {
        "slug": "good-nodes-binary-tree", "title": "Count Good Nodes in Binary Tree", "pattern": "tree-dfs", "tier": "B",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 1448,
        "cue": "Node >= all ancestors on path → carry running max down",
        "problem": "Count nodes whose value is ≥ every value on the path from root.",
        "solution": _TREENODE + '''
def good_nodes(root) -> int:
    def dfs(node, max_so_far):
        if not node:
            return 0
        good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return good + dfs(node.left, new_max) + dfs(node.right, new_max)
    return dfs(root, root.val)''',
        "time": "O(N)", "space": "O(H)",
        "related": ["path-sum"],
    },
    {
        "slug": "binary-tree-maximum-path-sum", "title": "Binary Tree Maximum Path Sum", "pattern": "tree-dfs", "tier": "C",
        "companies": "Amazon, Meta, Microsoft, Google", "difficulty": "Hard", "leetcode": 124,
        "cue": "Max path sum (any to any) → clamp child gains at 0, track global",
        "problem": "Return the maximum path sum where a path is any node sequence via parent-child edges.",
        "identify": "Each node returns its best downward gain (clamped at 0); the best path through it is val + leftGain + rightGain, tracked globally.",
        "solution": _TREENODE + '''
def max_path_sum(root) -> int:
    best = float('-inf')
    def gain(node):
        nonlocal best
        if not node:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)
    gain(root)
    return best''',
        "time": "O(N)", "space": "O(H)",
        "related": ["diameter-of-binary-tree"],
    },
    {
        "slug": "serialize-deserialize-binary-tree", "title": "Serialize and Deserialize Binary Tree", "pattern": "tree-dfs", "tier": "C",
        "companies": "Amazon, Meta, Google, LinkedIn", "difficulty": "Hard", "leetcode": 297,
        "cue": "Tree <-> string → preorder with null markers",
        "problem": "Design `serialize` and `deserialize` for a binary tree.",
        "solution": _TREENODE + '''
class Codec:
    def serialize(self, root) -> str:
        out = []
        def dfs(node):
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str):
        vals = iter(data.split(","))
        def build():
            v = next(vals)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node
        return build()''',
        "time": "O(N)", "space": "O(N)",
        "related": ["construct-tree-preorder-inorder"],
    },
    {
        "slug": "path-sum-iii", "title": "Path Sum III", "pattern": "tree-dfs", "tier": "C",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 437,
        "cue": "Count downward paths summing to target → prefix-sum hashmap on the path",
        "problem": "Count paths (any node to any descendant) summing to `targetSum`.",
        "solution": _TREENODE + '''
from collections import defaultdict

def path_sum_iii(root, target: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    def dfs(node, prefix):
        if not node:
            return 0
        prefix += node.val
        res = count[prefix - target]
        count[prefix] += 1
        res += dfs(node.left, prefix) + dfs(node.right, prefix)
        count[prefix] -= 1                       # backtrack
        return res
    return dfs(root, 0)''',
        "time": "O(N)", "space": "O(H)",
        "identify": "Combine Tree DFS with the Subarray-Sum-Equals-K prefix-sum trick along the current root-to-node path.",
        "related": ["path-sum-ii", "subarray-sum-equals-k"],
    },
]
