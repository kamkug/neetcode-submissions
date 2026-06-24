class Solution:
    def climbStairs(self, n: int) -> int:
        def memoization(n, cache):     
            if n <= 1:
                return 1
            
            if n in cache:
                return cache[n]
            
            cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
            return cache[n]
        
        return memoization(n, {})