import heapq
# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).

def k_closest_point(points, k):
    res = []
    minHeap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])
    
    heapq.heapify(minHeap)

    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1

    return res 

print(k_closest_point([[3,3],[5,-1],[-2,4]], 2))