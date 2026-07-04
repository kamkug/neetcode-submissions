impl Solution {
    pub fn shortest_path_binary_matrix(mut grid: Vec<Vec<i32>>) -> i32 {
        if grid.len() == 0 || grid[0].len() == 0 {
            return -1
        }

        let R = grid.len()-1;
        let C = grid[0].len()-1;


        if grid[0][0] != 0 || grid[R][C] != 0 {
            return -1
        }

        let dirs = [(0, 0), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]; 

        let mut q: VecDeque<(i32,i32)> = VecDeque::new();
        q.push_back((0, 0));
        let mut pathlen = 1;
        grid[0][0] = 1;

        while q.len() > 0 {
            let q_len = q.len();

            for _ in 0..q_len {
                if let Some(t) = q.pop_front() {
                    let r = t.0;
                    let c = t.1;
                    if r == R as i32 && c == C as i32 {
                        return pathlen
                    }

                    for d in dirs {
                        let nr: i32 = r as i32 + d.0;
                        let nc: i32 = c as i32 + d.1;

                        if nr >= 0 && nr <= R as i32 && nc >= 0 && nc <= C as i32 && grid[nr as usize][nc as usize] == 0 {
                            grid[nr as usize][nc as usize] = 1;
                            q.push_back((nr, nc))
                        }
                    }
                }
            }
            pathlen += 1;
        }

        return -1
    }
}
