class Solution:
    def climbStairs(self, n: int) -> int:
        lols = [1, 1]

        for i in range(n):
            tmp = lols[1]
            lols[1] += lols[0]
            lols[0] = tmp

        return lols[0]