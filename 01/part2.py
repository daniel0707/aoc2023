import re
import string


NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
NUMBERS.extend(string.digits)

NUMBERS_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


def parse_input() -> list[str]:
    with open("./01/input.txt", "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        result += find_first_digit(line) * 10 + find_last_digit(line)
    return result


def find_first_digit(line: str) -> int:
    matches: list[re.Match] = []
    for key in NUMBERS:
        match = re.search(key, line)
        if match is not None:
            matches.append(match)
    matches.sort(key=lambda m: m.start())
    return NUMBERS_MAP.get(matches[0].group(0))


def find_last_digit(line: str) -> int:
    matches: list[re.Match] = []
    for key in NUMBERS:
        match = re.search(key[::-1], line[::-1])
        if match is not None:
            matches.append(match)
    matches.sort(key=lambda m: m.start())
    return NUMBERS_MAP.get(matches[0].group(0)[::-1])


if __name__ == "__main__":
    print(solve(parse_input()))
