import string


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    result = 0
    for line in input:
        digits: list[int] = [int(char) for char in line if char in string.digits]
        line_value: int = 10 * digits[0] + digits[-1]
        result += line_value
    return result


if __name__ == "__main__":
    assert solve(parse_input("./01/part1.test")) == 142
    print(solve(parse_input("./01/input")))
