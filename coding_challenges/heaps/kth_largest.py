import heapq
def find_kth_largest(nums, k):
    # heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]
    


print(find_kth_largest([3,2,1,5,6,4], 3))
