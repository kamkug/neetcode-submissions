class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()                      
        q.append((0, 0))       # [(0, 2) new ->]
        visited.add((0, 0))    # [(0, 0), (0, 1), (0, 2), (1, 1), (0, 3),
                               #  (2, 2), (1, 3), (3, 2), (1, 2), (3, 3), (0, 2)]

        path_length = 0        # 6
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return path_length
                
                neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in neighbors:
                    if (min(r+dr, c+dc) < 0 or
                        r+dr == ROWS or c+dc == COLS or
                        (r+dr, c+dc) in visited or
                        grid[r+dr][c+dc] == 1):

                        continue
                    
                    q.append((r+dr, c+dc))           
                    visited.add((r+dr, c+dc))
            path_length += 1
        
        return -1
                



