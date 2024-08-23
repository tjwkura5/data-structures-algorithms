def trap(heights):
    water = len(heights) * [0]

    if not heights: return 0
    l, r = 0, len(heights) - 1

    leftMax, rightMax = heights[l], heights[r]
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, heights[l])
            water[l] = leftMax - heights[l]
        else:
            r -=1
            rightMax = max(rightMax, heights[r])
            water[r] = rightMax - heights[r]


    return water

print(trap([4,2,0,3,2,5]))