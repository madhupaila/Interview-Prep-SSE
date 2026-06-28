# -*- coding: utf-8 -*-
"""Trie questions."""

QUESTIONS = [
    {
        "slug": "implement-trie", "title": "Implement Trie (Prefix Tree)", "pattern": "trie", "tier": "A",
        "companies": "Amazon, Google, Meta, Microsoft", "difficulty": "Medium", "leetcode": 208,
        "cue": "Prefix dictionary → nested children dict + is_word flag",
        "problem": "Implement a trie with `insert`, `search`, and `startsWith`.",
        "solution": '''class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True                          # word-end marker

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and '$' in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node''',
        "time": "O(L) per op", "space": "O(total chars)",
        "related": ["design-add-search-words", "word-search-ii"],
    },
    {
        "slug": "design-add-search-words", "title": "Design Add and Search Words Data Structure", "pattern": "trie", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 211,
        "cue": "Search with '.' wildcard → trie + DFS on wildcard",
        "problem": "Support `addWord` and `search` where `.` matches any single character.",
        "solution": '''class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '$' in node
            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1)
                           for k, child in node.items() if k != '$')
            return ch in node and dfs(node[ch], i + 1)
        return dfs(self.root, 0)''',
        "time": "O(L) avg, O(26^L) worst", "space": "O(total chars)",
        "related": ["implement-trie"],
    },
    {
        "slug": "replace-words", "title": "Replace Words", "pattern": "trie", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 648,
        "cue": "Replace word by shortest root prefix → trie lookup",
        "problem": "Replace each word in a sentence with the shortest dictionary root that is its prefix.",
        "solution": '''def replace_words(dictionary: list[str], sentence: str) -> str:
    root = {}
    for w in dictionary:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = True

    def shortest_root(word):
        node = root
        for i, ch in enumerate(word):
            if ch not in node:
                break
            node = node[ch]
            if '$' in node:
                return word[:i + 1]
        return word

    return " ".join(shortest_root(w) for w in sentence.split())''',
        "time": "O(total chars)", "space": "O(total chars)",
        "related": ["implement-trie"],
    },
    {
        "slug": "word-search-ii", "title": "Word Search II", "pattern": "trie", "tier": "C",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Hard", "leetcode": 212,
        "cue": "Find many words on a board → trie of words + board DFS",
        "problem": "Return all words from the list that can be formed on the board (4-directional, no reuse).",
        "identify": "Searching each word separately is wasteful; a trie lets one DFS over the board match all words simultaneously.",
        "solution": '''def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w
    rows, cols = len(board), len(board[0])
    res = []
    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return
        nxt = node[ch]
        if '$' in nxt:
            res.append(nxt.pop('$'))             # found; avoid duplicates
        board[r][c] = '#'
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return res''',
        "time": "O(R·C·4^L)", "space": "O(total chars)",
        "related": ["implement-trie", "word-search"],
    },
]
