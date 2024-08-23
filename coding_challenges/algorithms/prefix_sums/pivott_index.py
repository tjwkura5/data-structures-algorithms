def pivot_index(nums):
    total = sum(nums)  # O(n)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1


print(pivot_index([1,7,3,6,5,6]))