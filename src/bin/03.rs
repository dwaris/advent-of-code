advent_of_code::solution!(3);

pub fn part_one(input: &str) -> Option<u32> {
    let re = regex::Regex::new(r"mul\((\d\d?\d?),(\d\d?\d?)\)").expect("Invalid regex");

    let mut output = 0;
    for x in re.captures_iter(input) {
        let a = x[1].parse::<u32>().unwrap();
        let b = x[2].parse::<u32>().unwrap();
        output += a * b;
    };

    Some(output)
}

pub fn part_two(input: &str) -> Option<u32> {
    let re = regex::Regex::new(r"mul\((\d\d?\d?),(\d\d?\d?)\)|do\(\)|don't\(\)").expect("Invalid regex");

    let mut output: u32 = 0;
    let mut enabled = true;
    for check in re.captures_iter(input) {
        if check[0].eq("do()") {
            enabled = true;
        } else if check[0].eq("don't()") {
            enabled = false;
        } else if enabled {
            let a = check[1].parse::<u32>().unwrap();
            let b = check[2].parse::<u32>().unwrap();
            output += a * b;
        }
    };
    Some(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(161));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(48));
    }
}
