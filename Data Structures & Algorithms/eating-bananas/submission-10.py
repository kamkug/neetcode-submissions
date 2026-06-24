class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        left, right = 1, max(piles)

        while left < right:
            rate = (left+right) // 2

            if sum([abs(-p // rate) for p in piles]) > h:
                left = rate+1
            else:
                right = rate
        
        return left