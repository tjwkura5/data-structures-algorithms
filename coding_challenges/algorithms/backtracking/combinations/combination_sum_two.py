# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.


def combo_sum(nums, target):
    res = []
    nums.sort()
    def dfs(i, curr):
        if sum(curr) == target:
            res.append(curr.copy())
            return 
        if i >= len(nums) or sum(curr) > target:
            return

        curr.append(nums[i])
        dfs(i+1, curr)

        #
        curr.pop()
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        dfs(i+1, curr)
    dfs(0, [])
    return res

print(combo_sum([10,1,2,7,6,1,5], 8))