
impl Solution {
    pub fn encode(strs: Vec<String>) -> String {

        let mut result = String::new();


        for s in strs {

            let u8s : String = s.bytes().map(|b| b.to_string()).collect::<Vec<String>>().join(";");

            result += "#";
            result += &u8s;
        }

        return result;


    }
pub fn decode(s: String) -> Vec<String> {
    if s.is_empty() {
        return Vec::new();
    }

    let parts: Vec<&str> = s.split('#').collect();
    let mut list = Vec::with_capacity(parts.len() - 1);

    // Skip the first empty part (before the leading '#')
    for part in parts.into_iter().skip(1) {
        if part.is_empty() {
            // empty string
            list.push(String::new());
        } else {
            let bytes: Vec<u8> = part
                .split(';')
                .map(|b| b.parse::<u8>().unwrap())
                .collect();
            list.push(String::from_utf8(bytes).unwrap());
        }
    }

    list
}
}




