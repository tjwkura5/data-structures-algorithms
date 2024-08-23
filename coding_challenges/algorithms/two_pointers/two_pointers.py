# Q: Check if an array is a palindrome.

def is_palindrome(nums):
    L = 0
    R = len(nums) -1
    while L < R:
        if nums[L] != nums[R]:
            return False
        
        L += 1
        R -= 1
        
    return True

    
print(is_palindrome([1,2,7,7,2,1]))

#Q: Give a sorted input array, return the two indices which sum up to the target value.
#Assume theres exactly one solution.

def find_target(nums, target):
    L = 0
    R = len(nums) - 1
    while L < R:
        sum = nums[L] + nums[R]
        if sum > target:
            R -= 1
        elif sum < target:
            L += 1
        else:
            return [L, R]
    return None

print(find_target([-1,2,3,4,7,9], 7))
    
