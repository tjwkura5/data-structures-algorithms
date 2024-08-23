def find_max_min(nums):
    i = 0
    min_v = nums[i]
    max_v = nums[i]
    while i < len(nums):
        min_v = min(min_v, nums[i])
        max_v = max(max_v, nums[i])
        i += 1
    return (min_v, max_v)


print(find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""