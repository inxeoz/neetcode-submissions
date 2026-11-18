impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mset : HashSet<i32> = nums.iter().copied().collect();

        return  nums.len() != mset.len() 

    }
}
