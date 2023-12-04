import re
import numpy as np
from typing import List
from aocd.models import Puzzle


YEAR: int = 2015
DAY: int = 25

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples
CODE = 20151125


def compute_password(input_str: str, code: int):
    pwd_row: int = int(re.findall(r"row \d+", input_str)[0].strip("row "))
    pwd_column: int = int(re.findall(r"column \d+", input_str)[0].strip("column "))

    # moving to next colum adds 2, 3, 4, ... to the value
    grid = np.sum(np.arange(2, pwd_column + 1)) + 1
    # moving to next row adds the column number, +1, +2 ... to the value
    grid = grid + np.sum(np.arange(pwd_column, pwd_column + pwd_row - 1))
    for i in range(grid - 1):
        code = code * 252533 % 33554393
    return code


# for example in examples:
#     print(example.input_data)
#     print(example.answer_a, compute_password(example.input_data, CODE))
#     print(example.answer_b)
#     print()


part_a = compute_password(puzzle.input_data, CODE)
print(part_a)
puzzle.answer_a = part_a
print("---------------------")
print()

# samples = [
#     ["qjhvhtzxzqqjkmpb", 1],
#     ["xxyxx", 1],
#     ["uurcxstgmygtbstg", 0],
#     ["ieodomkazucvgmuy", 0],
# ]
# for sample in samples:
#     print(sample[0])
#     print(sample[1])
#     print()

# part_b = number_of_nice_strings(puzzle.input_data, False)
# print(part_b)
# puzzle.answer_b = part_b
print("---------------------")
print()
