def is_prime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True


# print(is_prime(7))
print(is_prime(30))
print(is_prime(13))
print(is_prime(2))