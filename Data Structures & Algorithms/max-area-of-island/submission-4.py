class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def dfs(row, col):
            area = 1
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        area += 1
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
            
            return area
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                grid[row][col] = 0
                max_area = max(max_area, dfs(row, col))
        
        return max_area
            