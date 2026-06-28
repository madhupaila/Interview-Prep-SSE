# -*- coding: utf-8 -*-
"""Matrix Traversal questions."""

QUESTIONS = [
    {
        "slug": "spiral-matrix", "title": "Spiral Matrix", "pattern": "matrix-traversal", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, Google", "difficulty": "Medium", "leetcode": 54,
        "cue": "Read matrix in spiral order → shrink four boundaries",
        "problem": "Return all elements of the matrix in spiral order.",
        "solution": '''def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
    return res''',
        "time": "O(R·C)", "space": "O(1)",
        "related": ["spiral-matrix-ii", "rotate-image"],
    },
    {
        "slug": "rotate-image", "title": "Rotate Image", "pattern": "matrix-traversal", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, Apple", "difficulty": "Medium", "leetcode": 48,
        "cue": "Rotate 90 in place → transpose then reverse rows",
        "problem": "Rotate an `n×n` matrix 90° clockwise in place.",
        "solution": '''def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()''',
        "time": "O(N^2)", "space": "O(1)",
        "related": ["spiral-matrix"],
    },
    {
        "slug": "set-matrix-zeroes", "title": "Set Matrix Zeroes", "pattern": "matrix-traversal", "tier": "A",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 73,
        "cue": "Zero out rows/cols of any 0 → use first row/col as markers (O(1) space)",
        "problem": "If an element is 0, set its entire row and column to 0, in place.",
        "solution": '''def set_zeroes(matrix: list[list[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    first_row = any(matrix[0][c] == 0 for c in range(cols))
    first_col = any(matrix[r][0] == 0 for r in range(rows))
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row:
        for c in range(cols):
            matrix[0][c] = 0
    if first_col:
        for r in range(rows):
            matrix[r][0] = 0''',
        "time": "O(R·C)", "space": "O(1)",
        "related": ["rotate-image"],
    },
    {
        "slug": "spiral-matrix-ii", "title": "Spiral Matrix II", "pattern": "matrix-traversal", "tier": "B",
        "companies": "Amazon, Microsoft", "difficulty": "Medium", "leetcode": 59,
        "cue": "Fill 1..n^2 in spiral → same boundary shrink, write values",
        "problem": "Generate an `n×n` matrix filled with `1..n^2` in spiral order.",
        "solution": '''def generate_matrix(n: int) -> list[list[int]]:
    m = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    val = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            m[top][c] = val; val += 1
        top += 1
        for r in range(top, bottom + 1):
            m[r][right] = val; val += 1
        right -= 1
        for c in range(right, left - 1, -1):
            m[bottom][c] = val; val += 1
        bottom -= 1
        for r in range(bottom, top - 1, -1):
            m[r][left] = val; val += 1
        left += 1
    return m''',
        "time": "O(N^2)", "space": "O(N^2)",
        "related": ["spiral-matrix"],
    },
    {
        "slug": "diagonal-traverse", "title": "Diagonal Traverse", "pattern": "matrix-traversal", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 498,
        "cue": "Zigzag diagonals → group by r+c, reverse alternate diagonals",
        "problem": "Return matrix elements in diagonal (zigzag) order.",
        "solution": '''def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    if not mat:
        return []
    rows, cols = len(mat), len(mat[0])
    diagonals = {}
    for r in range(rows):
        for c in range(cols):
            diagonals.setdefault(r + c, []).append(mat[r][c])
    res = []
    for d in range(rows + cols - 1):
        if d % 2 == 0:
            res.extend(reversed(diagonals[d]))
        else:
            res.extend(diagonals[d])
    return res''',
        "time": "O(R·C)", "space": "O(R·C)",
        "related": ["spiral-matrix"],
    },
    {
        "slug": "game-of-life", "title": "Game of Life", "pattern": "matrix-traversal", "tier": "C",
        "companies": "Amazon, Google, Dropbox", "difficulty": "Medium", "leetcode": 289,
        "cue": "In-place next state → encode old/new in 2 bits",
        "problem": "Compute the next state of Conway's Game of Life in place.",
        "solution": '''def game_of_life(board: list[list[int]]) -> None:
    rows, cols = len(board), len(board[0])
    def live_neighbors(r, c):
        cnt = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] & 1:
                    cnt += 1
        return cnt
    for r in range(rows):
        for c in range(cols):
            n = live_neighbors(r, c)
            if board[r][c] & 1:
                if n in (2, 3):
                    board[r][c] |= 2             # stays alive (bit1 = next)
            elif n == 3:
                board[r][c] |= 2                 # becomes alive
    for r in range(rows):
        for c in range(cols):
            board[r][c] >>= 1''',
        "time": "O(R·C)", "space": "O(1)",
        "identify": "Store next state in a second bit so neighbor counts still see the old state, then shift.",
        "related": ["set-matrix-zeroes"],
    },
]
