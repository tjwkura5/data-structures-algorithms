# def longest_consecutive_sequence(nums):
#     nums.sort()
#     n = len(nums)
#     longest_consecutive_sequence = 0
#     if n == 1:
#         return 1
#     count = 1
#     for num in nums:
#         if num - 1 in set(nums):
#             count +=1
#         else:
#             count = 1
#         longest_consecutive_sequence = max(longest_consecutive_sequence, count)
#     return longest_consecutive_sequence

# def longest_consecutive_sequence(nums):
#     num_set = set(nums)
#     longest_sequence = 0
    
#     for num in nums:
#         if num - 1 not in num_set:
#             current_num = num
#             current_sequence = 1
            
#             while current_num + 1 in num_set:
#                 current_num += 1
#                 current_sequence += 1
            
#             longest_sequence = max(longest_sequence, current_sequence)
    
#     return longest_sequence

def longest_consecutive_sequence(nums):
  nums.sort()
  n = len(nums)
  count = 1
  if n == 1:
    return n
  longest_consecutive_sequence = 0
  for num in nums:
    complement = num +1 
    if complement not in nums:
      count = 1
    else:
      count += 1

    longest_consecutive_sequence = max(count, longest_consecutive_sequence)
  return longest_consecutive_sequence

print( longest_consecutive_sequence([100 ,99, 4, 200, 1, 3, 2, 6,7,8]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""