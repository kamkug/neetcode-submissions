use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut s = HashSet::new();

        for n in nums {
            if s.contains(&n) {
                return true
            }
            s.insert(n);
        }
        false
    }
}
