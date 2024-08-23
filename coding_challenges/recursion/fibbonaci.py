def fibbonaci(num):
    fibb = [0,1]
    num1 = 0
    num2 = 1

    for _ in range(num - 2):
        sum = num1 + num2
        fibb.append(sum)
        num1 = num2
        num2 = sum 

    return fibb

# Recursive implementation to calculate the n-th Fibonacci number
def __fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    return __fibonacci(n - 1) + __fibonacci(n - 2)

print(__fibonacci(6))

print(fibbonaci(10))