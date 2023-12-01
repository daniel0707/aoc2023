import string


def parse_input() -> list[str]:
    with open("./01/input.txt", "r") as input:
        return input.read().splitlines()


def solve() -> int:
    input = parse_input()
    result = 0
    for line in input:
        digits: list[int] = [int(char) for char in line if char in string.digits]
        line_value: int = 10 * digits[0] + digits[-1]
        result += line_value
    return result


if __name__ == "__main__":
    print(solve())
