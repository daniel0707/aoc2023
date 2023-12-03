import re


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def get_star_numbers(
    number: tuple[str, int, int, int], lines: list[str]
) -> list[tuple[int, int, int]]:
    area_min_x = number[1] - 1 if number[1] > 0 else number[1]
    area_max_x = number[2] + 1 if number[2] < len(lines[0]) else number[2]
    area_min_y = number[3] - 1 if number[3] > 0 else number[3]
    area_max_y = number[3] + 1 if number[3] < len(lines) - 1 else number[3]
    star_matches = []  # (X,Y,value)
    for area_y in range(area_min_y, area_max_y + 1):
        line_to_search = lines[area_y][area_min_x:area_max_x]
        matches = [
            (match.start() + area_min_x, area_y, int(number[0]))
            for match in re.finditer("\*", line_to_search)
        ]
        star_matches.extend(matches)
    return star_matches


def solve(input: list[str]) -> int:
    # find numbers and their coordinates
    numbers: list[tuple[str, int, int, int]] = []  # number,startX,endX,Y
    y = 0
    for line in input:
        matches = [
            (match.group(), match.start(), match.end(), y)
            for match in re.finditer("\d+", line)
        ]
        numbers.extend(matches)
        y += 1
    # find numbers that have stars around them
    star_numbers: list[tuple[int, int, int]] = []
    for number in numbers:
        star_numbers.extend(get_star_numbers(number, input))
    # keep only unique values
    star_numbers_filtered = set(star_numbers)
    star_number_map: dict[tuple[int, int], list[int]] = {}
    for star_number in star_numbers_filtered:
        try:
            star_number_map[(star_number[0], star_number[1])].append(star_number[2])
        except KeyError:
            star_number_map[(star_number[0], star_number[1])] = [star_number[2]]
    # filter stars that have exactly 2 numbers next to it
    filtered_star_numbers = [
        value for _, value in star_number_map.items() if len(value) == 2
    ]
    return sum([num[0] * num[1] for num in filtered_star_numbers])


if __name__ == "__main__":
    assert solve(parse_input("./03/part1.test")) == 467835
    print(solve(parse_input("./03/input")))
