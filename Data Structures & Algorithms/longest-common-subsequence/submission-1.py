class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)

        prev = [0] * (COLS+1)

        for i in range(ROWS-1, -1, -1):
            curr = [0] * (COLS+1)
            for j in range(COLS-1, -1, -1):
                # if chars are the same add one to whatever is diagonally to the bottom-right
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                    continue
                
                curr[j] += max(curr[j+1], prev[j])
            prev = curr

        return prev[0]