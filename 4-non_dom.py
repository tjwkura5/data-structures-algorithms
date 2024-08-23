def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

    for k in range(n):
            print(k)

print_items(10)

# Drop non dominants
# n * n + n = n^2 + n
# O(n^2 + n) can be simplified to O(n^2) because we drop non dominants