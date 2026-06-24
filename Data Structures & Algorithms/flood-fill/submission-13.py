class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if not image:
        #     return

        init_color = image[sr][sc]
        if color == init_color:
            return image
        
        ROWS, COLS = len(image), len(image[0])
        image[sr][sc] = color
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if min(nr, nc) < 0 or nr == ROWS or nc == COLS or image[nr][nc] != init_color:
                    continue
                
                image[nr][nc] = color

                stack.append((nr, nc))
        
        return image
            
            