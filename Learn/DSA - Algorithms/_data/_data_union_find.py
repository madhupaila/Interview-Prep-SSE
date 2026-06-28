# -*- coding: utf-8 -*-
"""Union-Find questions."""

_DSU = '''class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
'''

QUESTIONS = [
    {
        "slug": "number-of-provinces", "title": "Number of Provinces", "pattern": "union-find", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 547,
        "cue": "Count connected groups from adjacency matrix → union friends, count roots",
        "problem": "Given an `n×n` adjacency matrix `isConnected`, return the number of provinces (connected components).",
        "solution": _DSU + '''
def find_circle_num(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j]:
                dsu.union(i, j)
    return dsu.count''',
        "time": "O(N^2 α)", "space": "O(N)",
        "related": ["number-of-connected-components", "graph-valid-tree"],
    },
    {
        "slug": "number-of-connected-components", "title": "Number of Connected Components in an Undirected Graph", "pattern": "union-find", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 323,
        "cue": "Count components from edge list → union edges, count roots",
        "problem": "Return the number of connected components in an undirected graph with `n` nodes.",
        "solution": _DSU + '''
def count_components(n: int, edges: list[list[int]]) -> int:
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.count''',
        "time": "O(E α)", "space": "O(N)",
        "related": ["number-of-provinces", "graph-valid-tree"],
    },
    {
        "slug": "redundant-connection", "title": "Redundant Connection", "pattern": "union-find", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 684,
        "cue": "Edge forming a cycle in undirected → union returns False",
        "problem": "Return the edge that, if removed, makes the graph a tree (the one creating a cycle).",
        "solution": _DSU + '''
def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    dsu = DSU(len(edges) + 1)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []''',
        "time": "O(E α)", "space": "O(N)",
        "identify": "Adding an edge whose endpoints already share a root closes a cycle — that edge is redundant.",
        "related": ["graph-valid-tree"],
    },
    {
        "slug": "graph-valid-tree", "title": "Graph Valid Tree", "pattern": "union-find", "tier": "B",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 261,
        "cue": "Is it a tree → n-1 edges + no cycle (one component)",
        "problem": "Return True if `n` nodes and `edges` form a valid tree.",
        "solution": _DSU + '''
def valid_tree(n: int, edges: list[list[int]]) -> bool:
    if len(edges) != n - 1:
        return False
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return False                          # cycle
    return dsu.count == 1''',
        "time": "O(E α)", "space": "O(N)",
        "edges": ["Must have exactly n-1 edges", "No cycles", "Single component"],
        "related": ["redundant-connection", "number-of-connected-components"],
    },
    {
        "slug": "accounts-merge", "title": "Accounts Merge", "pattern": "union-find", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 721,
        "cue": "Merge accounts sharing emails → union by email owner",
        "problem": "Merge accounts that share any email; return merged accounts with sorted emails.",
        "solution": _DSU + '''
from collections import defaultdict

def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    dsu = DSU(len(accounts))
    email_to_id = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                dsu.union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    groups = defaultdict(set)
    for email, i in email_to_id.items():
        groups[dsu.find(i)].add(email)
    return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]''',
        "time": "O(N·K log K)", "space": "O(N·K)",
        "related": ["number-of-provinces"],
    },
    {
        "slug": "number-of-islands-ii", "title": "Number of Islands II", "pattern": "union-find", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Hard", "leetcode": 305,
        "cue": "Islands count after each addLand (online) → Union-Find dynamic",
        "problem": "After each land addition, return the current number of islands.",
        "solution": _DSU + '''
def num_islands2(m: int, n: int, positions: list[list[int]]) -> list[int]:
    dsu = DSU(m * n)
    land = set()
    res = []
    count = 0
    for r, c in positions:
        idx = r * n + c
        if idx in land:
            res.append(count)
            continue
        land.add(idx)
        count += 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            nidx = nr * n + nc
            if 0 <= nr < m and 0 <= nc < n and nidx in land:
                if dsu.union(idx, nidx):
                    count -= 1
        res.append(count)
    return res''',
        "time": "O(K α)", "space": "O(M·N)",
        "identify": "Each new land starts as its own island; merging with existing neighbors decrements the count.",
        "related": ["number-of-islands", "redundant-connection"],
    },
]
