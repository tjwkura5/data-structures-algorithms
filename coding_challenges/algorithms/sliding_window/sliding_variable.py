# Find the length of the longest subarray, with the same value in each position.

def longestSubarray(nums):
    max_length = 0
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] == nums[R]:
            length += 1
        
        if nums[L] != nums[R]:
            L = R
            length = 1
        
        max_length = max(max_length, length)

    return max_length

print(longestSubarray([4,2,2,3,3,3,3]))

# Find the minimum length subarray, wehre the sum is greater than or equal to the target.

def find_min_sub(nums, target):
    L = 0
    total = 0
    length = len(nums) + 100

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R-L + 1, length)
            total -= nums[L]
            L += 1

    return length

print(find_min_sub([2,3,1,2,4,3], 6))