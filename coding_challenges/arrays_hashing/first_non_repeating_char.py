def first_non_repeating_char(string):
    my_dict = {}

    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1

    for char in string:
        if my_dict[char] == 1:
            return char

    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""