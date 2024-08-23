# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

nums = [5,4,-1,7,8]

def max_sub_array(nums):
    maxSum = nums[0]
    currSum = -10^4
    for n in nums:
        currSum += n 
        if n > currSum:
            currSum = n
        maxSum = max(currSum, maxSum)
    return maxSum

print(max_sub_array(nums))

nums = [5,-3, 5]
def __max_sub_array(nums):
    maxSum = nums[0]
    currSum = -10 ** 4
    L = 0 
    R = 0
    for i, n in enumerate(nums):
        currSum += n 
        if n > currSum:
            L = i
            currSum = n
        if currSum > maxSum:
            maxSum = currSum
            R = i
    return sum(nums[L:R+1])

print(__max_sub_array(nums))