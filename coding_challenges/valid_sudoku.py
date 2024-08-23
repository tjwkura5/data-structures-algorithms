from collections import defaultdict

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def valid_sudoku(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or 
                board[r][c] in squares[(r //3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[((r //3, c // 3))].add(board[r][c])