class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      if not grid:
        return 0
      
      ROWS, COLS = len(grid), len(grid[0])
      NUMS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

      def dfs(r, c):
        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
            return 0

        grid[r][c] = 0

        # account for current cell
        counter = 1
        # account for every other cell
        for dr, dc in NUMS:
            nr, nc = r+dr, c+dc
            counter += dfs(nr, nc)

        return counter

      max_area = 0
      for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
      
      return max_area
