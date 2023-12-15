def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str):
    return sum([hash_string(line) for line in input.split(",")])


def hash_string(string_to_hash: str) -> int:
    value = 0
    for char in string_to_hash:
        value = ((ord(char) + value) * 17) % 256
    return value


if __name__ == "__main__":
    assert solve(parse_input("./15/part1.test")) == 1320
    print(solve(parse_input("./15/input")))
