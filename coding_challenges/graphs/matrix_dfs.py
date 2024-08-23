# count paths (backtracking)

# Q: Count the unique paths from the 
# top left to the bottom right.
# # A single path may only move 0's and can't visit 
# the same cell more than
# # once.
# # Time Complexity 4^nm 
# where n is the number of rows and m is the number of columns 
# # The space complexity will be the entire call 
# stack since this is recursive. 
# Therefore, it will be # O(n ∗ m).

def dfs(matrix, r, c, visit):
    count = 0
    ROWs = len(matrix)
    COLS = len(matrix[0])
    if (min(r, c) < 0 or r >= ROWs or c>= COLS):
          return 0
    if (r, c) in visit:
       return 0
    if matrix[r][c] != 0:
         return 0
    if r == ROWs - 1 and c == COLS - 1:
          return 1
    
    visit.add((r, c))
    count += dfs(matrix, r+1, c, visit)
    count += dfs(matrix, r-1, c, visit)
    count += dfs(matrix, r, c+1, visit)
    count += dfs(matrix, r, c-1, visit)
    visit.remove((r,c))

    return count 

matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

print(dfs(matrix, 0, 0, set()))