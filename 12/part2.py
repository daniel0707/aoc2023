from functools import cache
import re


def parse_input(path: str) -> list[tuple[str, str]]:
    with open(path, "r") as input:
        return [line.split() for line in input.readlines()]


def solve(input: list[tuple[str, str]]):
    possible_combinations = 0
    for nr, line in enumerate(input):
        nonogram, numbers = line
        nonogram = (nonogram + "?") * 4 + nonogram
        numbers = tuple([int(num) for num in numbers.split(",")] * 5)
        nonogram = compress_nonogram(nonogram)
        possible_combinations += solve_line(nonogram, numbers)
    return possible_combinations


def compress_nonogram(nonogram: str) -> str:
    return re.sub(
        r"\.+", ".", nonogram + "."
    )  # trailing dot to ease end of line detection


@cache
def solve_line(nonogram: str, numbers: list[int], group: str = "") -> int:
    # if group is empty we are NOT in group
    if not numbers and not nonogram and not group:
        return 1
    if not nonogram and not group and numbers:
        return 0
    if not nonogram and group and numbers:
        if len(group) == numbers[0] and len(numbers) == 1:
            return 1
        return 0
    if len(group) == 0:
        match nonogram[0]:
            case ".":
                if not numbers:  # all groups closed
                    if "#" in nonogram:
                        return 0
                    return 1
                return solve_line(nonogram[1:], numbers)
            case "#":  # group starts here
                if not numbers:  # invalid
                    return 0
                return solve_line(nonogram[1:], numbers, "#")
            case "?":
                if not numbers:
                    return solve_line(nonogram[1:], numbers)
                return solve_line(nonogram[1:], numbers) + solve_line(
                    nonogram[1:], numbers, "#"
                )
    else:  # in group
        if not nonogram:  # EOL
            if len(group) == numbers[0] and len(numbers) == 1:
                return 1
            return 0
        match nonogram[0]:
            case ".":
                if len(group) == numbers[0]:  # valid group ending
                    return solve_line(nonogram[1:], numbers[1:])
                return 0  # if it ended and group was shorter or longer then its wrong
            case "#":
                if len(group) < numbers[0]:  # continue group
                    return solve_line(nonogram[1:], numbers, group + "#")
                if len(group) == numbers[0]:
                    return 0  # invalid case ahead
                return 0  # invalid case
            case "?":
                if len(group) < numbers[0]:  # continue group
                    return solve_line(nonogram[1:], numbers, group + "#")
                if len(group) == numbers[0]:
                    return solve_line(nonogram[1:], numbers[1:])
                return 0  # invalid case


if __name__ == "__main__":
    assert solve(parse_input("./12/part2.test")) == 525152
    print(solve(parse_input("./12/input")))
