class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1

        for i in range(n):
            tmp = two
            two += one
            one = tmp
        
        return two
