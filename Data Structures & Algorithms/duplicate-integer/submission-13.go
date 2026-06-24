func hasDuplicate(nums []int) bool {
    s := make(map[int]struct{})

    for _, n := range nums {
        if _, ok := s[n]; ok {
            return true
        }
        s[n] = struct{}{}
    }

    return false
}
