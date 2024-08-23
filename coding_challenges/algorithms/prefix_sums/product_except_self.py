import math
def get_prefix(nums):
    prefix = []
    for i in range(len(nums)):
        product = math.prod(nums[:i]) if i > 0 else 1
        prefix.append(product)
    return prefix

def product_except_self(nums):
    output = len(nums) * [0]
    for i in range(len(nums) -1, -1, -1):
        prefix = math.prod(nums[:i]) if i > 0 else 1
        postfix = math.prod(nums[i+1:]) if i < len(nums) - 1 else 1
        output[i] = prefix * postfix
    return output

def __product_except_self(nums):
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

print(__product_except_self([1,2,3,4]))

print(product_except_self([1,2,3,4]))

print(product_except_self([-1,1,0,-3,3]))
