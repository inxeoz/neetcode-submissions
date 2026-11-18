impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        use std::collections::HashMap;

        if s.len() != t.len() {
            return false;
        }

        let mut map: HashMap<char , u32> = HashMap::new();

        for c1 in s.chars() {
            let count  = map.entry(c1).or_insert(0);
            *count += 1;
        }

        for c2 in t.chars() {

            if let Some(count) = map.get_mut(&c2) {

                if *count == 0 {
                    return false;
                }
                *count -= 1;

            }else{
                return false;
            }
        }

        return map.values().all(|&v| v == 0 );

        
         }
}
