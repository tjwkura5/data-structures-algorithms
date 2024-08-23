import heapq
def find_kth_largest(nums, k):
   heapq._heapify_max(nums)

   while len(nums) > k:
        heapq._heappop_max(nums)
    
   return nums[0]

print(find_kth_largest([3,2,1,5,6,4], 3))