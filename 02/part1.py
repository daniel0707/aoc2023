def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    id_sum = 0
    for line in input:
        max_color = {"blue": 14, "red": 12, "green": 13}
        game_id = int(line.split(" ")[1][:-1])
        game_draws = line.split(":")[1].split(";")
        game_ok = True
        for draw in game_draws:
            colors = draw.split(",")
            for color in colors:
                nr, col = color.strip().split(" ")
                if int(nr) > max_color.get(col):
                    game_ok = False
        if game_ok:
            id_sum += game_id
    return id_sum


if __name__ == "__main__":
    assert solve(parse_input("./02/part1.test")) == 8
    print(solve(parse_input("./02/input")))
