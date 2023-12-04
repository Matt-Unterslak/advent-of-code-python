import hashlib
from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 5

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def get_door_password(input_str: str, is_part_1: bool):
    number: int = 0
    if is_part_1:
        password_1 = []
        while True:
            hash_str = hashlib.md5(
                (input_str + str(number)).encode("utf-8")
            ).hexdigest()
            if hash_str.startswith("00000"):
                password_1.append(hash_str[5])
            if len(password_1) == 8:
                break
            number += 1
        return "".join(password_1)
    else:
        password_2 = ["" for _ in range(8)]
        while True:
            hash_str = hashlib.md5(
                (input_str + str(number)).encode("utf-8")
            ).hexdigest()
            if hash_str.startswith("00000") and hash_str[5].isnumeric():
                index = int(hash_str[5])
                if index < len(password_2) and password_2[index] == "":
                    password_2[index] = hash_str[6]
            if "" not in password_2:
                break
            number += 1
    return "".join(password_2)


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, get_door_password(example.input_data, True))
    print("05ace8e3", get_door_password(example.input_data, False))
    print()

"""
    Submission A
"""
part_a = get_door_password(puzzle.input_data, True)
print(part_a)
puzzle.answer_a = part_a


"""
    Samples for Part B
"""

# samples = [")", "()())"]
# for sample in samples:
#     print(sample)
#     print(first_basement(sample))
#     print()

"""
    Submission B
"""
part_b = get_door_password(puzzle.input_data, False)
print(part_b)
puzzle.answer_b = part_b
