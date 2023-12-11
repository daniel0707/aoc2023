import queue


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [[char for char in line.strip()] for line in input.readlines()]


def solve(input: list[list[str]]) -> int:
    # find starting point
    start = None
    start_pipes: list[tuple[int, int]] = []
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
    # DFS
    dfs_queue = queue.LifoQueue()  # (Y,X,dist)
    dfs_visited = [start]
    dfs_queue.put(start_pipes[0])
    while not dfs_queue.empty():
        current_pipe = dfs_queue.get()
        next_pipes = get_next_pipes(dfs_visited, input, current_pipe)
        dfs_visited.append(current_pipe[:2])
        if len(next_pipes) > 1:
            print("FAILED SANITY CHECK NR 1")
        if len(next_pipes) == 1:
            dfs_queue.put(next_pipes[0])

    # actual part 2
    # points on the right side of the direction we are moving in,
    # untill we meet another edge,
    # are potentially within the polygon,
    # assuming we are moving clockwise

    points_within: list[tuple[int, int]] = []
    jx = 1
    current_point = dfs_visited[jx]
    previous_point = start
    while input[current_point[0]][current_point[1]] != "S":
        points_on_right = get_points_on_right(
            current_point, previous_point, input, dfs_visited
        )
        if points_on_right:
            points_within.extend(points_on_right)
        jx += 1
        previous_point = current_point
        if jx == len(dfs_visited):
            break
        current_point = dfs_visited[jx]
    print(set(points_within))
    return len(set(points_within))


def get_points_on_right(
    current, previous, all_points, pipeline_points
) -> list[tuple[int, int]]:
    vector = (current[0] - previous[0], current[1] - previous[1])  # Y,X
    por = []
    match vector:
        case (0, 1):  # right
            if current[0] != 0:
                right_points = [
                    (y, current[1]) for y in range(current[0] + 1, len(all_points))
                ]
                also_right_points = [
                    (y, previous[1]) for y in range(previous[0] + 1, len(all_points))
                ]
                ix = 0
                jx = 0
                while right_points[ix] not in pipeline_points:
                    por.append(right_points[ix])
                    ix += 1
                while also_right_points[jx] not in pipeline_points:
                    por.append(also_right_points[jx])
                    jx += 1
        case (0, -1):  # left
            if current[0] != 0:
                right_points = [(y, current[1]) for y in range(current[0] - 1, -1, -1)]
                also_right_points = [
                    (y, previous[1]) for y in range(previous[0] - 1, -1, -1)
                ]
                ix = 0
                jx = 0
                while right_points[ix] not in pipeline_points:
                    por.append(right_points[ix])
                    ix += 1
                while also_right_points[jx] not in pipeline_points:
                    por.append(also_right_points[jx])
                    jx += 1
        case (1, 0):  # down
            if current[1] != 0:
                right_points = [(current[0], x) for x in range(current[1] - 1, -1, -1)]
                also_right_points = [
                    (previous[0], x) for x in range(previous[1] - 1, -1, -1)
                ]
                also_right_points
                ix = 0
                jx = 0
                while right_points[ix] not in pipeline_points:
                    por.append(right_points[ix])
                    ix += 1
                while also_right_points[jx] not in pipeline_points:
                    por.append(also_right_points[jx])
                    jx += 1
        case (-1, 0):  # up
            if current[1] != len(all_points[0]) - 1:
                right_points = [
                    (current[0], x) for x in range(current[1] + 1, len(all_points[0]))
                ]
                also_right_points = [
                    (previous[0], x) for x in range(previous[1] + 1, len(all_points[0]))
                ]
                also_right_points
                ix = 0
                jx = 0
                while right_points[ix] not in pipeline_points:
                    por.append(right_points[ix])
                    ix += 1
                while also_right_points[jx] not in pipeline_points:
                    por.append(also_right_points[jx])
                    jx += 1
    return por


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
            if x < len(pipe_map[0]):
                next_pipes.append((y, x + 1, dist))  # right
    if len(next_pipes) == 0:
        return []
    return [pipe for pipe in next_pipes if pipe[:2] not in visited_pipes]


if __name__ == "__main__":
    assert solve(parse_input("./10/part2.test")) == 8
    print(solve(parse_input("./10/input")))
