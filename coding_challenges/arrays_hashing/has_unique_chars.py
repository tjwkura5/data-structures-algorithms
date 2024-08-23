def has_unique_chars(string):
    # convert the string into a list
    lst = list(string)
    # convert that list into a set
    set_word = set(lst)
    if len(lst) == len(set_word):
        return True
    return False




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""