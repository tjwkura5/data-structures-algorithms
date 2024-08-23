def num_subs(nums, k, threshold):
    count = 0
    window = []
    for i in range(len(nums)):
        window.append(nums[i])
        if len(window) == k:
            if sum(window)/ k >= threshold:
                count += 1
            window.pop(0)
        

    return count 
print(num_subs([11,13,17,23,29,31,7,5,2,3], 3, 5))


def __num_subs(nums, K, threshold):
    count = 0
    curSum = sum(nums[:K-1])
    for L in range(len(nums) - K + 1): 
        curSum +=nums[L+K - 1]
        if (curSum/ K) >= threshold:
            count += 1
        curSum -= nums[L]
    return count

print(__num_subs([2,2,2,2,5,5,5,8], 3, 4))
