from collections import OrderedDict


def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str):
    boxes = [OrderedDict() for _ in range(256)]
    operations = input.split(",")
    for operation in operations:
        match operation[-1]:
            case "-":
                label = operation[:-1]
                label_hash = hash_string(label)
                try:
                    boxes[label_hash].pop(label)
                except KeyError:
                    pass
            case digits if operation[-1] in digits:
                label = operation[:-2]
                focal = operation[-1]
                label_hash = hash_string(label)
                boxes[label_hash][label] = int(focal)
    return sum(
        [
            ((1 + bx) * (1 + lx) * box[label])
            for (bx, box) in enumerate(boxes)
            for (lx, label) in enumerate(box)
        ]
    )


def hash_string(string_to_hash: str) -> int:
    value = 0
    for char in string_to_hash:
        value = ((ord(char) + value) * 17) % 256
    return value


if __name__ == "__main__":
    assert solve(parse_input("./15/part1.test")) == 145
    print(solve(parse_input("./15/input")))
