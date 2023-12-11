import queue


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]) -> int:
    max_dist = 0
    # find starting point
    start = None
    start_pipes = []
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "S":
                start = (y, x)
    y, x = start
    # find possible directions, assume S point is not an edge point
    if input[y - 1][x] in "|7F":  # up
        start_pipes.append((y - 1, x, 1))
    if input[y + 1][x] in "|LJ":  # down
        start_pipes.append((y + 1, x, 1))
    if input[y][x - 1] in "-LF":  # right
        start_pipes.append((y, x - 1, 1))
    if input[y][x + 1] in "-J7":  # left
        start_pipes.append((y, x + 1, 1))
    # BFS
    bfs_queue = queue.Queue()  # (Y,X,dist)
    bfs_visited = [start]
    for next in start_pipes:
        bfs_queue.put(next)
    while not bfs_queue.empty():
        current_pipe = bfs_queue.get()
        next_pipes = get_next_pipes(bfs_visited, input, current_pipe)
        bfs_visited.append(current_pipe[:2])
        if len(next_pipes) > 1:
            print("FAILED SANITY CHECK NR 1")
        if len(next_pipes) == 1:
            bfs_queue.put(next_pipes[0])
            if max_dist < next_pipes[0][2]:
                max_dist = next_pipes[0][2]
    return max_dist


def get_next_pipes(
    visited_pipes: list[tuple[int, int]],
    pipe_map: list[list[int]],
    current_pipe: tuple[int, int, int],
) -> list[tuple[int, int, int]]:
    y, x, dist = current_pipe
    current_pipe_char = pipe_map[y][x]
    next_pipes: list[tuple[int, int, int]] = []
    dist += 1
    match current_pipe_char:
        case "|":
            if y > 0:
                next_pipes.append((y - 1, x, dist))  # up
            if y < len(pipe_map):
                next_pipes.append((y + 1, x, dist))  # down
        case "-":
            if x > 0:
                next_pipes.append((y, x - 1, dist))  # left
            if x < len(pipe_map[0]):
                next_pipes.append((y, x + 1, dist))  # right
        case "L":
            if y > 0:
                next_pipes.append((y - 1, x, dist))  # up
            if x < len(pipe_map[0]):
                next_pipes.append((y, x + 1, dist))  # right
        case "J":
            if y > 0:
                next_pipes.append((y - 1, x, dist))  # up
            if x > 0:
                next_pipes.append((y, x - 1, dist))  # left
        case "7":
            if y < len(pipe_map):
                next_pipes.append((y + 1, x, dist))  # down
            if x > 0:
                next_pipes.append((y, x - 1, dist))  # left
        case "F":
            if y < len(pipe_map):
                next_pipes.append((y + 1, x, dist))  # down
            if x > 0:
                next_pipes.append((y, x + 1, dist))  # right
    if len(next_pipes) == 0:
        return []
    return [pipe for pipe in next_pipes if pipe[:2] not in visited_pipes]


if __name__ == "__main__":
    assert solve(parse_input("./10/part1.test")) == 8
    print(solve(parse_input("./10/input")))
