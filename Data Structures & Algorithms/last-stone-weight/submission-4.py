class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            one, two = -heapq.heappop(stones), -heapq.heappop(stones)
            if smashed := one-two:
                heapq.heappush(stones, -smashed)

        return 0 if not stones else -heapq.heappop(stones)


            