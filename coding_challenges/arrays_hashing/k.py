def morethanNbyK(arr, n, k):
    more_than = []
    occurences = n/k
    num_counts_map = {}
    for num in arr:
        num_counts_map[num] = num_counts_map.get(num, 0) + 1

    for key, value in num_counts_map.items():
        if value > occurences:
            more_than.append(key)

    return more_than

arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
n = len(arr)
k = 4

print(morethanNbyK(arr, n, k))