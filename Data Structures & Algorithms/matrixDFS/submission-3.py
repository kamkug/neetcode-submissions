class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(r, c):
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 1):
                
                return 0
            
            if r == ROWS-1 and c == COLS-1:
                return 1
            
            visited.add((r, c))
            count = sum(dfs(r+dr, c+dc) for dr, dc in directions)
            visited.remove((r, c))

            return count
        
        return dfs(0, 0)