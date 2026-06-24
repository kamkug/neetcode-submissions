class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        
        left, right = 1, max(piles)

        while left < right:
            pace = (left+right) // 2

            # if sum([-(-p // pace) for p in piles]) > h:
            if not self.good_pace(h, pace, piles):
                left = pace+1
            else:
                right = pace
        
        return left
    
    def good_pace(self, h, pace, piles):
        hours = 0
        for p in piles:
            hours += -(-p // pace)
            if hours > h:
                return False
        return True