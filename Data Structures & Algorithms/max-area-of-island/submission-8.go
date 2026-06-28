type Coords struct {
    row, col int
}

func maxAreaOfIsland(grid [][]int) int {
    if len(grid) == 0 || len(grid[0]) == 0 {
        return 0
    }
    ROWS := len(grid)
    COLS := len(grid[0])

    directions := []Coords{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
    var maxLen int
    
    for r := 0; r < ROWS; r++ {
        for c := 0; c < COLS; c++ {
            if grid[r][c] == 1 {
                counter := 1
                stack := []Coords{{r, c}}
                grid[r][c] = 0

                for len(stack) > 0 {
                    coord := stack[len(stack)-1]
                    stack = stack[:len(stack)-1]
                    for _, direction := range directions {
                        nr := coord.row+direction.row
                        nc := coord.col+direction.col
                        if nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS && grid[nr][nc] == 1 {
                            grid[nr][nc] = 0
                            counter += 1
                            stack = append(stack, Coords{nr, nc})
                        }
                    }
                    maxLen = max(maxLen, counter)
                }
            }
        }
    }

    return maxLen
}
