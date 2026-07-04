type Coord struct {
    row, col int
}

func shortestPathBinaryMatrix(grid [][]int) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
        return -1
    }

    R, C := len(grid)-1, len(grid[0])-1

    if grid[0][0] != 0 || grid[R][C] != 0 {
        return -1
    }

    dirs := []Coord {
        {1, 0}, {-1, 0}, 
        {0, 1}, {0, -1},
        {1, 1}, {1, -1},
        {-1, 1}, {-1, -1},
    }

    q := make([]Coord, 0, (R+1)*(C+1))
    q = append(q, Coord{0, 0})
    grid[0][0] = 1
    pathLen := 1
    head := 0

    for head < len(q) {
        levelSize := len(q) - head
        for i := 0; i < levelSize; i++ {
            coord := q[head]
            head++

            if coord.row == R && coord.col == C {
                return pathLen
            }

            for _, diff := range dirs {
                nr, nc := coord.row+diff.row, coord.col+diff.col

                if nr >= 0 && nr <= R && nc >= 0 && nc <= C && grid[nr][nc] == 0 {
                    grid[nr][nc] = 1
                    q = append(q, Coord{nr, nc})
                }
            }
        }
        pathLen++
    }
    return -1
}
