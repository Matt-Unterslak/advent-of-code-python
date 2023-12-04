from typing import List
from aocd.models import Puzzle

YEAR: int = 2016
DAY: int = 9

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples

"""
    Ref: Solution goes here
"""


def get_decompressed_length(input_str: str) -> int:
    input_str = input_str.strip()
    decrypted_length = 0
    ind: int = 0
    while ind < len(input_str):
        c = input_str[ind]
        if c == "(":
            closing_bracket_ind: int = input_str.index(")", ind + 1)
            number_of_next_letters, repetitions = [
                int(x) for x in input_str[ind + 1 : closing_bracket_ind].split("x")
            ]
            decrypted_length += number_of_next_letters * repetitions
            ind = closing_bracket_ind + 1
            ind += number_of_next_letters
        else:
            decrypted_length += 1
            ind += 1

    return decrypted_length


def calc(s):
    result = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "(":
            j = s.index(")", i + 1)
            marker = s[i + 1 : j]
            [ml, mr] = [int(x) for x in marker.split("x")]
            i = j + 1
            result += calc(s[i : i + ml]) * mr
            i += ml
        else:
            result += 1
            i += 1
    return result


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print(example.answer_a, get_decompressed_length(example.input_data))
    print(example.answer_b)
    print()

print(puzzle.input_data)
"""
    Submission A
"""
part_a = get_decompressed_length(puzzle.input_data)
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
part_b = calc(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
