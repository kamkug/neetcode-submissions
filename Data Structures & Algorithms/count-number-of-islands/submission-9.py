class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        NUMS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            for dr, dc in NUMS:
                dfs(r+dr, c+dc)

        islands_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands_count += 1
        
        return islands_count