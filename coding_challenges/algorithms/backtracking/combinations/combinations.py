# Q: Given two nums n&k, return all possible combinations
# of size = k, choose values between 1 and n. 

#Time: O(k * C(n, k))
def combinations(n, k):
    res = []
    combo = []
    def dfs(i):
        if len(combo) == k:
            res.append(combo.copy())
            return
         
        for j in range(i, n+1):
            combo.append(j)
            dfs(j+1)
            combo.pop()

    dfs(1)
    return res

print(combinations(5, 2))