class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first_bigger_value = heapq.heappop(max_heap)
            second_bigger_value = heapq.heappop(max_heap)
            new_stone = first_bigger_value - second_bigger_value
            if new_stone:
                heapq.heappush(max_heap, new_stone)
        return abs(max_heap[0]) if max_heap else 0