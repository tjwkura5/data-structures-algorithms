# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

def sub_array_sums(nums, k):
    count = 0
    for i in range(len(nums)):
        total = nums[i]
        if total == k:
            count +=1
        for j in range(i + 1, len(nums)):
            total += nums[j]
            if total == k:
                count +=1
    return count

print(sub_array_sums([1,7,3,6,5,6], 11))

def subarraySum(nums, k):
    count = 0
    sum = 0
    dic = {}
    dic[0] = 1
    for i in range(len(nums)):
        sum += nums[i]
        if sum-k in dic:
            count += dic[sum-k]
        dic[sum] = dic.get(sum, 0)+1
    return count

print(subarraySum([1,7,3,6,5,6], 11))
