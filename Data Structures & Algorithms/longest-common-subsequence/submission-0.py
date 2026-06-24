class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)

        grid = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for i in range(ROWS-1, -1, -1):
            for j in range(COLS-1, -1, -1):
                # if chars are the same add one to whatever is diagonally to the bottom-right
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                    continue
                
                grid[i][j] += max(grid[i+1][j], grid[i][j+1]) 

        return grid[0][0]