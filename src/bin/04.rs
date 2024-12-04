advent_of_code::solution!(4);

pub fn part_one(input: &str) -> Option<u32> {
    let mut grid = Vec::new();

    for line in input.lines() {
        let mut row = Vec::new();
        for c in line.chars() {
            row.push(c);
        }
        grid.push(row);
    }

    let mut count = 0;

    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            count += check_word(&grid, i, j, "XMAS");
        }
    }

    Some(count)
}

pub fn check_word(grid: &Vec<Vec<char>>, i: usize, j: usize, word: &str) -> u32 {
    let mut count = 0;

    let directions = [
        (0, 1),   // Right
        (1, 0),   // Down
        (1, 1),   // Down-Right
        (0, -1),  // Left
        (-1, 0),  // Up
        (-1, -1), // Up-Left
        (1, -1),  // Down-Left
        (-1, 1),  // Up-Right
    ];

    for &(di, dj) in &directions {
        count += check_word_all_directions(grid, i, j, word, di, dj);
    }

    count
}

pub fn check_word_all_directions(
    grid: &Vec<Vec<char>>,
    i: usize,
    j: usize,
    word: &str,
    di: i32,
    dj: i32,
) -> u32 {
    let mut count = 0;

    let mut i = i as i32;
    let mut j = j as i32;

    for c in word.chars() {
        if i < 0 || i >= grid.len() as i32 || j < 0 || j >= grid[i as usize].len() as i32 {
            return 0;
        }

        if grid[i as usize][j as usize] != c {
            return 0;
        }

        i += di;
        j += dj;
    }

    count += 1;

    count
}

pub fn part_two(input: &str) -> Option<u32> {
    let mut grid = Vec::new();

    for line in input.lines() {
        let mut row = Vec::new();
        for c in line.chars() {
            row.push(c);
        }
        grid.push(row);
    }

    let mut count = 0;

    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            count += check_word_cross(&grid, i, j, "MAS", -1, -1, -1, 1); // Diagonals forming an "X"
        }
    }

    Some(count)
}

pub fn check_word_cross(
    grid: &Vec<Vec<char>>,
    i: usize,
    j: usize,
    word: &str,
    di1: i32,
    dj1: i32,
    di2: i32,
    dj2: i32,
) -> u32 {
    let i = i as i32;
    let j = j as i32;

    //first diagonal
    if i + di1 < 0 || i + di1 >= grid.len() as i32 || j + dj1 < 0 || j + dj1 >= grid[0].len() as i32
    {
        return 0;
    }
    if i - di1 < 0 || i - di1 >= grid.len() as i32 || j - dj1 < 0 || j - dj1 >= grid[0].len() as i32
    {
        return 0;
    }

    // second diagonal
    if i + di2 < 0 || i + di2 >= grid.len() as i32 || j + dj2 < 0 || j + dj2 >= grid[0].len() as i32
    {
        return 0;
    }
    if i - di2 < 0 || i - di2 >= grid.len() as i32 || j - dj2 < 0 || j - dj2 >= grid[0].len() as i32
    {
        return 0;
    }

    let string1 = format!(
        "{}{}{}",
        grid[(i - di1) as usize][(j - dj1) as usize],
        grid[i as usize][j as usize],
        grid[(i + di1) as usize][(j + dj1) as usize]
    );

    let string2 = format!(
        "{}{}{}",
        grid[(i - di2) as usize][(j - dj2) as usize],
        grid[i as usize][j as usize],
        grid[(i + di2) as usize][(j + dj2) as usize]
    );

    if (string1.eq(word) || string1.chars().rev().collect::<String>().eq(word))
        && (string2.eq(word) || string2.chars().rev().collect::<String>().eq(word))
    {
        1
    } else {
        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(18));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(9));
    }
}
