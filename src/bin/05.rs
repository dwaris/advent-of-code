use std::ops::Range;

use nom::{
    bytes::complete::take_until,
    character::complete::{self, line_ending, multispace1, space1},
    multi::{many1, separated_list1},
    sequence::{separated_pair, tuple},
    IResult, Parser,
};
use nom_supreme::{tag::complete::tag, ParserExt};

use rayon::iter::{IntoParallelIterator, ParallelIterator};

advent_of_code::solution!(5);

struct SeedMap {
    mappings: Vec<(Range<u64>, Range<u64>)>,
}

impl SeedMap {
    fn translate(&self, source: u64) -> u64 {
        let valid_mapping = self
            .mappings
            .iter()
            .find(|(source_range, _)| source_range.contains(&source));
        let Some((source_range, destination_range)) = valid_mapping else {
            return source;
        };

        let offset = source - source_range.start;

        destination_range.start + offset
    }
}

fn seed_map(input: &str) -> IResult<&str, SeedMap> {
    take_until("map:")
        .precedes(tag("map:"))
        .precedes(many1(line_ending.precedes(line)).map(|mappings| SeedMap { mappings }))
        .parse(input)
}

fn line(input: &str) -> IResult<&str, (Range<u64>, Range<u64>)> {
    let (input, (destination, source, num)) = tuple((
        complete::u64,
        complete::u64.preceded_by(tag(" ")),
        complete::u64.preceded_by(tag(" ")),
    ))(input)?;

    Ok((
        input,
        (source..(source + num), destination..(destination + num)),
    ))
}

fn parse_seedmap(input: &str) -> IResult<&str, (Vec<u64>, Vec<SeedMap>)> {
    let (input, seeds) = tag("seeds: ")
        .precedes(separated_list1(multispace1, complete::u64))
        .parse(input)?;
    let (input, maps) = many1(seed_map)(input)?;

    Ok((input, (seeds, maps)))
}

fn parse_seedmap1(input: &str) -> IResult<&str, (Vec<Range<u64>>, Vec<SeedMap>)> {
    let (input, seeds) = tag("seeds: ")
        .precedes(separated_list1(
            space1,
            separated_pair(complete::u64, tag(" "), complete::u64)
                .map(|(start, offset)| start..(start + offset)),
        ))
        .parse(input)?;
    let (input, maps) = many1(seed_map)(input)?;

    Ok((input, (seeds, maps)))
}

pub fn part_one(input: &str) -> Option<u64> {
    let (_, (seeds, maps)) = parse_seedmap(input).expect("a valid parse");

    let locations = seeds
        .iter()
        .map(|seed| maps.iter().fold(*seed, |seed, map| map.translate(seed)))
        .collect::<Vec<u64>>();

    locations.iter().min().copied()
}

pub fn part_two(input: &str) -> Option<u64> {
    let (_, (seeds, maps)) = parse_seedmap1(input).expect("a valid parse");

    let minimum_location = seeds
        .into_par_iter()
        .flat_map(|range| range.clone())
        .map(|seed| maps.iter().fold(seed, |seed, map| map.translate(seed)))
        .min();

    minimum_location
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(35));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(46));
    }
}
