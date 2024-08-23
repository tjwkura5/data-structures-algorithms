def find_pairs(arr1, arr2, target):
    pairs_list = []
    for num in arr1:
        diff = target - num
        if diff in set(arr2):
             pairs_list.append((num, diff))
    
    return pairs_list



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""