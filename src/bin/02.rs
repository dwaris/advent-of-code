use std::slice::Windows;

advent_of_code::solution!(2);

fn check_condition(report: &[i32]) -> bool {
    let mut report: Windows<i32> = report.windows(2);

    let is_asc: bool = report.clone().all(|window| window[0] <= window[1]);
    let is_des = report.clone().all(|window| window[0] >= window[1]);

    let bounds = report.all(|x| {
        let diff = (x[0] - x[1]).abs();
        1 <= diff && diff <= 3
    });

    (is_asc || is_des) && bounds
}

pub fn part_one(input: &str) -> Option<u32> {
    let mut reports: Vec<Vec<i32>> = vec![];
    for line in input.lines() {
        reports.push(line.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect());
    }

    let mut output = 0;
    for report in reports {
        if check_condition(&report) {
            output += 1;
        }
    }
    Some(output)
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut reports: Vec<Vec<i32>> = vec![];
    for line in input.lines() {
        reports.push(line.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect());
    }

    let mut output = 0;
    for report in reports {
        if check_condition(&report) {
            output += 1;
        } else {
            for i in 0..report.len() {
                let mut new_report = report.clone();
                new_report.remove(i);
                if check_condition(&new_report) {
                    output += 1;
                    break;
                }
            }
        }
    }
    Some(output)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4));
    }
}
