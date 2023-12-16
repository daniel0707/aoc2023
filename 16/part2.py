from collections import deque
from typing import Deque


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]) -> int:
    start_positions = [
        *[(complex(ax, 0), complex(0, 1)) for ax in range(len(input[0]))],  # top
        *[(complex(0, ay), complex(1, 0)) for ay in range(len(input))],  # left
        *[
            (complex(ax, len(input) - 1), complex(0, -1)) for ax in range(len(input[0]))
        ],  # bottom
        *[
            (complex(len(input[0]) - 1, ay), complex(-1, 0)) for ay in range(len(input))
        ],  # right
    ]
    max_energized = 0
    for sp in start_positions:
        queue: Deque[
            tuple[complex, complex]
        ] = deque()  # (position x+jy, direction x+jy)
        visited = set()  # (position x+jy, direction x+jy)
        queue.append(sp)
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
        max_energized = max(max_energized, len(unique_visited))
    return max_energized


if __name__ == "__main__":
    assert solve(parse_input("./16/part2.test")) == 51
    print(solve(parse_input("./16/input")))
