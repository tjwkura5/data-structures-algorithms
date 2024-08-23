# Find a non-empty subarray with the largest sum.

list_nums = [4, -1, 2, -7, 3, 4]

# Brute Force: O(n^2)
def bruteForuce(nums):
    maxSum = nums[0]

    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum 

print(bruteForuce(list_nums))

# Brute Force: O(n^2)
list_nums = [4, -1, 2, -7, 3, 4]
def __bruteForuce(nums):
    maxSum = nums[0]
    max_subs = []

    for i in range(len(nums)):
        for j in range(i, len(nums) + 1):
            if sum(nums[i:j]) > maxSum:
                maxSum = sum(nums[i:j])
                max_subs.append(nums[i:j])
    return max_subs

print(__bruteForuce(list_nums))

def kadanes(nums):
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

print(kadanes(list_nums))

# Return the left and right index of the max subarray sum,
# Assuming theres exactly one result (no ties).
# sliding window variation of kadanes: O(n)

def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]

print(slidingWindow(list_nums))