from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        for i in range(n):
            tmp = two
            two = one + two
            one = tmp
        return two