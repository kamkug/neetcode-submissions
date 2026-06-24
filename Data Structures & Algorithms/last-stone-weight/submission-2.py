class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            one, two = -heapq.heappop(heap), -heapq.heappop(heap)
            smashed = one-two
            if one-two > 0:
                heapq.heappush(heap, -smashed)

        return 0 if not heap else -heapq.heappop(heap)


            