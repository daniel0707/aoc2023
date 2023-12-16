from collections import deque
from typing import Deque


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]) -> int:
    queue: Deque[tuple[complex, complex]] = deque()  # (position x+jy, direction x+jy)
    visited = set()  # (position x+jy, direction x+jy)
    queue.append((complex(0, 0), complex(1, 0)))
    while queue:
        (current, direction) = queue.popleft()
        x = int(current.real)
        y = int(current.imag)
        if 0 > x or x >= len(input[0]) or 0 > y or y >= len(input):
            continue
        if (current, direction) in visited:
            continue
        visited.add((current, direction))
        if input[y][x] == "|" and direction.imag == 0:
            queue.append((current + complex(0, 1), complex(0, 1)))
            queue.append((current + complex(0, -1), complex(0, -1)))
        elif input[y][x] == "-" and direction.real == 0:
            queue.append((current + complex(1, 0), complex(1, 0)))
            queue.append((current + complex(-1, 0), complex(-1, 0)))
        elif input[y][x] == "/":
            new_direction = (
                direction * complex(0, -1)
                if direction.real
                else direction * complex(0, 1)
            )
            queue.append((current + new_direction, new_direction))
        elif input[y][x] == "\\":
            new_direction = (
                direction * complex(0, 1)
                if direction.real
                else direction * complex(0, -1)
            )
            queue.append((current + new_direction, new_direction))
        else:
            queue.append((current + direction, direction))
    unique_visited = set(map(lambda x: x[0], visited))
    return len(unique_visited)


if __name__ == "__main__":
    assert solve(parse_input("./16/part1.test")) == 46
    print(solve(parse_input("./16/input")))
