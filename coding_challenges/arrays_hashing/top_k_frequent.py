def top_k_frequent(nums, k):
    num_map = {}
    freq = [[] for _ in range(len(nums) + 1)]
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1
    for num, count in num_map.items():
        freq[count].append(num)


    res = []
    freq = list(filter(None, freq))
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
print(top_k_frequent([1,1,1,2,3,100,100,100, 100], 2))