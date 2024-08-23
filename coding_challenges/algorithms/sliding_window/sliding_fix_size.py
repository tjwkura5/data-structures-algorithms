def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False

def closeDuplicates(nums, k):
    window = set()
    L = 0
    for n in nums:
        if len(window) == k:
            window.remove(nums[L])
            L += 1
        if n in window:
            return True
        window.add(n)
    return False

print(closeDuplicates([1,2,3,4,5], 3))