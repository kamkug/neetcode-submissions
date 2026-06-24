class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        NUMS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = '0'

            while stack:
                row, col = stack.pop()

                for dr, dc in NUMS:
                    nr, nc = row+dr, col+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        stack.append((nr, nc))
    
        islands_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands_count += 1
        
        return islands_count