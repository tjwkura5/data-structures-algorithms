pick = 6 
def guess_number(n):
    L = 1
    R = n

    while L <= R:
        mid = (L+R)//2

        if is_correct(mid) > 0:
            R = mid - 1
        elif is_correct(mid) < 0:
            L = mid + 1
        else:
            return mid
    return -1

def is_correct(mid):
    if mid > pick:
        return 1 
    elif mid < pick:
        return -1
    else:
        return 0

print(guess_number(10))

# You are a product manager and currently leading a team to develop a new product. 
# Unfortunately, the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.


def firstBadVersion(n):
    L = 1
    R = n
    while L <= R:
        mid = (L + R)//2

        if is_bad(mid) == "too big":
            R = mid - 1
        elif is_bad(mid) == "too small":
            L = mid + 1
        else:
            return mid 

bad = 4
def is_bad(mid):
    if mid > bad:
        return "too big"
    elif mid < bad:
        return "too small"
    else:
        return 0 
    
print(firstBadVersion(5))