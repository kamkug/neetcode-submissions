from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1
        queue = deque()
        visited = set()
        queue.append((0, 0, 1)) # (1, 1) new -> (1, 2), (-1, 1), 
        visited.add((0, 0))  # (0, 0), (1, 1), (1, 2)

        while queue:
            for _ in range(len(queue)):
                r, c, length = queue.popleft()


                if r == ROWS-1 and c == COLS-1:
                    return length

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1), (-1, 1), (1, 1)]:
                    if (min(r+dr, c+dc) < 0 or
                        r+dr == ROWS or c+dc == COLS or
                        (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == 1):

                        continue
                    
                    queue.append((r+dr, c+dc, length+1))
                    visited.add((r+dr, c+dc))

        return -1