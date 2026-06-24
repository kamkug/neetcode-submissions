class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS-1 and c == COLS-1:
                    return length
                
                coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d_row, d_col in coords:
                    if (min(r+d_row, c+d_col) < 0 or
                        r+d_row == ROWS or c+d_col == COLS or
                        (r+d_row, c+d_col) in visited or
                        grid[r+d_row][c+d_col] == 1):

                        continue
                    
                    queue.append((r+d_row, c+d_col))
                    visited.add((r+d_row, c+d_col))
            
            length += 1
        
        return -1