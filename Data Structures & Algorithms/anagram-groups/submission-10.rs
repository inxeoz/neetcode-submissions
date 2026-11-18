impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {


        use std::collections::HashMap;

        let mut map : HashMap<String, Vec<String>> = HashMap::new();

        for s in strs {

            let mut kc : Vec<char> = s.chars().collect();
            kc.sort();

            let k : String = kc.into_iter().collect();

            if let Some(vv) = map.get_mut(&k) {
                vv.push(s);
            }else{
                map.insert(k, vec![s]);
            }



        }

        let d : Vec<Vec<String>> = map.values().cloned().collect();

        return d
 
    }
}
