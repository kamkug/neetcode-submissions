class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)

        if ROWS == 0:
            return COLS
        
        if COLS == 0:
            return ROWS
        

        dp2 = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]

        for r in range(ROWS):
            dp2[r][COLS] = ROWS-r
        
        for c in range(COLS):
            dp2[ROWS][c] = COLS-c
        
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                if word1[r] == word2[c]:
                    dp2[r][c] = dp2[r+1][c+1]
                    continue
                
                dp2[r][c] = 1 + min(
                    dp2[r][c+1],
                    dp2[r+1][c],
                    dp2[r+1][c+1]
                )

        return dp2[0][0]