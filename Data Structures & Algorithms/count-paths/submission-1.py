class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def brute_force(r, c, cache):
            if r == m or c == n:
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]

            if r == m-1 and c == n-1:
                return 1
            
            cache[r][c] = brute_force(r+1, c, cache) + brute_force(r, c+1, cache)
            return cache[r][c]
        
        return brute_force(0, 0, [[0] * n for _ in range(m)])