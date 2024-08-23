# Q: Given a list of nums, return all possible disting permutations of nums.

nums = [1,2,3,4]

def solution(nums):
    res = []
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1 
    def dfs(curr, counter):
        if len(curr) == len(nums):
            res.append(curr.copy())
            return 
        
        for num in counter:
            if counter[num] > 0:
                curr.append(num)
                counter[num] -= 1
                dfs(curr, counter)
                curr.pop()
                counter[num] += 1
                
    dfs([], counter)
    return res 

print(solution(nums))