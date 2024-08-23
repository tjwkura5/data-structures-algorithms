def sum_two(arr, target):
    for num in arr:
        diff = target - num
        if diff in set(arr):
            return [num, diff]
    return []

print(sum_two([1,2,3,4,5], 4))