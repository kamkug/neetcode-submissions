class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c):
            nonlocal ROWS, COLS

            if (min(r, c) < 0 or 
                r == ROWS or c == COLS
                or grid[r][c] == "0"):

                return

            grid[r][c] = "0"
            
            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(grid, row, col)
                    count += 1
        
        return count
        
            