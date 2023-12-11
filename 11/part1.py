def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]) -> int:
    universe = expand_universe(input)
    galaxies = find_galaxies(universe)
    min_distances = []
    for kx, galaxy_one in enumerate(galaxies):
        galaxy_pair_distances = []
        for _, galaxy_two in enumerate(galaxies[kx:]):
            dist = manhattan_distance(galaxy_one, galaxy_two)
            if dist != 0:
                galaxy_pair_distances.append(dist)
        if galaxy_pair_distances:
            min_distances.extend(galaxy_pair_distances)
    return sum(min_distances)


def expand_universe(universe: list[list[str]]) -> list[list[str]]:
    row_expanded_universe = []
    for row in universe:
        if "#" not in row:
            row_expanded_universe.append(["." for _ in row])
        row_expanded_universe.append(row)
    rotated_column_expanded_universe = []

    rotated_row_expanded_universe = list(map(list, zip(*row_expanded_universe)))
    for column in rotated_row_expanded_universe:
        if "#" not in column:
            rotated_column_expanded_universe.append(["." for _ in column])
        rotated_column_expanded_universe.append(column)
    column_expanded_universe = list(map(list, zip(*rotated_column_expanded_universe)))
    return column_expanded_universe


def manhattan_distance(point_one: tuple[int, int], point_two: tuple[int, int]) -> int:
    y_one, x_one = point_one
    y_two, x_two = point_two
    return abs(x_two - x_one) + abs(y_two - y_one)


def find_galaxies(universe: list[list[int]]) -> list[int]:
    galaxies = []
    for ix, row in enumerate(universe):
        for jx, char in enumerate(row):
            if char == "#":
                galaxies.append((ix, jx))
    return galaxies


if __name__ == "__main__":
    assert solve(parse_input("./11/part1.test")) == 374
    print(solve(parse_input("./11/input")))
