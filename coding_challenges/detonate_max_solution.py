from collections import defaultdict
def maximumDetonation(bombs):
    graph = defaultdict(list)
    n = len(bombs)
        
    # Build the graph
    for i in range(n):
        for j in range(n):
            if i == j:
                continue         
            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]

            # Create a path from node i to node j, if bomb i detonates bomb j.
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    # DFS to get the number of nodes reachable from a given node cur
    def dfs(cur, visited):
        visited.add(cur)
        for neib in graph[cur]:
            if neib not in visited:
                dfs(neib, visited)
        return len(visited)
    print(graph)
    answer = 0
    for i in range(n):
        visited = set()
        answer = max(answer, dfs(i, visited))
        
    return answer
print(maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))