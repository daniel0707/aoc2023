import re


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]):
    state = input[:]
    seen = []
    cycle = None
    for ix in range(0, 1000000000):
        new_state = push_east(push_south(push_west(push_north(state))))
        state_string = "\n".join(["".join(row) for row in new_state])
        if state_string in seen:
            cycle = (ix, seen.index(state_string))
            break
        else:
            seen.append(state_string)
            state = new_state
    final_state_ix = cycle[1] + (1000000000 - cycle[1]) % (cycle[0] - cycle[1])
    final_state = input[:]
    for _ in range(0, final_state_ix):
        final_state = push_east(push_south(push_west(push_north(final_state))))
    return sum(
        [
            (len(final_state) - ix) * len(re.findall(r"O", "".join(row)))
            for ix, row in enumerate(final_state)
        ]
    )


def push_north(field: list[list[str]]) -> list[list[str]]:
    rotated: list[list[str]] = list(map(list, zip(*field)))
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
    return list(map(list, zip(*rotated_shifted)))


def push_south(field: list[list[str]]) -> list[list[str]]:
    rotated: list[list[str]] = list(map(list, zip(*field)))
    rotated_shifted = []
    for column in rotated:
        column = "".join(column[::-1])
        column_split = column.split("#")
        new_column = []
        for split in column_split:
            count = len(re.findall(r"O", split))
            split = split.replace("O", ".")
            split = split.replace(".", "O", count)
            new_column.append(split)
        new_column = "#".join(new_column)
        rotated_shifted.append(new_column[::-1])
    return list(map(list, zip(*rotated_shifted)))


def push_west(field: list[list[str]]) -> list[list[str]]:
    new_field = []
    for column in field:
        column = "".join(column)
        column_split = column.split("#")
        new_column = []
        for split in column_split:
            count = len(re.findall(r"O", split))
            split = split.replace("O", ".")
            split = split.replace(".", "O", count)
            new_column.append(split)
        new_column = "#".join(new_column)
        new_field.append(new_column)
    return new_field


def push_east(field: list[list[str]]) -> list[list[str]]:
    new_field = []
    for column in field:
        column = "".join(column[::-1])
        column_split = column.split("#")
        new_column = []
        for split in column_split:
            count = len(re.findall(r"O", split))
            split = split.replace("O", ".")
            split = split.replace(".", "O", count)
            new_column.append(split)
        new_column = "#".join(new_column)
        new_field.append(new_column[::-1])
    return new_field


if __name__ == "__main__":
    assert solve(parse_input("./14/part2.test")) == 64
    print(solve(parse_input("./14/input")))
