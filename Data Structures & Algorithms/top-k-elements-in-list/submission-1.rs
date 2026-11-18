impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {

    
        use std::collections::HashMap;

       let mut map: HashMap<i32, u32> = HashMap::new();


       for n in &nums {
        *map.entry(*n).or_insert(0) += 1;
       }

       let mut map_vec : Vec<(i32, u32)> = map.into_iter().collect();

       map_vec.sort_by(|a, b| b.1.cmp(&a.1));

       map_vec.iter().take(k as usize).map(|&(num, _) |  num ).collect()


        
    }
}
