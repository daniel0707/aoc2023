import re
from itertools import batched


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().split("\n\n")


def solve(input: list[str]) -> int:
    seeds: list[int] = [int(seed) for seed in re.findall(r"\d+", input[0])]
    # (destination_start,destination_end), inclusive end!
    solution_set = set(
        [(s_b[0], s_b[0] + s_b[1] - 1) for s_b in batched(seeds, 2)]
    )  # initial destination is eq to source
    for mapping in range(1, 8):
        parsed_mapping = [int(val) for val in re.findall(r"\d+", input[mapping])]
        # ((source_start,source_end),(destination_start,destination_end)), inclusive end!
        std_mappings = [
            ((i[1], i[1] + i[2] - 1), (i[0], i[0] + i[2] - 1))
            for i in batched(parsed_mapping, 3)
        ]
        processed_mappings: set[tuple[int, int]] = set()
        remaining_mappings: set[tuple[int, int]] = solution_set.copy()
        iteration_mappings: set[tuple[int, int]] = solution_set.copy()
        for std in std_mappings:
            shift = std[1][0] - std[0][0]
            for source in iteration_mappings:
                overlaps = find_overlaps(source, std[0])
                if len(overlaps) > 0:
                    overlap, *remainder = overlaps
                    processed_mappings.add((overlap[0] + shift, overlap[1] + shift))
                    remaining_mappings.remove(source)
                    remaining_mappings.update(remainder)
            # after iterating source ranges,
            # update for next loop to iterate over remaining ranges
            iteration_mappings = remaining_mappings.copy()
        # after processing all mappings from current map ,
        # update the solution set to contain all current destinations
        # to use as sources for next step
        solution_set = (
            processed_mappings | remaining_mappings
        )  # union returns new object to refer to
    return min([v[0] for v in solution_set])


# find overlap and if remaining, non processed parts
def find_overlaps(
    source_range: tuple[int, int], mapping_source_range: tuple[int, int]
) -> list[tuple[int, int]]:
    overlap_start = max(source_range[0], mapping_source_range[0])
    overlap_end = min(source_range[1], mapping_source_range[1])

    result_destinations: list[tuple[int, int]] = []
    if overlap_start <= overlap_end:
        # there is an overlap
        result_destinations.append((overlap_start, overlap_end))
        if overlap_start > source_range[0]:
            # there is a part in source before overlap
            result_destinations.append((source_range[0], overlap_start - 1))
        if overlap_end < source_range[1]:
            # there is a part in source after overlap
            result_destinations.append((overlap_end + 1, source_range[1]))
    else:
        # no overlaps, return empty to allow reprocessing by next map
        return []
    return result_destinations


if __name__ == "__main__":
    assert solve(parse_input("./05/part1.test")) == 46
    print(solve(parse_input("./05/input")))
