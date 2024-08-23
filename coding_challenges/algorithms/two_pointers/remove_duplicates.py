def remove_duplicates(nums):
    unique = set()
    L = 0
    while L < len(nums):
        if nums[L] in unique:
            nums.pop(L)
        else:
            unique.add(nums[L])
            L +=1
    return nums 

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))

def removeDuplicates(nums):
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        return L

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
     
def remove_dups_two(nums):
    k = 2
    L = 0
    R = L + k

    while L < R and R < len(nums):
        if nums[L] != nums[R]:
            L += 1
            R += 1
        else:
            while R < len(nums) and nums[L] == nums[R]:
                    nums.pop(L)
                        
    return nums 
        

print(remove_dups_two([0,0,1,1,1,1,2,3,3,3,3,3]))


def __remove_dups_two(nums):
    l = 0
    r = 0

    while r < len(nums):
        count = 1
        while r + 1 < len(nums) and nums[r] == nums[r+1]:
            r+= 1
            count +=1

        for _ in range(min(2, count)):
            nums[l] = nums[r]
            l +=1
        r +=1
    return l 

print(__remove_dups_two([0,0,1,1,1,1,2,3,3,3,3,3]))
