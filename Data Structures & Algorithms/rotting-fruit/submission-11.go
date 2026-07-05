type Coord struct {
    row, col int
}

func orangesRotting(grid [][]int) int {
    if len(grid) == 0 && len(grid[0]) == 0 {
        return -1
    }

    R, C := len(grid)-1, len(grid[0])-1
    dirs := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

    var fruit, minutes int

    q := make([][2]int, 0, (R+1)*(C+1))

    for r := range grid {
        for c := range grid[r] {
            if grid[r][c] == 1 {
                fruit++
                continue
            }

            if grid[r][c] == 2 {
                q = append(q, [2]int{r, c})
            }
        }
    }

    for len(q) > 0 && fruit > 0 {
        q_len := len(q)
        for _ = range q_len {
            coord := q[0]
            r, c := coord[0], coord[1]
            q = q[1:]

            for _, d := range dirs {
                dr, dc := d[0], d[1]
                nr, nc := r+dr, c+dc

                if nr >= 0 && nr <= R && nc >= 0 && nc <= C && grid[nr][nc] == 1 {
                    grid[nr][nc] = 2 // mark as rotten
                    q = append(q, [2]int{nr, nc})
                    fruit--
                }
            }
        }
        minutes++
    }

    if fruit > 0 {
        return -1
    }

    return minutes
}
