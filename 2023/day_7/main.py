from collections import Counter
from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 7

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def strength(hand: str, part2: bool):
    hand = hand.replace("T", chr(ord("9") + 1))
    hand = hand.replace("J", chr(ord("2") - 1) if part2 else chr(ord("9") + 2))
    hand = hand.replace("Q", chr(ord("9") + 3))
    hand = hand.replace("K", chr(ord("9") + 4))
    hand = hand.replace("A", chr(ord("9") + 5))

    hand_counter: Counter = Counter(hand)
    if part2:
        target = list(hand_counter.keys())[0]
        for k in hand_counter:
            if k != "1":
                if hand_counter[k] > hand_counter[target] or target == "1":
                    target = k
        assert target != "1" or list(hand_counter.keys()) == ["1"]
        if "1" in hand_counter and target != "1":
            hand_counter[target] += hand_counter["1"]
            del hand_counter["1"]
        assert "1" not in hand_counter or list(hand_counter.keys()) == [
            "1"
        ], f"{hand_counter} {hand}"

    if sorted(hand_counter.values()) == [5]:
        return 10, hand
    elif sorted(hand_counter.values()) == [1, 4]:
        return 9, hand
    elif sorted(hand_counter.values()) == [2, 3]:
        return 8, hand
    elif sorted(hand_counter.values()) == [1, 1, 3]:
        return 7, hand
    elif sorted(hand_counter.values()) == [1, 2, 2]:
        return 6, hand
    elif sorted(hand_counter.values()) == [1, 1, 1, 2]:
        return 5, hand
    elif sorted(hand_counter.values()) == [1, 1, 1, 1, 1]:
        return 4, hand
    else:
        assert False, f"{hand_counter} {hand} {sorted(hand_counter.values())}"


def camel_cards(input_str: str) -> list[int]:
    lines: list[str] = input_str.split("\n")
    answers = []
    for part2 in [False, True]:
        hands = []
        for line in lines:
            hand, bid = line.split()
            hands.append((hand, bid))
        hands = sorted(hands, key=lambda hb: strength(hb[0], part2))
        ans = 0
        for i, (h, b) in enumerate(hands):
            ans += (i + 1) * int(b)
        answers.append(ans)
    return answers


"""
    Examples
"""
for example in examples:
    example_solutions = camel_cards(example.input_data)
    print(example.input_data)
    print(example.answer_a, example_solutions[0])
    print(example.answer_b, example_solutions[1])
    print()

solutions = camel_cards(puzzle.input_data)
"""
    Submission A
"""
part_a = solutions[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = solutions[1]
print(part_b)
puzzle.answer_b = part_b
