# def subarray_sum(nums, target):
#    sum_index = {0: -1}
#    current_sum = 0

#    for i, num in enumerate(nums):
#       current_sum = current_sum + num
#       if current_sum - target in sum_index:
#          starting_index = sum_index[current_sum - target] + 1
#          return [starting_index, i]
#       else:
#          sum_index[current_sum] = i
#    return []

def find_all_subs(nums):
   n = len(nums)
   sublists = []
   for start in range(n):
      for end in range(start + 1, n + 1):
         sublists.append(nums[start:end])
   return sublists

def subarray_sum(nums, target):
   subslist = find_all_subs(nums)
   for list in subslist:
      if sum(list) == target:
         starting_index = nums.index(list[0])
         end = nums.index(list[len(list) - 1])
         return [starting_index, end]
   return []



nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""