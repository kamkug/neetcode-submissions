class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return
        ROWS, COLS = len(image), len(image[0])
        og_color = image[sr][sc]
        image[sr][sc] = color
        visited = set()

        def dfs(r, c):
            nonlocal ROWS, COLS, color, image, og_color
            if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visited or image[r][c] != og_color:
                return
            
            image[r][c] = color
            visited.add((r,c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r+dr, c+dc)
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(sr+dr, sc+dc)

        return image
