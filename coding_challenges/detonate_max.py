# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).
import math
from collections import defaultdict

bombs = [[2,1,3],[6,1,4]]

def max_detonation(bombs):
    bombs_map = defaultdict(list)
    for i in range(len(bombs)):
        bombs_map[i] = []
        x1 = bombs[i][0]
        y1 = bombs[i][1]
        r1 = bombs[i][2]
        for j in range(len(bombs)):
            x2 = bombs[j][0]
            y2 = bombs[j][1]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2


            if math.sqrt(dist) <= r1:
                if i != j:
                    bombs_map[i].append(j)
    def dfs(curr, visited):
        visited.add(curr)
        for neib in bombs_map[curr]:
            if neib not in visited:
                dfs(neib, visited)
        return len(visited)
    answer =0
    for i in range(len(bombs)):
        visited = set()
        answer = max(answer, dfs(i, visited))
    return answer


print(max_detonation([[2,1,3],[6,1,4]]))

print(max_detonation([[1,1,5],[10,10,5]]))

print(max_detonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))