class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # it helps that this is a square
        N = len(grid)
        # check if clear path is achievable
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        q = deque([(0, 0)])
        grid[0][0] = 1
        length = 0
        
        while q:
            # working it layer by layer hence we can increment the length safely
            length += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                # we have reached the bottom-right corner/found clear path
                if r == N-1 and c == N-1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
        
        return -1