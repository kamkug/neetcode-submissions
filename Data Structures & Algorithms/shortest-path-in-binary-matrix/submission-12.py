class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        R, C = len(grid) - 1, len(grid[0]) - 1

        if grid[0][0] != 0 or grid[R][C] != 0:
            return -1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]

        q = deque([(0, 0)])
        grid[0][0] = 1
        pathlen = 1

        while q:
            q_len = len(q)
            for _ in range(q_len):
                r, c = q.popleft()

                if r == R and c == C:
                    return pathlen

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr <= R and 0 <= nc <= C and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

            pathlen += 1

        return -1
