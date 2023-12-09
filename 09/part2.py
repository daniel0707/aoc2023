def parse_input(path: str) -> list[list[int]]:
    with open(path, "r") as input:
        return [
            [int(num) for num in line.split()] for line in input.read().splitlines()
        ]


def solve(input: list[int]) -> int:
    total = 0
    for sequence in input:
        current_sequence = sequence[::-1]
        value = current_sequence[-1]
        while not set(current_sequence) == set([0]):
            current_sequence = [
                current_sequence[ix + 1] - val
                for ix, val in enumerate(current_sequence)
                if ix < len(current_sequence) - 1
            ]
            value += current_sequence[-1]
        total += value
    return total


if __name__ == "__main__":
    assert solve(parse_input("./09/part2.test")) == 2
    print(solve(parse_input("./09/input")))
