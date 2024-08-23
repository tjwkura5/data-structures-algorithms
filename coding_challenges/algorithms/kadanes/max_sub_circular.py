def max_sub_array(nums):
    globMax, globMin = nums[0], nums[0]
    curMax, curMin = 0, 0
    total = 0

    for n in nums:
        curMax = max(curMax + n, n)
        curMin = min(curMin + n, n)
        total += n
        globMax = max(globMax, curMax)
        globMin = min(globMin, curMin)

    return max(globMax, total - globMin) if globMax > 0 else globMax
        
        
print(max_sub_array([5, -3, 5]))

