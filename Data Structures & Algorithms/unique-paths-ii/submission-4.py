class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if not ROWS or grid[ROWS-1][COLS-1] == 1:
            return 0

        prev = [0] * (COLS+1)

        for i in range(COLS-1, -1, -1):
            if grid[-1][i] == 1:
                break

            prev[i] = 1


        for r in range(ROWS-2, -1, -1):
            curr = [0] * (COLS+1)
            for c in range(COLS-1, -1, -1):
                # if obstacle just leave it as zero so it won't affect computation
                if grid[r][c] == 1:
                    continue
                curr[c] = curr[c+1] + prev[c]
            prev = curr

        return prev[0]
