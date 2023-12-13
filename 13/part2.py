def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [puzzle.splitlines() for puzzle in input.read().split("\n\n")]


def solve(input: list[str]):
    puzzle_total = 0
    for puzzle in input:
        horizontal_score = check_horizontal(puzzle) * 100
        vertical_score = check_vertical(puzzle)
        puzzle_total += horizontal_score + vertical_score
    return puzzle_total


def check_horizontal(puzzle: list[str]) -> int:
    puzzle = [[char for char in line] for line in puzzle]
    max_window_size = int(len(puzzle) / 2)
    for line_nr in range(len(puzzle) - 1):
        window_one = puzzle[: line_nr + 1]
        window_two = puzzle[line_nr + 1 :]
        while len(window_one) > max_window_size:
            window_one = window_one[1:]
        while len(window_two) > max_window_size:
            window_two = window_two[: len(window_two) - 1]
        if len(window_one) > len(window_two):
            difference = len(window_one) - len(window_two)
            window_one = window_one[difference:]
        if len(window_two) > len(window_one):
            difference = len(window_two) - len(window_one)
            window_two = window_two[:-difference]
        if find_smudge(window_one, window_two[::-1]):
            return line_nr + 1
    return 0


def check_vertical(puzzle: list[str]) -> int:
    rotated_puzzle = [[char for char in line] for line in puzzle]
    rotated_puzzle = list(map(list, zip(*rotated_puzzle)))
    max_window_size = int(len(rotated_puzzle) / 2)
    for line_nr in range(len(rotated_puzzle) - 1):
        window_one = rotated_puzzle[: line_nr + 1]
        window_two = rotated_puzzle[line_nr + 1 :]
        while len(window_one) > max_window_size:
            window_one = window_one[1:]
        while len(window_two) > max_window_size:
            window_two = window_two[: len(window_two) - 1]
        if len(window_one) > len(window_two):
            difference = len(window_one) - len(window_two)
            window_one = window_one[difference:]
        if len(window_two) > len(window_one):
            difference = len(window_two) - len(window_one)
            window_two = window_two[:-difference]
        if find_smudge(window_one, window_two[::-1]):
            return line_nr + 1
    return 0


def find_smudge(list_one: list[list[str]], list_two: list[list[str]]) -> bool:
    count = 0
    for sublist_one, sublist_two in zip(list_one, list_two):
        for char_one, char_two in zip(sublist_one, sublist_two):
            if char_one != char_two:
                count += 1
    return count == 1


if __name__ == "__main__":
    assert solve(parse_input("./13/part2.test")) == 400
    print(solve(parse_input("./13/input")))
