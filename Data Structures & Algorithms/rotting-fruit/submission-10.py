class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while fresh > 0:
            new_rotten = False
    
            for r in range(ROWS):
                for c in range(COLS):
                    # only process fruid around rotten fruits
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            new_row, new_col = r + dr, c + dc
                            if (0 <= new_row < ROWS and
                                0 <= new_col < COLS and
                                grid[new_row][new_col] == 1):
                                # mark as rotten
                                grid[new_row][new_col] = 3
                                fresh -= 1
                                new_rotten = True
                
            if not new_rotten:
                return -1
            
            # mark fresh expected to rot into the rot state
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2
                
            time += 1

        
        # can return the time as if we got here the freash was 0 else we have already returned -1
        return time