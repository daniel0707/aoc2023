from collections import Counter


SCORES = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def parse_input(path: str) -> dict[str, int]:
    with open(path, "r") as input:
        return {
            hand: int(bid)
            for hand, bid in (line.split() for line in input.read().splitlines())
        }


def solve(input: dict[str, int]) -> int:
    divided_hands = [[] for _ in range(7)]
    for hand in input.keys():
        hand_count = Counter(hand)
        hand_count_sorted = hand_count.most_common()
        match hand_count_sorted[0]:
            case (_, 5):  # 5
                divided_hands[0].append(hand)
            case ("J", 4):  # 5
                divided_hands[0].append(hand)
            case (_, 4):
                if "J" in hand:  # 5
                    divided_hands[0].append(hand)
                else:  # 4-1
                    divided_hands[1].append(hand)
            case ("J", 3):
                match hand_count_sorted[1]:
                    case (_, 2):  # 5
                        divided_hands[0].append(hand)
                    case (_, 1):  # 4-1
                        divided_hands[1].append(hand)
            case (_, 3):
                match hand_count_sorted[1]:
                    case ("J", 2):  # 5
                        divided_hands[0].append(hand)
                    case (_, 2):  # 3-2
                        divided_hands[2].append(hand)
                    case (_, 1):
                        if "J" in hand:  # 4-1
                            divided_hands[1].append(hand)
                        else:  # 3-1-1
                            divided_hands[3].append(hand)
            case ("J", 2):
                match hand_count_sorted[1]:
                    case (_, 2):  # 4-1
                        divided_hands[1].append(hand)
                    case (_, 1):  # 3-1-1
                        divided_hands[3].append(hand)
            case (_, 2):
                match hand_count_sorted[1]:
                    case ("J", 2):  # 4-1
                        divided_hands[1].append(hand)
                    case (_, 2):
                        if "J" in hand:  # 3-2
                            divided_hands[2].append(hand)
                        else:  # 2-2-1
                            divided_hands[4].append(hand)
                    case (_, 1):
                        if "J" in hand:  # 3-1-1
                            divided_hands[3].append(hand)
                        else:  # 2-1-1-1
                            divided_hands[5].append(hand)
            case (_, 1):
                if "J" in hand:  # 2-1-1-1
                    divided_hands[5].append(hand)
                else:  # 1-1-1-1-1
                    divided_hands[6].append(hand)
    divided_hands.reverse()
    sorted_hands = [
        h
        for h_list in divided_hands
        for h in sorted(h_list, key=lambda s: [SCORES[c] for c in s])
    ]
    return sum(input[h] * (i + 1) for i, h in enumerate(sorted_hands))


if __name__ == "__main__":
    assert solve(parse_input("./07/part2.test")) == 5905
    print(solve(parse_input("./07/input")))
