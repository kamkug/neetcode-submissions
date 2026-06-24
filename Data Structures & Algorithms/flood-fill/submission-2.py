class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return
        
        ROWS, COLS = len(image), len(image[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        init_color = image[sr][sc]
        stack = [(sr, sc)]
        visited = set()

        while stack:
            r, c = stack.pop()
            image[r][c] = color

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != init_color or (nr, nc) in visited:
                    continue
                
                stack.append((nr, nc))
                visited.add((nr, nc))
        
        return image
            
            