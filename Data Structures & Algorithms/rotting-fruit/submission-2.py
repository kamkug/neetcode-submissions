class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque((r, c) 
                   for r in range(len(grid)) 
                   for c in range(len(grid[r])) if grid[r][c] == 2)

        length = 0
        while q:
            increment = False
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in adj:
                    if (min(r+dr, c+dc) < 0 or
                        r+dr == ROWS or c+dc == COLS or
                        grid[r+dr][c+dc] in {0, 2}):
                        continue

                    if grid[r+dr][c+dc] == 1:
                        increment = True

                    grid[r+dr][c+dc] = 2
                    q.append((r+dr, c+dc))

            if increment:
                length += 1
        
        q = deque((r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 1)

        return length if not q else -1

        
        


                 

        
        return -1
