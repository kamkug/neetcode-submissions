class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []
        
        ROWS, COLS = len(image), len(image[0])
        init_color = image[sr][sc]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def dfs(r, c):
            nonlocal init_color, ROWS, COLS

            if (min(r, c) < 0 or 
                r == ROWS or c == COLS or 
                image[r][c] != init_color or
                (r, c) in visited):

                return
            
            image[r][c] = color
            visited.add((r, c))
            
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        dfs(sr, sc)

        return image