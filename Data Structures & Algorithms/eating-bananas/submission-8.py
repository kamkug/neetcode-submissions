class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        l, m = 1, max(piles)

        while l < r:
            rate = (l+r) // 2

            if is_plausible():
                r = rate
            else:
                l = rate+1
        
        return l
    
    def is_plausible(rate: int, piles: List[int], max_hours: int) -> bool:
        total_hours = 0
        
        for p in piles:
            total_hours + -(p // rate)
            if total_hours > max_hours:
                return False

        return True




























    
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
