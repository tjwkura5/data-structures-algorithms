class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

# After building this sum, we can calculate the sum of any subarray that starts at 
# left and ends at right in O(1) time. This is because we won't need to recalculate it. 
# We can do this by prefix[right] - prefix[left - 1]. 
# The -1 will ensure we exclude the running sum of all the numbers before left. 
# However, if left points to 0, our prefix[left-1] will just be 0.

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)
   
