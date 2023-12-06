use nom::{
    bytes::complete::is_not,
    character::complete::{self, digit1, line_ending, space1},
    multi::separated_list1,
    sequence::separated_pair,
    IResult, Parser,
};
use nom_supreme::ParserExt;

advent_of_code::solution!(6);

fn nums(input: &str) -> IResult<&str, Vec<u32>> {
    is_not("0123456789")
        .precedes(separated_list1(space1, complete::u32))
        .parse(input)
}

fn parse_times(input: &str) -> IResult<&str, (Vec<u32>, Vec<u32>)> {
    separated_pair(nums, line_ending, nums).parse(input)
}

fn nums1(input: &str) -> IResult<&str, u64> {
    is_not("0123456789")
        .precedes(
            separated_list1(space1, digit1)
                .map(|list| list.join("").parse::<u64>().expect("a valid number")),
        )
        .parse(input)
}

fn parse_times1(input: &str) -> IResult<&str, (u64, u64)> {
    separated_pair(nums1, line_ending, nums1).parse(input)
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_, (times, distances)) = parse_times(input).expect("a valid parse");
    let result = times
        .into_iter()
        .zip(distances)
        .map(|(time, record_distance)| {
            (0..time)
                .filter_map(|speed| {
                    let my_distance = (time - speed) * speed;
                    (my_distance > record_distance).then_some(my_distance)
                })
                .count()
        })
        .product::<usize>();
    Some(result as u32)
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, (time, record_distance)) = parse_times1(input).expect("a valid parse");
    let result = (0..time)
        .filter_map(|speed| {
            let my_distance = (time - speed) * speed;
            (my_distance > record_distance).then_some(my_distance)
        })
        .count();
    Some(result as u64)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(288));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(71503));
    }
}
