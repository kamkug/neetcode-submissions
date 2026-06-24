class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        paths = [[0] * (COLS+1) for _ in range(ROWS)]
        
        for i in range(COLS-1, -1, -1):
            if grid[-1][i] == 1:
                break
            
            paths[-1][i] = 1
        

        for r in range(ROWS-2, -1, -1):
            for c in range(COLS-1, -1, -1):
                # if obstacle just leave it as zero so it won't affect computation
                if grid[r][c] == 1:
                    continue
                paths[r][c] += paths[r+1][c] + paths[r][c+1]
        
        return paths[0][0]
