func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sm, tm := make(map[rune]int, len(t)), make(map[rune]int, len(t))

    for _, v := range s {
        sV, ok := sm[v]
        if !ok {
            sm[v] = 1
            continue
        }
        sm[v] = sV+1
    }

    for _, v := range t {
        tV, ok := tm[v]
        if !ok {
            tm[v] = 1
            continue
        }
        tm[v] = tV+1
    }

    for k, v := range sm {
        if tmV, ok := tm[k]; !ok || tmV != v {
            return false
        }
    }

    return true
}
