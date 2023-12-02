def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    power_sum = 0
    for line in input:
        max_color = {"blue": 0, "red": 0, "green": 0}
        game_draws = line.split(":")[1].split(";")
        for draw in game_draws:
            colors = draw.split(",")
            for color in colors:
                nr, col = color.strip().split(" ")
                if int(nr) > max_color.get(col):
                    max_color[col] = int(nr)
        power = max_color["blue"] * max_color["green"] * max_color["red"]
        power_sum += power
    return power_sum


if __name__ == "__main__":
    assert solve(parse_input("./02/part2.test")) == 2286
    print(solve(parse_input("./02/input")))
