from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 11

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

INVALID_CHARACTERS = ["i", "l", "o"]
ALPHAS = "abcdefghijklmnopqrstuvwxyz"


def check_if_consecutive(s) -> bool:
    # Get the length of the string
    l = len(s)

    has_consecutive = False

    # Iterate for every index and
    # check for the condition
    for i in range(2, l):
        # If are not consecutive
        word = s[i - 2] + s[i - 1] + s[i]
        order = [ord(s[i - 2]), ord(s[i - 1]), ord(s[i])]
        if order == list(range(order[0], order[0] + len(order))):
            has_consecutive = True

    return has_consecutive


def check_overlapping_pairs(input_str: str) -> bool:
    total_pairs = 0
    last_pair_ind = 1
    for i in range(len(input_str) - 1):
        a, b = input_str[i], input_str[i + 1]
        if a == b:
            if i == last_pair_ind:
                continue
            else:
                total_pairs += 1
                last_pair_ind = i + 1

    if total_pairs < 2:
        return False
    return True


def is_valid_password(input_str: str):
    has_invalid_characters = [x in input_str for x in INVALID_CHARACTERS]
    if True in has_invalid_characters:
        # print("has invalid")
        return False
    if not check_if_consecutive(input_str):
        # print("has no consecutive")
        return False

    if not check_overlapping_pairs(input_str):
        # print("two non-overlapping pairs not found")
        return False
    return True


def next_password(pwd: str):
    if pwd == "":
        return ""
    elif pwd[-1] == "z":
        return next_password(pwd[:-1]) + "a"
    else:
        return pwd[:-1] + ALPHAS[ALPHAS.index(pwd[-1]) + 1]


def create_valid_password(password: str):
    while not is_valid_password(password):
        password = next_password(password)
    return password


samples = [
    "hijklmmn",
    "abbceffg",
    "abdceffg",
    "abccefgh",
    "abcdffaa",
]
for sample in samples:
    print(sample)
    print(is_valid_password(sample))
    print()


for example in examples:
    print(example.input_data)
    print(example.answer_a, create_valid_password(example.input_data))
    print(example.answer_b)
    print()

print("----------------")

print(puzzle.input_data)
part_a = create_valid_password(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

print(next_password(part_a))
part_b = create_valid_password(next_password(part_a))
print(part_b)
puzzle.answer_b = part_b
print("---------------------")
print()
