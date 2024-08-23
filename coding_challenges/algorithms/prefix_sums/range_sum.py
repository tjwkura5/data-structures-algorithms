class PrefixSum:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left -1] if left > 0 else 0
        return preRight - preLeft


my_prefix = PrefixSum([-2, 0, 3, -5, 2, -1])
print(my_prefix.prefix)
print(my_prefix.sumRange(0, 2))
print(my_prefix.sumRange(2, 5))
print(my_prefix.sumRange(0, 5))