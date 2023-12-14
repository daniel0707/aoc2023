import re


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line] for line in input.readlines()]


def solve(input: list[list[str]]):
    rotated: list[list[str]] = list(map(list, zip(*input)))
    rotated_shifted = []
    for column in rotated:
        column = "".join(column)
        column_split = column.split("#")
        new_column = []
        for split in column_split:
            count = len(re.findall(r"O", split))
            split = split.replace("O", ".")
            split = split.replace(".", "O", count)
            new_column.append(split)
        new_column = "#".join(new_column)
        rotated_shifted.append(new_column)
    final_field = list(map(list, zip(*rotated_shifted)))
    return sum(
        [
            (len(final_field) - ix) * len(re.findall(r"O", "".join(row)))
            for ix, row in enumerate(final_field)
        ]
    )


if __name__ == "__main__":
    assert solve(parse_input("./14/part1.test")) == 136
    print(solve(parse_input("./14/input")))
