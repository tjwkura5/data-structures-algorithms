def three_sum(nums):
    L = 0
    R = len(nums) - 1
    num_map = {}
    res = []
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1
    while L < R:
        comp = 0 - (nums[L]+ nums[R])
        if comp in num_map:
            if num_map[comp] > 0:
                res.append([nums[L], nums[R], comp])
                num_map[comp] = num_map.get(comp) - 1
                num_map[nums[L]] = num_map.get(nums[L]) - 1
                num_map[nums[R]] = num_map.get(nums[R]) -1
            L +=1
        else:
            R -= 1
    print(num_map)
    return res
print(three_sum([-1,0,1,2,-1,-4]))

class Solution:
    def threeSum(nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res
