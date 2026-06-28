# -*- coding: utf-8 -*-
"""Topological Sort questions."""

QUESTIONS = [
    {
        "slug": "course-schedule", "title": "Course Schedule", "pattern": "topological-sort", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Medium", "leetcode": 207,
        "cue": "Can finish all with prerequisites → detect cycle via Kahn's",
        "problem": "Return True if you can finish all courses given prerequisite pairs.",
        "solution": '''from collections import deque, defaultdict

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    indeg = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indeg[course] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    seen = 0
    while q:
        node = q.popleft()
        seen += 1
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return seen == num_courses''',
        "time": "O(V+E)", "space": "O(V+E)",
        "edges": ["Cycle → False", "No prereqs → True"],
        "related": ["course-schedule-ii", "alien-dictionary"],
    },
    {
        "slug": "course-schedule-ii", "title": "Course Schedule II", "pattern": "topological-sort", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 210,
        "cue": "Return a valid course order → Kahn's, output order",
        "problem": "Return an ordering of courses to finish all, or [] if impossible.",
        "solution": '''from collections import deque, defaultdict

def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    indeg = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indeg[course] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in graph[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == num_courses else []''',
        "time": "O(V+E)", "space": "O(V+E)",
        "related": ["course-schedule"],
    },
    {
        "slug": "minimum-height-trees", "title": "Minimum Height Trees", "pattern": "topological-sort", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 310,
        "cue": "Roots giving min height → trim leaves layer by layer",
        "problem": "Return all roots that produce a minimum height tree.",
        "solution": '''from collections import defaultdict, deque

def find_min_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    if n == 1:
        return [0]
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    leaves = deque(node for node in range(n) if len(graph[node]) == 1)
    remaining = n
    while remaining > 2:
        size = len(leaves)
        remaining -= size
        for _ in range(size):
            leaf = leaves.popleft()
            nb = graph[leaf].pop()
            graph[nb].discard(leaf)
            if len(graph[nb]) == 1:
                leaves.append(nb)
    return list(leaves)''',
        "time": "O(V)", "space": "O(V)",
        "identify": "The centroids of the tree minimize height; peel leaves until ≤2 nodes remain.",
        "related": ["course-schedule"],
    },
    {
        "slug": "alien-dictionary", "title": "Alien Dictionary", "pattern": "topological-sort", "tier": "C",
        "companies": "Amazon, Meta, Google, Airbnb", "difficulty": "Hard", "leetcode": 269,
        "cue": "Derive char order from sorted words → build edges, topo sort",
        "problem": "Given words sorted in an alien language, return a valid character order (or '').",
        "solution": '''from collections import defaultdict, deque

def alien_order(words: list[str]) -> str:
    graph = defaultdict(set)
    indeg = {c: 0 for w in words for c in w}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""                        # prefix violation
    q = deque(c for c in indeg if indeg[c] == 0)
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for nb in graph[c]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    return "".join(order) if len(order) == len(indeg) else ""''',
        "time": "O(C)", "space": "O(1)",
        "edges": ["Invalid prefix ordering → ''", "Cycle → ''"],
        "related": ["course-schedule-ii"],
    },
]
