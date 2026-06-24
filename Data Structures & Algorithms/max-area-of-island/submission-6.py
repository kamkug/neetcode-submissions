class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      if not grid:
        return 0
      
      ROWS, COLS = len(grid), len(grid[0])
      NUMS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

      def dfs(r, c):
        stack = [(r, c)]
        grid[r][c] = 0
        counter = 1

        while stack:
            row, col = stack.pop()

            for dr, dc in NUMS:
                nr, nc = row+dr, col+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    counter += 1
                    stack.append((nr, nc))
        return counter

      max_area = 0
      for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
      
      return max_area
