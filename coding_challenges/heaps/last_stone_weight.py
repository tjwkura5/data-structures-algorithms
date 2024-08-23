import heapq
def last_stone(nums):
    stones = [-s for s in nums]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if abs(second) < abs(first):
            value = abs(first) - abs(second)
            heapq.heappush(stones, -value)
    return abs(stones[0])

print(last_stone([2,7,4,1,8,1]))