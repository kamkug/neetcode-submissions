class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
            
        prev_row = [0] * n

        for r in range(m-1, -1, -1):
            new_row = [0] * n
            new_row[n-1] = 1
            prev_row[n-1] = 1

            for c in range(n-2, -1, -1):
                new_row[c] = new_row[c+1] + prev_row[c]
            prev_row = new_row
        
        return prev_row[0]