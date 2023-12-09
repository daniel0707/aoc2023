import re
import math


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
    map_nodes = {
        line[:3]: MapNode(*re.findall(r"\w+", line)) for line in maps.splitlines()
    }
    starting_nodes = [k for k in map_nodes.keys() if k[2] == "A"]
    nodes_steps = {k: 0 for k in starting_nodes}
    for node in starting_nodes:
        current_node = node
        steps = 0
        while not current_node[2] == "Z":
            direction = instructions[steps % len(instructions)]
            current_node = map_nodes[current_node].__getattribute__(direction)
            steps += 1
        nodes_steps[node] = steps
    return math.lcm(*[nodes_steps[k] for k in nodes_steps])


def are_we_there_yet(positions: list[str]):
    for pos in positions:
        if pos[2] != "Z":
            return False
    return True


if __name__ == "__main__":
    assert solve(parse_input("./08/part2.test")) == 6
    print(solve(parse_input("./08/input")))
