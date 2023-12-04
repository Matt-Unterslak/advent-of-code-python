import re
from itertools import groupby
from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 10

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def get_grouped_digits(input_str: str):
    groups: list[tuple[str, str]] = re.findall(r"((.)\2*)", input_str)
    result = [str(len(repeat)) + number for repeat, number in groups]
    return "".join(result)


def get_grouped_digits_improved(input_str: str):
    return "".join([str(len(list(g))) + k for k, g in groupby(input_str)])


def get_result_after_n_rounds(input_str: str, n_rounds: int):
    result = input_str
    for i in range(n_rounds):
        result = get_grouped_digits_improved(result)
    return result


samples = [
    ["1", "11"],
    ["11", "21"],
    ["21", "1211"],
    ["1211", "111221"],
    ["111221", "312211"],
]
for sample in samples:
    print(sample[0])
    print(sample[1], get_grouped_digits(sample[0]))
    print()

print(puzzle.input_data)
part_a = get_result_after_n_rounds(puzzle.input_data, 40)
print(len(part_a))
puzzle.answer_a = len(part_a)
print("---------------------")
print()


part_b = get_result_after_n_rounds(part_a, 10)
print(len(part_b))
puzzle.answer_b = len(part_b)
print("---------------------")
print()
