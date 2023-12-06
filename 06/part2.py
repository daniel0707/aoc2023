import re
import math


def parse_input(path: str) -> tuple[int, int]:
    with open(path, "r") as input:
        return (
            int(str.join("", re.findall(r"\d+", line))) for line in input.readlines()
        )


def solve(input: tuple[int, int]) -> int:
    return solve_quadratic_equation(input)

    # distance_to_beat < Time_used * (time_total - time_used)
    # dtb < tu*tt - tu²
    # 0 < -dtb + tu*tt - tu²
    # delta = tt² - 4*dtb
    # a,b = (-tt +/-root(delta))/-2
    # a,b = (tt+/-root(delta))/2


def solve_quadratic_equation(variables: tuple[int, int]) -> tuple[int, int]:
    tt, dtb = variables
    delta = tt * tt - 4 * dtb
    a = (tt - math.sqrt(delta)) / 2
    b = (tt + math.sqrt(delta)) / 2
    c = b - a
    if c % 1 > 0:
        return math.ceil(b) - math.ceil(a)
    else:
        return c - 1


if __name__ == "__main__":
    assert solve(parse_input("./06/part1.test")) == 71503
    print(solve(parse_input("./06/input")))
