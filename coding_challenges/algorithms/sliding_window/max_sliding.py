from collections import deque
def max_sliding_window(nums, k):
    R = k
    max_w = []
    for L in range(len(nums)):
        if len(nums[L:R]) == k:
            max_w.append(max(nums[L:R]))
        R += 1
    return max_w

# print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))


def __max_sliding_window(nums, k):
    output = []
    q = deque()  # index
    l = r = 0
    # O(n) O(n)
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output

print(__max_sliding_window([1,3,-1,-3,5,3,6,7], 3))