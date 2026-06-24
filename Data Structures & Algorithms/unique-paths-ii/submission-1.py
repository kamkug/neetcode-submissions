class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[ROWS-1][COLS-1] == 1:
            return 0

        def dfs(r, c, cache):
            if r == ROWS or c == COLS or grid[r][c] == 1:
                return 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            if cache[r][c] > 0:
                return cache[r][c]
            
            cache[r][c] = dfs(r+1, c, cache) + dfs(r, c+1, cache)
            return cache[r][c]
        
        return dfs(0, 0, [[0] * COLS for _ in range(ROWS)])
            







