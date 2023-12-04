import re
from typing import List
from aocd.models import Puzzle

YEAR: int = 2023
DAY: int = 1

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


"""
    Ref: Solution goes here
"""


def find_sum_of_lines(input_str: str):
    lines = input_str.split("\n")
    part_1 = 0
    part_2 = 0
    for line in lines:
        part_1_digits = []
        part_2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                part_1_digits.append(c)
                part_2_digits.append(c)
            for d, val in enumerate(
                ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            ):
                if line[i:].startswith(val):
                    part_2_digits.append(str(d + 1))
        part_1 += int(part_1_digits[0] + part_1_digits[-1])
        part_2 += int(part_2_digits[0] + part_2_digits[-1])
    return part_1, part_2


"""
    Examples
"""
for example in examples:
    print(example.input_data)
    print()
    print(example.answer_a, find_sum_of_lines(example.input_data)[0])
    print(example.answer_b)
    print()

"""
    Submission A
"""
# print(puzzle.input_data)
part_a = find_sum_of_lines(puzzle.input_data)[0]
print(part_a)
puzzle.answer_a = part_a

"""
    Submission B
"""
part_b = find_sum_of_lines(puzzle.input_data)[1]
print(part_b)
puzzle.answer_b = part_b
