# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
# The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. 
# Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, 
# she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating 
# all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.
import math

def min_eating_speed(piles, h):
    total = sum(piles)
    L = 1
    R = max(piles)
    min_speed = total
    while L <= R:
        mid = (L + R) // 2
        eaten = mid * h
        if eaten >= total:
            if eaten == total:
                return mid
            else:
                min_speed = min(mid, min_speed)
                R = mid - 1
        elif eaten < total:
            L = mid + 1
    return min_speed 


print(min_eating_speed([3,6,7,11], 8))

print(min_eating_speed([30,11,23,4,20], 5))

print(min_eating_speed([30,11,23,4,20], 6))

def __min_eating_speed(piles, h):
    L = 1
    R = max(piles)
    min_speed = R

    while L <= R:
       k = (L+R)//2
       hours = 0
       for p in piles:
           hours += math.ceil(p/k)

       if hours <= h:
           min_speed = min(min_speed, k)
           R = k - 1
       else:
           L = k + 1

    return min_speed

print(__min_eating_speed([3,6,7,11], 8))

print(__min_eating_speed([30,11,23,4,20], 5))

print(__min_eating_speed([30,11,23,4,20], 6))
