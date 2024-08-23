# Given an integer array nums of unique elements, return all possible 
# subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
# Time: O(n * 2^n), Space: O(n)
def subsetsWithoutDups(nums):
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)
    return subsets 

def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())
        return 
    
    #decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)

    #decision Not to include  nums[i]
    curSet.pop()
    helper(i + 1, nums, curSet, subsets)

#Q: Given a list of nums that are not necessarily distinct, return all distinct subsets
# Time: O(n * 2^n), Space: O(n)
def subsetsWith(nums):
    nums.sort()
    subset = []
    res = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            print(res)
            return 
        
        #Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        #Descion not to include nums[i]
        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i+1)
    dfs(0)
    return res

print(subsetsWith([1,2,3]))