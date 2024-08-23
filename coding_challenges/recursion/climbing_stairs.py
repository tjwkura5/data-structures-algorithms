def climbing_stairs(n):
    one, two = 1, 1
    for _ in range(n - 1):
        temp = one
        one = one + two
        two = temp 

    return one 

print(climbing_stairs(5))