class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 1:
                return 0

            if r == ROWS-1 and c == COLS-1:
                return 1
            
            visited.add((r, c))

            count = 0
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            visited.remove((r, c))

            return count
        
        return dfs(0, 0)
