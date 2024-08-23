# Given an array a, your task is to output an array b of the same length by applying the following transformation: 
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

def get_index(my_list, index):
    if index > len(my_list) - 1 or index < 0:
        return 0 
    return my_list[index]

def array_manipulation(my_list):
    new_list = []

    for i in range(len(my_list)):
        value = get_index(my_list, i-1) + my_list[i] + get_index(my_list, i+1)
        new_list.append(value)
    return new_list


print(array_manipulation([4, 0, 1, -2, 3]))

# solution(a) = [4, 5, -1, 2, 1]