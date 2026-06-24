class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == "0"):

                return
            
            grid[r][c] = "0"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: # down, up, right, left
                dfs(r+dr, c+dc)
        
        islands_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands_count += 1
        
        return islands_count

        
