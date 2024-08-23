# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

def exist(matrix, word):
    ROWs = len(matrix)
    COLS = len(matrix[0])
    path = set()
    
    def backtrack(r, c, i):
        if i == len(word):
            return True
        if (r >= ROWs or c >= COLS) or (r < 0 or c < 0):
            return False
        if (r, c) in path:
            return False 
        if matrix[r][c] != word[i]:
            return False
         
        path.add((r, c))
        res = (backtrack(r+1, c, i+1) or
        backtrack(r-1, c, i+1) or
        backtrack(r, c+1, i+1) or   
        backtrack(r, c-1, i+1))
        path.remove((r,c))
        return res

    for r in range(ROWs):
        for c in range(COLS):
            if backtrack(r, c, 0): return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))