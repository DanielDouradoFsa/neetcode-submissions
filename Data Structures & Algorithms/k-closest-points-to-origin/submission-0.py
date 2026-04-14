class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_distance_heap = []
        for x,y in points:
            distance = math.sqrt((x)**2 + (y)**2)
            min_distance_heap.append((distance,x,y))

        heapq.heapify(min_distance_heap)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(min_distance_heap)
            res.append([x,y])
            k-=1
        return res

        