def product_except_self(nums):
    res = [1] * (len(nums))

    prefix = 1
    postfix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]
    print(res)
    for i in range(len(nums) -1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

print(product_except_self([1,2,3,4]))