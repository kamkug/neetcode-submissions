class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '0':
                    continue
                dfs(row, col)
                result += 1

        
        return result

