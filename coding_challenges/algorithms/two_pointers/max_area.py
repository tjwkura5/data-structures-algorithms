# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

def max_area(heights):

    L = 0
    R = len(heights) - 1
    max_area = 0

    while L < R:
        width = R - L
        height = min(heights[L], heights[R])
        max_area = max(max_area, width * height)

        if heights[L] < heights[R]:
            L += 1
        else:
            R -= 1


    return max_area

print(max_area([[1,8,6,2,5,4,8,3,7]]))