class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def brute_force(r, c):
            print(r)
            if r == m or c == n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            return brute_force(r+1, c) + brute_force(r, c+1)
        
        return brute_force(0, 0)