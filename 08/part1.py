import re


def parse_input(path: str) -> tuple[str, str]:
    with open(path, "r") as input:
        instructions, maps = input.read().split("\n\n")
        return (instructions, maps)


class MapNode:
    def __init__(self, name: str, left: str, right: str) -> None:
        self.name = name
        self.L = left
        self.R = right


def solve(input: tuple[str, str]) -> int:
    instructions, maps = input
    # create nodes
    map_nodes = {
        line[:3]: MapNode(*re.findall(r"\w+", line)) for line in maps.splitlines()
    }
    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        direction = instructions[steps % len(instructions)]
        current_node = map_nodes[current_node].__getattribute__(direction)
        steps += 1
    return steps


if __name__ == "__main__":
    assert solve(parse_input("./08/part1.test")) == 6
    print(solve(parse_input("./08/input")))
