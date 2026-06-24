class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROWS, COLS = len(word1), len(word2)

        if ROWS == 0:
            return COLS
        
        if COLS == 0:
            return ROWS
        
        curr_row = [0 for _ in range(COLS+1)]
        prev_row = [0 for _ in range(COLS+1)]
        for c in range(COLS):
            prev_row[c] = COLS-c

        for r in range(ROWS-1, -1, -1):
            
            curr_row[-1] = ROWS-r

            for c in range(COLS-1, -1, -1):
                if word1[r] == word2[c]:
                    curr_row[c] = prev_row[c+1]
                    continue
                
                curr_row[c] = 1 + min(
                    prev_row[c+1],
                    prev_row[c],
                    curr_row[c+1]
                )
            prev_row, curr_row = curr_row, prev_row

        return prev_row[0]