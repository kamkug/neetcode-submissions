class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(grid, r, c, visited):
            nonlocal ROWS, COLS

            if (min(r, c) < 0 or 
                r == ROWS or c == COLS
                or grid[r][c] == "0" 
                or (r, c) in visited):

                return

            grid[r][c] = "0"
            
            dfs(grid, r+1, c, visited)
            dfs(grid, r-1, c, visited)
            dfs(grid, r, c+1, visited)
            dfs(grid, r, c-1, visited)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    dfs(grid, row, col, visited)
                    count += 1
        
        return count
        
            