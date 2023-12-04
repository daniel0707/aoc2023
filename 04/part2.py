from collections import Counter


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    score_dict: dict[int, int] = {}
    for card_nr, line in enumerate(input):
        winning_numbers, drawn_numbers = [
            nums.strip().split() for nums in line.split(":")[1].split("|")
        ]
        common = set(winning_numbers) & set(drawn_numbers)
        score_dict[card_nr + 1] = len(common)
    score_counter = Counter({nr: 1 for nr in range(1, len(input) + 1)})
    for card_number in range(1, len(input) + 1):
        for copy_nr in range(1, score_dict[card_number] + 1):
            score_counter[card_number + copy_nr] += score_counter[card_number]
    return sum(score_counter.values())


if __name__ == "__main__":
    assert solve(parse_input("./04/part2.test")) == 30
    print(solve(parse_input("./04/input")))
