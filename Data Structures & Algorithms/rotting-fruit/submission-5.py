class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while fresh > 0:
            new_rotted = False

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            new_row, new_col = r+dr, c+dc 
                            if (new_row in range(ROWS)
                                and new_col in range(COLS)
                                and grid[new_row][new_col] == 1):
                                
                                new_rotted = True
                                grid[new_row][new_col] = 3
                                fresh -= 1
            
            if not new_rotted:
                return -1
            
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1
        
        return -1 if fresh else time

