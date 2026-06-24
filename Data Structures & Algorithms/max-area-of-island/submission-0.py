class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                grid[r][c] == 0):

                return 0
            
            grid[r][c] = 0

            area = 0
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return 1+area
        
        max_area = 0   # 6
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    curr_area = dfs(row, col)
                    max_area = max(max_area, curr_area)
        
        return max_area
