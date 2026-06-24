class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c, visited):
            nonlocal ROWS, COLS

            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 1:
                return 0

            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            visited.add((r, c))

            count = 0
            count += dfs(grid, r+1, c, visited) # down
            count += dfs(grid, r-1, c, visited) # up
            count += dfs(grid, r, c+1, visited) # right
            count += dfs(grid, r, c-1, visited) # left

            visited.remove((r, c))

            return count

        return dfs(grid, 0, 0, set())
        