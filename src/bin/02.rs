use std::collections::BTreeMap;

use nom::{
    bytes::complete::tag,
    character::complete::{self, alpha1, digit1, line_ending},
    multi::separated_list1,
    sequence::{preceded, separated_pair},
    IResult,
};

advent_of_code::solution!(2);

#[derive(Debug)]
struct Cube<'a> {
    color: &'a str,
    amount: u32,
}

#[derive(Debug)]
struct Game<'a> {
    id: &'a str,
    rounds: Vec<Vec<Cube<'a>>>,
}

impl<'a> Game<'a> {
    fn valid_for_cube_set(&self, map: &BTreeMap<&str, u32>) -> Option<u32> {
        self.rounds
            .iter()
            .all(|round| {
                round.iter().all(|shown_cube| {
                    shown_cube.amount <= *map.get(shown_cube.color).expect("a valid cube")
                })
            })
            .then_some(
                self.id
                    .parse::<u32>()
                    .expect("game id should be a parseable u32"),
            )
    }

    fn minimum_cube_set(&self) -> u32 {
        let map = BTreeMap::from([("red", 0), ("green", 0), ("blue", 0)]);

        self.rounds
            .iter()
            .fold(map, |mut acc, round| {
                for cube in round.iter() {
                    acc.entry(cube.color)
                        .and_modify(|v| {
                            *v = (*v).max(cube.amount);
                        })
                        .or_insert(cube.amount);
                }
                acc
            })
            .values()
            .product()
    }
}

fn cube(input: &str) -> IResult<&str, Cube> {
    let (input, (amount, color)) = separated_pair(complete::u32, tag(" "), alpha1)(input)?;
    Ok((input, Cube { color, amount }))
}

fn round(input: &str) -> IResult<&str, Vec<Cube>> {
    let (input, cubes) = separated_list1(tag(", "), cube)(input)?;
    Ok((input, cubes))
}

fn game(input: &str) -> IResult<&str, Game> {
    let (input, id) = preceded(tag("Game "), digit1)(input)?;
    let (input, rounds) = preceded(tag(": "), separated_list1(tag("; "), round))(input)?;
    Ok((input, Game { rounds, id }))
}

fn parse_games(input: &str) -> IResult<&str, Vec<Game>> {
    let (input, games) = separated_list1(line_ending, game)(input)?;
    Ok((input, games))
}

pub fn part_one(input: &str) -> Option<u32> {
    let map = BTreeMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let game = parse_games(input).expect("should parse");

    Some(
        game.1
            .iter()
            .filter_map(|game| game.valid_for_cube_set(&map))
            .sum::<u32>(),
    )
}

pub fn part_two(input: &str) -> Option<u32> {
    let game = parse_games(input).expect("should parse");

    Some(
        game.1
            .iter()
            .map(|game| game.minimum_cube_set())
            .sum::<u32>(),
    )
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file_part(
            "examples", DAY, 1,
        ));
        assert_eq!(result, Some(8));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file_part(
            "examples", DAY, 2,
        ));
        assert_eq!(result, Some(2286));
    }
}
