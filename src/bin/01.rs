use std::cmp;

advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u32> {
    let mut left = vec![];
    let mut right = vec![];
    let mut output = 0;

    for line in input.lines() {
        let mut numbers = line.split_whitespace().map(|x| x.parse::<u32>().unwrap());
        left.push(numbers.next().unwrap());
        right.push(numbers.next().unwrap());
    }

    left.sort();
    right.sort();

    for i in 0..left.len() {
        output += cmp::max(left[i], right[i]) - cmp::min(left[i], right[i]);
    }

    Some(output)
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut left = vec![];
    let mut right = vec![];
    let mut output = 0;

    for line in input.lines() {
        let mut numbers = line.split_whitespace().map(|x| x.parse::<u32>().unwrap());
        left.push(numbers.next().unwrap());
        right.push(numbers.next().unwrap());
    }

    for i in 0..left.len() {
        output += left[i] * right.iter().filter(|&&x| x == left[i]).count() as u32;
    }

    Some(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(11));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(31));
    }
}
