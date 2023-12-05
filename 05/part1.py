import re
from itertools import batched


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().split("\n\n")


def solve(input: list[str]) -> int:
    seeds: list[int] = [int(seed) for seed in re.findall(r"\d+", input[0])]
    solution_dict = {s: s for s in seeds}
    maps: list[list[tuple[int, int, int, int, int]]] = []
    for m in range(1, 8):
        # source_min,source_max,destination_min,destination_max,step
        source_to_destination: list[tuple[int, int, int, int, int]] = []
        std = [int(i) for i in re.findall(r"\d+", input[m])]
        for std_batch in batched(std, 3):
            source_to_destination.append(
                (
                    std_batch[1],
                    std_batch[1] + std_batch[2],
                    std_batch[0],
                    std_batch[0] + std_batch[2],
                    std_batch[2],
                )
            )
        maps.append(source_to_destination)
    # actual solution part
    for seed in seeds:
        for std_map_list in maps:
            for std_map in std_map_list:
                if std_map[0] <= solution_dict[seed] <= std_map[1]:
                    solution_dict[seed] = std_map[2] + solution_dict[seed] - std_map[0]
                    break
    return min([v for _, v in solution_dict.items()])


if __name__ == "__main__":
    assert solve(parse_input("./05/part1.test")) == 35
    print(solve(parse_input("./05/input")))
