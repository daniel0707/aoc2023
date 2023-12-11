def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]], increase: int) -> int:
    shifted_galaxies = shift_galaxies(input, increase - 1)
    min_distances = []
    for kx, galaxy_one in enumerate(shifted_galaxies):
        galaxy_pair_distances = []
        for _, galaxy_two in enumerate(shifted_galaxies[kx:]):
            dist = manhattan_distance(galaxy_one, galaxy_two)
            if dist != 0:
                galaxy_pair_distances.append(dist)
        if galaxy_pair_distances:
            min_distances.extend(galaxy_pair_distances)
    return sum(min_distances)


def shift_galaxies(input: list[tuple[int, int]], shift: int) -> list[tuple[int, int]]:
    galaxies = find_galaxies(input)
    galaxies_y_shift = {galaxy: 0 for galaxy in galaxies}
    galaxies_x_shift = {galaxy: 0 for galaxy in galaxies}
    for y, row in enumerate(input):
        if "#" not in row:
            for galaxy in galaxies:
                if galaxy[0] > y:
                    galaxies_y_shift[galaxy] += shift
    rotated_universe = list(map(list, zip(*input)))
    for x, column in enumerate(rotated_universe):
        if "#" not in column:
            for galaxy in galaxies:
                if galaxy[1] > x:
                    galaxies_x_shift[galaxy] += shift
    return [(g[0] + galaxies_y_shift[g], g[1] + galaxies_x_shift[g]) for g in galaxies]


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
    assert solve(parse_input("./11/part1.test"), 2) == 374
    assert solve(parse_input("./11/part2.test"), 10) == 1030
    assert solve(parse_input("./11/part2.test"), 100) == 8410
    print(solve(parse_input("./11/input"), 1000000))
