def search(nums, target):
    L = 0
    R = len(nums) -1
    while L <= R:
        M = (L + R)//2 
        if target > nums[M]:
            L = M + 1
        elif target < nums[M]:
            R = M - 1
        else:
            return M
    return -1 


print(search([-1,0,3,5,9,12], 9))

print(search([-1,0,3,5,9,12], 2))

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

def search_matrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top = 0
    bot = ROWS - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break 
    if not (top <= bot):
        return False
    
    row = (top+bot)// 2
    l = 0
    r = COLS - 1
    while l <= r:
        mid = (l+r)// 2
        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid -1 
        else:
            return True
    return False


print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))