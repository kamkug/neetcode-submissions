class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return 0
        
        speed = 1

        for i in range(1, max(piles)+1):
            total_time = 0
            for p in piles:
                total_time += abs(-p // i)
               
                if total_time > h:
                    break
            else:
                return i
        
        return speed

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(speed):
            return sum(abs(-p // speed) for p in piles) <= h
        
        l, r = 1, max(piles)
        while l < r:
            speed = (l+r) // 2
            
            if can_eat(speed):
                r = speed
            else:
                l = speed+1

        return l
