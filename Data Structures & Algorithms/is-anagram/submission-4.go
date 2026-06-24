func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    m := make(map[byte]int)
    for i := range s {
        m[s[i]] += 1
    }
    for j := range t {
        m[t[j]] -= 1
        if m[t[j]] < 0 {
            return false
        }
    }
    return true
}
