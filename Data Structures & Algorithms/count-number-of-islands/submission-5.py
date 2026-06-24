class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            for dr, dc in directions:
                dfs(r+dr, c+dc)
            
        return len(list(dfs(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == '1'))
