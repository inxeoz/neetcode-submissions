use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let num_set: HashSet<i32> = nums.into_iter().collect();
        let mut longest = 0;

        for &num in &num_set {
            // Only start counting if 'num' is the beginning of a sequence
            if !num_set.contains(&(num - 1)) {
                let mut current_num = num;
                let mut current_streak = 1;

                while num_set.contains(&(current_num + 1)) {
                    current_num += 1;
                    current_streak += 1;
                }

                if current_num - num + 1   > longest {
                    longest = current_streak;
                }
            }
        }

        longest
    }
}
