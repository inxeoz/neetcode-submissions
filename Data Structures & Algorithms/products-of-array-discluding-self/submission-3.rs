impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {

        let n = nums.len();

        let mut res: Vec<i32> = vec![1; n];

        let mut p = 1;

        for i in 0..n {
            res[i] = p;

            p *= nums[i];
        }

        let mut s = 1;

        for i in (0..n).rev() {
            res[i] *= s;
            s *= nums[i];
        }

        res
    

    }
}