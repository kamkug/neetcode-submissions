func countStudents(students []int, sandwiches []int) int {
    m := make(map[int]int)
    m[0] = 0
    m[1] = 0

    for _, s := range students {
        v := m[s]
        v += 1
        m[s] = v
    }

    for _, s := range sandwiches {
        if v, ok := m[s]; ok && v == 0 {
            break
        }
        v := m[s]
        v -= 1
        m[s] = v
    }
    a := m[0]
    b := m[1]

    return a+b 
}