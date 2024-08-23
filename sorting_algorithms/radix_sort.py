# get number of digits of the largest item in https://www.youtube.com/watch?v=BVGRgTALQ44
from functools import reduce
def __flatten(A):
    return reduce(lambda x,y: x + y, A)

def __get_num_digits(A):
    mx = 0
    for item in A:
        mx = max(mx, item)
    return len(str(mx))

def radix_sort(my_list):
    for digit in range(0, __get_num_digits(my_list)):
        B = [[] for i in range(10)]
        for item in my_list:
            num = item // 10 ** (digit) % 10
            print(digit, item, num)
            B[num].append(item)
        my_list = __flatten(B)
    return my_list

print(radix_sort([55, 45, 3, 289, 213, 1, 288, 53, 2]))

