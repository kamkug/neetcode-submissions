class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # it helps that this is a square
        N = len(grid)
        # check if clear path is achievable
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        if N == 1:
            return 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        q1 = deque([(0, 0)])
        q2 = deque([(N-1, N-1)])
        start, end = -1, -2
        grid[0][0] = -1 
        grid[N-1][N-1] = -2
        length = 2
        
        while q1:
            # working it layer by layer hence we can increment the length safely
            for _ in range(len(q1)):
                r, c = q1.popleft()
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == end:
                            return length
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            q1.append((nr, nc))
            q1, q2 = q2, q1
            start, end = end, start
            length += 1
        return -1