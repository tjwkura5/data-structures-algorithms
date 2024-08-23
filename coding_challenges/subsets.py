def subsets(nums):
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            print(res)
            return
        #decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)
        #decision not to include nums[i]
        subset.pop()
        dfs(i+1)
    dfs(0)
    return res

print(subsets([1,2,3]))
