use std::collections::{BTreeMap, HashSet};

use nom::{
    bytes::complete::tag,
    character::complete::{self, digit1, line_ending, space0, space1},
    multi::{fold_many1, separated_list1},
    sequence::{delimited, separated_pair, terminated, tuple},
    IResult, Parser,
};

advent_of_code::solution!(4);

struct Card {
    winning_numbers: HashSet<u32>,
    my_numbers: HashSet<u32>,
}

impl Card {
    fn score(&self) -> u32 {
        let power = self.matches();
        match power.checked_sub(1) {
            Some(num) => 2u32.pow(num),
            None => 0,
        }
    }
    fn matches(&self) -> u32 {
        self.winning_numbers.intersection(&self.my_numbers).count() as u32
    }
}

fn set(input: &str) -> IResult<&str, HashSet<u32>> {
    fold_many1(
        terminated(complete::u32, space0),
        HashSet::new,
        |mut acc: HashSet<u32>, item| {
            acc.insert(item);
            acc
        },
    )(input)
}

fn card(input: &str) -> IResult<&str, Card> {
    let (input, _) = delimited(
        tuple((tag("Card"), space1)),
        digit1,
        tuple((tag(":"), space1)),
    )(input)?;
    separated_pair(set, tuple((tag("|"), space1)), set)
        .map(|(winning_numbers, my_numbers)| Card {
            winning_numbers,
            my_numbers,
        })
        .parse(input)
}
fn cards(input: &str) -> IResult<&str, Vec<Card>> {
    separated_list1(line_ending, card)(input)
}

pub fn part_one(input: &str) -> Option<u32> {
    let (_, card_data) = cards(&input).expect("a valid parse");
    Some(card_data.iter().map(|card| card.score()).sum::<u32>())
}

pub fn part_two(input: &str) -> Option<u32> {
    let (_, card_data) = cards(&input).expect("a valid parse");
    let data = card_data
        .iter()
        .map(|card| card.matches())
        .collect::<Vec<_>>();

    let store = (0..card_data.len())
        .map(|index| (index, 1))
        .collect::<BTreeMap<usize, u32>>();

    let result = data
        .iter()
        .enumerate()
        .fold(store, |mut acc, (index, card_score)| {
            let to_add = *acc.get(&index).unwrap();

            for i in (index + 1)..(index + 1 + *card_score as usize) {
                acc.entry(i).and_modify(|value| {
                    *value += to_add;
                });
            }
            acc
        })
        .values()
        .sum::<u32>();
    Some(result)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file_part(
            "examples", DAY, 1,
        ));
        assert_eq!(result, Some(13));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file_part(
            "examples", DAY, 2,
        ));
        assert_eq!(result, Some(30));
    }
}
