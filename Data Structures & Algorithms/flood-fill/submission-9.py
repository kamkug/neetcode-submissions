class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        init_color = image[sr][sc]
        if color == init_color:
            return image
        
        q = deque([(sr, sc)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(image), len(image[0])

        while q:
            r, c = q.popleft()
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != init_color:
                    continue
                
                q.append((nr, nc))
        
        return image
