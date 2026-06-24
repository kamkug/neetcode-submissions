class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            area_from_here = 1
            for dr, dc in directions:
                area_from_here += dfs(r+dr, c+dc)
            
            return area_from_here
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                max_area = max(max_area, dfs(row, col))
        
        return max_area
            