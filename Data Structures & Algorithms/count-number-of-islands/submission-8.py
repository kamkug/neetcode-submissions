class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = 0

        def dfs(row, col):
            grid[row][col] = '0'
            stack = [(row, col)]

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    if 0 <= r+dr < ROWS and 0 <= c+dc < COLS and grid[r+dr][c+dc] == '1':
                        grid[r+dr][c+dc] = '0'
                        stack.append((r+dr, c+dc))
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '0':
                    continue
                dfs(row, col)
                result += 1

        
        return result

