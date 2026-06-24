class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for i in range(1, max(piles)+1):
            if sum(abs(-p // i) for p in piles) > h:
                continue
            
            return i
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            eating_rate = (left+right) // 2

            if sum(abs(-p // eating_rate) for p in piles) <= h:
                right = eating_rate
            else:
                left = eating_rate+1
        
        return left
