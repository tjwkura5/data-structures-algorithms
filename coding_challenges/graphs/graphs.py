from collections import defaultdict
# 1. Matrix - A matrix is just a two dimensional array
# 2. Adjacency Matrix
# 3. Adjacency List

# 0 - Free space 
# 1 - Blocked

matrix = [[0,0,0,0],
          [1,1,0,0],
          [0,0,0,1],
          [0,1,0,0]]

adjmatrix = [[0,0,0,0],
             [1,1,0,0],
             [0,0,0,1],
             [0,1,0,0]]

adjList = defaultdict(list)
adjList[2] = [3]
adjList[3] = [1]
adjList[1] = [1, 0]
adjList[0] = []