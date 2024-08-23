# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up 
# to target is less than 150 combinations for the given input.


def comb_sum(nums, target):
    res = []
    def dfs(i, cur):
        if sum(cur) == target:
            res.append(cur.copy())
            return
        if i >= len(nums) or sum(cur) > target:
            return 
         
        cur.append(nums[i])
        dfs(i, cur)
        cur.pop()
        dfs(i+1, cur)          
    dfs(0, [])
    return res

print(comb_sum([1], 2))