# -*- coding: utf-8 -*-
"""Graph BFS/DFS questions."""

QUESTIONS = [
    {
        "slug": "number-of-islands", "title": "Number of Islands", "pattern": "graph-traversal", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Medium", "leetcode": 200,
        "cue": "Count connected '1' regions in a grid → DFS/BFS flood fill",
        "problem": "Count islands (4-directionally connected '1's) in a binary grid.",
        "solution": '''def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count''',
        "time": "O(R·C)", "space": "O(R·C)",
        "edges": ["Empty grid", "All water → 0", "All land → 1"],
        "related": ["max-area-of-island", "surrounded-regions"],
    },
    {
        "slug": "max-area-of-island", "title": "Max Area of Island", "pattern": "graph-traversal", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 695,
        "cue": "Largest connected region size → DFS returning area",
        "problem": "Return the maximum area of an island in a binary grid.",
        "solution": '''def max_area_of_island(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
    return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "flood-fill", "title": "Flood Fill", "pattern": "graph-traversal", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 733,
        "cue": "Recolor connected region → DFS from a seed",
        "problem": "Flood fill the region connected to `(sr, sc)` with `color`.",
        "solution": '''def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    start = image[sr][sc]
    if start == color:
        return image
    rows, cols = len(image), len(image[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != start:
            return
        image[r][c] = color
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    dfs(sr, sc)
    return image''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "clone-graph", "title": "Clone Graph", "pattern": "graph-traversal", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 133,
        "cue": "Deep copy a graph → DFS with visited map old→new",
        "problem": "Return a deep copy of a connected undirected graph.",
        "solution": '''class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

def clone_graph(node):
    if not node:
        return None
    clones = {}
    def dfs(n):
        if n in clones:
            return clones[n]
        copy = Node(n.val)
        clones[n] = copy
        for nb in n.neighbors:
            copy.neighbors.append(dfs(nb))
        return copy
    return dfs(node)''',
        "time": "O(V+E)", "space": "O(V)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "rotting-oranges", "title": "Rotting Oranges", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 994,
        "cue": "Spread over time from multiple sources → multi-source BFS",
        "problem": "Return minutes until no fresh orange remains (or -1), rot spreading to 4-neighbors each minute.",
        "identify": "Simultaneous spread from all rotten cells = multi-source BFS; enqueue all sources at time 0.",
        "solution": '''from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q:
        r, c, t = q.popleft()
        minutes = max(minutes, t)
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
    return minutes if fresh == 0 else -1''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["number-of-islands", "walls-and-gates"],
    },
    {
        "slug": "pacific-atlantic-water-flow", "title": "Pacific Atlantic Water Flow", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 417,
        "cue": "Cells reaching both oceans → DFS inward from each ocean border",
        "problem": "Return cells from which water can flow to both the Pacific and Atlantic oceans.",
        "solution": '''def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    def dfs(r, c, seen, prev):
        if ((r, c) in seen or not (0 <= r < rows and 0 <= c < cols)
                or heights[r][c] < prev):
            return
        seen.add((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r+dr, c+dc, seen, heights[r][c])
    for c in range(cols):
        dfs(0, c, pac, 0)
        dfs(rows-1, c, atl, 0)
    for r in range(rows):
        dfs(r, 0, pac, 0)
        dfs(r, cols-1, atl, 0)
    return [[r, c] for r, c in pac & atl]''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "surrounded-regions", "title": "Surrounded Regions", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 130,
        "cue": "Capture regions not touching border → DFS from border 'O's first",
        "problem": "Flip all 'O' regions to 'X' unless connected to the border.",
        "solution": '''def solve(board: list[list[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    def dfs(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'O':
            return
        board[r][c] = '#'
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
    for r in range(rows):
        dfs(r, 0); dfs(r, cols-1)
    for c in range(cols):
        dfs(0, c); dfs(rows-1, c)
    for r in range(rows):
        for c in range(cols):
            board[r][c] = 'O' if board[r][c] == '#' else 'X' ''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["number-of-islands"],
    },
    {
        "slug": "word-ladder", "title": "Word Ladder", "pattern": "graph-traversal", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Hard", "leetcode": 127,
        "cue": "Shortest transformation sequence → BFS over word graph",
        "problem": "Return the length of the shortest transformation from `beginWord` to `endWord` changing one letter at a time within `wordList`.",
        "solution": '''from collections import deque, defaultdict

def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    q = deque([(begin, 1)])
    while q:
        word, steps = q.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i+1:]
                if nxt in words:
                    words.remove(nxt)
                    q.append((nxt, steps + 1))
    return 0''',
        "time": "O(N·L·26)", "space": "O(N·L)",
        "related": ["word-ladder-ii"],
    },
    {
        "slug": "network-delay-time", "title": "Network Delay Time", "pattern": "graph-traversal", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 743,
        "cue": "Time for signal to reach all → Dijkstra from source",
        "problem": "Return the time for all `n` nodes to receive a signal from node `k`, or -1.",
        "solution": '''import heapq
from collections import defaultdict

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}
    pq = [(0, k)]
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        for nb, w in graph[node]:
            if nb not in dist:
                heapq.heappush(pq, (d + w, nb))
    return max(dist.values()) if len(dist) == n else -1''',
        "time": "O(E log V)", "space": "O(V+E)",
        "identify": "Single-source shortest path with non-negative weights → Dijkstra; answer is the max finalized distance.",
        "related": ["cheapest-flights-within-k-stops"],
    },
    {
        "slug": "cheapest-flights-within-k-stops", "title": "Cheapest Flights Within K Stops", "pattern": "graph-traversal", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 787,
        "cue": "Cheapest path with <= k stops → Bellman-Ford relax k+1 times",
        "problem": "Find the cheapest price from `src` to `dst` with at most `k` stops.",
        "solution": '''def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        tmp = dist[:]
        for u, v, w in flights:
            if dist[u] + w < tmp[v]:
                tmp[v] = dist[u] + w
        dist = tmp
    return dist[dst] if dist[dst] != INF else -1''',
        "time": "O(K·E)", "space": "O(V)",
        "identify": "At most k stops = at most k+1 edges → Bellman-Ford with k+1 relaxation rounds (snapshot to bound edges).",
        "related": ["network-delay-time"],
    },
    {
        "slug": "walls-and-gates", "title": "Walls and Gates", "pattern": "graph-traversal", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 286,
        "cue": "Distance to nearest gate for every cell → multi-source BFS from gates",
        "problem": "Fill each empty room with the distance to its nearest gate (0).",
        "solution": '''from collections import deque

def walls_and_gates(rooms: list[list[int]]) -> None:
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])
    INF = 2147483647
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                q.append((nr, nc))''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["rotting-oranges"],
    },
]
