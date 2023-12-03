import re
import string

NUMDOT = set(string.digits + ".")


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def is_number_valid(number: tuple[str, int, int, int], lines: list[str]) -> bool:
    area_min_x = number[1] - 1 if number[1] > 0 else number[1]
    area_max_x = number[2] + 1 if number[2] < len(lines[0]) else number[2]
    area_min_y = number[3] - 1 if number[3] > 0 else number[3]
    area_max_y = number[3] + 1 if number[3] < len(lines) - 1 else number[3]
    area_chars = set()
    for area_y in range(area_min_y, area_max_y + 1):
        area_chars.update(lines[area_y][area_min_x:area_max_x])
    if len(area_chars.difference(NUMDOT)) > 0:
        return True
    else:
        return False


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
    return sum([int(number[0]) for number in numbers if is_number_valid(number, input)])


if __name__ == "__main__":
    assert solve(parse_input("./03/part1.test")) == 4361
    print(solve(parse_input("./03/input")))
