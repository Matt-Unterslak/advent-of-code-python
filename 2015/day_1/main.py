from typing import List
from aocd.models import Puzzle

YEAR: int = 2015
DAY: int = 1

puzzle: Puzzle = Puzzle(year=YEAR, day=DAY)
examples: List[Puzzle] = puzzle.examples


def calc_floors(input_data: str) -> int:
    floor = 0
    for x in input_data:
        if x == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def first_basement(input_data: str) -> int:
    floor = 0
    for ind, x in enumerate(input_data):
        if x == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            break
    return ind + 1


for example in examples:
    print(example.input_data)
    print(example.answer_a, calc_floors(example.input_data))
    print(example.answer_b)
    print()

part_a = calc_floors(puzzle.input_data)
print(part_a)
puzzle.answer_a = part_a


samples = [")", "()())"]
for sample in samples:
    print(sample)
    print(first_basement(sample))
    print()

part_b = first_basement(puzzle.input_data)
print(part_b)
puzzle.answer_b = part_b
