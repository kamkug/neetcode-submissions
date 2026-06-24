class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -(heapq.heappop(stones))
            second = -(heapq.heappop(stones))

            if new_stone := first - second:
                heapq.heappush(stones, -new_stone)
        
        return 0 if not stones else -stones[0]
