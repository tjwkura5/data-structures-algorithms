def turbulent_subs(nums):
    count = 1
    prev = ""
    res = 1
    if len(nums) == 1:
        return res
    for R in range(1, len(nums)):
        if nums[R-1] > nums[R]:
            if prev != ">":
                count += 1
            else:
                count = 1
            prev = ">"
        elif nums[R-1] < nums[R]:
            if prev != "<":
                count += 1
            else:
                count = 1
            prev = "<"
        else:
            prev = prev
            count = 1
        res = max(count, res)
    return res + 1
        

print(turbulent_subs([9,9])) 