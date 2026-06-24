class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        left, right = 1, max(piles)

        while left < right:
            rate = (left+right) // 2

            if not self.is_valid_rate(rate, piles, h):
                left = rate+1
            else:
                right = rate
        
        return left
    
    def is_valid_rate(self, rate, piles, h):
        total = 0

        for p in piles:
            total += -(-p // rate)
            if total > h:
                return False
        
        return True
            