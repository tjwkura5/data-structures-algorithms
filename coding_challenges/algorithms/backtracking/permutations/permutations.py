# Q: Given a list of nums, return all possible disting permutations of nums.

nums = [1,2,3,4]


def subsets(nums):
    curr = []
    res = []
    def dfs(i):
        if i>= len(nums):
            res.append(curr.copy())
            return

        #decision to include
        curr.append(nums[i])
        dfs(i+1)

        #decision not to include
        curr.pop()
        dfs(i+1)

    dfs(0)
    return res


# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

def permutations(nums):
    res = []
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return 
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    backtrack([])
    return res

# Time complexity O(n* 2^n) or n! space complexity o(n):
def permutationsWithDup(nums):
    res = []
    counter = {}
    for num in nums:
        counter[num] = counter.get(num,0) + 1
    def backtrack(curr, counter):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return 
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                backtrack(curr, counter)
                curr.pop()
                counter[num] += 1

    backtrack([], counter)
    return res 

print(permutationsWithDup([1,2,3]))
print(permutations([1,2,3]))
