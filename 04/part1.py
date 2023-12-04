def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    score = 0
    for line in input:
        winning_numbers, drawn_numbers = [
            nums.strip().split() for nums in line.split(":")[1].split("|")
        ]
        common = set(winning_numbers) & set(drawn_numbers)
        score += 2 ** (len(common) - 1) if len(common) > 0 else 0
    return score


if __name__ == "__main__":
    assert solve(parse_input("./04/part1.test")) == 13
    print(solve(parse_input("./04/input")))
